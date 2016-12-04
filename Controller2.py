import ClientView, ServerView, sys, socket, threading
from PySide import QtGui, QtCore


class Controller(QtGui.QWidget):
    HOST = ""
    PORT = 0
    def __init__(self, host, port, parent=None):
        super().__init__(parent)

        self.host = host
        self.HOST = host

        self.port = port
        self.PORT = port




    # if view == ClientView:
        # msg = self.view.input.textChanged
        # self.view.senden.clicked.connect(lambda: self.view.output.setText("asda"))
        # self.view.senden.clicked.connect(lambda: print(msg))

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
                print(serror.strerror)

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



class Acceptthread(QtGui.QWidget, threading.Thread):
    def __init__(self, parent=None):
        super().__init__(parent)
        threading.Thread.__init__(self)

        self.view = ServerView.Ui_Form()
        self.view.setupUi(self)

        self.host = "localhost"
        self.port = 50000

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))

        self.socket.listen(5)
        self.showChat(text="")

    def run(self):
        try:
            while True:
                #self.view.outputText.setText("Auf Clients warten...")
                print("Auf Clients warten...")
                (clientsocket, address) = self.socket.accept()
                #self.view.outputClients.setText("Client 1")
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

        except socket.error:
            self.run()
            print("Socket closed")

    def showChat(self, text):
        self.view.outputText.setText(text)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # server = Controller("localhost", 50000)
    # server.move(400,200)
    # server.show()
    #server.listen()
    t = Acceptthread()
    t.show()
    # t.join() ist nicht notwendig, denn wenn sich das Programm schließt wird t.daemon auf False gesetzt und der Thread schließt sich von selbst
    t.daemon = True
    t.start()

    #server = Controller(ServerView, "localhost", 50000)
    #server.move(823,200)
    #server.show()
    #server.connect_to_server()

    sys.exit(app.exec_())