#!/usr/bin/python
# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QObject, pyqtSignal

class SearchUtilities(QObject):
	"""
	用于将搜索放入子线程
	"""

	# ---<初始化>--------------
	def __init__(self, GUI):
		"""
		:param GUI:从父线程传递来的GUI
		"""
		super(SearchUtilities, self).__init__()
		self.ui = GUI

	# ---<信号>-----------------
	signal_start_search = pyqtSignal()  # 开始搜索的信号，连接此类中的search函数
	signal_start_loading_result = pyqtSignal(dict, int)  # 开始加载搜索结果的信号，连接

	# ---<搜索>-----------------
	def search(self):
		from global_search.globalSearch import global_search
		# ---<准备搜索所用参数>---------------------------------
		folder_path = str(self.ui.lineEdit_folder_path.text())  # 搜索的目标文件夹
		search_content = str(self.ui.lineEdit_search_content.text())  # 搜索的目标字符串
		browse_line = int(self.ui.spinBox_browse_line.text())  # 显示结果时，可以预览的匹配行上下文行数
		extend_name = str(self.ui.comboBox_extend_name.currentText())  # 搜索文件的拓展名限制
		# ---<开始搜索>---------------------------------------------------------------
		self.ui.statusbar.showMessage('Searching in: ' + self.ui.lineEdit_folder_path.text())
		matches = global_search(folder_path, search_content, browse_line, extend_name)
		# ---<准备加载结果所用参数>-----------------------------
		dic_file_lines = {}  # key = string,匹配的文件路径， value = list,匹配行及上下文
		cases_num = len(matches)  # 搜索结果总数
		# ---<将搜索结果以文件为单位合并>----------------------------------------
		for m in matches:
			if dic_file_lines.get(m.file) is None:
				dic_file_lines[m.file] = [self.concat_line_number_content(m)]
			else:
				dic_file_lines[m.file].append(self.concat_line_number_content(m))
		self.signal_start_loading_result.emit(dic_file_lines, cases_num)

	# ---<连接行数与行内容>-----------------------
	def concat_line_number_content(self, match):
		"""
		:param match: collections.namedtuple("search_result", "file(文件路径）, line（匹配行数）, text（匹配行及上下文）")
		:return: 列表，包含匹配行及其上下文
		"""
		line_num = match.line - int(self.ui.spinBox_browse_line.text())
		lines = match.text
		for i in range(len(lines)):
			lines[i] = QtCore.QString(str(line_num) + ': ' + lines[i])
			line_num += 1
		return lines