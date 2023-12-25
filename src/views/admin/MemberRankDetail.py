from PyQt5.QtWidgets import QFileDialog, QCalendarWidget
from PyQt5.QtCore import pyqtSlot, QFileInfo
from src.views.ui_generated.admin.member_rank_detail import Ui_Form
from src.views.common.Common import *
import os
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.CustomerController import CustomerController
from src.controllers.admin.MemberRankController import MemberRankController
from src.models.member_ranks import MemberRank
from src.models.images import Image
import shutil

class MemberRankDetailWindow(QWidget):
    def __init__(self):
        super(MemberRankDetailWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # khởi tạo controller
        self.customer_controller = CustomerController()
        self.member_rank_controller = MemberRankController()


    # def showEvent(self, event):
    #     self.category = self.category_controller.getDataByModel()
    #     if self.category:
    #         self.combobox_category.clear()
    #         for item in self.category:
    #             self.combobox_category.addItem(item.category_name)
    #     else:
    #         self.combobox_category.addItem("Không có dữ liệu")

    @pyqtSlot()
    def save_member_rank(self, form_mode, customer_id=None):
        code = self.ui.code_le.text().strip()
        name = self.ui.name_le.text().strip()
        spending = self.ui.spending_le.value()
        discount = self.ui.discount_le.value()
        self.clear_error()

        messages = {
            'nameEmpty': "Vui lòng nhập tên hạng thành viên.",
            'codeEmpty': "Vui lòng nhập mã hạng thành viên.",
            'codeExit': "Mã hạng thành viên đã tồn tại.",
            'spendingMin': "Chi tiêu tối thiểu phải lớn hơn 0",
            'discountMin': "Khuyến mãi tối thiểu phải lớn hơn 0",
        }
        # validate dữ liệu các cột không được trống
        is_valid = validateEmpty(self, {'name': name, 'code': code}, messages)

        if spending <= 0:
            is_valid = True
            self.ui.error_spending.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
            self.ui.error_spending.setText(messages["spendingMin"])
            self.ui.spending_le.setStyleSheet(Validate.BORDER_ERROR.value)

        if discount <= 0:
            is_valid = True
            self.ui.error_discount.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
            self.ui.error_discount.setText(messages["discountMin"])
            self.ui.discount_le.setStyleSheet(Validate.BORDER_ERROR.value)

        if is_valid:
            return
        member_rank = MemberRank(code=code, name=name, spending=spending, discount=discount)
        try:
            if form_mode == FormMode.ADD.value:
                if self.member_rank_controller.checkExitsDataWithModel(MemberRank.code, data=code):
                    self.ui.error_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_code.setText(messages["codeExit"])
                    self.ui.code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.member_rank_controller.insertData(member_rank)
            elif form_mode == FormMode.EDIT.value:
                if self.customer_controller.checkExitsDataUpdateWithModel(Customer.account, data=account, model_id=customer_id):
                    self.ui.error_account.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_account.setText(messages["accountExit"])
                    self.ui.account_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
            else:
                return
        except Exception as E:
            print(E)
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, member_rank_id):
        rank = self.member_rank_controller.getDataByIdWithModel(member_rank_id)
        if rank:
            self.ui.name_le.setText(rank.name)
            self.ui.code_le.setText(rank.code)
            self.ui.spending_le.setValue(int(rank.spending))
            self.ui.discount_le.setValue(int(rank.discount))

    # clear dữ liệu trên form
    def clear_form(self):
        self.clear_error()
        self.ui.code_le.setText("")
        self.ui.name_le.setText("")
        self.ui.spending_le.setValue(0)
        self.ui.discount_le.setValue(0)

    def clear_error(self):
        self.ui.code_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.name_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.spending_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.discount_le.setStyleSheet(Validate.BORDER_VALID.value)
        self.ui.error_code.setText("")
        self.ui.error_name.setText("")
        self.ui.error_spending.setText("")
        self.ui.error_discount.setText("")

    def handle_delete_event(self, member_rank_id):
        try:
            reply = message_box_delete()
            if reply == QMessageBox.Yes:
                self.category_controller.deleteDataWithModel(member_rank_id)
        except Exception as E:
            print(E)
            return False
        return True