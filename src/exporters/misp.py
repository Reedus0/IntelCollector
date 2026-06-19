import json
from typing import Any

import requests

from .exporter import Exporter
from ..objects.report import Report
from ..objects.ioc import IoC, IoCType


class MISPExporter(Exporter):
    __url: str
    __api_key: str
    __event_name: str

    def __init__(self, url: str, api_key: str, event_name: str = None) -> None:

        if not url:
            raise ValueError("URL cannot be None")

        if not api_key:
            raise ValueError("api_key cannot be None")

        self.__url = url.rstrip("/")
        self.__api_key = api_key
        self.__session = requests.Session()
        self.__session.headers.update({
            "Authorization": self.__api_key,
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

        if not event_name:
            event_name = "IntelCollector export"

        self.__event_name = event_name

    def export(self, report: Report) -> None:
        if not report:
            raise ValueError("Report cannot be None")

        iocs = report.get_iocs()
        if not iocs:
            raise ValueError("Report contains no IoCs to export")

        attributes = [self.__map_ioc_to_attribute(ioc) for ioc in iocs]

        self.__create_event(attributes)

    def __map_ioc_to_attribute(self, ioc: IoC) -> dict[str, Any]:
        ioc_type = ioc.get_type()
        value = ioc.get_value()
        tags = ioc.get_tags()

        if ioc_type == IoCType.IP:
            return {
                "type": "ip-dst",
                "category": "Network activity",
                "value": value,
                "to_ids": False,
                "Tag": [{"name": x} for x in tags],
            }

        if ioc_type == IoCType.DOMAIN:
            return {
                "type": "domain",
                "category": "Network activity",
                "value": value,
                "to_ids": False,
                "Tag": [{"name": x} for x in tags]
            }

        if ioc_type == IoCType.CVE:
            return {
                "type": "vulnerability",
                "category": "External analysis",
                "value": value,
                "to_ids": False,
                "Tag": [{"name": x} for x in tags]
            }

        if ioc_type == IoCType.MD5:
            return {
                "type": "md5",
                "category": "Payload delivery",
                "value": value,
                "to_ids": False,
                "Tag": [{"name": x} for x in tags]
            }

        if ioc_type == IoCType.SHA1:
            return {
                "type": "sha1",
                "category": "Payload delivery",
                "value": value,
                "to_ids": False,
                "Tag": [{"name": x} for x in tags]
            }

        if ioc_type == IoCType.SHA256:
            return {
                "type": "sha256",
                "category": "Payload delivery",
                "value": value,
                "to_ids": False,
                "Tag": [{"name": x} for x in tags]
            }

        return {
            "type": "text",
            "category": "External analysis",
            "value": value,
            "to_ids": False,
        }

    def __create_event(self, attributes: list[dict[str, Any]]) -> None:
        payload = {
            "Event": {
                "info": self.__event_name,
                "distribution": 0,
                "threat_level_id": 4,
                "analysis": 0,
                "Attribute": attributes,
            }
        }

        endpoint = f"{self.__url}/events"
        response = self.__session.post(
            endpoint, data=json.dumps(payload), verify=False)
        if response.status_code not in (200, 201):
            raise RuntimeError(
                f"MISP event creation failed: {response.status_code} {response.text}"
            )
