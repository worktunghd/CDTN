from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QCompleter, QComboBox
from PyQt5.QtCore import QLocale, pyqtSlot
from src.views.ui_generated.admin.supplier_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.UserController import UserController
from src.controllers.admin.SupplierController import SupplierController
from src.models.Suppliers import Suppliers
from src.views.common.form_group_btn_order import Test


class SupplierDetailWindow(QWidget):
    def __init__(self):
        super(SupplierDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.supplier_controller = SupplierController()
        self.user_controller = UserController()
        self.mode = FormMode.ADD.value

    def showEvent(self, event):
        self.ui.dialog_supplier_title.setText("Thêm mới nhà cung cấp")

    @pyqtSlot()
    def save_supplier(self, form_mode, supplier_id=None):
        code = self.ui.code_le.text().strip()
        name = self.ui.name_le.text().strip()
        phone = self.ui.phone_le.text().strip()
        address = self.ui.address_le.text().strip()
        self.clear_error()
        messages = {
            'codeEmpty': "Vui lòng nhập mã đơn vị cung cấp",
            'codeExit': "Mã đơn vị cung cấp đã tồn tại",
            'nameEmpty': "Vui lòng nhập tên đơn vị cung cấp",
            'phoneValid': "Số điện thoại không đúng định dạng",
        }

        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self, {'code': code, 'name': name}, messages)

        if phone:
            if not self.user_controller.isValidPhoneNumber(phone):
                self.ui.error_phone.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                self.ui.error_phone.setText(messages["phoneValid"])
                self.ui.phone_le.setStyleSheet(Validate.BORDER_ERROR.value)
                return
        if is_valid:
            return

        supplier = Suppliers(code=code, supplier_name=name, phone_number=phone, address=address)

        try:
            if form_mode == FormMode.ADD.value:
                if self.supplier_controller.checkExitsDataWithModel(Suppliers.code, data=code):
                    self.ui.error_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_code.setText(messages["codeExit"])
                    self.ui.code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.supplier_controller.insertData(supplier)
            elif form_mode == FormMode.EDIT.value:
                if self.supplier_controller.checkExitsDataUpdateWithModel(Suppliers.code, data=code,
                                                                       model_id=supplier_id):
                    self.ui.error_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_code.setText(messages["codeExit"])
                    self.ui.code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                data = {'code': code, 'supplier_name': name, 'phone_number': phone, 'address': address}
                self.supplier_controller.updateDataWithModel(data=data, model_id=supplier_id)

            else:
                return
        except Exception as E:
            print(E)
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, supplier_id):
        self.ui.dialog_supplier_title.setText("Sửa nhà cung cấp")
        self.mode = FormMode.EDIT.value
        supplier = self.supplier_controller.getDataByModelIdWithRelation(supplier_id)
        if supplier:
            self.ui.code_le.setText(supplier.code)
            self.ui.name_le.setText(supplier.supplier_name)
            self.ui.phone_le.setText(supplier.phone_number)
            self.ui.address_le.setText(supplier.address)

    # clear dữ liệu trên form
    def clear_form(self):
        self.clear_error()
        self.ui.code_le.setText("")
        self.ui.name_le.setText("")
        self.ui.phone_le.setText("")
        self.ui.address_le.setText("")

    # clear lỗi
    def clear_error(self):
        self.ui.code_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.name_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.phone_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.error_code.setText("")
        self.ui.error_name.setText("")
        self.ui.error_phone.setText("")
        self.ui.error_address.setText("")

    # xử lý xóa
    def handle_delete_event(self, supplier_id):
        try:
            reply = message_box_delete()
            if reply == QMessageBox.Yes:
                self.supplier_controller.deleteDataWithModel(supplier_id)
        except Exception as E:
            print(E)
            return False
        return True