from .collector import Collector


class FileCollector(Collector):
    __path: str

    def __init__(self, path: str):
        self.__path = path

    def collect(self) -> str:
        try:
            with open(self.__path, "rb") as file:
                data = file.read()
                return data.decode("utf-8")

        except Exception as e:
            raise RuntimeError(f"Failed to collect data: {e}")
