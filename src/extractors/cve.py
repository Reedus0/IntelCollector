import re

from .extractor import Extractor


class CVEExtractor(Extractor):
    def extract(self, data: str) -> list[str]:
        exp = r"\bCVE-\d{4}-\d{4,7}\b"

        return re.findall(exp, data)
