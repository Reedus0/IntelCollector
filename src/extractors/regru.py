import re

from .extractor import Extractor


class REGRUExtractor(Extractor):

    __keywords: list[str] | None

    def __init__(self, keywords: list[str] | None = None):
        self.__keywords = keywords

    def extract(self, data: str) -> list[str]:
        exp = r"(?:show_progress\(\)\">)(?:[a-zA-Z0-9-]+\[?\.\]?)+[a-zA-Z]{2,}"
        domains = [x[17:].lower() for x in re.findall(exp, data)]

        result = []

        if not self.__keywords:
            return domains

        for domain in domains:
            for keyword in self.__keywords:
                if re.match(keyword, domain):
                    result.append(domain)
                    continue

        return list(set(result))
