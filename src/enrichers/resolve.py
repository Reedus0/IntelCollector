from .enricher import Enricher
from ..objects.ioc import IoC, IoCType
from ..objects.report import Report
from ..objects.relation import Relation, RelationType

import socket


class ResolveEnricher(Enricher):
    def enrich(self, ioc: IoC) -> Report:
        ioc_type = ioc.get_type()

        if ioc_type != IoCType.DOMAIN:
            return Report()

        ip_address = socket.gethostbyname(ioc.get_value())

        ip_ioc = IoC(IoCType.IP, ip_address)
        ip_ioc.add_tag("c2")
        obj = Relation(RelationType.DOMAIN_IP, [ioc, ip_ioc])

        result = Report()
        result.add_object(obj)
        return result
