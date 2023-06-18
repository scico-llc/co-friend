import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from . import account

def get_friend_total_supply() -> int:
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")
    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))

    with open("./abi/FriendNFT.jon", "r") as file:
        contract_interface = file.read()
    contract_address = w3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )
    total_supply = contract.functions.totalSupply().call()

    return total_supply

def mint_nft(target_address: str, token_id: int):
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_SECRET_KEY = os.getenv("ADMIN_PRIVATE_KEY")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    wallet_address = w3.toChecksumAddress(target_address)
    admin_wallet_address = w3.toChecksumAddress(ADMIN_WALLET_ADDRESS)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("./abi/FriendNFT.jon", "r") as file:
        contract_interface = file.read()
    contract_address = w3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    mint_tx = contract.functions.safeMint(wallet_address, token_id).buildTransaction(
        {
            "nonce": w3.eth.get_transaction_count(admin_wallet_address),
            "gas": 10000000,
            "gasPrice": w3.toWei("2", "gwei"),
        }
    )
    sign_mint_tx = w3.eth.account.sign_transaction(
        mint_tx, private_key=ADMIN_SECRET_KEY
    )

    w3.eth.send_raw_transaction(sign_mint_tx.rawTransaction)
    tx_hash = w3.toHex(w3.keccak(sign_mint_tx.rawTransaction))
    w3.eth.wait_for_transaction_receipt(tx_hash)


def mint_sbt(friend_token_id: int, token_id: int):
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_SECRET_KEY = os.getenv("ADMIN_PRIVATE_KEY")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    CONTRACT_ADDRESS = os.getenv("NFT_CONTRACT_ADDRESS")
    WALLET_ADDLESS = account.get_account_from_token_id(friend_token_id)

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    wallet_address = w3.toChecksumAddress(WALLET_ADDLESS)
    admin_wallet_address = w3.toChecksumAddress(ADMIN_WALLET_ADDRESS)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("./abi/MemorySBT.jon", "r") as file:
        contract_interface = file.read()
    contract_address = w3.toChecksumAddress(CONTRACT_ADDRESS)
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    mint_tx = contract.functions.safeMint(wallet_address, token_id).buildTransaction(
        {
            "nonce": w3.eth.get_transaction_count(admin_wallet_address),
            "gas": 10000000,
            "gasPrice": w3.toWei("2", "gwei"),
        }
    )
    sign_mint_tx = w3.eth.account.sign_transaction(
        mint_tx, private_key=ADMIN_SECRET_KEY
    )

    w3.eth.send_raw_transaction(sign_mint_tx.rawTransaction)
    tx_hash = w3.toHex(w3.keccak(sign_mint_tx.rawTransaction))
    w3.eth.wait_for_transaction_receipt(tx_hash)
