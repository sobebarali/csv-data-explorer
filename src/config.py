import os
from dotenv import load_dotenv

load_dotenv()


SEGWISE_API_KEY = os.getenv("SEGWISE_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")

