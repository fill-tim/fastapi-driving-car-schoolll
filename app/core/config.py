import os

from dotenv import load_dotenv

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
db_name = os.getenv("DB_NAME")
test_db_name = os.getenv("TEST_DB_NAME")


class Config:
    url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
    echo = True

    test_url = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{test_db_name}"
    test_echo = True


settings = Config()
