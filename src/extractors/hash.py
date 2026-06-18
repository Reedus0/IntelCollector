import re

from .extractor import Extractor


class HashExtractor(Extractor):
    def extract(self, data: str) -> list[str]:
        patterns = {
            "md5": r"\b[a-fA-F0-9]{32}\b",
            "sha1": r"\b[a-fA-F0-9]{40}\b",
            "sha256": r"\b[a-fA-F0-9]{64}\b",
        }

        results = []

        for pattern in patterns.values():
            results += [h.lower() for h in re.findall(pattern, data)]

        return list(set(results))
