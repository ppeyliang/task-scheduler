import os
from dotenv import load_dotenv


load_dotenv()

TODO_URL = os.getenv('TODO_URL')
TODO_TOKEN = os.getenv('TODO_TOKEN')
