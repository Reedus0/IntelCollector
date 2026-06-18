from ..collectors.collector import Collector


class DataCollector:
    __collector: Collector

    def __init__(self, collector: Collector) -> None:
        if (not collector):
            raise ValueError("Collector cannot be None")

        self.__collector = collector

    def collect(self, **kwargs) -> str:
        return self.__collector.collect(**kwargs)
