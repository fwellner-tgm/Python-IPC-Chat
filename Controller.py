import ClientView, ServerView, sys, socket
from PySide import QtGui, QtCore


class Controller(QtGui.QWidget):
    def __init__(self, host, port, parent=None):
        super().__init__(parent)

        self.host = host
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
                    self.connect(self.view.senden, QtCore.SIGNAL("clicked()"), lambda: print("swag"))
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

    def bind_and_listen(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:

            serversocket.bind((self.host, self.port))
            serversocket.listen(5)

            try:

                while True:

                    print("Auf Clients warten...")

                    (clientsocket, address) = serversocket.accept()
                    print("Client verbunden! Warte auf Nachricht...")

                    while True:

                        data = clientsocket.recv(1024).decode()

                        if not data:
                            clientsocket.close()
                            break
                        if data == "exit":
                            clientsocket.send("Tschüss!".encode())
                            clientsocket.close()
                            break
                        else:
                            msg = input("Antwort an Client: ")
                            clientsocket.send(msg.encode())
            except socket.error as serror:
                print("Socket closed.")

    def send_msg(self, msg):
        self.view.senden.clicked.connect(self.clientsocket.send(msg.encode()))
        self.view.senden.clicked.connect(self.view.output.setText(msg))

    def get_msg(self):
        print(self.view.input.text())



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    client = Controller("localhost", 50000)
    client.move(400,200)
    client.show()
    client.connect_to_server()

    #server = Controller(ServerView, "localhost", 50000)
    #server.move(823,200)
    #server.show()
    #server.connect_to_server()

    sys.exit(app.exec_())