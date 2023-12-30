from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem, QHBoxLayout
from PyQt5.QtCore import pyqtSlot, QFileInfo, QDate
from src.views.ui_generated.admin.import_detail import Ui_Form
from src.views.common.Common import *
import os
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.ProductController import ProductController
from src.controllers.admin.SupplierController import SupplierController
from src.controllers.admin.PurchaseOrderController import PurchaseOrderController
from src.models.Products import Products
from src.models.PurchaseOrders import PurchaseOrders
from src.models.Suppliers import Suppliers
from datetime import datetime
from functools import partial


class ImportDetailWindow(QWidget):
    def __init__(self):
        super(ImportDetailWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.product_controller = ProductController()
        self.supplier_controller = SupplierController()
        self.import_controller = PurchaseOrderController()
        # khởi tạo biến
        self.selected_date = {
            'import_date': QDate.currentDate(),
            'delivery_date': QDate.currentDate(),
        }
        # danh sách sản phẩm
        self.product_list = []
        # danh sách nhà cung cấp
        self.supplier_list = []
        # danh sách sản phẩm được chọn
        self.product_selected = {}
        # danh sách nhà cung cấp được chọn
        self.supplier_selected = {}
        # giá tiền cuối (sau thuế và chiết khấu)
        self.final_price = 0
        self.original_price = 0

        # bắt sự kiện click input ngày nhập ngày giao (hiển thị dialog chọn ngày tháng)
        self.ui.import_date_le.mousePressEvent = partial(self.on_show_date_dialog, "import_date")
        self.ui.delivery_date_le.mousePressEvent = partial(self.on_show_date_dialog, "delivery_date")

        # khởi tạo biến cho ui
        self.search_box_product_order = self.ui.search_box_product_order
        self.search_box_product_order.lineEdit().setPlaceholderText("Tìm kiếm theo mã sản phẩm")
        self.search_box_product_order.activated.connect(self.handle_product_le_selected)
        self.search_box_supplier = self.ui.supplier_le
        self.search_box_supplier.lineEdit().setPlaceholderText("Tìm kiếm nhà cung cấp theo mã")
        self.search_box_supplier.activated.connect(self.handle_supplier_selected)
        self.table_product_import = self.ui.table_product_import
        self.table_supplier_import = self.ui.table_supplier

    def handle_product_le_selected(self, index):
        self.product_selected[self.product_list[index].id] = self.product_list[index]
        self.show_table_product()
        self.handle_total_quantity_product_order()

    # xử lý khi chọn nhà cung cấp từ combobox
    def handle_supplier_selected(self, index):
        self.supplier_selected[self.supplier_list[index].id] = self.supplier_list[index]
        self.show_table_supplier()
        self.handle_total_quantity_product_order()

    def handle_total_quantity_product_order(self):
        try:
            # có chiết khấu
            if self.ui.discount_le.value() > 0:
                # hiển thị giá gốc
                self.original_price = sum(int(int(product.stock_quantity) * int(product.price)) for product in self.product_selected.values())
                self.ui.total_price_main.setText(formatCurrency(int(self.original_price), 'đ'))
                self.final_price = self.original_price - int(self.original_price * (int(self.ui.discount_le.value()) / 100))
                self.ui.total_quantity_product_order.setText(formatCurrency(int(self.final_price), 'đ'))

            # không có khuyến mãi
            else:
                self.original_price = sum(int(int(product.stock_quantity) * int(product.price)) for product in self.product_selected.values())
                self.final_price = self.original_price
                self.ui.total_quantity_product_order.setText(formatCurrency(int(self.original_price), 'đ'))
        except Exception as E:
            print(f"{E} \n file OrderDetail function handle_total_quantity_product_order")
            return

    # hiển thị dữ liệu nhà cung cấp lên bảng
    def show_table_supplier(self):
        self.table_supplier_import.setRowCount(0)
        # độ rộng cột
        self.table_supplier_import.setColumnWidth(0, 100)
        self.table_supplier_import.setColumnWidth(1, 250)
        self.table_supplier_import.setColumnWidth(2, 200)
        self.table_supplier_import.setColumnWidth(3, 150)
        if self.supplier_selected:
            try:
                row_index = 0
                for index, item in self.supplier_selected.items():
                    column_index = 0
                    self.table_supplier_import.setRowCount(row_index + 1)
                    self.table_supplier_import.setRowHeight(row_index, 120)
                    # cột mã đơn vị cung cấp
                    self.table_supplier_import.setItem(row_index, column_index,
                                                            QTableWidgetItem(str(item.code)))
                    # cột tên
                    self.table_supplier_import.setItem(row_index, column_index + 1,
                                                      QTableWidgetItem(str(item.supplier_name)))
                    self.table_supplier_import.setItem(row_index, column_index + 2,
                                                       QTableWidgetItem(str(item.phone_number)))

                    # cột thao tác
                    self.delete_btn = QPushButton("")
                    self.delete_btn.setObjectName("delete_supplier")
                    icon = QIcon("resources/icon/red-delete-10433.svg")
                    self.delete_btn.setIcon(icon)
                    self.delete_btn.setFixedWidth(100)
                    self.delete_btn.setIconSize(QtCore.QSize(24, 24))
                    self.delete_btn.clicked.connect(self.delete_supplier_import)
                    layout = QHBoxLayout()
                    layout.addWidget(self.delete_btn)
                    layout.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    layout.setContentsMargins(0, 0, 0, 0)
                    widget = QWidget()
                    widget.setLayout(layout)
                    self.table_supplier_import.setCellWidget(row_index, column_index + 3, widget)
                    row_index += 1

            except Exception as E:
                print(f"{E} - file ImportDetail.py function show_table_supplier line 128")
                return

    # hàm xử lý xóa nhà cung cấp đã lựa chọn
    def delete_supplier_import(self):
        print(1)

    def on_show_date_dialog(self, *arg):
        try:
            date_dialog = DateDialog(self)
            date_dialog.date_selected.connect(partial(self.on_selected_date, arg[0]))
            date_dialog.exec_()
        except Exception as E:
            print(E)
            return

    # hàm luôn chạy khi class được gọi đến
    # dùng để lấy dữ liệu mỗi lần vào form
    def showEvent(self, event):
        try:
            self.ui.dialog_import_title.setText("Thêm mới chứng từ")
            self.selected_date['import_date'] = QDate.currentDate()
            self.selected_date['delivery_date'] = QDate.currentDate()
            # gắn ngày tháng hiện tại lên 2 input date ngày nhập và ngày giao
            self.ui.import_date_le.setText(self.selected_date['import_date'].toString("dd/MM/yyyy"))
            self.ui.delivery_date_le.setText(self.selected_date['delivery_date'].toString("dd/MM/yyyy"))

            # lấy dữ liệu
            self.product_list = self.product_controller.getDataByModel()
            self.supplier_list = self.supplier_controller.getDataByModel()

            # gắn dữ liệu
            self.search_box_product_order.clear()
            self.search_box_supplier.clear()

            self.search_box_product_order.addItems([item.product_code for index, item in enumerate(self.product_list)])
            self.search_box_supplier.addItems([item.code for index, item in enumerate(self.supplier_list)])
        except Exception as E:
            print(f'{E}- file ImportDetail.py function showEvent')

    # hiển thị ngày tháng được chọn lên label
    def on_selected_date(self, key, selected_date):
        try:
            self.selected_date[key] = selected_date
            input_date_name = f"{key}_le"
            input_date = getattr(self.ui, input_date_name, None)
            input_date.setText(f"{selected_date.toString('dd/MM/yyyy')}")
        except Exception as E:
            print(f"{E} file ImportDetail function on_selected_date")
            return

    def show_table_product(self):
        self.table_product_import.setRowCount(0)
        if self.product_selected:
            try:
                row_index = 0
                for index, item in self.product_selected.items():
                    column_index = 0
                    self.table_product_import.setRowCount(row_index + 1)
                    self.table_product_import.setRowHeight(row_index, 120)
                    # cột sản phẩm
                    self.table_product_import.setCellWidget(row_index, column_index,
                                                           self.generate_info_product_order(item))
                    self.table_product_import.setColumnWidth(column_index, 200)
                    # cột đơn giá
                    self.table_product_import.setItem(row_index, column_index + 1,
                                                     QTableWidgetItem(formatCurrency(int(item.price), 'đ')))

                    widget_price, label_price = self.generate_column_price(row_index, item)  # tạo view cột thành tiền

                    # cột số lượng
                    self.table_product_import.setItem(row_index, column_index + 2, QTableWidgetItem(str(item.stock_quantity)))
                    # cột thành tiền
                    self.table_product_import.setCellWidget(row_index, column_index + 3, widget_price)
                    row_index += 1

            except Exception as E:
                print(f"{E} - file OrderDetail.py")
                return

        # xóa sản phẩm đã chọn
    def on_delete_product_order_detail(self):
        try:
            button = self.sender()
            row_id = int(button.objectName().strip().rsplit('_', 1)[-1])
            self.product_selected.pop(row_id, None)
            self.handle_total_quantity_product_order()
            self.show_table_product()
        except Exception as E:
            print(f"{E} file ImportDetail function on_delete_product_order_detail")

    def generate_info_product_order(self, data):
        self.widget = QtWidgets.QWidget()
        self.widget.setMinimumSize(QtCore.QSize(0, 100))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 110))
        self.widget.setStyleSheet("#info_product_order QPushButton{\n"
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
        self.widget.setObjectName("info_product_order")
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
        image_url = None
        if data.product_image:
            image_url = data.product_image[0].image_url
        self.label.setPixmap(QPixmap(image_url))
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
        self.product_name_order.setText(data.product_name)
        self.product_name_order.setObjectName("product_name_order")
        self.verticalLayout_2.addWidget(self.product_name_order)
        self.product_code_order = QtWidgets.QLabel(self.group_info_order)
        self.product_code_order.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.product_code_order.setText(data.product_code)
        self.product_code_order.setObjectName("product_code_order")
        self.verticalLayout_2.addWidget(self.product_code_order)
        self.delete_order_product = QtWidgets.QPushButton(self.group_info_order)
        self.delete_order_product.setMinimumSize(QtCore.QSize(30, 20))
        self.delete_order_product.setMaximumSize(QtCore.QSize(30, 20))
        self.delete_order_product.setText("Xóa")
        self.delete_order_product.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_order_product.setObjectName(f"delete_order_product_{data.id}")
        self.delete_order_product.clicked.connect(self.on_delete_product_order_detail)
        self.verticalLayout_2.addWidget(self.delete_order_product)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addWidget(self.group_info_order)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        return self.widget

    def generate_column_price(self, row, data):
        self.label = QtWidgets.QLabel()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # sét giá trị cột thành tiền
        self.label.setText(formatCurrency(int(data.stock_quantity) * int(data.price),
                                          'đ'))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName(f"label_price_{row}")
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.setAlignment(Qt.AlignHCenter | Qt.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        widget = QWidget()
        widget.setLayout(layout)
        return widget, self.label

    @pyqtSlot()
    def save_import(self, form_mode, import_id=None):
        try:
            code = self.ui.code_le.text().strip()
            # xử lý ngày tháng
            import_date = datetime(self.selected_date['import_date'].year(), self.selected_date['import_date'].month(), self.selected_date['import_date'].day())
            delivery_date = datetime(self.selected_date['delivery_date'].year(), self.selected_date['delivery_date'].month(), self.selected_date['delivery_date'].day())
            self.clear_error()
            messages = {
                'codeEmpty': "Vui lòng nhập mã chứng từ",
                'codeExit': "Mã chứng từ đã tồn tại.",
                'categoryEmpty': "Vui lòng chọn loại sản phẩm.",
                'product_imageEmpty': "Vui lòng chọn ảnh cho sản phẩm.",
                'manufacture_dateEmpty': "Vui lòng chọn ngày sản xuất.",
                'product_codeExit': "Mã sản phẩm đã tồn tại.",
                'priceGreater': "Vui lòng nhập giá lớn hơn 0.",
                'quantityGreater': "Vui lòng nhập số lượng lớn hơn 0.",
            }

            # validate dữ liệu các cột không được trống
            is_invalid = validateEmpty(self,
                                       {'code': code}, messages)

            if is_invalid:
                return

            data = PurchaseOrders(code=code, import_date=import_date, delivery_date=delivery_date, original_price=self.original_price, final_price=self.final_price, status=1, description='')
            product_relation = []
            for index, item in self.product_selected.items():
                data.products.append(item)
                product_relation.append({'product_id': item.id, 'import_id': import_id})

            for index, item in self.supplier_selected.items():
                data.suppliers.append(item)

            if form_mode == FormMode.ADD.value:
                if self.import_controller.checkExitsDataWithModel(PurchaseOrders.code, data=code):
                    self.ui.error_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_code.setText(messages["codeExit"])
                    self.ui.code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.import_controller.insertData(data)
            elif form_mode == FormMode.EDIT.value:
                del data.products
                del data.suppliers
                data.id = import_id
                if self.import_controller.checkExitsDataUpdateWithModel(PurchaseOrders.code, data=code,
                                                                         model_id=import_id):
                    self.ui.error_code.setStyleSheet(Validate.COLOR_TEXT_ERROR.value)
                    self.ui.error_code.setText(messages["codeExit"])
                    self.ui.code_le.setStyleSheet(Validate.BORDER_ERROR.value)
                    return
                self.import_controller.updateDataTest(
                    data,
                    {
                        'products': product_relation,
                    }
                )
            else:
                return

            return True
        except Exception as E:
            print(f'{E} - file ImportDetail.py function save_import')

    def handle_delete_event(self, import_id):
        try:
            reply = message_box_delete()
            if reply == QMessageBox.Yes:
                self.import_controller.deleteDataWithModel(import_id)
        except Exception as E:
            print(E)
            return False
        return True

    # gán các giá trị lên form
    def handle_edit_event(self, import_id):
        self.ui.dialog_import_title.setText("Cập nhật chứng từ")
        data = self.import_controller.getDataByIdWithModel(import_id)
        if data:
            self.ui.code_le.setText(data.code)
            self.selected_date['import_date'] = QDate(data.import_date.year, data.import_date.month,
                                       data.import_date.day)
            self.selected_date['delivery_date'] = QDate(data.delivery_date.year, data.delivery_date.month,
                                                      data.delivery_date.day)

            # xử lý ngày tháng
            self.ui.import_date_le.setText(f"{self.selected_date['import_date'].toString('dd/MM/yyyy')}")
            self.ui.delivery_date_le.setText(f"{self.selected_date['delivery_date'].toString('dd/MM/yyyy')}")
            self.ui.discount_le.setValue(data.discount)
            self.ui.vat_le.setValue(data.vat)
            if data.products:
                self.product_selected = {product.id: product for product in data.products}
                self.show_table_product()
                self.handle_total_quantity_product_order()
            if data.suppliers:
                self.supplier_selected = {supplier.id: supplier for supplier in data.suppliers}
                self.show_table_supplier()




    # clear dữ liệu trên form
    def clear_form(self):
        try:
            self.clear_error()
            self.ui.code_le.setStyleSheet("border: 1px solid #e0e5e9;")
            # self.ui.supplier_le.currentIndex(1)
            # self.ui.search_box_product_order.currentIndex(1)
            self.ui.error_code.setText("")
            self.ui.code_le.setText("")
            self.ui.discount_le.setValue(0)
            self.ui.vat_le.setValue(0)
            self.ui.table_product_import.setRowCount(0)
            self.ui.table_supplier.setRowCount(0)
        except Exception as E:
            print(f'{E} - file ImportDetail.py function clear_form')


    def clear_error(self):
        self.ui.code_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.error_code.setText("")

