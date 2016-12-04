# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MasterFlo\Desktop\Server.ui'
#
# Created: Fri Dec  2 15:54:50 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 360)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.clientlist = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clientlist.sizePolicy().hasHeightForWidth())
        self.clientlist.setSizePolicy(sizePolicy)
        self.clientlist.setObjectName("clientlist")
        self.verticalLayout.addWidget(self.clientlist)
        self.outputClients = QtGui.QTextEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputClients.sizePolicy().hasHeightForWidth())
        self.outputClients.setSizePolicy(sizePolicy)
        self.outputClients.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.outputClients.setReadOnly(True)
        self.outputClients.setCursorWidth(1)
        self.outputClients.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.outputClients.setObjectName("outputClients")
        self.verticalLayout.addWidget(self.outputClients)
        self.chat = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy)
        self.chat.setObjectName("chat")
        self.verticalLayout.addWidget(self.chat)
        self.outputText = QtGui.QTextEdit(Form)
        self.outputText.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.outputText.setReadOnly(True)
        self.outputText.setObjectName("outputText")
        self.verticalLayout.addWidget(self.outputText)
        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.clientlist.setText(QtGui.QApplication.translate("Form", "Connected Clients:", None, QtGui.QApplication.UnicodeUTF8))
        self.chat.setText(QtGui.QApplication.translate("Form", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

