from PyQt5.QtWidgets import QFileDialog, QCalendarWidget
from PyQt5.QtCore import pyqtSlot, QFileInfo
from src.views.ui_generated.admin.customer_detail import Ui_Form
from src.views.common.Common import *
import os
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.CustomerController import CustomerController
from src.controllers.admin.UserController import UserController
from src.models.customers import Customer
from src.models.images import Image
import shutil

class CustomerDetailWindow(QWidget):
    def __init__(self):
        super(CustomerDetailWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # khởi tạo controller
        self.customer_controller = CustomerController()
        self.user_controller = UserController()


    # def showEvent(self, event):
    #     self.category = self.category_controller.getDataByModel()
    #     if self.category:
    #         self.combobox_category.clear()
    #         for item in self.category:
    #             self.combobox_category.addItem(item.category_name)
    #     else:
    #         self.combobox_category.addItem("Không có dữ liệu")


    # xử lý chọn ảnh sản phẩm
    @pyqtSlot()
    def on_chose_image(self):
        try:

            # Hiển thị hộp thoại chọn tệp
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Images (*.png *.xpm *.jpg *.bmp)")
            file_dialog.setViewMode(QFileDialog.Detail)
            file_dialog.setFileMode(QFileDialog.ExistingFile)  # Chọn một tệp

            if file_dialog.exec_():
                self.product_image = file_dialog.selectedFiles()[0]

                # Lấy ra và hiển thị tên của ảnh
                file_info = QFileInfo(self.product_image)
                selected_file_name = file_info.fileName()
                self.product_image_le.setText(selected_file_name)
                # Chọn nhiều ảnh
                # self.product_image = file_dialog.selectedFiles()
                # for file_path in self.product_image:
                #     pixmap = QPixmap(file_path)
                #     self.image_label.setPixmap(pixmap)
                #     self.image_label.show()
        except Exception as E:
            print(E)
            return

    # xử lý hiển thị dialog date
    def show_date_dialog(self):
        try:
            date_dialog = DateDialog(self)
            date_dialog.date_selected.connect(self.on_selected_date)
            date_dialog.exec_()
        except Exception as E:
            print(E)
            return

    # hiển thị ngày tháng được chọn lên label
    def on_selected_date(self, selected_date):
        self.manufacture_date_le.setText(f"{selected_date.toString('dd/MM/yyyy')}")

    @pyqtSlot()
    def save_customer(self, form_mode, customer_id=None):
        name = self.ui.name_le.text().strip()
        account = self.ui.account_le.text().strip()
        self.clear_error()

        messages = {
            'nameEmpty': "Vui lòng nhập họ và tên.",
            'accountEmpty': "Vui lòng nhập thông tin tài khoản.",
            'accountExit': "Tài khoản đã tồn tại",
        }
        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self, {'name': name, 'account': account}, messages)
        if is_valid:
            return

        customer = Customer(name=name, account=account)
        message = self.user_controller.checkUserEmailOrPhone(username=account)
        if message:
            self.ui.error_account.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
            self.ui.error_account.setText(message)
            self.ui.account_le.setStyleSheet(Validate.BORDER_ERROR.value)
            return
        try:
            if form_mode == FormMode.ADD.value:
                if self.customer_controller.checkExitsDataWithModel(Customer.account, data=account):
                    self.ui.error_account.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_account.setText(messages["accountExit"])
                    self.ui.account_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.customer_controller.insertData(customer)
            elif form_mode == FormMode.EDIT.value:
                if self.customer_controller.checkExitsDataUpdateWithModel(Customer.account, data=account, model_id=customer_id):
                    self.ui.error_account.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_account.setText(messages["accountExit"])
                    self.ui.account_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                # self.order_controller.updateDataWithModelRelation(
                #     order,
                #     {
                #         'order_details': self.order_details,
                #     },
                #     [
                #         {
                #             'action': FormMode.EDIT.value,
                #             'data': self.product_update,
                #         }
                #     ]
                # )

            else:
                return
        except Exception as E:
            print(E)
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, customer_id):
        customer = self.customer_controller.getDataByIdWithModel(customer_id)
        if customer:
            self.ui.name_le.setText(customer.name)
            self.ui.account_le.setText(customer.account)

    # clear dữ liệu trên form
    def clear_form(self):
        self.clear_error()
        self.ui.name_le.setText("")
        self.ui.account_le.setText("")

    def clear_error(self):
        self.ui.name_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.account_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.error_name.setText("")
        self.ui.error_account.setText("")

    # xử lý xóa
    def handle_delete_event(self, customer_id):
        try:
            reply = message_box_delete("Nếu bạn xóa tài khoản này sẽ xóa toàn bộ các đơn hàng của tài khoản này. Bạn có chắc chắn muốn xóa?")
            if reply == QMessageBox.Yes:
                self.customer_controller.deleteDataWithModel(customer_id)
        except Exception as E:
            print(E)
            return False
        return True