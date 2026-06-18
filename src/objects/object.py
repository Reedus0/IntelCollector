from .ioc import IoC


class Object:

    __ioc: IoC

    def __init__(self, ioc: IoC) -> None:
        self.__ioc = ioc
