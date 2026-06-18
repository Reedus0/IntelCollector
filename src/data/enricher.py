from ..objects.ioc import IoC
from ..objects.report import Report


class DataEnricher:
    __data: list[IoC]

    def __init__(self, data: list[IoC]) -> None:
        if not len(data):
            raise ValueError("Data cannot be None or empty")
        self.__data = data

    def enrich(self) -> Report:
        report = Report(self.__data)
        return report
