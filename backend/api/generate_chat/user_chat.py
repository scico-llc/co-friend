import os
import openai
import copy
from firebase_admin import firestore

model_name = "gpt-3.5-turbo-0301"
openai.api_key = os.getenv("OPENAI_KEY")


def get_character_setting(
    animal_id: str,
    animal_type: str,
    animal_name: str,
) -> None:
    # 人格の決定
    with open("./generate_chat/prompts/character_detail_prompt.txt") as f:
        character_text = f.read()
        character_prompt = {"role": "user", "content": character_text}
    response = openai.ChatCompletion.create(
        model=model_name, messages=[character_prompt]
    )
    profile = response.choices[0].message.content

    # 詳細条件の設定
    with open("./generate_chat/prompts/setting_prompt.txt") as f:
        setting_text = f.read().format(animal_type, animal_name, profile)
        setting_prompt = {"role": "system", "content": setting_text}

    # 詳細条件の入力
    response = openai.ChatCompletion.create(model=model_name, messages=[setting_prompt])
    response = {
        "role": "assistant",
        "content": response.choices[0].message.content,
    }
    history = [setting_prompt, response]

    # firestoreにhistoryを追加
    db = firestore.client()
    doc_ref = db.collection("characters").document(animal_id)
    doc_ref.set(
        {
            "id": animal_id,
            "type": animal_type,
            "name": animal_name,
            "history": history,
            "profile": profile,

        }
    )


def character_chat(
    animal_id: str,
    message: str = "",
) -> str:
    db = firestore.client()
    # firestoreから履歴を読み込む
    doc_ref = db.collection("characters").document(animal_id)
    character_data = doc_ref.get().to_dict()
    history = character_data['history']
    message_data = {"role": "user", "content": message}
    history.append(message_data)
    doc_ref.update({"history": history})

    # chatを実施
    response = completion(copy.deepcopy(history))

    # firestoreにresponseを追加
    history.append(response)
    doc_ref.update({"history": history})

    return response


def completion(messages: list = []) -> dict:
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=messages,
    )
    response_message = {
        "role": "assistant",
        "content": response.choices[0].message.content
    }

    return response_message
