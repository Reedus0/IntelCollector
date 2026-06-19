from .enricher import Enricher
from ..objects.ioc import IoC, IoCType
from ..objects.report import Report
from ..objects.object import Object, ObjectType

import socket


class ResolveEnricher(Enricher):
    def enrich(self, ioc: IoC) -> Report:
        ioc_type = ioc.get_type()

        if ioc_type != IoCType.DOMAIN:
            return Report()

        ip_address = socket.gethostbyname(ioc.get_value())

        ip_ioc = IoC(IoCType.IP, ip_address)
        obj = Object(ObjectType.DOMAIN_IP, [ioc, ip_ioc])

        result = Report()
        result.add_object(obj)
        return result
