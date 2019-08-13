#!/usr/bin/python
# -*- coding:utf-8 -*-

from PyQt4.QtCore import QThread, pyqtSignal

class SearchTread(QThread):

	signal_search_completed = pyqtSignal(list)

	def __init__(self, gui, parent=None):
		super(SearchTread,self).__init__(parent)
		self.ui = gui

	def run(self):
		from global_search.globalSearch import global_search
		from PyQt4.QtCore import QMutex
		# 公有变量读取到局部变量
		folder_path = str(self.ui.lineEdit_folder_path.text())
		search_content = str(self.ui.lineEdit_search_content.text())
		browse_line = int(self.ui.spinBox_browse_line.text())
		extend_name = str(self.ui.comboBox_extend_name)

		matches = global_search(folder_path, search_content, browse_line, extend_name)

		self.signal_search_completed.emit(matches)