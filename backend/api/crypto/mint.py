import os
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from . import account


def mint_cofriend_nft(target_address: str, token_id: int):
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_SECRET_KEY = os.getenv("ADMIN_PRIVATE_KEY")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    CONTRACT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    wa1 = w3.is_checksum_address(target_address)
    wa2 = w3.is_checksum_address(ADMIN_WALLET_ADDRESS)
    ca = w3.is_checksum_address(CONTRACT_ADDRESS)
    if not (wa1 and wa2 and ca):
        return

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("../abi/FriendNFT.json", "r") as file:
        contract_interface = json.load(file)
    contract = w3.eth.contract(
        address=CONTRACT_ADDRESS,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    mint_tx = contract.functions.safeMint(target_address, token_id).build_transaction(
        {
            "nonce": w3.eth.get_transaction_count(ADMIN_WALLET_ADDRESS),
            "gas": 10000000,
            "gasPrice": w3.to_wei("2", "gwei"),
        }
    )
    sign_mint_tx = w3.eth.account.sign_transaction(
        mint_tx, private_key=ADMIN_SECRET_KEY
    )

    w3.eth.send_raw_transaction(sign_mint_tx.rawTransaction)
    tx_hash = w3.to_hex(w3.keccak(sign_mint_tx.rawTransaction))
    w3.eth.wait_for_transaction_receipt(tx_hash)


def mint_memory_sbt(friend_token_id: int, token_id: int):
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_SECRET_KEY = os.getenv("ADMIN_PRIVATE_KEY")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    CONTRACT_ADDRESS = os.getenv("MEMORY_SBT_CONTRACT")
    WALLET_ADDLESS = account.get_account_from_token_id(friend_token_id)

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    wa1 = w3.is_checksum_address(WALLET_ADDLESS)
    wa2 = w3.is_checksum_address(ADMIN_WALLET_ADDRESS)
    ca = w3.is_checksum_address(CONTRACT_ADDRESS)
    if not (wa1 and wa2 and ca):
        return
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("../abi/MemorySBT.json", "r") as file:
        contract_interface = json.load(file)
    contract = w3.eth.contract(
        address=CONTRACT_ADDRESS,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    mint_tx = contract.functions.safeMint(WALLET_ADDLESS, token_id).build_transaction(
        {
            "nonce": w3.eth.get_transaction_count(ADMIN_WALLET_ADDRESS),
            "gas": 10000000,
            "gasPrice": w3.to_wei("2", "gwei"),
        }
    )
    sign_mint_tx = w3.eth.account.sign_transaction(
        mint_tx, private_key=ADMIN_SECRET_KEY
    )

    w3.eth.send_raw_transaction(sign_mint_tx.rawTransaction)
    tx_hash = w3.to_hex(w3.keccak(sign_mint_tx.rawTransaction))
    w3.eth.wait_for_transaction_receipt(tx_hash)


def mint_dialy_nft(target_address: str, token_id: int):
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_SECRET_KEY = os.getenv("ADMIN_PRIVATE_KEY")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    CONTRACT_ADDRESS = os.getenv("DIALY_NFT_CONTRACT")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    wa1 = w3.is_checksum_address(target_address)
    wa2 = w3.is_checksum_address(ADMIN_WALLET_ADDRESS)
    ca = w3.is_checksum_address(CONTRACT_ADDRESS)
    if not (wa1 and wa2 and ca):
        return

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("../abi/DialyNFT.json", "r") as file:
        contract_interface = json.load(file)
    contract = w3.eth.contract(
        address=CONTRACT_ADDRESS,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    mint_tx = contract.functions.safeMint(target_address, token_id).build_transaction(
        {
            "nonce": w3.eth.get_transaction_count(ADMIN_WALLET_ADDRESS),
            "gas": 10000000,
            "gasPrice": w3.to_wei("2", "gwei"),
        }
    )
    sign_mint_tx = w3.eth.account.sign_transaction(
        mint_tx, private_key=ADMIN_SECRET_KEY
    )

    w3.eth.send_raw_transaction(sign_mint_tx.rawTransaction)
    tx_hash = w3.to_hex(w3.keccak(sign_mint_tx.rawTransaction))
    w3.eth.wait_for_transaction_receipt(tx_hash)
