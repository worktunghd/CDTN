import sys

from PyQt5.QtWidgets import QApplication

from src.views.common.Login import LoginWindow
# from main_window import MainWindow


def setQss(file_path, obj):
    """
    function for reading style file
    """
    with open(file_path, "r") as rf:
        style = rf.read()
        obj.setStyleSheet(style)

# 
if __name__ == '__main__':
    app = QApplication(sys.argv)

    setQss("ui/style.qss", app)

    window = LoginWindow()
    window.show()

    sys.exit(app.exec_())
