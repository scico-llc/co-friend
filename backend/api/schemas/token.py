from typing import Optional, List
from pydantic import BaseModel, Field

class NFTMetaData(BaseModel):
    description: str = Field("", example="NFTのキャラ詳細")
    external_url: str = Field("", example="https://xxxxx")
    image: str = Field("", example="https://xxxxx")
    name: str = Field("", example="doggy")
    attributes: list = Field([], example=[])


class SBTMetaData(BaseModel):
    description: str = Field("", example="SBTを表現する日記")
    external_url: str = Field("", example="https://xxxxx")
    image: str = Field("", example="https://xxxxx")
    name: str = Field("", example="2023年08月12日")
    attributes: list = Field([], example=[])
