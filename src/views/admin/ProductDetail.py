from PyQt5.QtWidgets import QFileDialog, QCalendarWidget
from PyQt5.QtCore import pyqtSlot, QFileInfo
from src.views.ui_generated.admin.product_detail import Ui_Form
from src.views.common.Common import *
import os
from src.enums.enums import *
from src.views.common.Common import *
from src.controllers.admin.ProductController import ProductController
from src.controllers.admin.CategoryController import CategoryController
from src.models.products import Product
from src.models.images import Image
import shutil

class ProductDetailWindow(QWidget):
    def __init__(self):
        super(ProductDetailWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.category_controller = CategoryController()
        self.product_controller = ProductController()
        # khởi tạo biến
        self.product_image = None
        # khởi tạo các button
        self.btn_image_product = self.ui.btn_image_product
        self.btn_manufacture_date_product = self.ui.btn_manufacture_date_product

        # kết nôi với sự kiện
        self.btn_image_product.clicked.connect(
            lambda: self.on_chose_image()
        )
        self.btn_manufacture_date_product.clicked.connect(
            lambda: self.show_date_dialog()
        )

        # Lấy danh sách loại sản phẩm để gắn lên combobox
        self.category = None
        self.combobox_category = self.ui.category_le
        self.product_image_le = self.ui.product_image_le
        self.manufacture_date_le = self.ui.manufacture_date_le

    def showEvent(self, event):
        self.category = self.category_controller.getDataByModel()
        if self.category:
            self.combobox_category.clear()
            for item in self.category:
                self.combobox_category.addItem(item.category_name)
        else:
            self.combobox_category.addItem("Không có dữ liệu")


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
    def save_product(self, form_mode, product_id=None):
        product_name = self.ui.product_name_le.text().strip()
        product_code = self.ui.product_code_le.text().strip()
        category = self.ui.category_le.currentText()
        manufacture_date = self.ui.manufacture_date_le.text().strip()
        price = self.ui.price_le.value()
        quantity = self.ui.quantity_le.value()
        product_image = self.ui.product_image_le.text().strip()
        description = self.ui.description_le.toPlainText().strip()
        border_error = Validate.BORDER_ERROR.value
        border_valid = Validate.BORDER_VALID.value
        color_text_error = Validate.COLOR_TEXT_ERROR.value
        self.clear_error()
        messages = {
            'product_nameEmpty': "Vui lòng nhập tên sản phẩm.",
            'product_codeEmpty': "Vui lòng nhập mã sản phẩm.",
            'categoryEmpty': "Vui lòng chọn loại sản phẩm.",
            'product_imageEmpty': "Vui lòng chọn ảnh cho sản phẩm.",
            'manufacture_dateEmpty': "Vui lòng chọn ngày sản xuất.",
            'product_codeExit': "Mã sản phẩm đã tồn tại.",
            'priceGreater': "Vui lòng nhập giá lớn hơn 0.",
            'quantityGreater': "Vui lòng nhập số lượng lớn hơn 0.",
        }

        if category == SelectBox.DEFAULT.value:
            category = ''

        # validate dữ liệu các cột không được trống
        is_invalid = validateEmpty(self,{'product_name': product_name, 'product_code': product_code, 'category': category, 'manufacture_date': manufacture_date, 'product_image': product_image}, messages)
        if price == 0:
            self.ui.error_price.setStyleSheet(color_text_error)
            self.ui.error_price.setText(messages["priceGreater"])
            self.ui.price_le.setStyleSheet(border_error)
            is_invalid = True

        if quantity == 0:
            self.ui.error_quantity.setStyleSheet(color_text_error)
            self.ui.error_quantity.setText(messages["quantityGreater"])
            self.ui.quantity_le.setStyleSheet(border_error)
            is_invalid = True
        if is_invalid:
            return


        destination_folder = "resources/images/product"
        # Tạo thư mục lưu trữ ảnh sản phẩm nếu chưa có
        os.makedirs(destination_folder, exist_ok=True)
        # Đường dẫn đến thư mục đích
        new_file_name = generate_unique_filename(product_image)
        destination_path = os.path.join(destination_folder, new_file_name)
        product = Product(product_code=product_code, product_name=product_name, price=price, quantity=quantity, description=description, manufacture_date=manufacture_date)
        image = Image(image_url=destination_path)
        product.product_image = [image]
        if form_mode == FormMode.ADD.value:
            if self.product_controller.checkExitsDataWithModel(Product.product_code, data=product_code):
                self.ui.error_product_code.setStyleSheet(color_text_error)
                self.ui.error_product_code.setText(messages["product_codeExit"])
                self.ui.product_code_le.setStyleSheet(border_error)
                return

            self.product_controller.insertData(product)
        elif form_mode == FormMode.EDIT.value:
            if self.product_controller.checkExitsDataUpdateWithModel(Product.product_code, data=product_code, model_id=product_id):
                self.ui.error_product_code.setStyleSheet(color_text_error)
                self.ui.error_product_code.setText(messages["product_codeExit"])
                self.ui.product_code_le.setStyleSheet(border_error)
                return
            self.product_controller.updateDataWithModel(data={'product_name': product_name, 'product_code': product_code, 'price': price, 'quantity': quantity, 'description': description, 'manufacture_date':manufacture_date, 'product_image': [image]}, model_id=product_id)
        else:
            return

        return True

    # gán các giá trị lên form
    def handle_edit_event(self, category_id):
        product = self.product_controller.getDataByIdWithModel(category_id)
        if product:
            self.ui.product_name_le.setText(product.product_name)

    # clear dữ liệu trên form
    def clear_form(self):
        self.ui.product_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.product_code_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.product_image_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.category_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.price_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.quantity_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.manufacture_date_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.error_product_name.setText("")
        self.ui.error_product_code.setText("")
        self.ui.error_category.setText("")
        self.ui.error_product_image.setText("")
        self.ui.error_price.setText("")
        self.ui.error_quantity.setText("")
        self.ui.error_manufacture_date.setText("")
        self.ui.product_name_le.setText("")
        self.ui.product_image_le.setText("")
        # self.ui.combobox_category_i
        self.ui.price_le.setValue(0)
        self.ui.quantity_le.setValue(0)
        self.ui.manufacture_date_le.setText("")
        self.ui.description_le.setPlainText("")

    def clear_error(self):
        self.ui.product_name_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.product_code_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.product_image_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.category_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.price_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.quantity_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.manufacture_date_le.setStyleSheet("border: 1px solid #e0e5e9;")
        self.ui.error_product_name.setText("")
        self.ui.error_product_code.setText("")
        self.ui.error_category.setText("")
        self.ui.error_product_image.setText("")
        self.ui.error_price.setText("")
        self.ui.error_quantity.setText("")