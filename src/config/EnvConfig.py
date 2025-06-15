from config.Env import Env


class EnvConfig(Env):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EnvConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # インスタンスは一度のみ初期化されるようにする
        if hasattr(self, "_initialized") and self._initialized:
            return
        super().__init__()
        self.__execute_reservation: bool = self.parse_boolean(
            "EXECUTE_RESERVATION"
        )
        self._initialized = True

    @property
    def is_execute_reservation(self) -> bool:
        """
        getter

        Returns:
            bool: 予約を実行するかどうか
        """
        return self.__execute_reservation
