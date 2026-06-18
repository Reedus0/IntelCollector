import os

from dotenv import load_dotenv
from datetime import datetime, timedelta

from .data.collector import DataCollector
from .data.parser import DataParser
from .data.enricher import DataEnricher
from .data.exporter import DataExporter
from .data.extractor import DataExtractor

from .collectors.regru import REGRUCollector
from .extractors.regru import REGRUExtractor

from .exporters.misp import MISPExporter


def main():

    load_dotenv()

    collector = REGRUCollector()

    extractors = [
        REGRUExtractor()
    ]

    yesterday = (datetime.now() - timedelta(days=1)
                 ).strftime("%Y-%m-%d")
    event_name = f"Домены в зоне .RU за {yesterday}"

    exporter = MISPExporter(
        os.environ["MISP_URL"], os.environ["MISP_API_KEY"], event_name)

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
