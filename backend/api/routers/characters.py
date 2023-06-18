import sys
sys.path.append('../')
from generate_image.generate import initialize_diffusers, generate_image
from fastapi import APIRouter
import schemas.character as sch
import firebase.firebase as fb
import base64

router = APIRouter()
pipe = initialize_diffusers()

@router.post("/characters/image")
async def generate_character_image(
    reqBody: sch.CharacterImagePrompt,
) -> sch.CharacterInagesResponse:
    seed_byte = reqBody.wallet_address[2:12]
    seed = int.from_bytes(base64.b64decode(seed_byte+ '=' * (-len(seed_byte) % 4)), 'big')
    images = generate_image(pipe, reqBody.animal_type, seed)
    urls = fb.updaload_image(images, reqBody.animal_id)
    
    return sch.CharacterInagesResponse(urls)


@router.post("/characters/mint")
async def mint_character(
    reqBody: sch.CharacterMint,
) -> sch.CharacterMintResponse:
    # TODO: Mintコントラクトを実行する
    print(2)
    return sch.CharacterMintResponse()

# @router.get("/characters")
# async def get_characters(
#     reqBody: sch.CharacterHolders,
# ) -> sch.CharactersResponse:
#     # TODO: NFTメタデータを取得
#     return sch.CharactersResponse()

# @router.get("/characters/memory")
# async def get_character_memories() -> sch.CharacterMemoriesResponse:
#     # TODO: SBTのメタデータを取得
#     return sch.CharacterMemoriesResponse()
