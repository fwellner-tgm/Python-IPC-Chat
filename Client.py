import socket


class Client(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def connect_to_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
            try:
                clientsocket.connect((self.host, self.port))

                while True:
                    msg = input("Nachricht an den Server: ")
                    clientsocket.send(msg.encode())

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

if __name__ == "__main__":
    client = Client("127.0.0.1", 50000)
    client.connect_to_server()