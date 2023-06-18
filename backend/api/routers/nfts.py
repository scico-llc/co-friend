import sys

sys.path.append("../")
from fastapi import APIRouter
import schemas.nft as sch
import generate_chat.user_chat as chat

router = APIRouter()

@router.get("/nft/metadata/{id}")
async def get_nft_metadata(id: str) -> sch.NFTMetaData:

    return sch.NFTMetaData()


@router.get("/sbt/metadata/{id}")
async def get_sbt_metadata(id: str) -> sch.NFTMetaData:

    return sch.SBTMetaData()