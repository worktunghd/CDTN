from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot
from src.views.ui_generated.admin.home import Ui_MainWindow
from src.views.common.Common import *
from src.enums.enums import *
from src.models.Employees import Employees
from src.controllers.admin.UserController import UserController
from src.controllers.admin.CategoryController import CategoryController
from src.controllers.admin.ProductController import ProductController
from src.controllers.admin.OrderController import OrderController
from src.controllers.admin.CustomerController import CustomerController
from src.controllers.admin.CustomerCategoryController import CustomerCategoryController
from src.controllers.admin.SupplierController import SupplierController
from src.controllers.admin.PurchaseOrderController import PurchaseOrderController
from src.views.admin.CategoryDetail import CategoryDetailWindow
from src.views.admin.ProductDetail import ProductDetailWindow
from src.views.admin.OrderDetail import OrderDetailWindow
from src.views.admin.CustomerDetail import CustomerDetailWindow
from src.views.admin.MemberRankDetail import MemberRankDetailWindow
from src.views.admin.UserDetail import UserDetailWindow
from src.views.admin.SupplierDetail import SupplierDetailWindow
from src.views.admin.ImportDetail import ImportDetailWindow


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
        self.customer_widget_detail = CustomerDetailWindow()
        self.member_rank_widget_detail = MemberRankDetailWindow()
        self.user_widget_detail = UserDetailWindow()
        self.supplier_widget_detail = SupplierDetailWindow()
        self.import_widget_detail = ImportDetailWindow()

        # khởi tạo controller
        self.user_controller = UserController()
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        self.order_controller = OrderController()
        self.customer_controller = CustomerController()
        self.member_rank_controller = CustomerCategoryController()
        self.supplier_controller = SupplierController()
        self.import_controller = PurchaseOrderController()
        # lấy thông tin user
        self.EMPLOYEE = self.user_controller.getDataByIdWithModel(user_id)

        # khởi tạo table
        self.user_table = self.ui.tableUser
        self.category_table = self.ui.table_category
        self.product_table = self.ui.table_product
        self.order_table = self.ui.table_order
        self.customer_table = self.ui.table_customer
        self.table_rank = self.ui.table_rank
        self.table_supplier = self.ui.table_supplier
        self.table_purchase_order = self.ui.table_purchase_order

        # hiển thị header cho table
        self.user_table.horizontalHeader().setVisible(True)
        self.category_table.horizontalHeader().setVisible(True)
        self.customer_table.horizontalHeader().setVisible(True)
        self.product_table.horizontalHeader().setVisible(True)
        self.order_table.horizontalHeader().setVisible(True)
        self.table_rank.horizontalHeader().setVisible(True)
        self.table_supplier.horizontalHeader().setVisible(True)
        self.table_purchase_order.horizontalHeader().setVisible(True)
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
        self.rank_btn_2 = self.ui.rank_btn_2
        self.supplier_btn_2 = self.ui.supplier_btn_2
        self.purcharse_order_btn_2 = self.ui.purcharse_order_btn_2


        self.btn_add_category = self.ui.btn_add_category
        self.btn_save_category = self.category_widget_detail.ui.btn_save_category
        self.btn_cancel_category = self.category_widget_detail.ui.btn_cancel_category
        self.back_btn_category = self.category_widget_detail.ui.back_btn_category
        # khởi tạo các button product
        self.btn_add_product = self.ui.btn_add_product
        self.back_btn_product = self.product_widget_detail.ui.back_btn_product
        self.btn_save_product = self.product_widget_detail.ui.btn_save_product
        self.btn_cancel_product = self.product_widget_detail.ui.btn_cancel_product
        # khởi tạo các button order
        self.btn_add_order = self.ui.btn_add_order
        self.btn_save_order = self.order_widget_detail.ui.btn_save_order
        self.btn_cancel_order = self.order_widget_detail.ui.btn_cancel_order
        self.back_btn_order = self.order_widget_detail.ui.back_btn_order
        # khởi tạo các button customer
        self.btn_add_customer = self.ui.btn_add_customer
        self.btn_save_customer = self.customer_widget_detail.ui.btn_save_customer
        self.btn_cancel_customer = self.customer_widget_detail.ui.btn_cancel_customer
        self.back_btn_customer = self.customer_widget_detail.ui.back_btn_customer
        # khởi tạo các button member rank
        self.btn_add_rank = self.ui.btn_add_rank
        self.btn_save_rank = self.member_rank_widget_detail.ui.btn_save_rank
        self.btn_cancel_rank = self.member_rank_widget_detail.ui.btn_cancel_rank
        self.back_btn_rank = self.member_rank_widget_detail.ui.back_btn_rank
        # khởi tạo các button user
        self.btn_add_user = self.ui.btn_add_user
        self.btn_save_user = self.user_widget_detail.ui.btn_save_user
        self.btn_cancel_user = self.user_widget_detail.ui.btn_cancel_user
        self.back_btn_user = self.user_widget_detail.ui.back_btn_user
        # khởi tạo các button nhà cung cấp
        self.btn_add_supplier = self.ui.btn_add_supplier
        self.btn_save_supplier = self.supplier_widget_detail.ui.btn_save_supplier
        self.btn_cancel_supplier = self.supplier_widget_detail.ui.btn_cancel_supplier
        self.back_btn_supplier = self.supplier_widget_detail.ui.back_btn_supplier
        # khởi tạo các button nhập hàng
        self.btn_add_import = self.ui.btn_add_import
        self.btn_save_import = self.import_widget_detail.ui.btn_save_import
        self.btn_cancel_import = self.import_widget_detail.ui.btn_cancel_import
        self.back_btn_import = self.import_widget_detail.ui.back_btn_import
        # page index của các trang
        self.page_index = dict(
            HOME_PAGE=0,
            DASHBOARD_PAGE=1,
            # trang loại sản phẩm
            CATEGORY_PAGE=10,
            CATEGORY_PAGE_DETAIL=self.pages.addWidget(self.category_widget_detail),
            ORDER_PAGE=2,
            ORDER_PAGE_DETAIL=self.pages.addWidget(self.order_widget_detail),
            PRODUCT_PAGE=3,
            PRODUCT_PAGE_DETAIL=self.pages.addWidget(self.product_widget_detail),
            CUSTOMER_PAGE=4,
            CUSTOMER_PAGE_DETAIL=self.pages.addWidget(self.customer_widget_detail),
            MEMBER_RANK_PAGE=9,
            MEMBER_RANK_PAGE_DETAIL=self.pages.addWidget(self.member_rank_widget_detail),
            # trang thông tin người dùng
            USER_PAGE=8,
            # trang chi tiết người dùng
            USER_PAGE_DETAIL=self.pages.addWidget(self.user_widget_detail),
            # trang nhà cung cấp
            SUPPLIER_PAGE=6,
            SUPPLIER_PAGE_DETAIL=self.pages.addWidget(self.supplier_widget_detail),
            # trang nhập hàng
            IMPORT_PAGE=5,
            IMPORT_PAGE_DETAIL=self.pages.addWidget(self.import_widget_detail),
        )
        # hiển thị page mặc định khi mở form
        self.pages.setCurrentIndex(self.page_index['CATEGORY_PAGE'])
        self.show_category_table()
        self.check_permission()

        self.initializeSignal()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def showEvent(self, event):
        self.show_member_rank_table()

    # kiểm tra quyền để ẩn/hiện menu tương ứng
    def check_permission(self):
        if self.EMPLOYEE:
            if self.EMPLOYEE.role == UserRole.EMPLOYEE.value:
                self.hideAllMenu()
                self.ui.products_btn_2.setVisible(True)
                self.ui.orders_btn_2.setVisible(True)
                self.ui.rank_btn_2.setVisible(True)
                self.ui.customers_btn_2.setVisible(True)
                self.ui.category_btn_2.setVisible(True)
            elif self.EMPLOYEE and self.EMPLOYEE.role == UserRole.WAREHOUSE_EMPLOYEE.value:
                self.hideAllMenu()
                self.ui.products_btn_2.setVisible(True)
                self.ui.orders_btn_2.setVisible(True)
                self.ui.rank_btn_2.setVisible(True)
                self.ui.customers_btn_2.setVisible(True)
                self.ui.category_btn_2.setVisible(True)
                self.ui.supplier_btn_2.setVisible(True)
                self.ui.purcharse_order_btn_2.setVisible(True)
            else:
                self.openAllMenu()

    # ẩn toàn bộ menu
    def hideAllMenu(self):
        buttons = self.ui.icon_only_widget.findChildren(QPushButton) \
        + self.ui.full_menu_widget.findChildren(QPushButton)
        # Ẩn toàn bộ các QPushButton trong danh sách
        for button in buttons:
            button.setVisible(False)

        # mở button thoát
        self.ui.exit_btn_2.setVisible(True)
        self.ui.exit_btn_1.setVisible(True)

    # mở toàn bộ menu
    def openAllMenu(self):
        buttons = self.ui.icon_only_widget.findChildren(QPushButton) \
                  + self.ui.full_menu_widget.findChildren(QPushButton)
        # Ẩn toàn bộ các QPushButton trong danh sách
        for button in buttons:
            button.setVisible(True)

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
        self.supplier_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['SUPPLIER_PAGE'])
        )
        self.purcharse_order_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index['IMPORT_PAGE'])
        )
        self.category_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index["CATEGORY_PAGE"])
        )
        self.rank_btn_2.toggled.connect(
            lambda: self.do_change_page(self.page_index["MEMBER_RANK_PAGE"])
        )
        # kết nối sự kiện màn loại sản phẩm và chi tiết loại sản phẩm
        self.btn_add_category.clicked.connect(
            lambda: self.hanle_btn_add(self.category_widget_detail, FormMode.ADD.value,
                                       self.page_index['CATEGORY_PAGE_DETAIL'])
        )
        self.back_btn_category.clicked.connect(
            lambda: self.do_change_page(self.page_index['CATEGORY_PAGE'])
        )
        self.cancel_btn_category.clicked.connect(
            lambda: self.do_change_page(self.page_index['CATEGORY_PAGE'])
        )
        self.btn_save_category.clicked.connect(
            lambda: self.handle_save(self.category_widget_detail, self.mode, self.page_index['CATEGORY_PAGE'],
                                     "category")
        )
        # kết nôi sự kiện màn sản phẩm
        self.btn_add_product.clicked.connect(
            lambda: self.hanle_btn_add(self.product_widget_detail, FormMode.ADD.value,
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

        # kết nối sự kiện màn order
        self.btn_add_order.clicked.connect(
            lambda: self.hanle_btn_add(self.order_widget_detail, FormMode.ADD.value,
                                       self.page_index['ORDER_PAGE_DETAIL'])
        )
        self.back_btn_order.clicked.connect(
            lambda: self.do_change_page(self.page_index['ORDER_PAGE'])
        )
        self.btn_cancel_order.clicked.connect(
            lambda: self.do_change_page(self.page_index['ORDER_PAGE'])
        )
        self.btn_save_order.clicked.connect(
            lambda: self.handle_save(self.order_widget_detail, self.mode, self.page_index['ORDER_PAGE'],
                                     "order")
        )

        # kết nối sự kiện màn order
        self.btn_add_customer.clicked.connect(
            lambda: self.hanle_btn_add(self.customer_widget_detail, FormMode.ADD.value,
                                       self.page_index['CUSTOMER_PAGE_DETAIL'])
        )
        self.back_btn_customer.clicked.connect(
            lambda: self.do_change_page(self.page_index['CUSTOMER_PAGE'])
        )
        self.btn_cancel_customer.clicked.connect(
            lambda: self.do_change_page(self.page_index['CUSTOMER_PAGE'])
        )
        self.btn_save_customer.clicked.connect(
            lambda: self.handle_save(self.customer_widget_detail, self.mode, self.page_index['CUSTOMER_PAGE'],
                                     "customer")
        )

        # kết nối sự kiện màn hạng thành viên
        self.btn_add_rank.clicked.connect(
            lambda: self.hanle_btn_add(self.member_rank_widget_detail, FormMode.ADD.value,
                                       self.page_index['MEMBER_RANK_PAGE_DETAIL'])
        )
        self.back_btn_rank.clicked.connect(
            lambda: self.do_change_page(self.page_index['MEMBER_RANK_PAGE'])
        )
        self.btn_cancel_rank.clicked.connect(
            lambda: self.do_change_page(self.page_index['MEMBER_RANK_PAGE'])
        )
        self.btn_save_rank.clicked.connect(
            lambda: self.handle_save(self.member_rank_widget_detail, self.mode, self.page_index['MEMBER_RANK_PAGE'],
                                     "member_rank")
        )

        # kết nối sự kiện màn nhân viên
        self.btn_add_user.clicked.connect(
            lambda: self.hanle_btn_add(self.user_widget_detail, FormMode.ADD.value,
                                       self.page_index['USER_PAGE_DETAIL'])
        )
        self.back_btn_user.clicked.connect(
            lambda: self.do_change_page(self.page_index['USER_PAGE'])
        )
        self.btn_cancel_user.clicked.connect(
            lambda: self.do_change_page(self.page_index['USER_PAGE'])
        )
        self.btn_save_user.clicked.connect(
            lambda: self.handle_save(self.user_widget_detail, self.mode, self.page_index['USER_PAGE'],
                                     "user")
        )

        # kết nối sự kiện màn nhà cung cấp
        self.btn_add_supplier.clicked.connect(
            lambda: self.hanle_btn_add(self.supplier_widget_detail, FormMode.ADD.value,
                                       self.page_index['SUPPLIER_PAGE_DETAIL'])
        )
        self.back_btn_supplier.clicked.connect(
            lambda: self.do_change_page(self.page_index['SUPPLIER_PAGE'])
        )
        self.btn_cancel_supplier.clicked.connect(
            lambda: self.do_change_page(self.page_index['SUPPLIER_PAGE'])
        )
        self.btn_save_supplier.clicked.connect(
            lambda: self.handle_save(self.supplier_widget_detail, self.mode, self.page_index['SUPPLIER_PAGE'],
                                     "supplier")
        )

        # kết nối sự kiện màn nhập hàng
        self.btn_add_import.clicked.connect(
            lambda: self.hanle_btn_add(self.import_widget_detail, FormMode.ADD.value,
                                       self.page_index['IMPORT_PAGE_DETAIL'])
        )
        self.back_btn_import.clicked.connect(
            lambda: self.do_change_page(self.page_index['IMPORT_PAGE'])
        )
        self.btn_cancel_import.clicked.connect(
            lambda: self.do_change_page(self.page_index['IMPORT_PAGE'])
        )
        self.btn_save_import.clicked.connect(
            lambda: self.handle_save(self.import_widget_detail, self.mode, self.page_index['IMPORT_PAGE'],
                                     "import")
        )

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.label_9.setText(search_text)

    """
    function for change page
    """

    def do_change_page(self, index):
        self.pages.setCurrentIndex(index)
        if index == self.page_index['USER_PAGE']:
            self.show_user_table()
        if index == self.page_index['ORDER_PAGE']:
            self.show_order_table()
        if index == self.page_index['PRODUCT_PAGE']:
            self.show_product_table()
        if index == self.page_index['CUSTOMER_PAGE']:
            self.show_customer_table()
        if index == self.page_index['MEMBER_RANK_PAGE']:
            self.show_member_rank_table()
        if index == self.page_index['CATEGORY_PAGE']:
            self.show_category_table()
        if index == self.page_index['SUPPLIER_PAGE']:
            self.show_supplier_table()
        if index == self.page_index['IMPORT_PAGE']:
            self.show_import_table()

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

    # function click edit row
    def on_row_click(self, form_mode, page_index, widget_detail, widget_name):
        try:
            # lấy data
            button = self.sender()
            row_id = int(button.objectName().strip().rsplit('_', 1)[-1])
            # xử lý sự kiện cho từng màn
            if form_mode == FormMode.DELETE.value:
                # gắn data lên form
                function_delete_data = getattr(widget_detail, "handle_delete_event")
                if function_delete_data:
                    if function_delete_data(row_id):
                        function_list = f"show_{widget_name}_table"
                        function_list = getattr(self, function_list)
                        function_list()
                    else:
                        warningMessagebox("Đã xảy ra lỗi, vui lòng liên hệ quản trị viên")
            elif form_mode == FormMode.EDIT.value:
                self.handle_btn_row_edit(widget_detail, page_index, row_id)
        except Exception as E:
            print(f"{E} - file Home.py function on_row_click")
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

    # xử lý sự kiện click button add trên màn danh sách
    def hanle_btn_add(self, widget_detail, form_mode, page_to_index):
        try:
            # gắn data lên form
            self.mode = form_mode
            function_clear_data = getattr(widget_detail, "clear_form")
            function_clear_data()
            self.do_change_page(page_to_index)
        except Exception as E:
            print(f"{E} - file Home.py function hanle_btn_add")
            return

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
                else:
                    print(2)
        except Exception as E:
            print(E)

    # xử lý sự kiện click button edit trên row
    def handle_btn_row_edit(self, widget_detail, page_index, row_id):
        try:
            self.mode = FormMode.EDIT.value
            self.id_data_selected = row_id
            self.pages.setCurrentIndex(page_index)
            # gắn data lên form
            function_binding_data = getattr(widget_detail, "handle_edit_event")
            function_binding_data(row_id)
        except Exception as E:
            print(f"{E} - file Home.py function handle_btn_row_edit")

    # table category
    def show_category_table(self):
        category_list = self.category_controller.getDataByModel()
        self.category_table.setRowCount(0)
        # độ rộng cột
        self.category_table.setColumnWidth(0, 40)
        self.category_table.setColumnWidth(1, 250)
        self.category_table.setColumnWidth(2, 550)

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
                                              self.page_index["CATEGORY_PAGE_DETAIL"], self.category_widget_detail,
                                              "category"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["CATEGORY_PAGE_DETAIL"], self.category_widget_detail,
                                              "category"))
                self.category_table.setCellWidget(index, column_index + 3, widget)

    # table user
    def show_user_table(self):
        user_list = self.user_controller.getDataByModel()
        self.user_table.setRowCount(0)
        # format độ rộng bảng
        self.user_table.setColumnWidth(0, 40)
        self.user_table.setColumnWidth(1, 100)
        self.user_table.setColumnWidth(2, 350)
        self.user_table.setColumnWidth(3, 350)
        if user_list:
            for index, item in enumerate(user_list):
                column_index = 0
                self.user_table.setRowCount(index + 1)
                self.user_table.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.user_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.id)))
                self.user_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.username)))
                self.user_table.setItem(index, column_index + 3, QTableWidgetItem(str(item.employee_name)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "user")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value, self.page_index["USER_PAGE_DETAIL"],
                                              self.user_widget_detail, "user"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value, self.page_index["USER_PAGE_DETAIL"],
                                              self.user_widget_detail, "user"))
                self.user_table.setCellWidget(index, column_index + 4, widget)

    def show_product_table(self):
        product_list = self.product_controller.getDataByModel()
        self.product_table.setRowCount(0)
        # độ rộng cột
        self.product_table.setColumnWidth(0, 40)
        self.product_table.setColumnWidth(1, 200)
        self.product_table.setColumnWidth(2, 280)
        self.product_table.setColumnWidth(3, 200)
        self.product_table.setColumnWidth(4, 150)

        if product_list:
            for index, item in enumerate(product_list):
                column_index = 0
                self.product_table.setRowCount(index + 1)
                self.product_table.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.product_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.product_code)))
                self.product_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.product_name)))
                self.product_table.setItem(index, column_index + 3, QTableWidgetItem(str(item.stock_quantity)))
                self.product_table.setItem(index, column_index + 4, QTableWidgetItem(str(formatCurrency(int(item.price), 'đ'))))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "product")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value,
                                              self.page_index["PRODUCT_PAGE_DETAIL"], self.product_widget_detail, "product"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["USER_PAGE_DETAIL"], self.product_widget_detail, "product"))
                self.product_table.setCellWidget(index, column_index + 5, widget)

    def show_order_table(self):
        try:
            order_list = self.order_controller.getDataByModel()
            self.order_table.setRowCount(0)
            # độ rộng cột
            self.order_table.setColumnWidth(0, 40)
            self.order_table.setColumnWidth(1, 150)
            self.order_table.setColumnWidth(2, 220)
            self.order_table.setColumnWidth(3, 170)
            self.order_table.setColumnWidth(4, 160)
            self.order_table.setColumnWidth(5, 160)
            if order_list:
                for index, item in enumerate(order_list):
                    column_index = 0
                    self.order_table.setRowCount(index + 1)
                    self.order_table.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                    self.order_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.order_code)))
                    self.order_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.customer.customer_name)))
                    self.order_table.setItem(index, column_index + 3, QTableWidgetItem(str(item.customer.phone_number)))
                    self.order_table.setItem(index, column_index + 4, QTableWidgetItem(str(item.quantity)))
                    self.order_table.setItem(index, column_index + 5,
                                             QTableWidgetItem(str(formatCurrency(int(item.final_price), 'đ'))))
                    widget, edit_btn, delete_btn = generate_action_row(item.id, "order")
                    edit_btn.clicked.connect(
                        lambda: self.on_row_click(FormMode.EDIT.value,
                                                  self.page_index["ORDER_PAGE_DETAIL"], self.order_widget_detail, "order"))
                    delete_btn.clicked.connect(
                        lambda: self.on_row_click(FormMode.DELETE.value,
                                                  self.page_index["ORDER_PAGE_DETAIL"], self.order_widget_detail, "order"))
                    self.order_table.setCellWidget(index, column_index + 6, widget)
        except Exception as E:
            print(E)
            return

    # danh sách khách hàng
    def show_customer_table(self):
        customer_list = self.customer_controller.getDataByModel()
        self.customer_table.setRowCount(0)
        # độ rộng cột
        self.customer_table.setColumnWidth(0, 40)
        self.customer_table.setColumnWidth(1, 200)
        self.customer_table.setColumnWidth(2, 350)
        self.customer_table.setColumnWidth(3, 280)
        if customer_list:
            for index, item in enumerate(customer_list):
                column_index = 0
                self.customer_table.setRowCount(index + 1)
                self.customer_table.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.customer_table.setItem(index, column_index + 1, QTableWidgetItem(str(item.id)))
                self.customer_table.setItem(index, column_index + 2, QTableWidgetItem(str(item.customer_name)))
                self.customer_table.setItem(index, column_index + 3, QTableWidgetItem(str(item.phone_number)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "customer")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value,
                                              self.page_index["CUSTOMER_PAGE_DETAIL"], self.customer_widget_detail, "customer"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["CUSTOMER_PAGE_DETAIL"], self.customer_widget_detail, "customer"))
                self.customer_table.setCellWidget(index, column_index + 4, widget)

        # danh sách khách hàng

    def show_member_rank_table(self):
        member_rank_list = self.member_rank_controller.getDataByModel()
        self.table_rank.setRowCount(0)
        # sét độ rộng cột
        self.table_rank.setColumnWidth(0, 40)
        self.table_rank.setColumnWidth(1, 200)
        self.table_rank.setColumnWidth(2, 300)
        self.table_rank.setColumnWidth(3, 180)
        self.table_rank.setColumnWidth(4, 180)
        if member_rank_list:
            for index, item in enumerate(member_rank_list):
                column_index = 0
                self.table_rank.setRowCount(index + 1)
                self.table_rank.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.table_rank.setItem(index, column_index + 1, QTableWidgetItem(str(item.code)))
                self.table_rank.setItem(index, column_index + 2, QTableWidgetItem(str(item.category_name)))
                self.table_rank.setItem(index, column_index + 3,
                                        QTableWidgetItem(str(formatCurrency(int(item.min_spending), 'đ'))))
                self.table_rank.setItem(index, column_index + 4, QTableWidgetItem(str(item.discount_percentage)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "member_rank")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value,
                                              self.page_index["MEMBER_RANK_PAGE_DETAIL"],
                                              self.member_rank_widget_detail, "member_rank"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["MEMBER_RANK_PAGE_DETAIL"],
                                              self.member_rank_widget_detail, "member_rank"))
                self.table_rank.setCellWidget(index, column_index + 5, widget)

    def show_supplier_table(self):
        supplier_list = self.supplier_controller.getDataByModel()
        self.table_supplier.setRowCount(0)
        # sét độ rộng cột
        self.table_supplier.setColumnWidth(0, 40)
        self.table_supplier.setColumnWidth(1, 180)
        self.table_supplier.setColumnWidth(2, 260)
        self.table_supplier.setColumnWidth(3, 200)
        self.table_supplier.setColumnWidth(4, 200)
        if supplier_list:
            for index, item in enumerate(supplier_list):
                column_index = 0
                self.table_supplier.setRowCount(index + 1)
                self.table_supplier.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.table_supplier.setItem(index, column_index + 1, QTableWidgetItem(str(item.code)))
                self.table_supplier.setItem(index, column_index + 2, QTableWidgetItem(str(item.supplier_name)))
                # cột số điện thoại
                if not item.phone_number:
                    item.phone_number = 'Chưa thiết lập'
                self.table_supplier.setItem(index, column_index + 3, QTableWidgetItem(str(item.phone_number)))
                # cột địa chỉ
                if not item.address:
                    item.address = 'Chưa thiết lập'
                self.table_supplier.setItem(index, column_index + 4, QTableWidgetItem(str(item.address)))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "member_rank")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value,
                                              self.page_index["SUPPLIER_PAGE_DETAIL"],
                                              self.supplier_widget_detail, "supplier"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["SUPPLIER_PAGE_DETAIL"],
                                              self.supplier_widget_detail, "supplier"))
                self.table_supplier.setCellWidget(index, column_index + 5, widget)

    # table màn nhập hàng
    def show_import_table(self):
        import_list = self.import_controller.getDataByModel()
        self.table_purchase_order.setRowCount(0)
        # sét độ rộng cột
        self.table_purchase_order.setColumnWidth(0, 40)
        self.table_purchase_order.setColumnWidth(1, 180)
        self.table_purchase_order.setColumnWidth(2, 260)
        self.table_purchase_order.setColumnWidth(3, 200)
        self.table_purchase_order.setColumnWidth(4, 200)
        if import_list:
            for index, item in enumerate(import_list):
                column_index = 0
                self.table_purchase_order.setRowCount(index + 1)
                self.table_purchase_order.setItem(index, column_index, QTableWidgetItem(str(index + 1)))
                self.table_purchase_order.setItem(index, column_index + 1, QTableWidgetItem(str(item.code)))
                self.table_purchase_order.setItem(index, column_index + 2, QTableWidgetItem(str(item.created_at)))
                self.table_purchase_order.setItem(index, column_index + 3, QTableWidgetItem(str(item.import_date)))
                self.table_purchase_order.setItem(index, column_index + 4, QTableWidgetItem(formatCurrency(int(item.final_price), 'đ')))
                widget, edit_btn, delete_btn = generate_action_row(item.id, "import")
                edit_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.EDIT.value,
                                              self.page_index["IMPORT_PAGE_DETAIL"],
                                              self.import_widget_detail, "import"))
                delete_btn.clicked.connect(
                    lambda: self.on_row_click(FormMode.DELETE.value,
                                              self.page_index["IMPORT_PAGE_DETAIL"],
                                              self.import_widget_detail, "import"))
                self.table_purchase_order.setCellWidget(index, column_index + 5, widget)