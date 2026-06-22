from ..extractors.extractor import Extractor


class DataExtractor:
    __data: str
    __extractors: list[Extractor]

    def __init__(self, data: str, extractors: list[Extractor]):
        if (not data):
            raise ValueError("Data cannot be empty")

        if (not len(extractors)):
            raise ValueError("Extractors list cannot be empty")

        self.__data = data
        self.__extractors = extractors

    def extract(self) -> dict[str, list[str]]:
        result = {}
        for extractor in self.__extractors:
            extracted_data = extractor.extract(self.__data)
            result[str(extractor)] = list(set(extracted_data))
        return result
