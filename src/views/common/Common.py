# messagebox.py
from PyQt5.QtWidgets import QMessageBox, QPushButton, QWidget, QCalendarWidget, QVBoxLayout, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, pyqtSignal, QLocale, Qt
import uuid
from src.enums.enums import *

def warningMessagebox(content):
    """
    Common messagebox function
    """
    msgbox = QMessageBox()
    msgbox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
    msgbox.setIconPixmap(QPixmap("./static/icon/exclamation-48.ico"))
    msgbox.setWindowTitle("Warning")
    msgbox.setText(content)
    msgbox.setStandardButtons(QMessageBox.Close)

    msgbox.exec_()


# validate form input not empty
def validateEmpty(self, data: dict, messages: dict):
    result = []
    try:
        for key, value in data.items():
            label_name = f"error_{key}"
            label = getattr(self.ui, label_name, None)
            input_name = f"{key}_le"
            input_text = getattr(self.ui, input_name, None)
            if not value:
                message = messages[f"{key}Empty"]
                result.append(message)
                if label:
                    label.setText(message)
                    label.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                if input_text:
                    input_text.setStyleSheet(Validate.BORDER_ERROR.value)
            else:
                if label:
                    label.setText("")
                if input_text:
                    input_text.setStyleSheet(Validate.BORDER_VALID.value)

    except Exception as E:
        print(E)
        return
    return result


# tạo view button xóa sửa trên row
def generate_action_row(row_id, model):
    horizontalLayout = QtWidgets.QHBoxLayout()
    horizontalLayout.setContentsMargins(0, 0, 0, 0)
    horizontalLayout.setSpacing(0)
    horizontalLayout_3 = QtWidgets.QHBoxLayout()
    spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    horizontalLayout_3.addItem(spacerItem)
    widget_2 = QtWidgets.QWidget()
    horizontalLayout_4 = QtWidgets.QHBoxLayout(widget_2)
    horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_4.setSpacing(0)
    # button sửa
    pushButton = QPushButton(widget_2)
    pushButton.setMinimumSize(QtCore.QSize(36, 36))
    pushButton.setMaximumSize(QtCore.QSize(36, 36))
    pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    pushButton.setText("")
    icon = QtGui.QIcon("resources/icon/pen.svg")
    pushButton.setIcon(icon)
    pushButton.setIconSize(QtCore.QSize(24, 24))
    pushButton.setObjectName(f"row_edit_{model}_{row_id}")
    pushButton.setToolTip("Sửa")
    horizontalLayout_4.addWidget(pushButton)
    # button xóa
    pushButton_2 = QtWidgets.QPushButton(widget_2)
    pushButton_2.setMinimumSize(QtCore.QSize(36, 36))
    pushButton_2.setMaximumSize(QtCore.QSize(36, 36))
    pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    pushButton_2.setText("")
    pushButton_2.setToolTip("Xóa")
    icon1 = QtGui.QIcon("resources/icon/red-delete-10433.svg")
    pushButton_2.setIcon(icon1)
    pushButton_2.setIconSize(QtCore.QSize(24, 24))
    pushButton_2.setObjectName(f"row_delete_{model}_{row_id}")
    # # kết nối click button xóa với hàm xóa
    # pushButton_2.clicked.connect(
    #     lambda: selon_row_click(self.user_table, FormMode.DELETE, self.page_index["USER_PAGE_DETAIL"], FormMode.EDIT))
    horizontalLayout_4.addWidget(pushButton_2)
    horizontalLayout_3.addWidget(widget_2)
    horizontalLayout_3.addWidget(widget_2, 0, QtCore.Qt.AlignTop)
    spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
    horizontalLayout_3.addItem(spacerItem1)
    horizontalLayout.addLayout(horizontalLayout_3)

    widget = QWidget()
    widget.setContentsMargins(0, 0, 0, 0)
    widget.setLayout(horizontalLayout)
    widget.setObjectName(f"row_{model}_{row_id}")
    return widget, pushButton, pushButton_2


class DateDialog(QDialog):
    date_selected = pyqtSignal(QDate)

    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)

        self.calendar_widget = QCalendarWidget(self)
        self.calendar_widget.selectionChanged.connect(self.handle_date_selection)
        layout.addWidget(self.calendar_widget)

    def handle_date_selection(self):
        selected_date = self.calendar_widget.selectedDate()
        self.date_selected.emit(selected_date)
        # Ẩn QDialog khi người dùng chọn một ngày
        self.hide()


# tạo tên file duy nhất
def generate_unique_filename(file_name):
    unique_filename = f"{str(uuid.uuid4())}_{file_name}"
    return unique_filename


# Định dạng tiền
def formatCurrency(value, suffix):
    locale = QLocale(QLocale.Vietnamese, QLocale.Vietnam)
    return f"{locale.toString(value)}{suffix}"


# tạo group button trên giỏ hàng
def generate_group_order_btn(row):
    widget = QtWidgets.QWidget()
    widget.setContentsMargins(0, 0, 0, 0)
    widget.setStyleSheet("#order_group_btn{\n"
                                  "    border: 1px solid #e5e5e5;\n"
                                  "    border-left: 0;\n"
                                  "    border-right: 0;\n"
                                  "}\n"
                                  "\n"
                                  "#group_order_btn QPushButton{\n"
                                  "    min-width: 7px;\n"
                                  "    max-width: 7px;\n"
                                  "    width: 7x;\n"
                                  "    min-height: 22px;\n"
                                  "    max-height: 22px;\n"
                                  "    border: none;\n"
                                  "    text-align: center;\n"
                                  "    border-left: 1px solid #e5e5e5;\n"
                                  "    border-right: 1px solid #e5e5e5;\n"
                                  "    border-radius: 0;\n"
                                  "}\n"
                                  "#group_order_btn QSpinBox{\n"
                                  "    border-radius: 0;\n"
                                  "    background: transparent;\n"
                                  "    max-width: 35px;\n"
                                  "    min-width: 35px;\n"
                                  "    width: 35px;\n"
                                  "    padding: 0;\n"
                                  "    margin: 0;\n"
                                  "    min-height: 0px;\n"
                                  "    max-height: 0px;\n"
                                  "    height: 28px;\n"
                                  "    border: none;\n"
                                  "    color: #222;\n"
                                  "    font-size: 13px;\n"
                                  "}\n")
    widget.setObjectName("group_order_btn")
    horizontalLayout_2 = QtWidgets.QHBoxLayout(widget)
    horizontalLayout_2.setObjectName("horizontalLayout_2")
    horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_2.setSpacing(0)
    order_group_btn = QtWidgets.QWidget(widget)
    order_group_btn.setMinimumSize(QtCore.QSize(0, 28))
    order_group_btn.setMaximumSize(QtCore.QSize(100, 28))
    order_group_btn.setObjectName("order_group_btn")
    horizontalLayout_3 = QtWidgets.QHBoxLayout(order_group_btn)
    horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
    horizontalLayout_3.setSpacing(0)
    horizontalLayout_3.setObjectName("horizontalLayout_3")
    horizontalLayout = QtWidgets.QHBoxLayout()
    horizontalLayout.setSpacing(0)
    horizontalLayout.setObjectName("horizontalLayout")
    minus_order_btn = QtWidgets.QPushButton(order_group_btn)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(minus_order_btn.sizePolicy().hasHeightForWidth())
    minus_order_btn.setSizePolicy(sizePolicy)
    minus_order_btn.setMinimumSize(QtCore.QSize(29, 28))
    minus_order_btn.setMaximumSize(QtCore.QSize(28, 28))
    minus_order_btn.setText("-")
    minus_order_btn.setCursor(QtGui.QCursor(Qt.PointingHandCursor))
    minus_order_btn.setObjectName(f"minus_order_{row}_btn")
    horizontalLayout.addWidget(minus_order_btn)
    quantity_order = QtWidgets.QSpinBox(order_group_btn)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(quantity_order.sizePolicy().hasHeightForWidth())
    quantity_order.setSizePolicy(sizePolicy)
    quantity_order.setMinimumSize(QtCore.QSize(35, 0))
    quantity_order.setMaximumSize(QtCore.QSize(35, 20))
    quantity_order.setLayoutDirection(Qt.LeftToRight)
    quantity_order.setFrame(False)
    quantity_order.setAlignment(Qt.AlignCenter)
    quantity_order.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
    quantity_order.setObjectName(f"quantity_{row}_order")
    quantity_order.setMinimum(1)
    quantity_order.setMaximum(50)
    horizontalLayout.addWidget(quantity_order, 0, Qt.AlignTop)
    plus_order_btn = QtWidgets.QPushButton(order_group_btn)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(plus_order_btn.sizePolicy().hasHeightForWidth())
    plus_order_btn.setSizePolicy(sizePolicy)
    plus_order_btn.setMinimumSize(QtCore.QSize(29, 28))
    plus_order_btn.setMaximumSize(QtCore.QSize(28, 28))
    plus_order_btn.setText("+")
    plus_order_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    plus_order_btn.setObjectName(f"plus_order_{row}_btn")
    horizontalLayout.addWidget(plus_order_btn)
    horizontalLayout_3.addLayout(horizontalLayout)
    horizontalLayout_2.addWidget(order_group_btn)
    return widget, minus_order_btn, plus_order_btn, quantity_order
