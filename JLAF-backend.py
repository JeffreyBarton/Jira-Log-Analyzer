import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from JLAF import Ui_myfirstgui

class MyFirstGuiProgram(Ui_myfirstgui):
	def __init__(self, dialog):
		Ui_myfirstgui.__init__(self)
		self.setupUi(dialog)
		self.actionOpen_File.triggered.connect(self.showOpenFile)

	def showOpenFile(self):
		fname = QFileDialog.getOpenFileName(dialog, 'Open file', '/home')
		self.label_3.setText(str(fname[0]))
		
	

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