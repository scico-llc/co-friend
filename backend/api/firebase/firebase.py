import os
import base64
import json
import firebase_admin
from firebase_admin import credentials, storage


def initialize():
    cred_text = base64.b64decode(os.environ["FIREBASE_CRED"]).decode()
    credential = json.loads(cred_text)
    firebase_admin.initialize_app(
        credentials.Certificate(credential),
        {'storageBucket': 'co-friend-dev.appspot.com'}
    )


def updaload_image(files: list[str], animal_id: str) -> list[str]:
    bucket = storage.bucket()
    content_type = 'image/png'
    urls = []
    for path in files:
        blob = bucket.blob(f"{animal_id}/{path.split('/')[-1]}.json")
        blob.upload_from_filename(path, content_type=content_type)
        blob.make_public()
        urls.append(blob.public_url)
        os.remove(path)

    return urls