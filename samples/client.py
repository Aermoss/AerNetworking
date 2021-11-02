from aernetworking import * # this will import everything we need from AerNetworking with just one line.

client = Client(ip = get_local_ip(), port = 5656)

client.connect() # this is for connecting the server

message = client.recv() # this will recieves the message from connection
print(message)