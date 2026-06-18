from .ioc import IoC


class Report():

    __iocs: list[IoC]

    def __init__(self, iocs: list[IoC]) -> None:

        if (not len(iocs)):
            raise ValueError("IoC list cannot be empty")

        self.__iocs = iocs

    def get_iocs(self) -> list[IoC]:
        return self.__iocs
