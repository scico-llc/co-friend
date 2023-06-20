import sys

sys.path.append("../")
from generate_image.generate import initialize_diffusers, generate_image
from fastapi import APIRouter, Depends
import schemas.character as sch
import firebase.firebase as fb
import crypto.mint as mint
import crypto.account as acc
import crypto.supply as spl

from . import auth
import base64

router = APIRouter()
pipe = initialize_diffusers()


@router.post("/characters/image", dependencies=[Depends(auth.api_key_auth)])
async def generate_character_image(
    reqBody: sch.CharacterImagePrompt,
) -> sch.CharacterImagesResponse:
    seed_byte = reqBody.wallet_address[2:12]
    seed = int.from_bytes(
        base64.b64decode(seed_byte + "=" * (-len(seed_byte) % 4)), "big"
    )
    images = generate_image(pipe, reqBody.animal_type, seed)
    urls = fb.updaload_image(images, reqBody.animal_id)

    return sch.CharacterImagesResponse(image_urls=urls)


@router.post("/characters/mint", dependencies=[Depends(auth.api_key_auth)])
async def mint_character(
    reqBody: sch.CharacterMint,
):
    published = spl.get_friend_total_supply()
    token_id = published + 1
    # NFTをMint
    mint.mint_cofriend_nft(reqBody.wallet_address, published + 1)
    # Token bound Accountを作成
    address = acc.create_account_from_token_id(token_id)
    attr = [
        {"trait_type": "Account", "value": address},
        {"trait_type": "Id", "value": reqBody.animal_id},
        {"trait_type": "Type", "value": reqBody.animal_type},
    ]
    fb.save_character_metadata(
        token_id,
        reqBody.animal_id,
        reqBody.animal_name,
        reqBody.image_url,
        attr,
    )
