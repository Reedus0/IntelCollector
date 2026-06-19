from .ioc import IoC
from .object import Object


class Report():

    __iocs: list[IoC]
    __objects: list[Object]

    def __init__(self):
        self.__iocs = []
        self.__objects = []

    def add_ioc(self, ioc: IoC) -> list[IoC]:
        self.__iocs.append(ioc)
        return self.__iocs

    def add_object(self, object: Object) -> list[Object]:
        self.__objects.append(object)
        return self.__objects

    def get_iocs(self) -> list[IoC]:
        return self.__iocs

    def get_objects(self) -> list[Object]:
        return self.__objects

    def __add__(self, other: "Report") -> "Report":
        if not isinstance(other, Report):
            return NotImplemented

        seen_values: set[str] = set()
        result = Report()

        for ioc in self.__iocs + other.get_iocs():
            if ioc.get_value() not in seen_values:
                seen_values.add(ioc.get_value())
                result.add_ioc(ioc)

        return result
