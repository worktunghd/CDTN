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


class OrderStatus(Enum):
    PROGRESS = 0
    ORDER_SUCCESS = 1
    ORDER_FAIL = 2


class ProductSelected(Enum):
    # số lượng tối đa được chọn khi đặt hàng
    MAX_SELECTED = 50
    # số lượng tối thiểu để cảnh báo khi sản phẩm sắp hết
    WARNING_SELECTED = 10


class UserRole(Enum):
    EMPLOYEE = 0  # nhân viên
    WAREHOUSE_EMPLOYEE = 1  # nhân viên kho
    ADMIN = 2  # admin
