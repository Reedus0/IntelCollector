from ..objects.ioc import IoC, IoCType


class DataParser:
    __data: dict[str, list[str]]

    def __init__(self, data: dict[str, list[str]]) -> None:
        self.__data = data

    def parse(self) -> list[IoC]:
        result = []

        for ip in self.__data["IP"]:
            result.append(IoC(IoCType.IP, ip))

        for hash in self.__data["Hash"]:
            if (len(hash) == 32):
                result.append(IoC(IoCType.MD5, hash))
            elif (len(hash) == 40):
                result.append(IoC(IoCType.SHA1, hash))
            elif (len(hash) == 64):
                result.append(IoC(IoCType.SHA256, hash))

        for cve in self.__data["CVE"]:
            result.append(IoC(IoCType.CVE, cve))
        for domain in self.__data["Domain"]:
            result.append(IoC(IoCType.DOMAIN, domain))

        return result
