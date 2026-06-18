from abc import ABC, abstractmethod
from ..objects.report import Report


class Exporter(ABC):
    @abstractmethod
    def export(self, report: Report) -> None:
        raise NotImplementedError(
            "Export method must be implemented by subclass")
