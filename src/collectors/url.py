import requests

from .collector import Collector


class URLCollector(Collector):
    __url: str

    def __init__(self, url: str):
        self.__url = url

    def collect(self) -> str:
        try:

            host = self.__url.split("/")[2]
            referer = f"https://{host}/"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Referer": referer,
                "Host": host
            }

            response = requests.get(self.__url, headers=headers)
            response.raise_for_status()
            return response.text

        except requests.RequestException as e:
            raise RuntimeError(f"Failed to collect data from URL: {e}")
