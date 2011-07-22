# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Tue Jul 19 22:09:29 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 632)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mudOutput = QtGui.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier,Nimbus Mono,monospace"))
        self.mudOutput.setFont(font)
        self.mudOutput.setStyleSheet(_fromUtf8("background-color: #000;\n"
"color: #ccc;\n"
"font-family: Courier,\"Nimbus Mono\",monospace; "))
        self.mudOutput.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.mudOutput.setObjectName(_fromUtf8("mudOutput"))
        self.verticalLayout.addWidget(self.mudOutput)
        self.mudInput = QtGui.QLineEdit(self.centralwidget)
        self.mudInput.setStyleSheet(_fromUtf8("background-color: #000;\n"
"color: #ccc;\n"
"font-family: Courier,\"Nimbus Mono\",monospace; "))
        self.mudInput.setObjectName(_fromUtf8("mudInput"))
        self.verticalLayout.addWidget(self.mudInput)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuV_iew = QtGui.QMenu(self.menubar)
        self.menuV_iew.setObjectName(_fromUtf8("menuV_iew"))
        self.menuTheme = QtGui.QMenu(self.menuV_iew)
        self.menuTheme.setObjectName(_fromUtf8("menuTheme"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Python_Console = QtGui.QDockWidget(MainWindow)
        self.Python_Console.setObjectName(_fromUtf8("Python_Console"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents_2)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.consoleInput = QtGui.QLineEdit(self.dockWidgetContents_2)
        self.consoleInput.setStyleSheet(_fromUtf8("background-color: #000;\n"
"color: #ccc;\n"
"font-family: Courier,\"Nimbus Mono\",monospace; "))
        self.consoleInput.setObjectName(_fromUtf8("consoleInput"))
        self.gridLayout.addWidget(self.consoleInput, 0, 1, 1, 1)
        self.consoleOutput = QtGui.QTextBrowser(self.dockWidgetContents_2)
        self.consoleOutput.setStyleSheet(_fromUtf8("background-color: #000;\n"
"color: #ccc;\n"
"font-family: Courier,\"Nimbus Mono\",monospace; "))
        self.consoleOutput.setObjectName(_fromUtf8("consoleOutput"))
        self.gridLayout.addWidget(self.consoleOutput, 1, 0, 1, 2)
        self.Python_Console.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.Python_Console)
        self.actionLight = QtGui.QAction(MainWindow)
        self.actionLight.setObjectName(_fromUtf8("actionLight"))
        self.actionDark = QtGui.QAction(MainWindow)
        self.actionDark.setObjectName(_fromUtf8("actionDark"))
        self.menuTheme.addAction(self.actionLight)
        self.menuTheme.addAction(self.actionDark)
        self.menuV_iew.addAction(self.menuTheme.menuAction())
        self.menubar.addAction(self.menuV_iew.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.mudInput, self.consoleInput)
        MainWindow.setTabOrder(self.consoleInput, self.mudOutput)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.mudInput.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Enter Mud commands here", None, QtGui.QApplication.UnicodeUTF8))
        self.menuV_iew.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTheme.setTitle(QtGui.QApplication.translate("MainWindow", "Theme", None, QtGui.QApplication.UnicodeUTF8))
        self.Python_Console.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Python Console", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", ">>>", None, QtGui.QApplication.UnicodeUTF8))
        self.consoleInput.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Enter Python commands here", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLight.setText(QtGui.QApplication.translate("MainWindow", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDark.setText(QtGui.QApplication.translate("MainWindow", "Dark", None, QtGui.QApplication.UnicodeUTF8))

