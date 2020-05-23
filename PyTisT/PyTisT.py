# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyTisT.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class Window(QMainWindow):
   
   def __init__(self):
    super(Window, self).__init__()
    self.setGeometry(50,50,500,300)
    self.setWindowTitle("PyTisT")
    #self.setWindowIcon(QtGui.QIcon)

    saveFile = QAction('&Save File',self)
    saveFile.setShortcut('Ctrl+S')
    saveFile.setStatusTip('Save the file')
    saveFile.triggered.connect(self.save)

    openFile = QAction('&Open File',self)
    openFile.setShortcut('Ctrl+O')
    openFile.setStatusTip('Open the file')
    openFile.triggered.connect(self.open)

    chstyle = QAction('&Change Style',self)
    chstyle.setShortcut('Ctrl+1')
    chstyle.setStatusTip('Change style')
    #chstyle.triggered.connect(self.change_style)

    #chfont = QAction('&Change Font',self)
    #chfont.addMenu(chstyle)
    #chfont.setStatusTip('Font options')


    chtheme = QAction('&Change Theme',self)
    chtheme.setShortcut('Ctrl+3')
    chtheme.setStatusTip('Change theme')
    #chtheme.triggered.connect(self.change_theme)

    #Menus
    self.statusBar()

    mainMenu = self.menuBar()

    fileMenu = mainMenu.addMenu('&File')
    fileMenu.addAction(saveFile)
    fileMenu.addAction(openFile)

    prefMenu = mainMenu.addMenu("&Preferences")
    prefMenu.addAction(chstyle)
    prefMenu.addAction(chtheme)

    subPrefMenu = prefMenu.addMenu("&Change Font")

    editMenu = mainMenu.addMenu("&Edit")
    #editMenu.addAction()
    #editMenu.addAction()

    #typing area
    self.textEdit  = QTextEdit()
    self.setCentralWidget(self.textEdit)

    #default style
    QApplication.setStyle('Fusion')
    self.show()


   def save(self):
    text = self.textEdit.toPlainText()
    name,dummy = QFileDialog.getSaveFileName(self,'Save File',
    options = QFileDialog.DontUseNativeDialog)
    file = open(name, 'w')
    file.write(text)
    file.close()

   def open(self):
    name,dummy = QFileDialog.getOpenFileName(self,'Open File',
    options = QFileDialog.DontUseNativeDialog)
    file = open(name, 'r')

    with file:
        text = file.read()
        self.textEdit.setText(text)


app = QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())
