import socket

class Server(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

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

if __name__ == "__main__":
    server = Server("localhost", 50000)
    server.bind_and_listen()