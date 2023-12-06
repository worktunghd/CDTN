from PyQt5.QtWidgets import QHeaderView, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QPushButton
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from src.views.ui_generated.admin.home import Ui_MainWindow
from src.views.common.Common import *
from src.enums.enums import *
from src.controllers.admin.UserController import UserController
from src.controllers.admin.CategoryController import CategoryController
from src.controllers.admin.ProductController import ProductController
from src.models.users import User
from src.views.admin.Product import ProductWindow
from src.views.admin.Category import CategoryWindow
from src.views.admin.CategoryDetail import CategoryDetailWindow
from src.views.admin.ProductDetail import ProductDetailWindow
from src.views.admin.OrderDetail import OrderDetailWindow
from functools import partial


class HomeWindow(QMainWindow):
    def __init__(self, user_id):
        super(HomeWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.USER_ID = user_id

        # khởi tạo widget
        self.customers_btn_2 = self.ui.customers_btn_2
        self.products_btn_2 = self.ui.products_btn_2
        self.user_btn_2 = self.ui.user_btn_2
        self.orders_btn_2 = self.ui.orders_btn_2
        self.dashboard_btn_2 = self.ui.dashboard_btn_2
        self.home_btn_2 = self.ui.home_btn_2
        # khởi tạo các page thêm vào stackWidget
        self.category_widget_detail = CategoryDetailWindow()
        self.product_widget_detail = ProductDetailWindow()
        self.order_widget_detail = OrderDetailWindow()

        # khởi tạo controller
        self.user_controller = UserController()
        self.category_controller = CategoryController()
        self.product_controller = ProductController()

        # khởi tạo table
        self.user_table = self.ui.tableUser
        self.category_table = self.ui.table_category
        self.product_table = self.ui.table_product

        # hiển thị header cho table
        self.user_table.horizontalHeader().setVisible(True)
        self.category_table.horizontalHeader().setVisible(True)
        # lưu giá trị data khi click row trong table
        self.id_data_selected = None
        # trạng thái form
        self.mode = FormMode.ADD.value

        # ẩn menu nhỏ
        self.ui.icon_only_widget.hide()

        # khởi tạo page
        # sét trang mặc định hiển thị khi page được hiển thị
        self.pages = self.ui.stackedWidget

        # khởi tạo các button change page
        self.category_btn_2 = self.ui.category_btn_2
        self.customers_btn_2 = self.ui.customers_btn_2
        self.btn_add_user = self.ui.btn_add_user
        self.back_btn_category = self.category_widget_detail.ui.back_btn_category
        self.cancel_btn_category = self.category_widget_detail.ui.btn_cancel_category
        self.products_btn_2 = self.ui.products_btn_2

        self.btn_add_category = self.ui.btn_add_category
        self.btn_save_category = self.category_widget_detail.ui.btn_save_category
        self.btn_cancel_category = self.category_widget_detail.ui.btn_cancel_category
        self.back_btn_category = self.category_widget_detail.ui.back_btn_category
        # khởi tạo các button product
        self.btn_add_product = self.ui.btn_add_product
        self.back_btn_product = self.product_widget_detail.ui.back_btn_product
        self.btn_save_product = self.product_widget_detail.ui.btn_save_product
        self.btn_cancel_product = self.product_widget_detail.ui.btn_cancel_product

        # page index của các trang
        self.page_index = dict(
            HOME_PAGE=0,
            DASHBOARD_PAGE=1,
            # trang loại sản phẩm
            CATEGORY_PAGE=7,
            CATEGORY_PAGE_DETAIL=self.pages.addWidget(self.category_widget_detail),
            PRODUCT_PAGE_DETAIL=self.pages.addWidget(self.product_widget_detail),
            ORDER_PAGE=2,
            ORDER_PAGE_DETAIL=self.pages.addWidget(self.order_widget_detail),
            PRODUCT_PAGE=3,
            CUSTOMER_PAGE=4,
            # trang thông tin người dùng
            USER_PAGE=6,
            # trang chi tiết người dùng
            USER_PAGE_DETAIL=8,
        )
        # hiển thị page mặc định khi mở form
        self.pages.setCurrentIndex(self.page_index['ORDER_PAGE_DETAIL'])
        self.show_product_table()

        self.initializeSignal()
        self.show_category_table()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    # Khởi tạo kết nối các button liên kết
    def initializeSignal(self):
        # khởi tạo signal và slot
        # bắt sự kiện click menu
        self.customers_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['CUSTOMER_PAGE']))
        self.user_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['USER_PAGE']))
        self.products_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['PRODUCT_PAGE'])
        )
        self.orders_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['ORDER_PAGE'])
        )
        self.dashboard_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['DASHBOARD_PAGE'])
        )
        self.home_btn_2.toggled.connect(
            lambda: self.do_change_page(0)
        )
        self.category_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index["CATEGORY_PAGE"])
        )
        # kết nối sự kiện màn loại sản phẩm và chi tiết loại sản phẩm
        self.btn_add_category.clicked.connect(
            lambda: self.hanle_btn_add(self.category_widget_detail, FormMode.EDIT.value, self.page_index['CATEGORY_PAGE_DETAIL'])
        )
        self.back_btn_category.clicked.connect(
            lambda: self.do_change_page(self.page_index['CATEGORY_PAGE'])
        )
        self.cancel_btn_category.clicked.connect(
            lambda: self.do_change_page(self.page_index['CATEGORY_PAGE'])
        )
        self.btn_save_category.clicked.connect(
            lambda: self.handle_save(self.category_widget_detail, self.mode, self.page_index['CATEGORY_PAGE'], "category")
        )
        # kết nôi sự kiện màn sản phẩm
        self.btn_add_product.clicked.connect(
            lambda: self.hanle_btn_add(self.product_widget_detail, FormMode.EDIT.value,
                                       self.page_index['PRODUCT_PAGE_DETAIL'])
        )
        self.back_btn_product.clicked.connect(
            lambda: self.do_change_page(self.page_index['PRODUCT_PAGE'])
        )
        self.btn_cancel_product.clicked.connect(
            lambda: self.do_change_page(self.page_index['PRODUCT_PAGE'])
        )
        self.btn_save_product.clicked.connect(
            lambda: self.handle_save(self.product_widget_detail, self.mode, self.page_index['PRODUCT_PAGE'],
                                     "product")
        )


    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    @pyqtSlot()
    def on_back_btn_user_clicked(self):
        self.pages.setCurrentIndex(self.page_index['USER_PAGE'])
        # load lại dữ liệu
        self.show_user_table()

    # clear input form user
    def clearUserForm(self):
        self.ui.username_le.setText("")
        self.ui.password_le.setText("")
        self.ui.confirm_le.setText("")
        self.ui.name_le.setText("")

    # sự kiện click button thêm mới tài khoản
    @pyqtSlot()
    def on_btn_add_user_clicked(self):
        self.pages.setCurrentIndex(self.page_index['USER_PAGE_DETAIL'])
        self.mode = FormMode.ADD.value
        self.clearUserForm()

    """
    function for change page
    """

    def do_change_page(self, index):
        self.pages.setCurrentIndex(index)
        if index == self.page_index['USER_PAGE']:
            self.show_user_table()

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    # validate form input empty
    def validateEmpty(self, data: dict, messages: dict, color_style, border_style):
        result = []
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
                    label.setStyleSheet(color_style)
                if input_text:
                    input_text.setStyleSheet(border_style)
        return result

    # function click edit row
    def on_row_click(self, form_mode, page_index, widget_detail, page_back_index, widget_name):
        # lấy data
        button = self.sender()
        row_id = int(button.objectName().strip().rsplit('_', 1)[-1])
        # xử lý sự kiện cho từng màn
        if page_index == self.page_index["USER_PAGE_DETAIL"]:
            if form_mode == FormMode.DELETE.value:
                self.on_delete_user(row_id)
            elif form_mode == FormMode.EDIT.value:
                # hiển thị màn hình
                self.pages.setCurrentIndex(page_index)
                self.on_edit_user(row_id)
        else:
            if form_mode == FormMode.DELETE.value:
                self.on_delete_user(row_id)
            elif form_mode == FormMode.EDIT.value:
                self.handle_btn_row_edit(widget_detail, page_index, row_id)



    # hàm chỉnh sửa thông tin user
    def on_edit_user(self, user_id):
        self.mode = FormMode.EDIT.value
        self.id_data_selected = user_id
        user = self.user_controller.getDataByIdWithModel(user_id)
        self.ui.name_le.setText(user.name)
        self.ui.username_le.setText(user.username)
        self.ui.password_le.setText(user.password)
        self.ui.confirm_le.setText(user.password)

    # xóa user
    def on_delete_user(self, user_id):
        reply = self.initialize_message_box_delete().exec_()
        if reply == QMessageBox.Yes:
            self.user_controller.deleteUserWithModel(user_id)
            self.show_user_table()
        else:
            return

    # tạo form hiển thị cảnh báo xóa
    def initialize_message_box_delete(self):
        # Create QMessageBox
        msgBox = QMessageBox(self)
        msgBox.setWindowIcon(QIcon("./static/icon/key-6-128.ico"))
        msgBox.setIconPixmap(QPixmap("./static/icon/question-mark-7-48.ico"))
        msgBox.setWindowTitle("Thông báo")
        msgBox.setText("Bạn có chắc chắn muốn xóa không?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        return msgBox

    # click button thêm mới user
    @pyqtSlot()
    def on_btnUser_clicked(self):
        name = self.ui.name_le.text().strip()
        username = self.ui.username_le.text().strip()
        password = self.ui.password_le.text().strip()
        confirm = self.ui.confirm_le.text().strip()
        color_style = "color: #ef5350;"
        border_style = "border: 1px solid #ef5350;"
        # sét border mặc định cho input
        self.ui.name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.password_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.username_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.confirm_le.setStyleSheet("border: 1px solid #e0e5e9;")
        # xóa error text
        self.ui.error_username.setText("")
        self.ui.error_confirm.setText("")
        self.ui.error_name.setText("")
        self.ui.error_password.setText("")

        messages = {
            'nameEmpty': "Vui lòng nhập họ và tên.",
            'usernameEmpty': "Vui lòng nhập thông tin tài khoản.",
            'usernameExit': "Tài khoản đã tồn tại.",
            'passwordEmpty': "Vui lòng nhập thông tin mật khẩu.",
            'confirmEmpty': "Vui lòng nhập lại mật khẩu.",
            'confirmNotMatch': "Mật  khẩu không trùng khớp.",
        }
        # validate dữ liệu các cột không được trống
        is_valid = self.validateEmpty({'name': name, 'username': username, 'password': password, 'confirm': confirm},
                                      messages, color_style, border_style)
        if is_valid:
            return

        if password != confirm:
            self.ui.error_confirm.setStyleSheet(color_style)
            self.ui.error_confirm.setText(messages["confirmNotMatch"])
            self.ui.confirm_le.setStyleSheet(border_style)
            return

        user_controller = UserController()
        message = user_controller.checkUserEmailOrPhone(username=username)
        if message:
            self.ui.error_username.setStyleSheet(color_style)
            self.ui.error_username.setText(message)
            self.ui.username_le.setStyleSheet(border_style)
            return

        if self.mode == FormMode.ADD.value:
            if user_controller.checkExitsUser(username=username):
                self.ui.error_username.setStyleSheet(color_style)
                self.ui.error_username.setText(messages["usernameExit"])
                self.ui.username_le.setStyleSheet(border_style)
                return
            user = User(name=name, username=username, password=password)
            user_controller.saveUser(user=user)
        elif self.mode == FormMode.EDIT.value:
            if user_controller.checkExitsUserUpdate(username=username, user_id=self.id_data_selected):
                self.ui.error_username.setStyleSheet(color_style)
                self.ui.error_username.setText(messages["usernameExit"])
                self.ui.username_le.setStyleSheet(border_style)
                return
            user = {'username': username, 'name': name, 'password': password}
            user_controller.updateUserWithModel(data=user, user_id=self.id_data_selected)
        else:
            return
        # quay về trang danh sách
        self.pages.setCurrentIndex(self.page_index["USER_PAGE"])
        # load lại dữ liệu
        self.show_user_table()

    # xử lý sự kiện click button add trên màn danh sách
    def hanle_btn_add(self, widget_detail, form_mode, page_to_index):
        # gắn data lên form
        function_clear_data = getattr(widget_detail, "clear_form")
        function_clear_data()
        self.do_change_page(page_to_index)

    # xử lý sự kiện click button lưu dữ liệu của form chi tiết
    def handle_save(self, widget_detail, form_mode, page_back_index, widget_name):
        try:
            # lấy ra tên function lưu của các trang
            function_save_name = f"save_{widget_name}"
            function_save = getattr(widget_detail, function_save_name)
            function_list = f"show_{widget_name}_table"
            function_list = getattr(self, function_list)
            if function_save:
                if function_save(form_mode, self.id_data_selected):
                    # quay về trang danh sách
                    self.pages.setCurrentIndex(page_back_index)
                    function_list()
                else: print(2)
        except Exception as E:
            print(E)


    # xử lý sự kiện click button edit trên row
    def handle_btn_row_edit(self, widget_detail, page_index, row_id):
        self.mode = FormMode.EDIT.value
        self.id_data_selected = row_id
        self.pages.setCurrentIndex(page_index)
        # gắn data lên form
        function_binding_data = getattr(widget_detail, "handle_edit_event")
        function_binding_data(row_id)

    # table category
    def show_category_table(self):
        category_list = self.category_controller.getDataByModel()
        self.category_table.setRowCount(0)
        if category_list:
            for index, item in enumerate(category_list):
                column_index = 0
                self.category_table.setRowCount(index + 1)
                self.category_table.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.category_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.id)))
                self.category_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.category_name)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "user")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value,
                                              self.page_index["CATEGORY_PAGE_DETAIL"], self.category_widget_detail, self.page_index["CATEGORY_PAGE"], "category"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["CATEGORY_PAGE_DETAIL"], self.category_widget_detail, self.page_index["CATEGORY_PAGE"], "category"))
                self.category_table.setCellWidget(index, column_index + 3, widget)

    # table user
    def show_user_table(self):
        user_list = self.user_controller.getDataByModel()
        self.user_table.setRowCount(0)
        if user_list:
            for index, item in enumerate(user_list):
                column_index = 0
                self.user_table.setRowCount(index + 1)
                self.user_table.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.user_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.id)))
                self.user_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.username)))
                self.user_table.setItem(index, column_index + 3, QTableWidgetItem(str(item.name)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "user")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(self.user_table, FormMode.EDIT.value, self.page_index["USER_PAGE_DETAIL"]))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(self.user_table, FormMode.DELETE.value, self.page_index["USER_PAGE_DETAIL"]))
                self.user_table.setCellWidget(index, column_index + 4, widget)

    def show_product_table(self):
        product_list = self.product_controller.getDataByModel()
        self.product_table.setRowCount(0)
        if product_list:
            for index, item in enumerate(product_list):
                column_index = 0
                self.product_table.setRowCount(index + 1)
                self.product_table.setItem(index, column_index, QTableWidgetItem(str(item.product_code)))
                self.product_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.product_name)))
                self.product_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.quantity)))
                self.product_table.setItem(index, column_index + 3, QTableWidgetItem(str(item.price)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "product")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(self.product_table, FormMode.EDIT.value, self.page_index["USER_PAGE_DETAIL"]))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(self.product_table, FormMode.DELETE.value, self.page_index["USER_PAGE_DETAIL"]))
                self.product_table.setCellWidget(index, column_index + 4, widget)