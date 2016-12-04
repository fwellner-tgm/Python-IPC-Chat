# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MasterFlo\Desktop\Client.ui'
#
# Created: Fri Dec  2 15:54:15 2016
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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.message = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setObjectName("message")
        self.horizontalLayout.addWidget(self.message)
        self.input = QtGui.QLineEdit(Form)
        self.input.setObjectName("input")
        self.horizontalLayout.addWidget(self.input)
        self.senden = QtGui.QPushButton(Form)
        self.senden.setObjectName("senden")
        self.horizontalLayout.addWidget(self.senden)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 25, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chat = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat.sizePolicy().hasHeightForWidth())
        self.chat.setSizePolicy(sizePolicy)
        self.chat.setObjectName("chat")
        self.verticalLayout.addWidget(self.chat)
        self.output = QtGui.QTextEdit(Form)
        self.output.setProperty("cursor", QtCore.Qt.ArrowCursor)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setText(QtGui.QApplication.translate("Form", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.senden.setText(QtGui.QApplication.translate("Form", "Senden", None, QtGui.QApplication.UnicodeUTF8))
        self.chat.setText(QtGui.QApplication.translate("Form", "Chat:", None, QtGui.QApplication.UnicodeUTF8))

