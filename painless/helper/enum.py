from enum import StrEnum


class RegexPatternEnum(StrEnum):
    IRAN_PHONE_NUMBER = r'^(?:\+98|0)?9\d{9}$'
    NAME = r'^[a-zA-Z\s]+$'
    DATE = r'^\d{4}-\d{2}-\d{2}$'
    GENDER = r'(?:m|M|male|Male|f|F|female|Female|FEMALE|MALE|Not prefer to say)$'
    STUDENT_NUMBER = r'^\d{10}$'
    EDUCATIONAL_LEVEL = r"^(high school|college|bachelor|master|phd)$"


class Emoji(StrEnum):
    STUDENT = '\U0001f9d1'
