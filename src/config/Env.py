from os import getenv
from dotenv import load_dotenv


class Env:
    __ENV_PATH: str = ".env"

    def __init__(self):
        load_dotenv(self.__ENV_PATH)

    @classmethod
    def parse_boolean(cls, key: str) -> bool:
        """
        環境変数からboolean値を取得する

        Args:
            key (str): 環境変数のキー

        Returns:
            bool: 環境変数のbool値
        """
        return getenv(key).lower() == "true"
