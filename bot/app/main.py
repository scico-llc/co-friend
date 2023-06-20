# from dotenv import load_dotenv
# load_dotenv('../../.env')

from rocketry import Rocketry
from rocketry.args import TaskLogger
from rocketry.log import MinimalRecord
from rocketry.conds import cron
from redbird.repos import MemoryRepo
from firebase.firebase import initialize, fetch_random_two_animals
from worker.characters_bot import start_bot

app = Rocketry()

@app.setup()
def setup_app(task_logger=TaskLogger()):
    repo = MemoryRepo(model=MinimalRecord)
    task_logger.set_repo(repo)

@app.task(cron(minute="*/30"))
def start_chat():
    animals = fetch_random_two_animals()
    start_bot(animals)

@app.task(cron(minute="*/1"))
def check_cron():
    print('1min task')

if __name__ == "__main__":
    initialize()
    print('start bot') 
    app.run()