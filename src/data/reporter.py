from ..objects.ioc import IoC, IoCType
from ..objects.report import Report


class DataReporter:
    __data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]) -> None:
        self.__data = data

    def parse(self) -> Report:
        iocs = []

        if ("IP" in self.__data):
            for ip in self.__data["IP"]:
                iocs.append(IoC(IoCType.IP, ip))

        if ("Hash" in self.__data):
            for hash in self.__data["Hash"]:
                if (len(hash) == 32):
                    iocs.append(IoC(IoCType.MD5, hash))
                elif (len(hash) == 40):
                    iocs.append(IoC(IoCType.SHA1, hash))
                elif (len(hash) == 64):
                    iocs.append(IoC(IoCType.SHA256, hash))

        if ("CVE" in self.__data):
            for cve in self.__data["CVE"]:
                iocs.append(IoC(IoCType.CVE, cve))

        if ("Domain" in self.__data):
            for domain in self.__data["Domain"]:
                iocs.append(IoC(IoCType.DOMAIN, domain))

        if ("REGRU" in self.__data):
            for domain in self.__data["REGRU"]:
                iocs.append(IoC(IoCType.DOMAIN, domain))

        result = Report(iocs)

        return result
