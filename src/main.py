import os
import argparse

from dotenv import load_dotenv

from .data.collector import DataCollector
from .data.reporter import DataReporter
from .data.enricher import DataEnricher
from .data.exporter import DataExporter
from .data.extractor import DataExtractor

from .collectors.url import URLCollector
from .collectors.file import FileCollector

from .extractors.ip import IPExtractor
from .extractors.hash import HashExtractor
from .extractors.cve import CVEExtractor
from .extractors.domain import DomainExtractor

from .enrichers.tag import TagEnricher
from .enrichers.resolve import ResolveEnricher

from .exporters.misp import MISPExporter


COLLECTORS = {
    "url": URLCollector,
    "file": FileCollector
}

EXPORTERS = {
    "misp": MISPExporter,
}


def main():

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(
        dest="source",
        required=True,
    )

    url_parser = subparsers.add_parser("url")
    url_parser.add_argument("url")

    file_parser = subparsers.add_parser("file")
    file_parser.add_argument("path")

    args = parser.parse_args()

    # parser.add_argument(
    #     "--export",
    #     required=True,
    #     choices=EXPORTERS.keys(),
    #     help="Exporter to use."
    # )

    args = parser.parse_args()
    params = vars(args)
    source = params["source"]
    params.pop("source")

    load_dotenv()

    # exporter = EXPORTERS[args.export]
    collector = COLLECTORS[source](**params)
    exporter = MISPExporter(os.environ["MISP_URL"], os.environ["MISP_API_KEY"])

    extractors = [
        IPExtractor(),
        HashExtractor(),
        CVEExtractor(),
        DomainExtractor()
    ]

    enrichers = [
        TagEnricher(),
        ResolveEnricher()
    ]

    data_collector = DataCollector(collector=collector)
    raw_data = data_collector.collect()

    data_extractor = DataExtractor(raw_data, extractors=extractors)
    extracted_data = data_extractor.extract()

    data_parser = DataReporter(extracted_data)
    report = data_parser.parse()

    data_enricher = DataEnricher(report, enrichers=enrichers)
    report = data_enricher.enrich()

    data_exporter = DataExporter(report, exporter=exporter)
    data_exporter.export()


if __name__ == "__main__":
    main()
