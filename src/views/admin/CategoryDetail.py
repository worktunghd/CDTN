from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.category_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.CategoryController import CategoryController
from src.models.category import Category


class CategoryDetailWindow(QWidget):
    def __init__(self):
        super(CategoryDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.category_controller = CategoryController()

    @pyqtSlot()
    def save_category(self, form_mode, category_id=None):
        category_name = self.ui.category_name_le.text().strip()
        color_style = "color: #ef5350;"
        border_style = "border: 1px solid #ef5350;"
        # sét border mặc định cho input
        self.ui.category_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        # xóa error text
        self.ui.error_category_name.setText("")

        messages = {
            'category_nameEmpty': "Vui lòng nhập tên loại sản phẩm.",
            'category_nameExit': "Tên loại sản phẩm đã tồn tại.",
        }

        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self,{'category_name': category_name}, messages)
        if is_valid:
            return
        try:
            if form_mode == FormMode.ADD.value:
                if self.category_controller.checkExitsDataWithModel(Category.category_name, data=category_name):
                    self.ui.error_category_name.setStyleSheet(color_style)
                    self.ui.error_category_name.setText(messages["category_nameExit"])
                    self.ui.category_name_le.setStyleSheet(border_style)
                    return
                self.category_controller.insertData(Category(category_name=category_name))
            elif form_mode == FormMode.EDIT.value:
                if self.category_controller.checkExitsDataUpdateWithModel(Category.category_name, data=category_name, model_id=category_id):
                    self.ui.error_category_name.setStyleSheet(color_style)
                    self.ui.error_category_name.setText(messages["category_nameExit"])
                    self.ui.category_name_le.setStyleSheet(border_style)
                    return
                self.category_controller.updateDataWithModel(data={'category_name': category_name}, model_id=category_id)
            else:
                return
        except Exception as E:
            print(E)
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, category_id):
        category = self.category_controller.getDataByIdWithModel(category_id)
        if category:
            self.ui.category_name_le.setText(category.category_name)

    # clear dữ liệu trên form
    def clear_form(self):
        self.ui.category_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.error_category_name.setText("")
        self.ui.category_name_le.setText("")
