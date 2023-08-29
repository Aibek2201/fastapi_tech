from enum import StrEnum, auto


class WalletCurrency(StrEnum):
    USD = auto()
    KZT = auto()
    RUB = auto()


class GenderType(StrEnum):
    MALE = auto()
    FEMALE = auto()


class LocaleType(StrEnum):
    KZ = auto()
    RU = auto()
    EN = auto()