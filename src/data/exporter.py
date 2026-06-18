from ..objects.report import Report
from ..exporters.exporter import Exporter


class DataExporter:
    __report: Report
    __exporter: Exporter

    def __init__(self, report: Report, exporter: Exporter) -> None:
        if not report:
            raise ValueError("Report cannot be None")

        if not exporter:
            raise ValueError("Exporter cannot be None")

        self.__report = report
        self.__exporter = exporter

    def export(self) -> None:
        self.__exporter.export(self.__report)
