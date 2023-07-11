import sys

sys.path.append("../")
from fastapi import APIRouter, Depends
import indexers.character_indexer as indexer
import firebase.firebase as fb

import schemas.users as sch

from . import auth

router = APIRouter()


@router.get("/users/{wallet_address}", dependencies=[Depends(auth.api_key_auth)])
async def fetch_caharacters(wallet_address: str) -> sch.UserCharacter:
    infos = indexer.fetchCaharacterMetadata(wallet_address)
    return sch.UserCharacter(urls=infos)


@router.get(
    "/users/characters/{animal_id}/keywords", dependencies=[Depends(auth.api_key_auth)]
)
async def fetch_caharacters(account_wallet_address: str) -> sch.UserCharacterKeywords:
    keywords = fb.fetchCharacterKeywords(account_wallet_address)
    return sch.UserCharacterKeywords(keywords=keywords)


@router.get(
    "/users/characters/{account_wallet_address}",
    dependencies=[Depends(auth.api_key_auth)],
)
async def fetch_caharacters(account_wallet_address: str) -> sch.CharacterMemories:
    infos = indexer.fetchCaharacterMemoryMetadata(account_wallet_address)
    return sch.CharacterMemories(sbt_urls=infos["sbt"], nft_urls=infos["nft"])
