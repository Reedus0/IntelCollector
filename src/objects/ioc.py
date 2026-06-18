from enum import Enum, auto
import re


class IoCType(Enum):
    SHA256 = auto()
    SHA1 = auto()
    MD5 = auto()
    DOMAIN = auto()
    IP = auto()
    EMAIL = auto()
    CVE = auto()


class IoC():
    __type: IoCType
    __value: str

    def __init__(self, type: IoCType, value: str):
        self.__type = type

        if (not value):
            raise ValueError("Value cannot be empty")

        if (type == IoCType.SHA256 and len(value) != 64):
            raise ValueError("SHA256 hash must be 64 characters long")
        elif (type == IoCType.SHA1 and len(value) != 40):
            raise ValueError("SHA1 hash must be 40 characters long")
        elif (type == IoCType.MD5 and len(value) != 32):
            raise ValueError("MD5 hash must be 32 characters long")
        elif (type == IoCType.IP and not re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", value)):
            raise ValueError("Wrong IP address format")
        elif (type == IoCType.CVE and not re.match(r"^CVE-\d{4}-\d{4,}$", value)):
            raise ValueError("Wrong CVE format")

        self.__value = value

    def get_type(self) -> IoCType:
        return self.__type

    def get_value(self) -> str:
        return self.__value

    def __str__(self) -> str:
        return f"{self.__type}: {self.__value}"
