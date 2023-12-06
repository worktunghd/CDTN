from enum import Enum, auto


class Validate(Enum):
    EMPTY = 1
    NOT_MATCH = 2
    VALID = 3
    BORDER_ERROR = "border: 1px solid #ef5350;"
    COLOR_TEXT_ERROR = "color: #ef5350;"
    BORDER_VALID = "border: 1px solid #e0e5e9;"


class FormMode(Enum):
    ADD = 0
    EDIT = 1
    DELETE = 2


class SelectBox(Enum):
    DEFAULT = 'Không có dữ liệu'

