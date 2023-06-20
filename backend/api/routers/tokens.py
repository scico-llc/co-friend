import sys

sys.path.append("../")
from fastapi import APIRouter
import schemas.token as sch
import firebase.firebase as fb

router = APIRouter()


@router.get("/cofrd/metadata/{id}")
async def get_friend_nft_metadata(id: str) -> sch.NFTMetaData:
    metadata = fb.fetch_character_metadata(id)
    if metadata == None:
        return
    return sch.NFTMetaData(
        description=metadata["description"].replace("\\n", "\n"),
        external_url="",
        image=metadata["image"],
        name=metadata["name"],
        attributes=metadata["attributes"],
    )


@router.get("/comem/metadata/{id}")
async def get_memory_sbt_metadata(id: str) -> sch.NFTMetaData:
    metadata = fb.fetch_memory_metadata(id)
    if metadata == None:
        return
    return sch.NFTMetaData(
        description=metadata["description"].replace("\\n", "\n"),
        external_url="",
        image="",
        name=metadata["name"],
        attributes=[],
    )


@router.get("/codal/metadata/{id}")
async def get_dialy_nft_metadata(id: str) -> sch.NFTMetaData:
    metadata = fb.fetch_dialy_metadata(id)
    if metadata == None:
        return
    return sch.NFTMetaData(
        description=metadata["description"].replace("\\n", "\n"),
        external_url="",
        image="",
        name=metadata["name"],
        attributes=[],
    )
