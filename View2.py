import ServerView, ClientView
from pyside import QtCore, QtGui


class View2(QtGui.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.sview = ServerView.Ui_Form()
        self.sview.setupUi(self)

        self.cview = View()


    def writeChat(self):
        self.cview.senden



class View(QtGui.QWidget):
    def __init__(self):
        super().__init__(self)

        self.cview = ClientView.Ui_Form()
        self.cview.setupUi(self)

        self.sview = View2()



