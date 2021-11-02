from socket import *

import pickle

class Client:
    def __init__(self, ip, port):
        self.client = socket(AF_INET, SOCK_STREAM)

        self.ip = ip
        self.port = port

    def connect(self):
        self.client.connect((self.ip, self.port))

    def send(self, data):
        self.client.send(pickle.dumps(data))

    def recv(self, size = 1024):
        return pickle.loads(self.client.recv(size))

    def destroy(self):
        self.client.close()