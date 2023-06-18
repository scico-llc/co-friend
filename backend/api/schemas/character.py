from typing import Optional, List
from pydantic import BaseModel, Field

class CharacterImagePrompt(BaseModel):
    wallet_address: str = Field(None, example="0x3CCcF9DFaC3D0Ff6A20aD2a6396fE8119b10A92e")
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    animal_type: str = Field(None, example="dog")

class CharacterInagesResponse(BaseModel):
    image_urls: List[str] = Field([], example=["https://xxx", "https://yyy"])

class CharacterMint(BaseModel):
    wallet_address: str = Field(None, example="0x3CCcF9DFaC3D0Ff6A20aD2a6396fE8119b10A92e")
    image_url: str = Field(None, example="https://xxx")
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    animal_type: str = Field(None, example="dog")
    animal_name: str = Field(None, example="doggy")

class CharacterMintResponse(BaseModel):
    is_success: str = Field(False, example=True)

class CharacterHolders(BaseModel):
    wallet_address: str = Field("", example="0x3CCcF9DFaC3D0Ff6A20aD2a6396fE8119b10A92e")

class CharacterMetaData():
    image_url: str = Field(None, example="https://xxx")
    memory_id: str = Field("", example="0x579cB2931869Ea158Bcd7b7823a3a0c543486b93")
    chat_id: str = Field("", example="bnrevd0tjC9zWbpyN7dU")

# class CharactersResponse(BaseModel):
#     characters: List[CharacterMetaData] = Field([], example=[CharacterMetaData()])

class CharacterMemoryData:
    timestamp: int = Field(-1, exmple=1686497747)
    memory_title: str = Field("", exmple="XXXをしたよ")
    memory_detail: str = Field("", exmple="今日、XXと一緒にXXX")
    contract_address: str = Field("", exmple="0x579cB2931869Ea158Bcd7b7823a3a0c543486b93")
    contract_id: int = Field(-1, exmple=100)
    linked_nft_contract_address: str = Field("", exmple="0x579cB2931869Ea158Bcd7b7823a3a0c543400000")
    linked_nft_contract_id: int = Field(-1, exmple=2)

# class CharacterMemoriesResponse(BaseModel):
#     memories: List[CharacterMemoryData] = Field([], example=[CharacterMemoryData()])
