#!/usr/bin/python
# -*- coding:utf-8 -*-

from GUI.Main_Window import Ui_Main_Window
from PyQt4 import QtGui, QtCore
from global_search import globalSearch
import os

# ---<文件路径异常弹窗>---------------
FOLDER_PATH_ERROR_TITLE = 'Folder path error.'
FOLDER_PATH_ERROR_CONTENT = 'Folder path not exists.'

# ---<ccs文件路径异常弹窗>----------------------------
CCS_PROJECT_PATH_ERROR_TITLE = 'CCS path error.'
CCS_PROJECT_PATH_ERROR_CONTENT_1 = 'Folder path not exists.'
CCS_PROJECT_PATH_ERROR_CONTENT_2 = 'No ccs file included this csd file.'

class MainWindow(QtGui.QMainWindow, Ui_Main_Window):
	'''
	主窗口
	'''

	# ---<初始化>---------------------------
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_Main_Window()
		self.ui.setupUi(self)

		# ---<初始化 GUI>--------------------------
		self._lineEdit_file_formate = QtGui.QLineEdit()
		self.ui.statusbar.showMessage('Ready!')
		self._result = []
		self.search_thread = QtCore.QThread()
		self.search_thread.start()

		# ---<信号与槽函数连接>---------------------------------------------------------------
		self.ui.comboBox_extend_name.currentIndexChanged.connect(self.enable_ccs_file_select)
		self.ui.button_select_folder.clicked.connect(self.folder_browser)
		self.ui.treeWidget_search_result.itemClicked.connect(self.itemClicked_print_item)
		self.ui.treeWidget_search_result.itemDoubleClicked.connect(self.itemDoubleClicked_open_project_file)
		self.ui.button_search.clicked.connect(self.multithreading_global_search)
		self.ui.lineEdit_folder_path.textChanged.connect(self.textChanged_checking_path)
		self.ui.button_select_ccs_file_folder.clicked.connect(self.select_ccs_file_folder)

	# ---<选择目标文件夹>-------------
	def folder_browser(self):
		folder_choose = QtGui.QFileDialog.getExistingDirectory(self, 'Select Folder', os.getcwd())

		# ---<检查路径异常>------------
		if folder_choose == '':
			print 'canceled'
			return
		if not os.path.exists(folder_choose):
			print 'Error: Selected folder not exists.'
			return

		# --<设置当前选定路径到GUI>------------------------
		print 'selected folder:', folder_choose
		self.ui.lineEdit_folder_path.setText(folder_choose)

		# ---<设置ccs文件默认路径>-------------------------
		if self.ui.widget_ccs_file_select.isEnabled():
			ccs_file_path = os.path.dirname(str(folder_choose))
			self.ui.lineEdit_ccs_file_folder.setText(QtCore.QString(ccs_file_path))
		else:
			self.ui.lineEdit_ccs_file_folder.clear()

	# ---<选择ccs项目文件夹>-------------
	def select_ccs_file_folder(self):
		folder_choose = QtGui.QFileDialog.getExistingDirectory(self, 'Select Folder', os.getcwd())

		# ---<检查路径异常>------------
		if folder_choose == '':
			print 'canceled'
			return
		if not os.path.exists(folder_choose):
			print 'Error: Selected folder not exists.'
			return

		# --<设置当前选定路径到GUI>------------------------
		print 'selected folder:', folder_choose
		self.ui.lineEdit_ccs_file_folder.setText(folder_choose)

	# ---<检查更改后的路径是否合法>---------------
	def textChanged_checking_path(self):
		file_path = str(self.ui.lineEdit_folder_path.text())
		if(os.path.isdir(file_path)):
			return
		else:
			QtGui.QMessageBox.information(self, QtCore.QString(FOLDER_PATH_ERROR_TITLE), QtCore.QString(FOLDER_PATH_ERROR_CONTENT))
			return

	# ---<ccs 文件选择框激活设定>------------------
	# 根据comboBox的内容，选择性的激活ccs文件选择框
	# 当comboBox内容仅为*.csd时，激活ccs文件选择
	def enable_ccs_file_select(self):
		if self.ui.comboBox_extend_name.currentText() == 'CSD Files (*.csd)':
			self.ui.widget_ccs_file_select.setEnabled(True)
		else:
			self.ui.widget_ccs_file_select.setEnabled(False)

	# ---<创建子进程进行搜索>----------------
	def multithreading_global_search(self):
		from search_utilities.Search_Utilities import SearchUtilities
		self.search_utilities = SearchUtilities(self.ui)
		self.search_utilities.moveToThread(self.search_thread)
		self.search_utilities.signal_start_search.connect(self.search_utilities.search)
		self.search_utilities.signal_start_loading_result.connect(self.load_search_result)
		self.search_utilities.signal_start_search.emit()
		self.ui.comboBox_extend_name.currentText()

	# ---<槽函数，加载搜索结果>------------------------------------------
	# 由子线程signal_start_loading_result信号激活
	def load_search_result_t(self, dic_file_lines, cases_num):
		"""
		:param dic_file_lines: dictionary, key = file path, value = lines matched
		:param cases_num: int, the number of cases matched
		:return: void
		"""
		from PyQt4.QtCore import QMutexLocker, QMutex

		mutex = QMutex()
		lock = QMutexLocker(mutex)

		self.ui.statusbar.showMessage('Start loading results.')
		self.ui.treeWidget_search_result.clear()
		self.load_search_result(dic_file_lines, cases_num)

	# ---<槽函数，加载搜索结果>------------------------------------------
	# 由子线程signal_start_loading_result信号激活
	def load_search_result(self, dic_file_lines, cases_num):
		"""
		:param dic_file_lines: dictionary, key = file path, value = lines matched
		:param cases_num: int, the number of cases matched
		:return: void
		"""
		self.ui.treeWidget_search_result.clear()
		if cases_num == 0:
			self.ui.statusbar.showMessage('Completed. {} cases founded.'.format(cases_num))
			return
		node_list = []
		self.ui.progress_bar.setMaximum(cases_num)
		self.ui.progress_bar.setMinimum(0)
		cur_case = 0
		for k in dic_file_lines.iterkeys():
			node_file = QtGui.QTreeWidgetItem(self.ui.treeWidget_search_result)
			node_file.setText(0, QtCore.QString(k))
			# self.ui.treeWidget_search_result.addTopLevelItem(node_file)
			# ---<若该文件下只有一个匹配结果，匹配行直接作为子节点加入到路径节点下>---------------
			if len(dic_file_lines[k]) == 1:
				for line in dic_file_lines[k][0]:
					node_line = QtGui.QTreeWidgetItem(node_file)
					label = QtGui.QLabel(QtCore.QString.fromUtf8(line))
					label.setWordWrap(True)
					label.setTextFormat(QtCore.Qt.RichText)
					self.ui.treeWidget_search_result.setItemWidget(node_line, 0, label)
				print cur_case
				cur_case += 1
				self.ui.progress_bar.setValue(cur_case)
				self.ui.statusbar.showMessage('Loading {0}/{1}'.format(str(cur_case), str(cases_num)))
			# ---<若文件中有多于一个匹配结果，匹配行作为子节点加入到case节点下，case节点再作为子节点挂路径节点下>-----
			else:
				case_num = 1
				for case in dic_file_lines[k]:
					node_case = QtGui.QTreeWidgetItem(node_file)
					node_case.setText(0, QtCore.QString('Case: {}'.format(case_num)))
					for line in case:
						node_line = QtGui.QTreeWidgetItem(node_case)
						label = QtGui.QLabel(QtCore.QString.fromUtf8(line))
						label.setWordWrap(True)
						label.setTextFormat(QtCore.Qt.RichText)
						self.ui.treeWidget_search_result.setItemWidget(node_line, 0, label)
					print cur_case
					case_num += 1
					cur_case += 1
					self.ui.progress_bar.setValue(cur_case)
					self.ui.statusbar.showMessage('Loading {0}/{1}'.format(str(cur_case), str(cases_num)))
			node_list.append(node_file)
		# ---<更新GUI>-----------------------------------------------
		self.ui.treeWidget_search_result.addTopLevelItems(node_list)
		self.ui.statusbar.showMessage('Completed. {} cases founded.'.format(cases_num))

	# ---<将行号与该行内容连接到一起>--------------
	def concat_line_number_content(self, match):
		"""
		:param match: collections.namedtuple("search_result", "file(文件路径）, line（匹配行数）, text（匹配行及上下文）")
		:return: list of string
		"""
		line_num = match.line - int(self.ui.spinBox_browse_line.text())
		lines = match.text
		for i in range(len(lines)):
			lines[i] = QtCore.QString(str(line_num) + ': ' + lines[i])
			line_num += 1
		return lines

	# ---<测试用函数>-------------------------------------
	# ---<点击treeWidget_search_result行时打印其内容>------
	def itemClicked_print_item(self, item):
		"""
		:param item: treeWidgetItem
		:return: void
		"""
		print item.text(0)
		try:
			label = self.ui.treeWidget_search_result.itemWidget(item,0)
			print label.text()
		except:
			return

	# ---<双击打开文件>------------------
	def itemDoubleClicked_open_project_file(self, item):
		"""
		:param item: treeWidgetItem
		:return: void
		"""
		import os
		import thread
		selected_content = str(item.text(0))
		# ---<异常处理>------------------------------
		if not os.path.isfile(selected_content):
			return
		# ---<非csd文件搜索逻辑>--------------------------------------------------------
		if not self.ui.comboBox_extend_name.currentText() == 'CSD Files (*.csd)':
			self.ui.statusbar.showMessage('Opening file: ' + selected_content)
			pos = selected_content.rfind('\\')
			selected_content = selected_content[:pos+1] + '\"' + selected_content[pos+1:] + '\"'
			thread.start_new_thread(os.system, (selected_content,))
			return
		# ---<csd文件处理>----------------------------------------------
		# ---<获取csd文件名及ccs文件路径>-----------------------------------------------
		self.ui.statusbar.showMessage('Opening file: ' + selected_content)
		pos = selected_content.rfind('\\')
		csd_file_name = selected_content[pos+1:]
		ccs_file_path = str(self.ui.lineEdit_ccs_file_folder.text())
		# ---<异常处理，ccs项目路径错误>-------------------------------------------------------
		if not os.path.isdir(ccs_file_path):
			QtGui.QMessageBox.information(self, QtCore.QString(CCS_PROJECT_PATH_ERROR_TITLE),
			                              QtCore.QString(CCS_PROJECT_PATH_ERROR_CONTENT_1))
			return
		project_name, have_projcet = globalSearch.get_project_name(csd_file_name, ccs_file_path)
		if not have_projcet:
			QtGui.QMessageBox.information(self, QtCore.QString(CCS_PROJECT_PATH_ERROR_TITLE),
			                              QtCore.QString(CCS_PROJECT_PATH_ERROR_CONTENT_2))
			return
		thread.start_new_thread(globalSearch.open_project, (project_name, ccs_file_path))

import sys
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	myapp = MainWindow()
	myapp.show()
	sys.exit(app.exec_())