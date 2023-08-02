# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledJhlmXw.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)
from PySide6 import QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.ico"),
        QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)

        try:
            from PyQt5.QtWinExtras import QtWin  # !!!
            myappid = 'mycompany.myproduct.subproduct.version'  # !!!
            QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
        except ImportError:
            pass

        MainWindow.resize(382, 633)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(66, 66, 66, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(99, 99, 99, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(82, 82, 82, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(33, 33, 33, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(44, 44, 44, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(45, 45, 45, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        brush8 = QBrush(QColor(0, 0, 0, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush8)
        brush9 = QBrush(QColor(255, 255, 255, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush8)
        brush10 = QBrush(QColor(33, 33, 33, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush10)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Consolas"])

        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.encrypt_Button = QRadioButton(self.centralwidget)
        self.encrypt_Button.setObjectName(u"encrypt_Button")
        self.encrypt_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.encrypt_Button.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.encrypt_Button)

        self.decipher_Button = QRadioButton(self.centralwidget)
        self.decipher_Button.setObjectName(u"decipher_Button")
        self.decipher_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.decipher_Button.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout.addWidget(self.decipher_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.text_label = QLabel(self.centralwidget)
        self.text_label.setObjectName(u"text_label")
        self.text_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.text_label)

        self.text_in = QTextEdit(self.centralwidget)
        self.text_in.setObjectName(u"text_in")

        self.verticalLayout.addWidget(self.text_in)

        self.shift_label = QLabel(self.centralwidget)
        self.shift_label.setObjectName(u"shift_label")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.shift_label.setFont(font1)
        self.shift_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.shift_label)

        self.Shift_box = QSpinBox(self.centralwidget)
        self.Shift_box.setObjectName(u"Shift_box")
        self.Shift_box.setCursor(QCursor(Qt.PointingHandCursor))
        self.Shift_box.setMinimum(1)
        self.Shift_box.setStyleSheet(u"color: rgb(88, 88, 88);")
        self.Shift_box.setMaximum(25)

        self.verticalLayout.addWidget(self.Shift_box)

        self.do_Button = QPushButton(self.centralwidget)
        self.do_Button.setObjectName(u"do_Button")
        self.do_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.do_Button.setStyleSheet(u"color: rgb(88, 88, 88);")

        self.verticalLayout.addWidget(self.do_Button)

        self.text_out = QTextEdit(self.centralwidget)
        self.text_out.setObjectName(u"text_out")
        self.text_out.setReadOnly(True)

        self.verticalLayout.addWidget(self.text_out)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.encrypt_Button.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decipher_Button.setText(QCoreApplication.translate("MainWindow", u"Decipher", None))
        self.text_label.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.shift_label.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.do_Button.setText(QCoreApplication.translate("MainWindow", u"/// Calculate ///", None))
#if QT_CONFIG(shortcut)
        self.do_Button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

