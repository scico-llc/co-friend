import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware


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
    # buildTransaction(
    #     {
    #         "nonce": w3.eth.get_transaction_count(ADMIN_WALLET_ADDRESS),
    #         "gas": 10000000,
    #         "gasPrice": w3.toWei("2", "gwei"),
    #     }
    # )
    # sign_create_tx = w3.eth.account.sign_transaction(
    #     create_tx, private_key=ADMIN_SECRET_KEY
    # )

    # w3.eth.send_raw_transaction(sign_create_tx.rawTransaction)
    # tx_hash = w3.toHex(w3.keccak(sign_create_tx.rawTransaction))
    # w3.eth.wait_for_transaction_receipt(tx_hash)


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
