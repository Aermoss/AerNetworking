from threading import *
from socket import *

from aernetworking.client_handler import ClientHandler

server = socket(AF_INET, SOCK_STREAM)

class Server:
    def __init__(self, ip = gethostbyname(gethostname()), port = None, size = 1024, format = "utf-8", max_client = 20):
        self.ip = ip
        self.port = port
        self.size = size
        self.format = format
        self.max_client = max_client

    def listen(self, function = None):
        address = (self.ip, self.port)
        server.bind(address)
        server.listen(20)

        while True:
            connection, address = server.accept()

            client_handler = ClientHandler(connection, address, function)
            client_handler.start()

    def send(self, connection = None, data = ""):
        connection.send(str(data).encode(self.format))

    def recv(self, connection = None):
        reply = connection.recv(self.size).decode()

        return reply

    def get_local_ip(self):
        ip = gethostbyname(gethostname())

        return ip