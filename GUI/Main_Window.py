# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Main_Window(object):
    def setupUi(self, Main_Window):
        import os, sys
        Main_Window.setObjectName(_fromUtf8("Main_Window"))
        Main_Window.resize(801, 600)
        try:
            base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        except Exception:
            base_path = os.path.abspath(".")
        icon_path = os.path.join(base_path, "pixil-frame-0.png")
        print base_path
        print icon_path
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(icon_path)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Main_Window.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(Main_Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(3, 1, 3, 1)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.widget_search_setting = QtGui.QWidget(self.centralwidget)
        self.widget_search_setting.setObjectName(_fromUtf8("widget_search_setting"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget_search_setting)
        self.verticalLayout.setMargin(1)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_file_select = QtGui.QWidget(self.widget_search_setting)
        self.widget_file_select.setObjectName(_fromUtf8("widget_file_select"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_file_select)
        self.horizontalLayout.setMargin(1)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_select_folder = QtGui.QLabel(self.widget_file_select)
        self.label_select_folder.setObjectName(_fromUtf8("label_select_folder"))
        self.horizontalLayout.addWidget(self.label_select_folder)
        self.lineEdit_folder_path = QtGui.QLineEdit(self.widget_file_select)
        self.lineEdit_folder_path.setObjectName(_fromUtf8("lineEdit_folder_path"))
        self.horizontalLayout.addWidget(self.lineEdit_folder_path)
        self.label_search_file_format = QtGui.QLabel(self.widget_file_select)
        self.label_search_file_format.setObjectName(_fromUtf8("label_search_file_format"))
        self.horizontalLayout.addWidget(self.label_search_file_format)
        self.comboBox_extend_name = QtGui.QComboBox(self.widget_file_select)
        self.comboBox_extend_name.setMinimumSize(QtCore.QSize(130, 0))
        self.comboBox_extend_name.setEditable(True)
        self.comboBox_extend_name.setObjectName(_fromUtf8("comboBox_extend_name"))
        self.comboBox_extend_name.addItem(_fromUtf8(""))
        self.comboBox_extend_name.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_extend_name)
        self.button_select_folder = QtGui.QPushButton(self.widget_file_select)
        self.button_select_folder.setObjectName(_fromUtf8("button_select_folder"))
        self.horizontalLayout.addWidget(self.button_select_folder)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_file_select)
        self.widget_ccs_file_select = QtGui.QWidget(self.widget_search_setting)
        self.widget_ccs_file_select.setEnabled(True)
        self.widget_ccs_file_select.setObjectName(_fromUtf8("widget_ccs_file_select"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_ccs_file_select)
        self.horizontalLayout_3.setMargin(1)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_ccs_file_folder = QtGui.QLabel(self.widget_ccs_file_select)
        self.label_ccs_file_folder.setObjectName(_fromUtf8("label_ccs_file_folder"))
        self.horizontalLayout_3.addWidget(self.label_ccs_file_folder)
        self.lineEdit_ccs_file_folder = QtGui.QLineEdit(self.widget_ccs_file_select)
        self.lineEdit_ccs_file_folder.setObjectName(_fromUtf8("lineEdit_ccs_file_folder"))
        self.horizontalLayout_3.addWidget(self.lineEdit_ccs_file_folder)
        self.button_select_ccs_file_folder = QtGui.QPushButton(self.widget_ccs_file_select)
        self.button_select_ccs_file_folder.setObjectName(_fromUtf8("button_select_ccs_file_folder"))
        self.horizontalLayout_3.addWidget(self.button_select_ccs_file_folder)
        self.verticalLayout.addWidget(self.widget_ccs_file_select)
        self.widget_target_setting = QtGui.QWidget(self.widget_search_setting)
        self.widget_target_setting.setObjectName(_fromUtf8("widget_target_setting"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_target_setting)
        self.horizontalLayout_2.setMargin(1)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_search_content = QtGui.QLabel(self.widget_target_setting)
        self.label_search_content.setObjectName(_fromUtf8("label_search_content"))
        self.horizontalLayout_2.addWidget(self.label_search_content)
        self.lineEdit_search_content = QtGui.QLineEdit(self.widget_target_setting)
        self.lineEdit_search_content.setObjectName(_fromUtf8("lineEdit_search_content"))
        self.horizontalLayout_2.addWidget(self.lineEdit_search_content)
        self.label_browse_line = QtGui.QLabel(self.widget_target_setting)
        self.label_browse_line.setObjectName(_fromUtf8("label_browse_line"))
        self.horizontalLayout_2.addWidget(self.label_browse_line)
        self.spinBox_browse_line = QtGui.QSpinBox(self.widget_target_setting)
        self.spinBox_browse_line.setProperty("value", 2)
        self.spinBox_browse_line.setObjectName(_fromUtf8("spinBox_browse_line"))
        self.horizontalLayout_2.addWidget(self.spinBox_browse_line)
        self.button_search = QtGui.QPushButton(self.widget_target_setting)
        self.button_search.setObjectName(_fromUtf8("button_search"))
        self.horizontalLayout_2.addWidget(self.button_search)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget_target_setting)
        self.verticalLayout_3.addWidget(self.widget_search_setting)
        self.widget_search_result = QtGui.QWidget(self.centralwidget)
        self.widget_search_result.setObjectName(_fromUtf8("widget_search_result"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_search_result)
        self.verticalLayout_2.setMargin(1)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_search_result = QtGui.QLabel(self.widget_search_result)
        self.label_search_result.setObjectName(_fromUtf8("label_search_result"))
        self.verticalLayout_2.addWidget(self.label_search_result)
        self.treeWidget_search_result = QtGui.QTreeWidget(self.widget_search_result)
        self.treeWidget_search_result.setStyleSheet(_fromUtf8(""))
        self.treeWidget_search_result.setUniformRowHeights(True)
        self.treeWidget_search_result.setObjectName(_fromUtf8("treeWidget_search_result"))
        self.treeWidget_search_result.headerItem().setText(0, _fromUtf8("1"))
        self.treeWidget_search_result.header().setVisible(False)
        self.verticalLayout_2.addWidget(self.treeWidget_search_result)
        self.progress_bar = QtGui.QProgressBar(self.widget_search_result)
        self.progress_bar.setMaximum(1)
        self.progress_bar.setProperty("value", 1)
        self.progress_bar.setObjectName(_fromUtf8("progress_bar"))
        self.verticalLayout_2.addWidget(self.progress_bar)
        self.verticalLayout_3.addWidget(self.widget_search_result)
        self.verticalLayout_3.setStretch(1, 1)
        Main_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Main_Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)

    def retranslateUi(self, Main_Window):
        Main_Window.setWindowTitle(_translate("Main_Window", "global_reference_search_v_1_0_by_Yves", None))
        self.label_select_folder.setText(_translate("Main_Window", "Target Folder", None))
        self.label_search_file_format.setText(_translate("Main_Window", "Filter", None))
        self.comboBox_extend_name.setItemText(0, _translate("Main_Window", "CSD Files (*.csd)", None))
        self.comboBox_extend_name.setItemText(1, _translate("Main_Window", "All Files (*.*)", None))
        self.button_select_folder.setText(_translate("Main_Window", "Browse", None))
        self.label_ccs_file_folder.setText(_translate("Main_Window", "CCS File Folder:", None))
        self.button_select_ccs_file_folder.setText(_translate("Main_Window", "Browse", None))
        self.label_search_content.setText(_translate("Main_Window", "Search Text:", None))
        self.label_browse_line.setText(_translate("Main_Window", "Content Preview Lines:", None))
        self.button_search.setText(_translate("Main_Window", "Search", None))
        self.label_search_result.setText(_translate("Main_Window", "Search Result:", None))

