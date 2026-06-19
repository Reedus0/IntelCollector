from .enricher import Enricher
from ..objects.ioc import IoC, IoCType


class TagEnricher(Enricher):
    def enrich(self, ioc: IoC) -> IoC:
        ioc_type = ioc.get_type()

        match (ioc_type):
            case IoCType.MD5 | IoCType.SHA256 | IoCType.SHA1:
                ioc.add_tag("malware")
            case IoCType.DOMAIN | IoCType.IP:
                ioc.add_tag("c2")

        return ioc
