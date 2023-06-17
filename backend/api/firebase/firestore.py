import os
import base64
import json
import firebase_admin
from firebase_admin import credentials

def initialize():
    cred_text = base64.b64decode(os.environ["FIREBASE_CRED"]).decode()
    credential = json.loads(cred_text)
    firebase_admin.initialize_app(credentials.Certificate(credential))
