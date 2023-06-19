from firebase_admin import firestore

def get_friend_total_supply() -> int:
    db = firestore.client()
    docs = db.collection("character_metadata").stream()
    ids = []
    for doc in docs:
        ids.append(doc.id)

    return len(ids)

def get_memory_total_supply() -> int:
    db = firestore.client()
    docs = db.collection("memory_metadata").stream()
    ids = []
    for doc in docs:
        ids.append(doc.id)

    return len(ids)

def get_dialy_total_supply() -> int:
    db = firestore.client()
    docs = db.collection("dialy_metadata").stream()
    ids = []
    for doc in docs:
        ids.append(doc.id)

    return len(ids)