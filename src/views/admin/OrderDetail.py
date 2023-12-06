from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow, QTableWidgetItem, QAbstractItemView, QApplication, \
    QCompleter, QComboBox
from PyQt5.QtCore import QLocale, pyqtSlot
from src.views.ui_generated.admin.order_detail import Ui_Form
from src.views.common.Common import *
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.UserController import UserController
from src.controllers.admin.ProductController import ProductController
from src.models.category import Category
from src.views.common.form_group_btn_order import Test


class OrderDetailWindow(QWidget):
    def __init__(self):
        super(OrderDetailWindow, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # khởi tạo các ui
        self.search_box_product_order = self.ui.search_box_product_order
        self.search_box_product_order.lineEdit().setPlaceholderText("Tìm kiếm theo mã sản phẩm")
        self.user_le = self.ui.user_le
        self.user_le.lineEdit().setPlaceholderText("Tìm kiếm theo số điện thoại")
        self.table_product_order = self.ui.table_product_order
        self.table_product_order.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # khởi tạo biến
        self.user_controller = UserController()
        self.product_controller = ProductController()
        # danh sách người dùng
        self.user_list = []
        # danh sách sản phẩm
        self.product_list = []
        self.user_selected = None
        # danh sách sản phẩm được chọn
        self.product_selected = {}
        # tổng tiền các sản phẩm
        self.total_price = 0

        self.user_le.setInsertPolicy(QComboBox.NoInsert)
        self.user_le.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.user_le.activated.connect(self.handle_user_le_selected)
        self.search_box_product_order.setInsertPolicy(QComboBox.NoInsert)
        self.search_box_product_order.completer().setCompletionMode(QCompleter.PopupCompletion)
        self.search_box_product_order.activated.connect(self.handle_product_le_selected)

    # Hàm luôn chạy khi form được show
    # Thực hiện lấy dữ liệu từ database
    def showEvent(self, event):
        # Lấy dữ liệu từ database
        self.user_list = self.user_controller.getDataByModel()
        self.product_list = self.product_controller.getDataByModel()
        # gắn dữ liệu lên combobox
        self.user_le.addItems([item.username for index, item in enumerate(self.user_list)])
        self.search_box_product_order.addItems([item.product_code for index, item in enumerate(self.product_list)])

    # Xử lý khi người dùng chọn người đặt hàng
    def handle_user_le_selected(self, index):
        print(self.user_list[index])

    # xử lý khi người dùng chọn sản phẩm
    def handle_product_le_selected(self, index):
        # quantity_order_product = 1
        # # nếu sản phẩm đã được thêm thì tăng số lượng
        # if index in self.product_selected:
        #     quantity_order_product = self.product_selected.get(index).quantity_order + 1


        self.show_table_product()

    # Hiển thị các sản phẩm được chọn
    def show_table_product(self):
        self.table_product_order.setRowCount(0)
        if self.product_selected:
            try:
                for index, item in self.product_selected.items():
                    column_index = 0
                    self.table_product_order.setRowCount(index + 1)
                    self.table_product_order.setRowHeight(index, 120)
                    # cột sản phẩm
                    self.table_product_order.setCellWidget(index, column_index, self.generate_info_product_order())
                    self.table_product_order.setColumnWidth(column_index, 200)
                    # cột đơn giá
                    self.table_product_order.setItem(index, column_index + 1, QTableWidgetItem(formatCurrency(int(item.price), 'đ')))
                    # cột số lượng
                    widget,  minus_order_btn, plus_order_btn, quantity_label = generate_group_order_btn(item.id) # tạo view
                    minus_order_btn.clicked.connect(
                        lambda: self.decreaseQuantity(quantity_label)
                    )
                    plus_order_btn.clicked.connect(
                        lambda: self.increaseQuantity(quantity_label)
                    )
                    self.table_product_order.setCellWidget(index, column_index + 2, widget)

            except Exception as E:
                print(f"{E} - OrderDetail.py")
                return

    # sự kiện click button giảm số lượng sản phẩm
    def decreaseQuantity(self, quantity_label):
        print(1)

    def increaseQuantity(self, quantity_label):
        button = self.sender()
        row_id = int(button.objectName().strip().rsplit('_', 1)[-1])
        quantity = int(quantity_label.value())
        quantity += 1
        quantity_label.setValue(quantity)


    def generate_info_product_order(self):
        self.widget = QtWidgets.QWidget()
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 110))
        self.widget.setStyleSheet("#delete_order_product{\n"
                                  "    max-width: 30px;\n"
                                  "    min-width: 30px;\n"
                                  "    width: 30px;\n"
                                  "    height: 18px;\n"
                                  "    min-height: 18px;\n"
                                  "    text-align: left;\n"
                                  "    border: none;\n"
                                  "    padding: 0;\n"
                                  "    color: #46694f;\n"
                                  "    background: transparent;\n"
                                  "}\n"
                                  "\n"
                                  "#delete_order_product:hover, #product_name_order:hover{\n"
                                  "    color: #80b885;\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 80))
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setText("Iphone 11")
        self.label.setPixmap(QtGui.QPixmap(":/icon/resources/img/facebook.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.group_info_order = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_info_order.sizePolicy().hasHeightForWidth())
        self.group_info_order.setSizePolicy(sizePolicy)
        self.group_info_order.setMaximumSize(QtCore.QSize(16777215, 110))
        self.group_info_order.setObjectName("group_info_order")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_info_order)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.setSpacing(10)
        self.product_name_order = QtWidgets.QLabel(self.group_info_order)
        self.product_name_order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.product_name_order.setWordWrap(True)
        self.product_name_order.setText("Iphone 11")
        self.product_name_order.setObjectName("product_name_order")
        self.verticalLayout_2.addWidget(self.product_name_order)
        self.product_code_order = QtWidgets.QLabel(self.group_info_order)
        self.product_code_order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.product_code_order.setText("test")
        self.product_code_order.setObjectName("product_code_order")
        self.verticalLayout_2.addWidget(self.product_code_order)
        self.delete_order_product = QtWidgets.QPushButton(self.group_info_order)
        self.delete_order_product.setMinimumSize(QtCore.QSize(30, 20))
        self.delete_order_product.setMaximumSize(QtCore.QSize(30, 20))
        self.delete_order_product.setText("Xóa")
        self.delete_order_product.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_order_product.setObjectName("delete_order_product")
        self.verticalLayout_2.addWidget(self.delete_order_product)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addWidget(self.group_info_order)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        return self.widget

    def on_btn_save_order_clicked(self):
        print(self.combo_box_handler.selected_item)

    @pyqtSlot()
    def save_category(self, form_mode, order_id=None):
        # category_name = self.ui.category_name_le.text().strip()
        # color_style = "color: #ef5350;"
        # border_style = "border: 1px solid #ef5350;"
        # # sét border mặc định cho input
        # self.ui.category_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        # # xóa error text
        # self.ui.error_category_name.setText("")
        #
        # messages = {
        #     'category_nameEmpty': "Vui lòng nhập tên loại sản phẩm.",
        #     'category_nameExit': "Tên loại sản phẩm đã tồn tại.",
        # }
        #
        # # validate dữ liệu các cột không được trống
        # is_valid = validateEmpty(self,{'category_name': category_name}, messages)
        # if is_valid:
        #     return
        # try:
        #     if form_mode == FormMode.ADD.value:
        #         if self.category_controller.checkExitsDataWithModel(Category.category_name, data=category_name):
        #             self.ui.error_category_name.setStyleSheet(color_style)
        #             self.ui.error_category_name.setText(messages["category_nameExit"])
        #             self.ui.category_name_le.setStyleSheet(border_style)
        #             return
        #         self.category_controller.insertData(Category(category_name=category_name))
        #     elif form_mode == FormMode.EDIT.value:
        #         if self.category_controller.checkExitsDataUpdateWithModel(Category.category_name, data=category_name, model_id=order_id):
        #             self.ui.error_category_name.setStyleSheet(color_style)
        #             self.ui.error_category_name.setText(messages["category_nameExit"])
        #             self.ui.category_name_le.setStyleSheet(border_style)
        #             return
        #         self.category_controller.updateDataWithModel(data={'category_name': category_name}, model_id=order_id)
        #     else:
        #         return
        # except Exception as E:
        #     print(E)
        #     return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, category_id):
        category = self.category_controller.getDataByIdWithModel(category_id)
        # if category:
        #     self.ui.category_name_le.setText(category.category_name)

    # clear dữ liệu trên form
    def clear_form(self):
        self.ui.order_code_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.order_code_le.setText("")
        self.ui.user_le.setText("")
