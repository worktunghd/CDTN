from PyQt5.QtWidgets import QFileDialog, QCalendarWidget
from PyQt5.QtCore import pyqtSlot, QFileInfo
from src.views.ui_generated.admin.user_detail import Ui_user_form
from src.views.common.Common import *
import os
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.CustomerController import CustomerController
from src.controllers.admin.UserController import UserController
from src.models.users import User
from src.models.images import Image
import shutil

class UserDetailWindow(QWidget):
    def __init__(self):
        super(UserDetailWindow, self).__init__()
        self.ui = Ui_user_form()
        self.ui.setupUi(self)
        # khởi tạo controller
        self.user_controller = UserController()

    @pyqtSlot()
    def save_user(self, form_mode, user_id=None):
        name = self.ui.name_le.text().strip()
        username = self.ui.username_le.text().strip()
        password = self.ui.password_le.text().strip()
        confirm = self.ui.confirm_le.text().strip()
        level_text = self.ui.level.currentText()
        self.clear_error()

        messages = {
            'nameEmpty': "Vui lòng nhập họ và tên.",
            'usernameEmpty': "Vui lòng nhập thông tin tài khoản.",
            'usernameExit': "Tài khoản đã tồn tại.",
            'passwordEmpty': "Vui lòng nhập thông tin mật khẩu.",
            'confirmEmpty': "Vui lòng nhập lại mật khẩu.",
            'confirmNotMatch': "Mật  khẩu không trùng khớp.",
        }
        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self, {'name': name, 'username': username, 'password': password, 'confirm': confirm}, messages)
        if is_valid:
            return

        if password != confirm:
            self.ui.error_confirm.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
            self.ui.error_confirm.setText(messages["confirmNotMatch"])
            self.ui.confirm_le.setStyleSheet(Validate.BORDER_ERROR.value)
            return

        user_controller = UserController()
        message = user_controller.checkUserEmailOrPhone(username=username)
        if message:
            self.ui.error_username.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
            self.ui.error_username.setText(message)
            self.ui.username_le.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
            return
        if level_text == 'Nhân viên':
            level = UserRole.EMPLOYEE.value
        elif level_text == 'Nhân viên kho':
            level = UserRole.WAREHOUSE_EMPLOYEE.value
        else:
            level = UserRole.ADMIN.value
        if form_mode == FormMode.ADD.value:
            if user_controller.checkExitsUser(username=username):
                self.ui.error_username.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                self.ui.error_username.setText(messages["usernameExit"])
                self.ui.username_le.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                return
            user = User(name=name, username=username, password=password, level=level)
            user_controller.saveUser(user=user)
        elif form_mode == FormMode.EDIT.value:
            if user_controller.checkExitsUserUpdate(username=username, user_id=user_id):
                self.ui.error_username.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                self.ui.error_username.setText(messages["usernameExit"])
                self.ui.username_le.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                return
            user = {'username': username, 'name': name, 'password': password, 'level': level}
            user_controller.updateUserWithModel(data=user, user_id=user_id)
        return True

    # gán các giá trị lên form
    def handle_edit_event(self, user_id):
        user = self.user_controller.getDataByIdWithModel(user_id)
        if user:
            self.ui.name_le.setText(user.name)
            self.ui.username_le.setText(user.username)
            self.ui.password_le.setText(user.password)
            self.ui.confirm_le.setText(user.password)

    # xử lý xóa
    def handle_delete_event(self, user_id):
        try:
            reply = message_box_delete()
            if reply == QMessageBox.Yes:
                self.user_controller.deleteDataWithModel(user_id)
        except Exception as E:
            print(E)
            return False
        return True


    # clear dữ liệu trên form
    def clear_form(self):
        self.ui.username_le.setText("")
        self.ui.password_le.setText("")
        self.ui.confirm_le.setText("")
        self.ui.name_le.setText("")
        self.clear_error()

    def clear_error(self):
        self.ui.name_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.username_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.confirm_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.password_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.error_name.setText("")
        self.ui.error_username.setText("")
        self.ui.error_password.setText("")
        self.ui.error_confirm.setText("")
