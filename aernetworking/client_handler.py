from threading import *

class ClientHandler(Thread):
    def __init__(self, connection, address, function):
        Thread.__init__(self)

        self.connection = connection
        self.address = address
        self.function = function

        self.handle()

    def handle(self):
        handler = Thread(target = self.function, args = [self.connection, self.address])
        handler.start()