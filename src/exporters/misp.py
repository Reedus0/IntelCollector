from typing import Any

import urllib3
from pymisp import MISPEvent, MISPObject, PyMISP, MISPAttribute

from .exporter import Exporter
from ..objects.report import Report
from ..objects.ioc import IoC, IoCType
from ..objects.relation import Relation, RelationType


class MISPExporter(Exporter):
    __misp: PyMISP
    __event_name: str

    def __init__(
        self,
        url: str,
        api_key: str,
        event_name: str = None,
    ):
        if not url:
            raise ValueError("URL cannot be None")

        if not api_key:
            raise ValueError("api_key cannot be None")

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.__misp = PyMISP(
            url.rstrip("/"),
            api_key,
            ssl=False,
            http_headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
        )

        if not event_name:
            event_name = "IntelCollector export"

        self.__event_name = event_name

    def export(self, report: Report) -> None:
        if not report:
            raise ValueError("Report cannot be None")

        iocs = report.get_iocs()
        objects = report.get_objects()

        if not iocs and not objects:
            raise ValueError("Report contains no IoCs or Relations to export")

        event = MISPEvent(
            info=self.__event_name,
            distribution=0,
            threat_level_id=4,
            analysis=0,
        )
        created_event = self.__misp.add_event(event, pythonify=True)

        for ioc in iocs:
            misp_attribute = self.__map_ioc_to_misp_attribute(ioc)
            self.__misp.add_attribute(created_event, misp_attribute)

        for obj in objects:
            misp_object = self.__map_obejct_to_misp_object(obj)
            self.__misp.add_object(created_event, misp_object)

    def __map_ioc_to_misp_attribute(self, ioc: IoC, object_relation: str | None = None) -> MISPAttribute:
        ioc_type = ioc.get_type()
        value = ioc.get_value()
        tags = ioc.get_tags()

        attribute: dict[str, Any] = {
            "type": "text",
            "category": "External analysis",
            "value": value,
            "to_ids": False,
        }

        if ioc_type == IoCType.IP:
            attribute["type"] = "ip-dst"
            attribute["category"] = "Network activity"
        elif ioc_type == IoCType.DOMAIN:
            attribute["type"] = "domain"
            attribute["category"] = "Network activity"
        elif ioc_type == IoCType.CVE:
            attribute["type"] = "vulnerability"
            attribute["category"] = "External analysis"
        elif ioc_type == IoCType.MD5:
            attribute["type"] = "md5"
            attribute["category"] = "Payload delivery"
        elif ioc_type == IoCType.SHA1:
            attribute["type"] = "sha1"
            attribute["category"] = "Payload delivery"
        elif ioc_type == IoCType.SHA256:
            attribute["type"] = "sha256"
            attribute["category"] = "Payload delivery"

        if tags:
            attribute["Tag"] = [{"name": x} for x in tags]

        if object_relation:
            attribute["object_relation"] = object_relation

        result = MISPAttribute()
        result.from_dict(**attribute)

        if tags:
            result.Tag = [{"name": tag} for tag in tags]

        return result

    def __map_obejct_to_misp_object(self, obj: Relation) -> MISPObject:
        object_type = obj.get_type()

        if object_type == RelationType.DOMAIN_IP:
            misp_object = MISPObject("domain-ip")

            for ioc in obj.get_iocs():
                if ioc.get_type() == IoCType.DOMAIN:
                    relation = "domain"
                elif ioc.get_type() == IoCType.IP:
                    relation = "ip"
                else:
                    raise ValueError(
                        f"Unsupported IoC type in object: {ioc.get_type()}"
                    )

                misp_object.add_attribute(
                    object_relation=relation,
                    simple_value=ioc.get_value(),
                )

            return misp_object

        raise ValueError(f"Unsupported object type: {object_type}")
