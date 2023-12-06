from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow,QTableWidgetItem,QAbstractItemView, QApplication, QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.product import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.controllers.admin.UserController import UserController
from src.models.users import User


class ProductWindow(QWidget):
    def __init__(self):
        super(ProductWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

