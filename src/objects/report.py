from .ioc import IoC
from .relation import Relation


class Report():

    __iocs: list[IoC]
    __relations: list[Relation]

    def __init__(self):
        self.__iocs = []
        self.__relations = []

    def add_ioc(self, ioc: IoC) -> list[IoC]:
        self.__iocs.append(ioc)
        return self.__iocs

    def add_relation(self, object: Relation) -> list[Relation]:
        self.__relations.append(object)
        return self.__relations

    def get_iocs(self) -> list[IoC]:
        return self.__iocs

    def get_objects(self) -> list[Relation]:
        return self.__relations

    def __add__(self, other: "Report") -> "Report":
        if not isinstance(other, Report):
            return NotImplemented

        self_iocs = self.get_iocs()

        for ioc in other.get_iocs():
            if ioc not in self_iocs:
                self_iocs.append(ioc)

        for obj in other.get_objects():
            self.add_relation(obj)

        return self
