from typing import List
from diffusers import UniPCMultistepScheduler, StableDiffusionPipeline
from rembg import remove

import os
import torch
from torch import autocast
import requests
from safetensors.torch import load_file
from . import model_util

def initialize_diffusers():
    device = 'cuda'
    safetensors_path = "./models/anything-v5.safetensors"
    model_path = "./models/anything-v5"

    safetensors_url = "https://huggingface.co/ckpt/anything-v5.0/resolve/main/AnythingV5V3_v5PrtRE.safetensors"
    ref_name = "stablediffusionapi/anything-v5"
    if not os.path.isfile(safetensors_path):
        print('get model')
        urlData = requests.get(safetensors_url).content
        print('save model')
        with open(safetensors_path, mode="wb") as f:
            f.write(urlData)
        print('load model')
        convert(safetensors_path, model_path, ref_name)
    if not os.path.isdir(model_path):
        convert(safetensors_path, model_path, ref_name)

    # Loraの確認と取得
    lora_path = "./models/CuteCreatures.safetensors"
    lora_url = "https://civitai.com/api/download/models/64757"
    if not os.path.isfile(lora_path):
        print('get lora')
        urlData = requests.get(lora_url).content
        print('save lora')
        with open(lora_path, mode="wb") as f:
            f.write(urlData)

    # Diffuserの構築
    pipe = StableDiffusionPipeline.from_pretrained(model_path)
    pipe = load_safetensors_lora(pipe, lora_path, alpha=0.9)
    pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.to(device)


def generate_image(pipe, animal_name: str, seed: int) -> List[str]:
    # Generativeの生成
    device = 'cuda'
    generator = torch.manual_seed(seed)
    negative_prompt = "glass, pedestal, socle, basement, camera, subsurface, underwater, hypermaximalist, diamond, (flowers), water, (leaves) (worst quality:2), (low quality:2), (normal quality:2), border, frame, poorly drawn, childish, hands, hand, hair, ((dof)), bad fingers, bad anatomy, missing fingersmissing_limb, liquid fingers, cropped, many legs, text, sign"
    prompt = f"<lora:CuteCreatures:0.95> Cu73Cre4ture {animal_name}"

    with autocast(device):
        images = pipe(
            prompt=prompt,
            generator=generator,
            negative_prompt=negative_prompt,
            num_inference_steps=50,
            guidance_scale=7,
            width=512,
            height=512,
            num_images_per_prompt=3,
        ).images

    # 一時保存
    images = [remove(img).save(f'./{i}.png') for i, img in enumerate(images)]
    # return [f'./{i}.png' for i in 0..len(images)]


def convert(model_to_load: str, model_to_save: str, ref: str):
    (text_encoder, vae, unet) = model_util.load_models_from_stable_diffusion_checkpoint(
        False,
        model_to_load,
    )

    model_util.save_diffusers_checkpoint(
        False,
        model_to_save,
        text_encoder,
        unet,
        ref,
        vae,
        True,
    )

def load_safetensors_lora(
    pipeline,
    checkpoint_path,
    LORA_PREFIX_UNET="lora_unet",
    LORA_PREFIX_TEXT_ENCODER="lora_te",
    alpha=0.75,
):
    # load LoRA weight from .safetensors
    state_dict = load_file(checkpoint_path)

    visited = []

    # directly update weight in diffusers model
    for key in state_dict:
        # it is suggested to print out the key, it usually will be something like below
        # "lora_te_text_model_encoder_layers_0_self_attn_k_proj.lora_down.weight"

        # as we have set the alpha beforehand, so just skip
        if ".alpha" in key or key in visited:
            continue

        if "text" in key:
            layer_infos = (
                key.split(".")[0].split(LORA_PREFIX_TEXT_ENCODER + "_")[-1].split("_")
            )
            curr_layer = pipeline.text_encoder
        else:
            layer_infos = key.split(".")[0].split(LORA_PREFIX_UNET + "_")[-1].split("_")
            curr_layer = pipeline.unet

        # find the target layer
        temp_name = layer_infos.pop(0)
        while len(layer_infos) > -1:
            try:
                curr_layer = curr_layer.__getattr__(temp_name)
                if len(layer_infos) > 0:
                    temp_name = layer_infos.pop(0)
                elif len(layer_infos) == 0:
                    break
            except Exception:
                if len(temp_name) > 0:
                    temp_name += "_" + layer_infos.pop(0)
                else:
                    temp_name = layer_infos.pop(0)

        pair_keys = []
        if "lora_down" in key:
            pair_keys.append(key.replace("lora_down", "lora_up"))
            pair_keys.append(key)
        else:
            pair_keys.append(key)
            pair_keys.append(key.replace("lora_up", "lora_down"))

        # update weight
        if len(state_dict[pair_keys[0]].shape) == 4:
            weight_up = state_dict[pair_keys[0]].squeeze(3).squeeze(2).to(torch.float32)
            weight_down = (
                state_dict[pair_keys[1]].squeeze(3).squeeze(2).to(torch.float32)
            )
            curr_layer.weight.data += alpha * torch.mm(
                weight_up, weight_down
            ).unsqueeze(2).unsqueeze(3)
        else:
            weight_up = state_dict[pair_keys[0]].to(torch.float32)
            weight_down = state_dict[pair_keys[1]].to(torch.float32)
            curr_layer.weight.data += alpha * torch.mm(weight_up, weight_down)

        # update visited list
        for item in pair_keys:
            visited.append(item)

    return pipeline