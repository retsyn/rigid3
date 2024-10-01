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
        Form.resize(470, 405)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 30, 381, 361))
        self.visuals_tab = QWidget()
        self.visuals_tab.setObjectName(u"visuals_tab")
        self.verticalLayoutWidget = QWidget(self.visuals_tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 211, 201))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.load_data_button = QPushButton(self.verticalLayoutWidget)
        self.load_data_button.setObjectName(u"load_data_button")

        self.verticalLayout.addWidget(self.load_data_button)

        self.save_data_button = QPushButton(self.verticalLayoutWidget)
        self.save_data_button.setObjectName(u"save_data_button")

        self.verticalLayout.addWidget(self.save_data_button)

        self.copy_data_button = QPushButton(self.verticalLayoutWidget)
        self.copy_data_button.setObjectName(u"copy_data_button")

        self.verticalLayout.addWidget(self.copy_data_button)

        self.replace_sel_button = QPushButton(self.verticalLayoutWidget)
        self.replace_sel_button.setObjectName(u"replace_sel_button")

        self.verticalLayout.addWidget(self.replace_sel_button)

        self.build_button = QPushButton(self.verticalLayoutWidget)
        self.build_button.setObjectName(u"build_button")

        self.verticalLayout.addWidget(self.build_button)

        self.build_match_button = QPushButton(self.verticalLayoutWidget)
        self.build_match_button.setObjectName(u"build_match_button")

        self.verticalLayout.addWidget(self.build_match_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mirror_x_button = QPushButton(self.verticalLayoutWidget)
        self.mirror_x_button.setObjectName(u"mirror_x_button")

        self.horizontalLayout.addWidget(self.mirror_x_button)

        self.mirror_y_button = QPushButton(self.verticalLayoutWidget)
        self.mirror_y_button.setObjectName(u"mirror_y_button")

        self.horizontalLayout.addWidget(self.mirror_y_button)

        self.mirror_z_button = QPushButton(self.verticalLayoutWidget)
        self.mirror_z_button.setObjectName(u"mirror_z_button")

        self.horizontalLayout.addWidget(self.mirror_z_button)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.frame = QFrame(self.visuals_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(230, 10, 131, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 1, 101, 21))
        self.cur_data_label = QLabel(self.frame)
        self.cur_data_label.setObjectName(u"cur_data_label")
        self.cur_data_label.setGeometry(QRect(10, 20, 101, 41))
        self.horizontalSlider = QSlider(self.visuals_tab)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(230, 150, 81, 21))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.build_scale = QSpinBox(self.visuals_tab)
        self.build_scale.setObjectName(u"build_scale")
        self.build_scale.setGeometry(QRect(320, 150, 41, 21))
        self.label_3 = QLabel(self.visuals_tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 130, 81, 20))
        self.verticalLayoutWidget_2 = QWidget(self.visuals_tab)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 220, 355, 116))
        self.colourLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.colourLayout.setSpacing(3)
        self.colourLayout.setObjectName(u"colourLayout")
        self.colourLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.recolour_button = QPushButton(self.verticalLayoutWidget_2)
        self.recolour_button.setObjectName(u"recolour_button")

        self.verticalLayout_2.addWidget(self.recolour_button)

        self.thicken_button = QPushButton(self.verticalLayoutWidget_2)
        self.thicken_button.setObjectName(u"thicken_button")

        self.verticalLayout_2.addWidget(self.thicken_button)

        self.unthicken_button = QPushButton(self.verticalLayoutWidget_2)
        self.unthicken_button.setObjectName(u"unthicken_button")

        self.verticalLayout_2.addWidget(self.unthicken_button)

        self.pushButton_11 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_2.addWidget(self.pushButton_11)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_8 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: #fffeee000;")

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 2, 1, 1)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"background-color: #EEEFFF999")

        self.gridLayout_2.addWidget(self.pushButton_7, 2, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background-color: #FF5733;")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: #FFF999999")

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: #FFF000FFF;")

        self.gridLayout_2.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"background-color: #01ff16")

        self.gridLayout_2.addWidget(self.pushButton_6, 3, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"background-color: #555555FFF;")

        self.gridLayout_2.addWidget(self.pushButton_9, 1, 3, 1, 1)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"background-color: #999999FFF")

        self.gridLayout_2.addWidget(self.pushButton_10, 2, 3, 1, 1)

        self.pushButton_12 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"background-color: #464646;")

        self.gridLayout_2.addWidget(self.pushButton_12, 3, 3, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.colourLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.visuals_tab, "")
        self.build_tab = QWidget()
        self.build_tab.setObjectName(u"build_tab")
        self.verticalLayoutWidget_3 = QWidget(self.build_tab)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(9, 12, 271, 111))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fast_fk_button = QPushButton(self.verticalLayoutWidget_3)
        self.fast_fk_button.setObjectName(u"fast_fk_button")

        self.verticalLayout_3.addWidget(self.fast_fk_button)

        self.fast_fk_button_2 = QPushButton(self.verticalLayoutWidget_3)
        self.fast_fk_button_2.setObjectName(u"fast_fk_button_2")

        self.verticalLayout_3.addWidget(self.fast_fk_button_2)

        self.ribbon_joints_button = QPushButton(self.verticalLayoutWidget_3)
        self.ribbon_joints_button.setObjectName(u"ribbon_joints_button")

        self.verticalLayout_3.addWidget(self.ribbon_joints_button)

        self.tabWidget.addTab(self.build_tab, "")
        self.debug = QWidget()
        self.debug.setObjectName(u"debug")
        self.gridLayoutWidget = QWidget(self.debug)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 461, 221))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.deleteBindPose_button = QPushButton(self.gridLayoutWidget)
        self.deleteBindPose_button.setObjectName(u"deleteBindPose_button")

        self.gridLayout.addWidget(self.deleteBindPose_button, 1, 0, 1, 1)

        self.fixShapeName_button = QPushButton(self.gridLayoutWidget)
        self.fixShapeName_button.setObjectName(u"fixShapeName_button")

        self.gridLayout.addWidget(self.fixShapeName_button, 0, 0, 1, 1)

        self.fixShapeAll_radio = QRadioButton(self.gridLayoutWidget)
        self.fixShapeAll_radio.setObjectName(u"fixShapeAll_radio")

        self.gridLayout.addWidget(self.fixShapeAll_radio, 0, 1, 1, 1)

        self.label_4 = QLabel(self.debug)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 561, 20))
        self.tabWidget.addTab(self.debug, "")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 381, 16))

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
        self.recolour_button.setText(QCoreApplication.translate("Form", u"Recolour Selected", None))
        self.thicken_button.setText(QCoreApplication.translate("Form", u"Thickness to 5.0", None))
        self.unthicken_button.setText(QCoreApplication.translate("Form", u"Thickness to default", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"Copy Colour", None))
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_12.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.visuals_tab), QCoreApplication.translate("Form", u"Controllers", None))
        self.fast_fk_button.setText(QCoreApplication.translate("Form", u"Fast FK", None))
        self.fast_fk_button_2.setText(QCoreApplication.translate("Form", u"Fast IK", None))
        self.ribbon_joints_button.setText(QCoreApplication.translate("Form", u"Ribbon Joints", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.build_tab), QCoreApplication.translate("Form", u"Build", None))
        self.deleteBindPose_button.setText(QCoreApplication.translate("Form", u"Delete Bind Poses", None))
        self.fixShapeName_button.setText(QCoreApplication.translate("Form", u"Correct ShapeNode Name", None))
        self.fixShapeAll_radio.setText(QCoreApplication.translate("Form", u"On Entire Scene", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Debugging Tools to spot fix rig issues.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.debug), QCoreApplication.translate("Form", u"Debug", None))
        self.label.setText(QCoreApplication.translate("Form", u"Matt Riche 2023-07-11  (MIT lic.)", None))
    # retranslateUi

