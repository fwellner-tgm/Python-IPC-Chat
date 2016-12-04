import ClientView, ServerView, sys, socket, threading
import _thread
from PySide import QtGui, QtCore


class Controller(QtGui.QWidget):
    def __init__(self, host, port, parent=None):
        super().__init__(parent)

        self.host = host
        self.port = port

        self.view = ServerView.Ui_Form()
        self.view.setupUi(self)



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



    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        print("Test")
        self.socket.listen(5)
        while True:
            print("Auf Clients warten...")
            client, address = self.socket.accept()
            threading.Thread(target = self.listenClient, args = (client, address)).start()

    def listenClient(self, client, address):
        while True:
             try:

                data = client.recv(1024)
                if data:
                    response = data
                    client.send(response)
                else:
                    raise Exception("Client disconnected")

             except socket.error:
                 print("Socket closed")


    def send_msg(self, msg):
        self.view.senden.clicked.connect(self.clientsocket.send(msg.encode()))
        self.view.senden.clicked.connect(self.view.output.setText(msg))

    def get_msg(self):
        print(self.view.input.text())


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    server = Controller("localhost", 50000)
    server.move(400,200)
    server.show()
    server.listen()



    #server = Controller(ServerView, "localhost", 50000)
    #server.move(823,200)
    #server.show()
    #server.connect_to_server()

    sys.exit(app.exec_())