from typing import List
from diffusers import UniPCMultistepScheduler
from diffusers import StableDiffusionPipeline
from rembg import remove
from PIL.Image import Image as PILImage

import os
import torch
import requests

from load_lora import load_safetensors_lora
import model_util


def generate_image(animal_name: str, seed: int) -> List[PILImage]:
    # Modelの確認・変換と取得
    safetensors_path = "../../models/anything-v5.safetensors"
    safetensors_url = "https://huggingface.co/ckpt/anything-v5.0/resolve/main/AnythingV5V3_v5PrtRE.safetensors"
    model_path = "../../models/anything-v5"
    ref_name = "stablediffusionapi/anything-v5"
    if not os.path.isfile(safetensors_path):
        print("download Model")
        urlData = requests.get(safetensors_url).content
        with open(safetensors_path, mode="wb") as f:
            f.write(urlData)
        convert(safetensors_path, model_path, ref_name)
    if not os.path.isdir(model_path):
        convert(safetensors_path, model_path, ref_name)

    # Loraの確認と取得
    lora_path = "../../models/CuteCreatures.safetensors"
    lora_url = "https://civitai.com/api/download/models/64757"
    if not os.path.isfile(lora_path):
        print("download Lora")
        urlData = requests.get(lora_url).content
        with open(lora_path, mode="wb") as f:
            f.write(urlData)

    # Diffuserの構築
    pipe = StableDiffusionPipeline.from_pretrained(model_path)
    pipe = load_safetensors_lora(pipe, lora_path, alpha=0.9)
    pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)

    # Generativeの生成
    generator = torch.manual_seed(seed)
    negative_prompt = "glass, pedestal, socle, basement, camera, subsurface, underwater, hypermaximalist, diamond, (flowers), water, (leaves) (worst quality:2), (low quality:2), (normal quality:2), border, frame, poorly drawn, childish, hands, hand, hair, ((dof)), bad fingers, bad anatomy, missing fingersmissing_limb, liquid fingers, cropped, many legs, text, sign"
    prompt = f"<lora:CuteCreatures:0.95> Cu73Cre4ture {animal_name}"

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

    return [remove(img) for img in images]


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
