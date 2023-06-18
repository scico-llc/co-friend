import os
from web3 import Web3
from web3.middleware import geth_poa_middleware

def get_account_from_token_id(token_id: int) -> str:
    NETWORK_RPC = os.getenv("NETWORK_RPC")
    FRIEND_NFT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")
    REGISTRY_ADDRESS = os.getenv("REGISTRY_ADDRESS")

    w3 = Web3(Web3.HTTPProvider(NETWORK_RPC))
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    with open("./contracts/AccountRegistry.jon", "r") as file:
        contract_interface = file.read()
    contract_address = w3.toChecksumAddress(REGISTRY_ADDRESS)
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_interface["abi"],
        bytecode=contract_interface["bytecode"],
    )

    account_address = contract.functions.account(FRIEND_NFT_ADDRESS, token_id).call()
    return account_address
