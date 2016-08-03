import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from JLAF import Ui_myfirstgui

class MyFirstGuiProgram(Ui_myfirstgui):
	
	def __init__(self, dialog):
		Ui_myfirstgui.__init__(self)
		self.setupUi(dialog)
	
		self.fname = ""
		self.directory = ""

		self.actionOpen_File.triggered.connect(self.showOpenFile)
		self.commandLinkButton.clicked.connect(self.analyzeLogs)

	def showOpenFile(self):

		self.fname = QFileDialog.getOpenFileName(dialog, 'Open file')
		self.label_3.setText(str(self.fname[0]))
		
	def analyzeLogs(self):
		self.listWidget.clear()
		f = open(self.fname[0],'r')
		word_to_check = self.getlist()
		for line in f:
			if any(word in line for word in word_to_check):
				self.listWidget.addItem(line)


	def getlist(self):
		words_to_check = []
		if self.checkBox_3.isChecked():
			words_to_check.append("Re-indexing started")
			words_to_check.append("Re-indexing finished")
		if self.checkBox.isChecked():
			words_to_check.append("JIRA-Bootstrap INFO      [c.a.jira.startup.JiraStartupLogger]")
			words_to_check.append("Stopped JIRA monitoring")
		if self.checkBox_2.isChecked():
			words_to_check.append(str(self.lineEdit.text()))

		return words_to_check

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QMainWindow()
 
	prog = MyFirstGuiProgram(dialog)
 
	dialog.show()
	sys.exit(app.exec_())

#if __name__ == '__main__':
#	app = QtWidgets.QApplication(sys.argv)
#	MainWindow = QtWidgets.QMainWindow()
#
#	prog = MyFirstGuiProgram(MainWindow)
#
#	MainWindow.show()
#	sys.exit(app.exec_())