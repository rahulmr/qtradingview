# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(639, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/base/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks|QtWidgets.QMainWindow.ForceTabbedDocks)
        MainWindow.setProperty("currentExchange", "")
        MainWindow.setProperty("currentMarket", "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.webview = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webview.setObjectName("webview")
        self.horizontalLayout.addWidget(self.webview)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionMarkets = QtWidgets.QAction(MainWindow)
        self.actionMarkets.setCheckable(True)
        self.actionMarkets.setChecked(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/actions/actions/markets.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarkets.setIcon(icon1)
        self.actionMarkets.setObjectName("actionMarkets")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/actions/actions/salir.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSalir.setIcon(icon2)
        self.actionSalir.setObjectName("actionSalir")
        self.actionPantalla_completa = QtWidgets.QAction(MainWindow)
        self.actionPantalla_completa.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/actions/actions/screen.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPantalla_completa.setIcon(icon3)
        self.actionPantalla_completa.setObjectName("actionPantalla_completa")
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setCheckable(True)
        self.actionInfo.setObjectName("actionInfo")
        self.actionDebug = QtWidgets.QAction(MainWindow)
        self.actionDebug.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/actions/actions/debug.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDebug.setIcon(icon4)
        self.actionDebug.setObjectName("actionDebug")
        self.actionAlarms = QtWidgets.QAction(MainWindow)
        self.actionAlarms.setCheckable(True)
        self.actionAlarms.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/actions/actions/alarms.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlarms.setIcon(icon5)
        self.actionAlarms.setObjectName("actionAlarms")
        self.actionConfigurar = QtWidgets.QAction(MainWindow)
        self.actionConfigurar.setObjectName("actionConfigurar")
        self.toolBar.addAction(self.actionMarkets)
        self.toolBar.addAction(self.actionAlarms)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPantalla_completa)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionConfigurar)
        self.toolBar.addAction(self.actionDebug)
        self.toolBar.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)
        self.actionSalir.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QTradingview"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "Barra de herramientas"))
        self.actionMarkets.setText(_translate("MainWindow", "Mercados"))
        self.actionMarkets.setToolTip(_translate("MainWindow", "Mercados"))
        self.actionMarkets.setShortcut(_translate("MainWindow", "F1"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionPantalla_completa.setText(_translate("MainWindow", "Pantalla completa"))
        self.actionPantalla_completa.setShortcut(_translate("MainWindow", "F11"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionDebug.setText(_translate("MainWindow", "Depurar"))
        self.actionDebug.setToolTip(_translate("MainWindow", "Depurar"))
        self.actionDebug.setShortcut(_translate("MainWindow", "F10"))
        self.actionAlarms.setText(_translate("MainWindow", "Alarmas"))
        self.actionAlarms.setToolTip(_translate("MainWindow", "Alarmas"))
        self.actionAlarms.setShortcut(_translate("MainWindow", "F2"))
        self.actionConfigurar.setText(_translate("MainWindow", "Configurar"))
from PyQt5 import QtWebEngineWidgets
import iconos_rc