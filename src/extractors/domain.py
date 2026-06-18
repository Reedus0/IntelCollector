import re

from .extractor import Extractor


class DomainExtractor(Extractor):
    def extract(self, data: str) -> list[str]:
        exp = r"(?:[a-zA-Z0-9-]+\[?\.\]?)+[a-zA-Z]{2,}"
        domains = re.findall(exp, data)

        result = []

        for domain in domains:
            if "[" in domain:
                result.append(domain.replace("[.]", "."))

        return result
