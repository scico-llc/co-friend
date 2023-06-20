from firebase.firebase import initialize, fetch_random_two_animals
from worker.characters_bot import start_bot
from dotenv import load_dotenv


if __name__ == "__main__":
    initialize()
    animals = fetch_random_two_animals()
    start_bot(animals)