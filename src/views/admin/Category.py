from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow,QTableWidgetItem,QAbstractItemView, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.category import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.controllers.admin.CategoryController import CategoryController
from src.models.users import User


class CategoryWindow(QWidget):
    def __init__(self):
        super(CategoryWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.category_controller = CategoryController()
        self.table_category = self.ui.table_category
        self.table_category.horizontalHeader().setVisible(True)

    def show_category_table(self, btn_add):
        category_list = self.getAllCategory()
        self.table_category.setRowCount(0)
        if category_list:
            for index, item in enumerate(category_list):
                column_index = 0
                self.table_category.setRowCount(index + 1)
                self.table_category.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.table_category.setItem(index, column_index + 1, QTableWidgetItem(str(item.id)))
                self.table_category.setItem(index, column_index + 2, QTableWidgetItem(str(item.category_name)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "category")
                # edit_btn.clicked.connect(btn_add)
                # delete_btn.clicked.connect(
                #     lambda: self.on_row_click(self.table_category, FormMode.DELETE, self.page_index["USER_PAGE_DETAIL"]))
                # self.user_table.setCellWidget(index, column_index + 3, widget)

    def getAllCategory(self):
        return self.category_controller.getDataByModel()
