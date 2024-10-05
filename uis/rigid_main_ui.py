# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rigid_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(419, 429)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(10, 30, 401, 401))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.visuals_tab = QWidget()
        self.visuals_tab.setObjectName(u"visuals_tab")
        self.verticalLayoutWidget = QWidget(self.visuals_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 211, 201))
        self.gridLayout_3 = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.load_data_button = QPushButton(self.verticalLayoutWidget)
        self.load_data_button.setObjectName(u"load_data_button")

        self.gridLayout_3.addWidget(self.load_data_button, 0, 0, 1, 1)

        self.save_data_button = QPushButton(self.verticalLayoutWidget)
        self.save_data_button.setObjectName(u"save_data_button")

        self.gridLayout_3.addWidget(self.save_data_button, 1, 0, 1, 1)

        self.copy_data_button = QPushButton(self.verticalLayoutWidget)
        self.copy_data_button.setObjectName(u"copy_data_button")

        self.gridLayout_3.addWidget(self.copy_data_button, 2, 0, 1, 1)

        self.replace_sel_button = QPushButton(self.verticalLayoutWidget)
        self.replace_sel_button.setObjectName(u"replace_sel_button")

        self.gridLayout_3.addWidget(self.replace_sel_button, 3, 0, 1, 1)

        self.build_button = QPushButton(self.verticalLayoutWidget)
        self.build_button.setObjectName(u"build_button")

        self.gridLayout_3.addWidget(self.build_button, 4, 0, 1, 1)

        self.build_match_button = QPushButton(self.verticalLayoutWidget)
        self.build_match_button.setObjectName(u"build_match_button")

        self.gridLayout_3.addWidget(self.build_match_button, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mirror_x_button = QPushButton(self.verticalLayoutWidget)
        self.mirror_x_button.setObjectName(u"mirror_x_button")
        self.mirror_x_button.setStyleSheet(u"background-color: #CCC444444;")

        self.horizontalLayout.addWidget(self.mirror_x_button)

        self.mirror_y_button = QPushButton(self.verticalLayoutWidget)
        self.mirror_y_button.setObjectName(u"mirror_y_button")
        self.mirror_y_button.setStyleSheet(u"background-color: #888888222;")

        self.horizontalLayout.addWidget(self.mirror_y_button)

        self.mirror_z_button = QPushButton(self.verticalLayoutWidget)
        self.mirror_z_button.setObjectName(u"mirror_z_button")
        self.mirror_z_button.setStyleSheet(u"background-color: #333333CCC;")

        self.horizontalLayout.addWidget(self.mirror_z_button)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout_3.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.frame = QFrame(self.visuals_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(240, 10, 121, 111))
        self.frame.setStyleSheet(u"background-color: #6B6A5B; color: #FFFFFF; font: bold;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 1, 101, 21))
        self.cur_data_label = QLabel(self.frame)
        self.cur_data_label.setObjectName(u"cur_data_label")
        self.cur_data_label.setGeometry(QRect(10, 20, 101, 81))
        self.label_3 = QLabel(self.visuals_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 130, 81, 20))
        self.verticalLayoutWidget_2 = QWidget(self.visuals_tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 220, 341, 145))
        self.colourLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.colourLayout.setSpacing(3)
        self.colourLayout.setObjectName(u"colourLayout")
        self.colourLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.thicken25_button = QPushButton(self.verticalLayoutWidget_2)
        self.thicken25_button.setObjectName(u"thicken25_button")

        self.verticalLayout_2.addWidget(self.thicken25_button)

        self.thicken40_button = QPushButton(self.verticalLayoutWidget_2)
        self.thicken40_button.setObjectName(u"thicken40_button")

        self.verticalLayout_2.addWidget(self.thicken40_button)

        self.unthicken_button = QPushButton(self.verticalLayoutWidget_2)
        self.unthicken_button.setObjectName(u"unthicken_button")

        self.verticalLayout_2.addWidget(self.unthicken_button)

        self.copycolour_button = QPushButton(self.verticalLayoutWidget_2)
        self.copycolour_button.setObjectName(u"copycolour_button")

        self.verticalLayout_2.addWidget(self.copycolour_button)

        self.pastecolour_button = QPushButton(self.verticalLayoutWidget_2)
        self.pastecolour_button.setObjectName(u"pastecolour_button")

        self.verticalLayout_2.addWidget(self.pastecolour_button)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.yellow_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.yellow_pushbutton.setObjectName(u"yellow_pushbutton")
        self.yellow_pushbutton.setStyleSheet(u"background-color: #ffee00;")

        self.gridLayout_2.addWidget(self.yellow_pushbutton, 1, 2, 1, 1)

        self.paleyellow_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.paleyellow_pushbutton.setObjectName(u"paleyellow_pushbutton")
        self.paleyellow_pushbutton.setStyleSheet(u"background-color: #EEFF99")

        self.gridLayout_2.addWidget(self.paleyellow_pushbutton, 2, 2, 1, 1)

        self.red_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.red_pushbutton.setObjectName(u"red_pushbutton")
        self.red_pushbutton.setStyleSheet(u"background-color: #FF5733;")

        self.gridLayout_2.addWidget(self.red_pushbutton, 1, 1, 1, 1)

        self.palered_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.palered_pushbutton.setObjectName(u"palered_pushbutton")
        self.palered_pushbutton.setStyleSheet(u"background-color: #FF9999")

        self.gridLayout_2.addWidget(self.palered_pushbutton, 2, 1, 1, 1)

        self.purple_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.purple_pushbutton.setObjectName(u"purple_pushbutton")
        self.purple_pushbutton.setStyleSheet(u"background-color: #FF00FF;")

        self.gridLayout_2.addWidget(self.purple_pushbutton, 3, 1, 1, 1)

        self.green_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.green_pushbutton.setObjectName(u"green_pushbutton")
        self.green_pushbutton.setStyleSheet(u"background-color: #01ff16")

        self.gridLayout_2.addWidget(self.green_pushbutton, 3, 2, 1, 1)

        self.blue_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.blue_pushbutton.setObjectName(u"blue_pushbutton")
        self.blue_pushbutton.setStyleSheet(u"background-color: #5555FF;")

        self.gridLayout_2.addWidget(self.blue_pushbutton, 1, 3, 1, 1)

        self.paleblue_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.paleblue_pushbutton.setObjectName(u"paleblue_pushbutton")
        self.paleblue_pushbutton.setStyleSheet(u"background-color: #9999FF")

        self.gridLayout_2.addWidget(self.paleblue_pushbutton, 2, 3, 1, 1)

        self.black_pushbutton = QPushButton(self.verticalLayoutWidget_2)
        self.black_pushbutton.setObjectName(u"black_pushbutton")
        self.black_pushbutton.setStyleSheet(u"background-color: #464646;")

        self.gridLayout_2.addWidget(self.black_pushbutton, 3, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.colourLayout.addLayout(self.horizontalLayout_2)

        self.resize_dial = QDial(self.visuals_tab)
        self.resize_dial.setObjectName(u"resize_dial")
        self.resize_dial.setGeometry(QRect(240, 150, 61, 51))
        self.resize_dial.setMaximum(100)
        self.sizeup_button = QPushButton(self.visuals_tab)
        self.sizeup_button.setObjectName(u"sizeup_button")
        self.sizeup_button.setGeometry(QRect(310, 150, 21, 21))
        self.sizeup_button.setStyleSheet(u"background-color: #F08969; color: black; font-size: 14px;")
        self.sizedown_button = QPushButton(self.visuals_tab)
        self.sizedown_button.setObjectName(u"sizedown_button")
        self.sizedown_button.setGeometry(QRect(310, 180, 21, 21))
        self.sizedown_button.setStyleSheet(u"background-color: #F08969; color: black; font-size: 14x;")
        self.tabWidget.addTab(self.visuals_tab, "")
        self.build_tab = QWidget()
        self.build_tab.setObjectName(u"build_tab")
        self.verticalLayoutWidget_3 = QWidget(self.build_tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 12, 351, 111))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fast_fk_button = QPushButton(self.verticalLayoutWidget_3)
        self.fast_fk_button.setObjectName(u"fast_fk_button")

        self.verticalLayout_3.addWidget(self.fast_fk_button)

        self.fast_fk_button_2 = QPushButton(self.verticalLayoutWidget_3)
        self.fast_fk_button_2.setObjectName(u"fast_fk_button_2")
        self.fast_fk_button_2.setEnabled(False)

        self.verticalLayout_3.addWidget(self.fast_fk_button_2)

        self.ribbon_joints_button = QPushButton(self.verticalLayoutWidget_3)
        self.ribbon_joints_button.setObjectName(u"ribbon_joints_button")

        self.verticalLayout_3.addWidget(self.ribbon_joints_button)

        self.tabWidget.addTab(self.build_tab, "")
        self.naming_tab = QWidget()
        self.naming_tab.setObjectName(u"naming_tab")
        self.gridLayoutWidget_2 = QWidget(self.naming_tab)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 351, 131))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.smartrename_lineedit = QLineEdit(self.gridLayoutWidget_2)
        self.smartrename_lineedit.setObjectName(u"smartrename_lineedit")

        self.gridLayout_4.addWidget(self.smartrename_lineedit, 1, 1, 1, 1)

        self.prefix_button = QPushButton(self.gridLayoutWidget_2)
        self.prefix_button.setObjectName(u"prefix_button")

        self.gridLayout_4.addWidget(self.prefix_button, 2, 0, 1, 1)

        self.suffix_button = QPushButton(self.gridLayoutWidget_2)
        self.suffix_button.setObjectName(u"suffix_button")

        self.gridLayout_4.addWidget(self.suffix_button, 3, 0, 1, 1)

        self.smart_rename_button = QPushButton(self.gridLayoutWidget_2)
        self.smart_rename_button.setObjectName(u"smart_rename_button")

        self.gridLayout_4.addWidget(self.smart_rename_button, 1, 0, 1, 1)

        self.suffix_lineedit = QLineEdit(self.gridLayoutWidget_2)
        self.suffix_lineedit.setObjectName(u"suffix_lineedit")

        self.gridLayout_4.addWidget(self.suffix_lineedit, 3, 1, 1, 1)

        self.prefix_lineedit = QLineEdit(self.gridLayoutWidget_2)
        self.prefix_lineedit.setObjectName(u"prefix_lineedit")

        self.gridLayout_4.addWidget(self.prefix_lineedit, 2, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.gridLayout_4.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_6 = QLabel(self.naming_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 150, 351, 81))
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.tabWidget.addTab(self.naming_tab, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 341, 16))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.exit_button = QPushButton(Form)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(370, 10, 16, 16))

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.load_data_button.setText(QCoreApplication.translate("Form", u"Load CurveData from JSON", None))
        self.save_data_button.setText(QCoreApplication.translate("Form", u"Save CurveData to JSON", None))
        self.copy_data_button.setText(QCoreApplication.translate("Form", u"Copy From Selected", None))
        self.replace_sel_button.setText(QCoreApplication.translate("Form", u"Replace Selected", None))
        self.build_button.setText(QCoreApplication.translate("Form", u"Make New at Origin", None))
        self.build_match_button.setText(QCoreApplication.translate("Form", u"Make Matching Selected", None))
        self.mirror_x_button.setText(QCoreApplication.translate("Form", u"Mirror X", None))
        self.mirror_y_button.setText(QCoreApplication.translate("Form", u"Mirror Y", None))
        self.mirror_z_button.setText(QCoreApplication.translate("Form", u"Mirror Z", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Invert", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Current Data:", None))
        self.cur_data_label.setText(QCoreApplication.translate("Form", u"Unknown", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Control Scale:", None))
        self.thicken25_button.setText(QCoreApplication.translate("Form", u"Thickness 2.5", None))
        self.thicken40_button.setText(QCoreApplication.translate("Form", u"Thickness 4.0", None))
        self.unthicken_button.setText(QCoreApplication.translate("Form", u"Default Thickness", None))
        self.copycolour_button.setText(QCoreApplication.translate("Form", u"Copy Colour", None))
        self.pastecolour_button.setText(QCoreApplication.translate("Form", u"Paste Colour", None))
        self.yellow_pushbutton.setText("")
        self.paleyellow_pushbutton.setText("")
        self.red_pushbutton.setText("")
        self.palered_pushbutton.setText("")
        self.purple_pushbutton.setText("")
        self.green_pushbutton.setText("")
        self.blue_pushbutton.setText("")
        self.paleblue_pushbutton.setText("")
        self.black_pushbutton.setText("")
        self.sizeup_button.setText(QCoreApplication.translate("Form", u"+", None))
        self.sizedown_button.setText(QCoreApplication.translate("Form", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visuals_tab), QCoreApplication.translate("Form", u"CONTROLS", None))
        self.fast_fk_button.setText(QCoreApplication.translate("Form", u"Fast FK", None))
        self.fast_fk_button_2.setText(QCoreApplication.translate("Form", u"Fast IK", None))
        self.ribbon_joints_button.setText(QCoreApplication.translate("Form", u"Ribbon Joints", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.build_tab), QCoreApplication.translate("Form", u"BUILD", None))
        self.prefix_button.setText(QCoreApplication.translate("Form", u"Prefix", None))
        self.suffix_button.setText(QCoreApplication.translate("Form", u"Suffix", None))
#if QT_CONFIG(tooltip)
        self.smart_rename_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.smart_rename_button.setText(QCoreApplication.translate("Form", u"Smart Rename", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Rename Selections in bulk:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"To use Smart rename, put '#' chars where the numbering is preferred.  Number of '#'s determines the number of zeroes as padding.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.naming_tab), QCoreApplication.translate("Form", u"RENAME", None))
        self.label.setText(QCoreApplication.translate("Form", u"Matt Riche 2024  (MIT lic.)", None))
        self.exit_button.setText(QCoreApplication.translate("Form", u"X", None))
    # retranslateUi

