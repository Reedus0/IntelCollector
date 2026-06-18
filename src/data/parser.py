from ..objects.ioc import IoC, IoCType


class DataParser:
    __data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]) -> None:
        self.__data = data

    def parse(self) -> list[IoC]:
        result = []

        if ("IP" in self.__data):
            for ip in self.__data["IP"]:
                result.append(IoC(IoCType.IP, ip))

        if ("Hash" in self.__data):
            for hash in self.__data["Hash"]:
                if (len(hash) == 32):
                    result.append(IoC(IoCType.MD5, hash))
                elif (len(hash) == 40):
                    result.append(IoC(IoCType.SHA1, hash))
                elif (len(hash) == 64):
                    result.append(IoC(IoCType.SHA256, hash))

        if ("CVE" in self.__data):
            for cve in self.__data["CVE"]:
                result.append(IoC(IoCType.CVE, cve))

        if ("Domain" in self.__data):
            for domain in self.__data["Domain"]:
                result.append(IoC(IoCType.DOMAIN, domain))

        if ("REGRU" in self.__data):
            for domain in self.__data["REGRU"]:
                result.append(IoC(IoCType.DOMAIN, domain))

        return result
