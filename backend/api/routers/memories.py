import sys
sys.path.append("../")
from fastapi import APIRouter, Depends
import schemas.character_memory as sch
import firebase.firebase as fb
import crypto.mint as mint
import crypto.account as acc
import crypto.supply as spl

from . import auth

router = APIRouter()

@router.post("/memory/mint", dependencies=[Depends(auth.api_key_auth)])
async def mint_memory(
    reqBody: sch.MemoryMint,
):
    published = spl.get_memory_total_supply()
    token_id = published + 1

    wallet_address, _ = acc.get_account_from_nft_id(reqBody.nft_id)
    mint.mint_memory_sbt(wallet_address, published + 1)

    memory = fb.fetch_memory_raw_data(reqBody.memory_id)
    fb.save_memory_metadata(
        token_id,
        memory
    )

@router.post("/dialy/mint", dependencies=[Depends(auth.api_key_auth)])
async def mint_dialy(
    reqBody: sch.DialyMint,
):
    published = spl.get_dialy_total_supply()
    token_id = published + 1

    mint.mint_dialy_nft(reqBody.wallet_address, published + 1)
    memory = fb.fetch_memory_raw_data(reqBody.memory_id)
    fb.save_memory_metadata(
        token_id,
        memory
    )
