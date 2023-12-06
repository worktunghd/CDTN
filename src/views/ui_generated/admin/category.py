# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/admin/category.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(870, 742)
        Form.setStyleSheet("#btn_add_category{\n"
"        width:  100px;\n"
"        background: #2979ff;\n"
"        color: #fff;\n"
"}\n"
"\n"
"#btn_add_category:hover{\n"
"    background: #1a73e8;\n"
"}\n"
"\n"
"#btn_add_category QLabel{\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"      height: 48px;\n"
"    font-weight: 600;\n"
"    text-align: left;\n"
"    font-size: 14px;\n"
"    border-bottom: 1px solid #e0e1ef;\n"
"    border-right: 1px solid #e0e1ef;\n"
"    font-weight: 600;\n"
"    background: #fff;\n"
"    padding: 0 16px;\n"
"}\n"
"#tableUserContainer{\n"
"    border: none;\n"
"    border-radius:  4px;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"       padding: 0 16px;\n"
"    vertical-align: middle;\n"
"    height: 50px;\n"
"    border-bottom: 1px solid #ddd;    \n"
"    border-right: 1px solid #ddd;\n"
"}\n"
"\n"
"#stackedWidget{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#userDialogForm QLabel{\n"
"    color: #000;\n"
"    font-size: 16px;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"#userDialogForm  QLineEdit{\n"
"    border: 1px solid #e0e5e9;\n"
"    background: transparent;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid #e0e5e9;\n"
"    font-size: 16px;\n"
"    line-height: 1.2;\n"
"    min-height:34px;\n"
"    height: 34px;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    min-width: 200px;\n"
"}\n"
"\n"
"#centralwidget QLineEdit:focus {\n"
"    border-color: #5500ff;\n"
"}\n"
"\n"
"#btnCancelUser{\n"
"    background: #ebebeb;\n"
"    outline: none;\n"
"    border: 1px solid #e0e0e0;\n"
"    min-height: 36px;\n"
"    min-width: 80px;\n"
"    border-radius: 4px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"#btnCancelUser:hover{\n"
"    background: #f4f5f8;\n"
"}\n"
"\n"
"#btnUser{\n"
"    min-height: 36px;\n"
"    border-radius: 4px;\n"
"    color: #fff;\n"
"    background: #2979ff;\n"
"    border: 1px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    min-height: 36px;\n"
"    font-size: 14px;\n"
"    padding: 2px 12px;\n"
"}\n"
"\n"
"#btnUser:hover{\n"
"        background: #0062cc;\n"
"}\n"
"\n"
"#footerUserContainer{\n"
"     background-color: #fbfbfe;\n"
"    padding: 12px 24px;\n"
"    border-top: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"#backBtn{\n"
"    margin-left: 10px;\n"
"    margin-right: 10px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"#dialogTitleUser{\n"
"    font-size: 20px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#popupHeader{\n"
"    height: 60px;\n"
"    min-height: 24px;\n"
"}\n"
"\n"
"#widget_12, #widget_11, #widget_10, #widget_7{\n"
"        border-bottom: 1px solid #e0e0e0;\n"
"}    \n"
"\n"
"#userDialogForm{\n"
"        border-radius: 4px;\n"
"        border: 1px solid #e0e0e0;\n"
"}\n"
"\n"
"\n"
"\n"
"#userDialogFormSubContainer{\n"
"    background: #e9e9e9;\n"
"    border-radius: 4px;\n"
"}\n"
" #formInput_4 QLabel {\n"
"    margin-top: 10px;\n"
"}\n"
"QHBoxLayout QLabel{\n"
"    background: red;\n"
"}\n"
"\n"
"#labelName, #labelUserName, #labelPassword, #labelConfirm{\n"
"    margin-top:30px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    min-width: 80px;\n"
"    min-height: 36px;\n"
"    border-radius: 4px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#error_name, #error_password, #error_username, #error_confirm{\n"
"    padding-top: 8px;\n"
"    padding-bottom: 8px;\n"
"}\n"
"\n"
"#addUserBtn{\n"
"        width:  100px;\n"
"        background: #2979ff;\n"
"        color: #fff;\n"
"}\n"
"\n"
"#addUserBtn:hover{\n"
"    background: #1a73e8;\n"
"}\n"
"\n"
"#addUserBtn QLabel{\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"#search_btn_2{\n"
"    min-width: 40px;\n"
"    border: none;\n"
"}\n"
"\n"
"#searchBoxContainer QLineEdit, #searchBoxContainer_2 QLineEdit{\n"
"    border: none;\n"
"}\n"
"\n"
"#searchBoxContainer{\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 3.5px;    \n"
"    min-height: 36px;\n"
"}\n"
"\n"
"#searchBoxContainer_2{\n"
"    border: 1px solid #e0e0e0;\n"
"    border-radius: 3.5px;\n"
"    min-height: 36px;\n"
"}\n"
"\n"
"#headerAdmin{\n"
"    background: #fff;\n"
"}\n"
"\n"
"#change_btn{\n"
"    max-width: 20px !important;\n"
"}\n"
"\n"
"#change_btn:hover{\n"
"    background: #ddd;\n"
"}\n"
"\n"
"#change_btn, #search_btn_5,  #search_btn_2, #back_btn_user{\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"#search_input_5{\n"
"    padding: 0;\n"
"    padding-left: 10px\n"
"}\n"
"\n"
"#customers_btn_2, #products_btn_2, #orders_btn_2, #dashboard_btn_2,#home_btn_2,#user_btn_2{\n"
"    text-align: left;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.userContainer = QtWidgets.QWidget(Form)
        self.userContainer.setObjectName("userContainer")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.userContainer)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.titleContainer = QtWidgets.QWidget(self.userContainer)
        self.titleContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.titleContainer.setObjectName("titleContainer")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.titleContainer)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget_4 = QtWidgets.QWidget(self.titleContainer)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.gridLayout_12.addWidget(self.widget_4, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.titleContainer)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.searchBoxContainer = QtWidgets.QWidget(self.widget_2)
        self.searchBoxContainer.setObjectName("searchBoxContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.searchBoxContainer)
        self.horizontalLayout_5.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.searchBox = QtWidgets.QHBoxLayout()
        self.searchBox.setContentsMargins(2, -1, -1, -1)
        self.searchBox.setSpacing(0)
        self.searchBox.setObjectName("searchBox")
        self.search_input_2 = QtWidgets.QLineEdit(self.searchBoxContainer)
        self.search_input_2.setMinimumSize(QtCore.QSize(220, 44))
        self.search_input_2.setObjectName("search_input_2")
        self.searchBox.addWidget(self.search_input_2)
        self.search_btn_2 = QtWidgets.QPushButton(self.searchBoxContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn_2.sizePolicy().hasHeightForWidth())
        self.search_btn_2.setSizePolicy(sizePolicy)
        self.search_btn_2.setMinimumSize(QtCore.QSize(54, 40))
        self.search_btn_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.search_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/icon/search-13-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn_2.setIcon(icon)
        self.search_btn_2.setObjectName("search_btn_2")
        self.searchBox.addWidget(self.search_btn_2)
        self.horizontalLayout_5.addLayout(self.searchBox)
        self.horizontalLayout_6.addWidget(self.searchBoxContainer)
        spacerItem = QtWidgets.QSpacerItem(308, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setMinimumSize(QtCore.QSize(100, 0))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.btn_add_category = QtWidgets.QPushButton(self.widget_5)
        self.btn_add_category.setMinimumSize(QtCore.QSize(124, 40))
        self.btn_add_category.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/resources/icon/plus-solid.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_add_category.setIcon(icon1)
        self.btn_add_category.setAutoRepeatInterval(100)
        self.btn_add_category.setObjectName("btn_add_category")
        self.verticalLayout_12.addWidget(self.btn_add_category)
        self.horizontalLayout_6.addWidget(self.widget_5)
        self.gridLayout_12.addWidget(self.widget_2, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.titleContainer, 0, 0, 1, 1)
        self.tableContainer = QtWidgets.QWidget(self.userContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableContainer.sizePolicy().hasHeightForWidth())
        self.tableContainer.setSizePolicy(sizePolicy)
        self.tableContainer.setObjectName("tableContainer")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tableContainer)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tableUserContainer = QtWidgets.QFrame(self.tableContainer)
        self.tableUserContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableUserContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableUserContainer.setObjectName("tableUserContainer")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tableUserContainer)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.table_category = QtWidgets.QTableWidget(self.tableUserContainer)
        self.table_category.setEnabled(True)
        self.table_category.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.table_category.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_category.setAcceptDrops(False)
        self.table_category.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.table_category.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_category.setProperty("showDropIndicator", True)
        self.table_category.setDragEnabled(False)
        self.table_category.setAlternatingRowColors(False)
        self.table_category.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_category.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_category.setIconSize(QtCore.QSize(0, 0))
        self.table_category.setTextElideMode(QtCore.Qt.ElideRight)
        self.table_category.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.table_category.setShowGrid(False)
        self.table_category.setGridStyle(QtCore.Qt.NoPen)
        self.table_category.setRowCount(2)
        self.table_category.setColumnCount(5)
        self.table_category.setObjectName("table_category")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.table_category.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_category.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_category.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_category.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.table_category.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_category.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_category.setItem(1, 0, item)
        self.table_category.horizontalHeader().setVisible(False)
        self.table_category.horizontalHeader().setCascadingSectionResizes(False)
        self.table_category.horizontalHeader().setDefaultSectionSize(200)
        self.table_category.horizontalHeader().setHighlightSections(True)
        self.table_category.horizontalHeader().setMinimumSectionSize(57)
        self.table_category.horizontalHeader().setSortIndicatorShown(False)
        self.table_category.horizontalHeader().setStretchLastSection(True)
        self.table_category.verticalHeader().setVisible(False)
        self.table_category.verticalHeader().setCascadingSectionResizes(False)
        self.table_category.verticalHeader().setDefaultSectionSize(40)
        self.table_category.verticalHeader().setHighlightSections(True)
        self.table_category.verticalHeader().setMinimumSectionSize(21)
        self.gridLayout_9.addWidget(self.table_category, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.tableUserContainer, 0, 0, 1, 1)
        self.gridLayout_10.addWidget(self.tableContainer, 1, 0, 1, 1)
        self.gridLayout_8.addWidget(self.userContainer, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_8)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Danh sách loại sản phẩm"))
        self.search_input_2.setPlaceholderText(_translate("Form", "Search..."))
        self.btn_add_category.setText(_translate("Form", "Thêm mới"))
        self.table_category.setSortingEnabled(False)
        item = self.table_category.horizontalHeaderItem(0)
        item.setText(_translate("Form", "#"))
        item = self.table_category.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID"))
        item = self.table_category.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tài khoản"))
        item = self.table_category.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Họ và tên"))
        item = self.table_category.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thao tác"))
        __sortingEnabled = self.table_category.isSortingEnabled()
        self.table_category.setSortingEnabled(False)
        item = self.table_category.item(0, 0)
        item.setText(_translate("Form", "1"))
        item = self.table_category.item(1, 0)
        item.setText(_translate("Form", "2"))
        self.table_category.setSortingEnabled(__sortingEnabled)
import ui.resource_rc
