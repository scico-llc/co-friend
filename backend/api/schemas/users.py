from pydantic import BaseModel, Field


class UserCharacter(BaseModel):
    urls: list[str] = Field([], example=["http://xxx/1", "http://xxx/2"])


class UserCharacterKeywords(BaseModel):
    key_words: list[str] = Field([], example=["春", "秋"])


class CharacterMemories(BaseModel):
    sbt_urls: list = Field([], example=["http://xxx/1", "http://xxx/2"])
    nft_urls: list = Field([], example=["http://yyy/1", "http://yyy/2"])
