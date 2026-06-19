from ..objects.ioc import IoC, IoCType
from ..objects.report import Report


class DataReporter:
    __data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]):
        self.__data = data

    def parse(self) -> Report:
        result = Report()

        if ("IP" in self.__data):
            for ip in self.__data["IP"]:
                result.add_ioc(IoC(IoCType.IP, ip))

        if ("Hash" in self.__data):
            for hash in self.__data["Hash"]:
                if (len(hash) == 32):
                    result.add_ioc(IoC(IoCType.MD5, hash))
                elif (len(hash) == 40):
                    result.add_ioc(IoC(IoCType.SHA1, hash))
                elif (len(hash) == 64):
                    result.add_ioc(IoC(IoCType.SHA256, hash))

        if ("CVE" in self.__data):
            for cve in self.__data["CVE"]:
                result.add_ioc(IoC(IoCType.CVE, cve))

        if ("Domain" in self.__data):
            for domain in self.__data["Domain"]:
                result.add_ioc(IoC(IoCType.DOMAIN, domain))

        if ("REGRU" in self.__data):
            for domain in self.__data["REGRU"]:
                result.add_ioc(IoC(IoCType.DOMAIN, domain))

        return result
