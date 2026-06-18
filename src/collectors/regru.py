import requests

import re

from datetime import datetime, timedelta

from .collector import Collector


class REGRUCollector(Collector):
    def collect(self) -> str:
        try:

            result = ""

            yesterday = (datetime.now() - timedelta(days=1)
                         ).strftime("%Y-%m-%d")

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
            }

            url = f"https://statonline.ru/actions?search=&regfilter=&rows_per_page=200&page=1&order=ASC&sort_field=domain_name_idn&tld=ru&added=1&action_from={yesterday}&action_to={yesterday}"

            response = requests.get(url, headers=headers)
            response.encoding = 'cp1251'
            response.raise_for_status()

            result += response.text

            exp = r"Позиций: ([0-9]+)"

            total_pages = int((int(re.findall(exp, result)[0]) / 200) + 1)

            for i in range(1, total_pages):
                url = f"https://statonline.ru/actions?search=&regfilter=&rows_per_page=200&page={i}&order=ASC&sort_field=domain_name_idn&tld=ru&added=1&action_from={yesterday}&action_to={yesterday}"

                response = requests.get(url, headers=headers)
                response.encoding = 'cp1251'
                response.raise_for_status()

                result += response.text

            return result

        except requests.RequestException as e:
            raise RuntimeError(f"Failed to collect data from URL: {e}")
