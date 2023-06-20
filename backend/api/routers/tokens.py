import sys

sys.path.append("../")
from fastapi import APIRouter
import schemas.token as sch
import firebase.firebase as fb

router = APIRouter()


@router.get("/nft/metadata/{id}")
async def get_nft_metadata(id: str) -> sch.NFTMetaData:
    metadata = fb.fetch_character_metadata(id)
    return sch.NFTMetaData(
        description=metadata["description"].replace("\\n", "\n"),
        external_url="",
        image=metadata["image"],
        name=metadata["name"],
        attributes=metadata["attributes"],
    )


@router.get("/sbt/metadata/{id}")
async def get_sbt_metadata(id: str) -> sch.NFTMetaData:
    metadata = fb.fetch_memory_metadata(id)
    return sch.NFTMetaData(
        description=metadata["description"].replace("\\n", "\n"),
        external_url="",
        image="",
        name=metadata["name"],
        attributes=[],
    )

