# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dock_debug.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockDebug(object):
    def setupUi(self, DockDebug):
        DockDebug.setObjectName("DockDebug")
        DockDebug.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/actions/actions/debug.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DockDebug.setWindowIcon(icon)
        DockDebug.setAutoFillBackground(False)
        DockDebug.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        DockDebug.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        DockDebug.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.TopDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.edit_logger = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.edit_logger.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.edit_logger.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.edit_logger.setAcceptRichText(False)
        self.edit_logger.setObjectName("edit_logger")
        self.verticalLayout.addWidget(self.edit_logger)
        self.btn_clear = QtWidgets.QPushButton(self.dockWidgetContents)
        self.btn_clear.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.btn_clear.setAutoDefault(True)
        self.btn_clear.setDefault(True)
        self.btn_clear.setObjectName("btn_clear")
        self.verticalLayout.addWidget(self.btn_clear)
        DockDebug.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockDebug)
        self.btn_clear.released.connect(self.edit_logger.clear)
        QtCore.QMetaObject.connectSlotsByName(DockDebug)

    def retranslateUi(self, DockDebug):
        _translate = QtCore.QCoreApplication.translate
        DockDebug.setWindowTitle(_translate("DockDebug", "Debug"))
        self.btn_clear.setText(_translate("DockDebug", "Clear"))
import iconos_rc