import re

from .extractor import Extractor


class IPExtractor(Extractor):
    def extract(self, data: str) -> list[str]:
        exp = r"\b(?:[1-2]?[0-9]{1,2}\[?\.\]?){3}[1-2]?[0-9]{1,2}\b"
        ips = re.findall(exp, data)

        result = []
        for ip in ips:
            if "[" in ip:
                result.append(ip.replace("[.]", "."))

        if not len(result):
            for ip in ips:
                result.append(ip)

        return list(set(result))
