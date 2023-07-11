from pydantic import BaseModel, Field


class CharacterImagePrompt(BaseModel):
    wallet_address: str = Field(
        None, example="0x3CCcF9DFaC3D0Ff6A20aD2a6396fE8119b10A92e"
    )
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    animal_type: str = Field(None, example="dog")


class CharacterImagesResponse(BaseModel):
    image_urls: list[str] = Field([], example=["https://xxx", "https://yyy"])


class CharacterMint(BaseModel):
    wallet_address: str = Field(
        None, example="0x3CCcF9DFaC3D0Ff6A20aD2a6396fE8119b10A92e"
    )
    image_url: str = Field(None, example="https://xxx")
    animal_id: str = Field(None, example="xxxxxxxxxxxx123")
    animal_type: str = Field(None, example="dog")
    animal_name: str = Field(None, example="doggy")
