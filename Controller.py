import ClientView, ServerView, sys, socket, threading
from PySide import QtGui, QtCore



class Connectthread(QtGui.QWidget, threading.Thread):
    def __init__(self, parent=None):
        super().__init__(parent)
        threading.Thread.__init__(self)

        self.view = ClientView.Ui_Form()
        self.view.setupUi(self)

        self.msg = ""
        self.buttonHandle()

        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Connectthread.view.senden.clicked.connect(lambda: print("Test"))


    def run(self):
        try:
            self.clientsocket.connect(("localhost", 50000))

            while True:
                #self.conn(, QtCore.SIGNAL("clicked()"), self.clientsocket.send("Funktioniert!!"))
                #self.controller.connect(self.controller.view.senden, QtCore.SIGNAL("clicked()"), lambda: self.clientsocket.send("Funktioniert!!".encode()))
                self.clientsocket.send(self.buttonHandle().encode())

                # self.clientsocket.send(haram.encode())

                data = self.clientsocket.recv(1024).decode()

                print("Server: " + data)



        except socket.error as serror:
            print("Socketerror: " + serror.strerror)


    def buttonHandle(self):
        self.view.senden.clicked.connect(lambda: self.setmsg("Client 1: " + self.view.input.text()))
        self.view.senden.clicked.connect(lambda: self.view.input.clear())
        self.view.senden.clicked.connect(lambda: self.view.input.setFocus())
        self.view.output.verticalScrollBar()
        return self.msg

    def setmsg(self, msg):
        self.msg += msg + "<br>"
        self.view.output.setText(self.msg)
        return self.msg





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # client = Controller("localhost", 50000)
    # client.move(400,200)
    # client.show()
    #
    # t = Connectthread()
    # t.daemon = True
    # t.start()

    client2 = Connectthread()
    client2.show()

    client2.daemon = True
    client2.start()


    #server = Controller(ServerView, "localhost", 50000)
    #server.move(823,200)
    #server.show()
    #server.connect_to_server()

    sys.exit(app.exec_())