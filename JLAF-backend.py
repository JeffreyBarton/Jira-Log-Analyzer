import sys, pathlib
from os import walk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from JLAF import Ui_MainWindow

class MyFirstGuiProgram(Ui_MainWindow):
	
	def __init__(self, dialog):
		Ui_MainWindow.__init__(self)
		self.setupUi(dialog)
	
		self.fname = ""
		self.activeFile = ""
		self.directory = ""

		self.fileWatcher = QtCore.QFileSystemWatcher()

		self.actionOpen_File.triggered.connect(self.showOpenFile)
		self.commandLinkButton.clicked.connect(self.analyzeLogs)
		self.listWidget_2.itemClicked.connect(self.changeActiveFile)
		self.fileWatcher.fileChanged.connect(self.fileChanged)
		
	def fileChanged(self):
		self.label_3.setText(self.activeFile + " CHANGED")

	def showOpenFile(self):
		self.fname = QFileDialog.getOpenFileName(dialog, 'Open file')

		self.activeFile = str(self.fname[0])
		self.fileWatcher.addPath(self.activeFile)
		
		self.label_3.setText(self.activeFile)

		self.listWidget_2.clear()
		f = []
		for (dirpath, dirnames, filenames) in walk(str(self.getDir(self.activeFile))):
			f.extend(filenames)
			self.listWidget_2.addItems(filenames)
			break

	def changeActiveFile(self):
		#print(str(self.directory) + "\\" + str(self.listWidget_2.currentItem().text()))
		self.fileWatcher.removePath(self.activeFile)

		self.activeFile = str(str(self.directory) + "\\" + str(self.listWidget_2.currentItem().text()))

		self.fileWatcher.addPath(self.activeFile)

		self.label_3.setText(self.activeFile)

	def analyzeLogs(self):
		self.listWidget.clear()
		try:
			f = open(self.activeFile,'r')
			word_to_check = self.getlist()
			for line in f:
				if any(word in line for word in word_to_check):
					self.listWidget.addItem(line)
		except:
			 self.label_3.setText(str("No file selected"))

	def getDir(self,path_name):
		existGDBPath = pathlib.Path(path_name)
		wkspFldr = existGDBPath.parent
		self.directory = wkspFldr
		return wkspFldr

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