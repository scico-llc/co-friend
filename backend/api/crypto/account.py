import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from firebase_admin import firestore


def create_account_from_token_id(token_id: int) -> str:
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    FRIEND_NFT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")
    REGISTRY_ADDRESS = os.getenv("REGISTRY_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    wa = w3.is_checksum_address(ADMIN_WALLET_ADDRESS)
    ca = w3.is_checksum_address(REGISTRY_ADDRESS)
    if not(wa and ca):
        return

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("../abi/AccountRegistry.json", "r") as file:
        contract_interface = json.load(file)
    contract = w3.eth.contract(
        address=REGISTRY_ADDRESS,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    create_address = contract.functions.createAccount(FRIEND_NFT_ADDRESS, token_id).call()
    return create_address


def get_account_from_token_id(token_id: int) -> str:
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    FRIEND_NFT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")
    REGISTRY_ADDRESS = os.getenv("REGISTRY_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("../abi/AccountRegistry.json", "r") as file:
        contract_interface = json.load(file)
    ca = w3.is_checksum_address(REGISTRY_ADDRESS)
    if not ca:
        return
    contract = w3.eth.contract(
        address=REGISTRY_ADDRESS,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    account_address = contract.functions.account(FRIEND_NFT_ADDRESS, token_id).call()
    return account_address


def get_account_from_nft_id(nft_id: str) -> tuple:
    db = firestore.client()
    character_ref = db.collection("character_metadata").document(nft_id)
    character_data = character_ref.get().to_dict()

    account = character_data["attributes"]["account"]
    animal_id = character_data["attributes"]["id"]

    return account, animal_id