import re

from .extractor import Extractor

KEYWORDS = [
    "yandex", "ya", "disk",
    "esia", "365", "mail",
    "vpn", "drone", "gos",
    "rkn", "roskom", "nadzor",
    "sber", "vtb"
]


class REGRUExtractor(Extractor):
    def extract(self, data: str) -> list[str]:
        exp = r"(?:show_progress\(\)\">)(?:[a-zA-Z0-9-]+\[?\.\]?)+[a-zA-Z]{2,}"
        domains = [x[17:].lower() for x in re.findall(exp, data)]

        result = []

        for domain in domains:
            for keyword in KEYWORDS:
                if keyword in domain:
                    result.append(domain)
                    continue

        return result
