import os
from web3 import Web3
from web3.middleware import geth_poa_middleware

<<<<<<< HEAD

def create_account_from_token_id(token_id: int):
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    ADMIN_SECRET_KEY = os.getenv("ADMIN_PRIVATE_KEY")
    ADMIN_WALLET_ADDRESS = os.getenv("ADMIN_WALLET_ADDRESS")
    FRIEND_NFT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")
    REGISTRY_ADDRESS = os.getenv("REGISTRY_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    admin_wallet_address = w3.toChecksumAddress(ADMIN_WALLET_ADDRESS)
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("./abi/AccountRegistry.jon", "r") as file:
        contract_interface = file.read()
    contract_address = w3.toChecksumAddress(REGISTRY_ADDRESS)
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    create_tx = contract.functions.createAccount(FRIEND_NFT_ADDRESS, token_id).buildTransaction(
        {
            "nonce": w3.eth.get_transaction_count(admin_wallet_address),
            "gas": 10000000,
            "gasPrice": w3.toWei("2", "gwei"),
        }
    )
    sign_create_tx = w3.eth.account.sign_transaction(
        create_tx, private_key=ADMIN_SECRET_KEY
    )

    w3.eth.send_raw_transaction(sign_create_tx.rawTransaction)
    tx_hash = w3.toHex(w3.keccak(sign_create_tx.rawTransaction))
    w3.eth.wait_for_transaction_receipt(tx_hash)


=======
>>>>>>> f7aaa01b68a78f1151b868e47da0cee295c084e9
def get_account_from_token_id(token_id: int) -> str:
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    FRIEND_NFT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")
    REGISTRY_ADDRESS = os.getenv("REGISTRY_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

<<<<<<< HEAD
    with open("./abi/AccountRegistry.jon", "r") as file:
=======
    with open("./contracts/AccountRegistry.jon", "r") as file:
>>>>>>> f7aaa01b68a78f1151b868e47da0cee295c084e9
        contract_interface = file.read()
    contract_address = w3.toChecksumAddress(REGISTRY_ADDRESS)
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    account_address = contract.functions.account(FRIEND_NFT_ADDRESS, token_id).call()
    return account_address
