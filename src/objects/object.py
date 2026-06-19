from enum import Enum, auto

from .ioc import IoC


class ObjectType(Enum):
    DOMAIN_IP = auto()


class Object:

    __type: ObjectType
    __iocs: list[IoC]

    def __init__(self, type: ObjectType, iocs: list[IoC]):

        if not len(iocs):
            raise ValueError("IoCs cannot be empty")

        self.__iocs = iocs
        self.__type = type

    def get_type(self) -> ObjectType:
        return self.__type

    def get_iocs(self) -> list[IoC]:
        return self.__iocs
