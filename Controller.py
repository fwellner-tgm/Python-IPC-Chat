import ClientView, ServerView, sys, socket, threading
from PySide import QtGui, QtCore


class Controller(QtGui.QWidget):
    HOST = ""
    PORT = 0

    def __init__(self, host, port, parent=None):
        super().__init__(parent)

        self.HOST = host
        self.host = host

        self.PORT = port
        self.port = port

        self.view = ClientView.Ui_Form()
        self.view.setupUi(self)

    # if view == ClientView:
        # msg = self.view.input.textChanged
        # self.view.senden.clicked.connect(lambda: self.view.output.setText("asda"))
        # self.view.senden.clicked.connect(lambda: print(self.view.input.text()))
        # self.view.senden.clicked.connect(lambda: self.view.output.textChanged())

    def connect_to_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                clientsocket.connect((self.host, self.port))

                while True:
                    self.connect(self.view.senden, QtCore.SIGNAL("clicked()"), clientsocket.send("Funktioniert!!"))
                    # Controller.send_msg(msg)

                    data = clientsocket.recv(1024).decode()

                    if not data:
                        clientsocket.close()
                        break

                    print("Server: " + data)

                    if data == "exit":
                        clientsocket.close()
                        break

            except socket.error as serror:
                print("Socketerror: " + serror.strerror)


    def send_msg(self, msg):
        self.view.senden.clicked.connect(self.clientsocket.send(msg.encode()))
        self.view.senden.clicked.connect(self.view.output.setText(msg))

    def get_msg(self):
        print(self.view.input.text())




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