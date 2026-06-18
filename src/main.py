import os

from dotenv import load_dotenv

from .data.collector import DataCollector
from .data.parser import DataParser
from .data.enricher import DataEnricher
from .data.exporter import DataExporter
from .data.extractor import DataExtractor

from .collectors.url import URLCollector

from .extractors.ip import IPExtractor
from .extractors.hash import HashExtractor
from .extractors.cve import CVEExtractor
from .extractors.domain import DomainExtractor

from .exporters.misp import MISPExporter


def main():

    # https://rt-solar.ru/solar-4rays/blog/6523/
    # https://bi.zone/expertise/blog/fluffy-wolf-ispytal-novinki-na-rossiyskikh-kompaniyakh/
    # https://securelist.ru/tr/hacktivists-broaden-attack-geography/115916/

    load_dotenv()

    collector = \
        URLCollector(
            "https://bi.zone/expertise/blog/fluffy-wolf-ispytal-novinki-na-rossiyskikh-kompaniyakh/")

    extractors = [
        IPExtractor(),
        HashExtractor(),
        CVEExtractor(),
        DomainExtractor()
    ]

    exporter = MISPExporter(os.environ["MISP_URL"], os.environ["MISP_API_KEY"])

    data_collector = DataCollector(collector=collector)
    raw_data = data_collector.collect()

    data_extractor = DataExtractor(raw_data, extractors=extractors)
    extracted_data = data_extractor.extract()

    data_parser = DataParser(extracted_data)
    iocs = data_parser.parse()

    data_enricher = DataEnricher(iocs)
    report = data_enricher.enrich()

    data_exporter = DataExporter(report, exporter=exporter)
    data_exporter.export()


if __name__ == "__main__":
    main()
