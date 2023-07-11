import os
import base64
import json
import datetime
import random
import firebase_admin
from firebase_admin import credentials, storage, firestore


def initialize():
    cred_text = base64.b64decode(os.environ["FIREBASE_CRED"]).decode()
    credential = json.loads(cred_text)
    firebase_admin.initialize_app(
        credentials.Certificate(credential),
        {"storageBucket": "co-friend-dev.appspot.com"},
    )


def updaloadImage(files: list[str], animal_id: str) -> list[str]:
    bucket = storage.bucket()
    content_type = "image/png"
    urls = []
    for path in files:
        blob = bucket.blob(f"{animal_id}/{path.split('/')[-1]}")
        blob.upload_from_filename(path, content_type=content_type)
        blob.make_public()
        urls.append(blob.public_url)
        os.remove(path)

    return urls


def saveCharacterMetadata(
    token_id: int, animal_id: str, animal_name: str, image_url: str, attr: list = []
) -> None:
    db = firestore.client()
    character_ref = db.collection("characters").document(animal_id)
    character_data = character_ref.get().to_dict()

    profile = character_data["profile"]
    character_id = f"{token_id}".zfill(6)

    metadata_ref = db.collection("character_metadata").document(character_id)
    metadata_ref.set(
        {
            "description": profile,
            "external_url": "",
            "image": image_url,
            "name": animal_name,
            "attributes": attr,
        }
    )


def saveCharacterKeywords(animal_id: str, keywords: list[str]) -> None:
    db = firestore.client()
    keyword_ref = db.collection("keywords").document(animal_id)
    keyword_ref.set(
        [
            {"id": i, "keyword": word, "is_detected": False}
            for i, word in enumerate(keywords)
        ]
    )


def saveMemoryMetadata(
    token_id: int,
    memory: str,
) -> None:
    dt_now = datetime.datetime.now()
    today = dt_now.strftime("%Y年%m月%d日")
    memory_id = f"{token_id}".zfill(8)

    db = firestore.client()
    metadata_ref = db.collection("memory_metadata").document(memory_id)
    metadata_ref.set(
        {
            "description": memory,
            "external_url": "",
            "image": "",
            "name": today,
            "attributes": [],
        }
    )


def saveDialyMetadata(
    token_id: int,
    title: str,
    memory: str,
    image_url: str,
    author: str,
) -> None:
    dialy_id = f"{token_id}".zfill(8)

    db = firestore.client()
    metadata_ref = db.collection("dialy_metadata").document(dialy_id)
    metadata_ref.set(
        {
            "description": memory,
            "external_url": "",
            "image": image_url,
            "name": title,
            "attributes": [{"trait_type": "Author", "value": author}],
        }
    )


def fetchCharacterMetadata(
    token_id: int,
) -> dict:
    db = firestore.client()
    character_id = f"{token_id}".zfill(6)

    metadata_ref = db.collection("character_metadata").document(character_id)
    metadata = metadata_ref.get().to_dict()
    return metadata


def fetchMemoryMetadata(
    token_id: int,
) -> dict:
    db = firestore.client()
    memory_id = f"{token_id}".zfill(8)

    metadata_ref = db.collection("memory_metadata").document(memory_id)
    return metadata_ref.get().to_dict()


def fetchDialyMetadata(
    token_id: int,
) -> dict:
    db = firestore.client()
    dialy_id = f"{token_id}".zfill(8)

    metadata_ref = db.collection("dialy_metadata").document(dialy_id)
    return metadata_ref.get().to_dict()


def fetchRandomTwoAnimals() -> list[str]:
    db = firestore.client()
    docs = db.collection("characters").stream()
    characters = []

    for doc in docs:
        characters.append(doc.id)

    if len(characters) < 2:
        return []

    return random.sample(characters, 2)


def fetchMemoryRawData(
    memory_id: str,
) -> str:
    db = firestore.client()

    doc_ref = db.collection("memories").document(memory_id)
    memory = doc_ref.get().to_dict()

    return memory["memory"]


def fetchCharacterKeywords(animal_id: str) -> list[dict]:
    db = firestore.client()
    keyword_ref = db.collection("keywords").document(animal_id)
    return keyword_ref.get().to_dict()
