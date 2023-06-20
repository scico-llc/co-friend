from pydantic import BaseModel, Field


class MemoryMint(BaseModel):
    nft_id: str = Field(None, example="000001")
    memory_id: str = Field(None, example="1686953620000000")


class DialyMint(BaseModel):
    nft_id: str = Field(None, example="000001")
    title: str = Field(None, example="XXXの思い出")
    memory_id: str = Field(None, example="1686953620000000")
    author_name: str = Field(None, example="はまべみなみ")
    image_url: str = Field(None, example="https://xxxx")
    wallet_address: str = Field(None, example="0x3CCcF9DFaC3D0Ff6A20aD2a6396fE8119b10A92e")
