from abc import ABC, abstractmethod


class Collector(ABC):
    @abstractmethod
    def collect(self) -> str:
        raise NotImplementedError(
            "Collect method must be implemented by subclass")

    def __str__(self) -> str:
        return self.__class__.__name__.replace("Collector", "")
