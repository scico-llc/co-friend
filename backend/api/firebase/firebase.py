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


def updaload_image(files: list[str], animal_id: str) -> list[str]:
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


def save_character_metadata(
    token_id: int,
    animal_id: str,
    animal_name: str,
    image_url: str,
    attr: dict = {}
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


def save_memory_metadata(
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


def fetch_character_metadata(
    token_id: int,
) -> dict:
    db = firestore.client()
    character_id = f"{token_id}".zfill(6)

    metadata_ref = db.collection("character_metadata").document(character_id)
    metadata = metadata_ref.get().to_dict()
    return metadata


def fetch_memory_metadata(
    token_id: int,
) -> dict:
    db = firestore.client()
    memory_id = f"{token_id}".zfill(8)

    metadata_ref = db.collection("memory_metadata").document(memory_id)
    return metadata_ref.get().to_dict()


def fetch_random_two_animals() -> list[str]:
    db = firestore.client()
    docs = db.collection("characters").stream()
    characters = []

    for doc in docs:
        characters.append(doc.id)

    if len(characters) < 2:
        return []
    
    return random.sample(characters, 2)
