from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel


from src.views.ui_generated.admin.toast import Ui_Form_gourp_btn


class Test(QWidget):
    def __init__(self):
        super(Test, self).__init__()
        self.ui = Ui_Form_gourp_btn()
        self.ui.setupUi(self)

