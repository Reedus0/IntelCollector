import re

from .extractor import Extractor

KEYWORDS = [
    ".*yandex.*", "ya.*", ".*d[1i]sk.*",
    ".*es[1i]a.*", ".*365.*",
    ".*dr[0o]ne.*", ".*gos.*", ".*rkn.*",
    ".*r[0o]sk[0o]m.*", ".*nadz[0o]r.*", ".*sber.*",
    ".*vtb.*", ".*rzd.*", ".*cum.*", ".*milos.*",
    ".*rikardo.*", ".*alfa.*"
]


class REGRUExtractor(Extractor):
    def extract(self, data: str) -> list[str]:
        exp = r"(?:show_progress\(\)\">)(?:[a-zA-Z0-9-]+\[?\.\]?)+[a-zA-Z]{2,}"
        domains = [x[17:].lower() for x in re.findall(exp, data)]

        result = []

        for domain in domains:
            for keyword in KEYWORDS:
                if re.match(keyword, domain):
                    result.append(domain)
                    continue

        return list(set(result))
