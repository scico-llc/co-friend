import sys
sys.path.append('../')
from generate_image import generate_image
from fastapi import APIRouter
import schemas.character as sch
import base58

router = APIRouter()


@router.post("/characters/image")
async def generate_character_image(
    reqBody: sch.CharacterImagePrompt,
) -> sch.CharacterInagesResponse:
    walletAddress = reqBody.wallet_address[2:]
    seed = int.from_bytes(base58.b58decode(walletAddress), "big")
    images = generate_image(reqBody.animal_type, seed)
    # TODO: Firebase Storageに保存する
    return sch.CharacterInagesResponse()


@router.post("/characters/mint")
async def mint_character(
    reqBody: sch.CharacterMint,
) -> sch.CharacterMintResponse:
    # TODO: Mintコントラクトを実行する
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
