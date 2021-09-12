from aernetworking import * # this will import everything we need from AerNetworking with just one line.

client = Client()

client.ip = client.get_local_ip()
client.port = 5656

client.connect() # this is for connecting the server

message = client.recv() # this will recieves the message from connection
print(message)