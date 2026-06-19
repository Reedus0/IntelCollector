from .enricher import Enricher
from ..objects.ioc import IoC, IoCType
from ..objects.report import Report


class TagEnricher(Enricher):
    def enrich(self, ioc: IoC) -> Report:
        ioc_type = ioc.get_type()

        match (ioc_type):
            case IoCType.MD5 | IoCType.SHA256 | IoCType.SHA1:
                ioc.add_tag("malware")
            case IoCType.DOMAIN | IoCType.IP:
                ioc.add_tag("c2")

        result = Report()
        result.add_ioc(ioc)
        return result
