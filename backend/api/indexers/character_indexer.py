import os
import requests

base_url = "https://polygon-mumbai.g.alchemy.com"
ALCHEMY_KEY = os.getenv("NETWORK_KEY")
FRIEND_NFT_ADDRESS = os.getenv("FRIEND_NFT_ADDRESS")
MEMORY_SBT_CONTRACT = os.getenv("MEMORY_SBT_CONTRACT")
DIALY_NFT_CONTRACT = os.getenv("DIALY_NFT_CONTRACT")


def fetchCaharacterMetadata(wallet_address: str) -> list:
    url = f"{base_url}/nft/v2/{ALCHEMY_KEY}/getNFTs"
    query = {
        "owner": wallet_address,
        "contractAddresses[]": FRIEND_NFT_ADDRESS,
        "withMetadata": "true",
        "pageSize": 100,
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=query)
    if response.status_code != 200:
        return []
    else:
        return [nft["tokenUri"]["raw"] for nft in response.content["ownedNfts"]]


def fetchCaharacterMemoryMetadata(account_wallet_address: str) -> dict:
    url = f"{base_url}/nft/v2/{ALCHEMY_KEY}/getNFTs"
    query = {
        "owner": account_wallet_address,
        "contractAddresses[]": MEMORY_SBT_CONTRACT,
        "contractAddresses[]": DIALY_NFT_CONTRACT,
        "withMetadata": "true",
        "pageSize": 100,
    }
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=query)
    contents = response.content["ownedNfts"]

    if response.status_code != 200:
        return {}
    else:
        return {
            "sbt": [sbt["tokenUri"]["raw"] for sbt in contents if sbt["contract"]["address"] == MEMORY_SBT_CONTRACT],
            "nft": [nft["tokenUri"]["raw"] for nft in contents if nft["contract"]["address"] == DIALY_NFT_CONTRACT],
        }
