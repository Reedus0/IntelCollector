from abc import ABC, abstractmethod

from ..objects.ioc import IoC
from ..objects.report import Report


class Enricher(ABC):

    @abstractmethod
    def enrich(self, ioc: IoC) -> Report:
        raise NotImplementedError(
            "Extract method must be implemented by subclass")

    def __str__(self) -> str:
        return self.__class__.__name__.replace("Enricher", "")
