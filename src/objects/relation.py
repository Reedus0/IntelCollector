from enum import Enum, auto

from .ioc import IoC


class RelationType(Enum):
    DOMAIN_IP = auto()


class Relation:

    __type: RelationType
    __iocs: list[IoC]

    def __init__(self, type: RelationType, iocs: list[IoC]):

        if not len(iocs):
            raise ValueError("IoCs cannot be empty")

        self.__iocs = iocs
        self.__type = type

    def get_type(self) -> RelationType:
        return self.__type

    def get_iocs(self) -> list[IoC]:
        return self.__iocs
