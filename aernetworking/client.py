from socket import *

client = socket(AF_INET, SOCK_STREAM)

class Client:
    def __init__(self, ip = gethostbyname(gethostname()), port = None, size = 1024, format = "utf-8"):
        self.ip = ip
        self.port = port
        self.size = size
        self.format = format

    def connect(self):
        address = (self.ip, self.port)
        client.connect(address)

    def send(self, data):
        client.send(data.encode(self.format))

    def recv(self):
        reply = client.recv(self.size).decode()

        return reply

    def get_local_ip(self):
        ip = gethostbyname(gethostname())

        return ip