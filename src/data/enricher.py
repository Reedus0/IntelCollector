from ..objects.report import Report
from ..enrichers.enricher import Enricher


class DataEnricher:
    __report: Report
    __enrichers: list[Enricher]

    def __init__(self, report: Report, enrichers: list[Enricher]):
        self.__report = report
        self.__enrichers = enrichers

    def enrich(self) -> Report:
        for ioc in self.__report.get_iocs():
            for enricher in self.__enrichers:
                self.__report += enricher.enrich(ioc)

        return self.__report
