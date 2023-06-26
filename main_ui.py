# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 1054)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(169, 188, 188))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("QTabWidget::pane\n"
"{\n"
"    border: 2px solid rgb(48,144,145);\n"
"    background-color: transparent;\n"
"    color: #000000;\n"
"}\n"
"\n"
"QMainWindow::pane\n"
"{\n"
"    background-color: rgb(102,117,117)\n"
"}\n"
"\n"
"QTabBar::tab\n"
"{\n"
"    background-color: transparent;\n"
"    color: #000000\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    background-color: rgb(48,144,145);\n"
"    color: #000000\n"
"}\n"
"\n"
"QTabBar::tab:hover\n"
"{\n"
"    background-color: rgb(48,144,145,160);\n"
"    color: #000000\n"
"}\n"
"\n"
"QTabWidget::tab-bar{\n"
"    alignment: center;\n"
"}\n"
"")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 1201, 1001))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 30, 211, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(10, 200, 1181, 761))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_Add = QtWidgets.QPushButton(self.tab)
        self.pushButton_Add.setGeometry(QtCore.QRect(10, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setObjectName("pushButton_Add")
        self.pushButton_Create = QtWidgets.QPushButton(self.tab)
        self.pushButton_Create.setGeometry(QtCore.QRect(230, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pushButton_Create.setFont(font)
        self.pushButton_Create.setObjectName("pushButton_Create")
        self.pushButton_Open = QtWidgets.QPushButton(self.tab)
        self.pushButton_Open.setGeometry(QtCore.QRect(670, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pushButton_Open.setFont(font)
        self.pushButton_Open.setObjectName("pushButton_Open")
        self.pushButton_Remove = QtWidgets.QPushButton(self.tab)
        self.pushButton_Remove.setGeometry(QtCore.QRect(450, 140, 191, 51))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.pushButton_Remove.setFont(font)
        self.pushButton_Remove.setObjectName("pushButton_Remove")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1201, 981))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1247, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Projects"))
        self.pushButton_Add.setText(_translate("MainWindow", "Add"))
        self.pushButton_Create.setText(_translate("MainWindow", "Create"))
        self.pushButton_Open.setText(_translate("MainWindow", "Open"))
        self.pushButton_Remove.setText(_translate("MainWindow", "Remove"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Projects"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Learn"))
