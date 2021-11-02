from threading import *
from socket import *

import pickle

from aernetworking.client_handler import ClientHandler

class Server:
    def __init__(self, ip, port):
        self.server = socket(AF_INET, SOCK_STREAM)

        self.ip = ip
        self.port = port

    def listen(self, function, max = 20):
        self.server.bind((self.ip, self.port))
        self.server.listen(max)

        while True:
            connection, address = self.server.accept()

            client_handler = ClientHandler(connection, address, function)
            client_handler.start()

    def send(self, connection, data):
        connection.send(pickle.dumps(data))

    def recv(self, connection, size = 1024):
        return pickle.dumps(connection.recv(size))

    def destroy(self):
        self.server.close()