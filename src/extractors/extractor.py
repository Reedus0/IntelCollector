from abc import ABC, abstractmethod


class Extractor(ABC):

    @abstractmethod
    def extract(self, data: str) -> list[str]:
        raise NotImplementedError(
            "Extract method must be implemented by subclass")

    def __str__(self) -> str:
        return self.__class__.__name__.replace("Extractor", "")
