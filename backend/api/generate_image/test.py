import model_util

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
    )

    
if __name__ == "__main__":
    convert(
        "../../models/anything-v5.safetensors",
        "../../models/anything-v5",
        "stablediffusionapi/anything-v5",
    )
