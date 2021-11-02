# AerNetworking
An easy-to-use network interface module for python.

## Getting Started
1) Install Python
2) Open cmd/terminal and type:

```
pip install AerNetworking
```

## Examples
# Server
``` python
from aernetworking import * # this will import everything we need from AerNetworking with just one line.

def handler(connection, address): # this function will be run on the new connection
    print("New Connection.")

    message = "Welcome to my server!" 

    server.send(connection = connection, data = message) # this will send message to connection

server = Server(ip = get_local_ip(), port = 5656)

server.listen(function = handler) # this will starts the server
```

# Client
``` python
from aernetworking import * # this will import everything we need from AerNetworking with just one line.

client = Client(ip = get_local_ip(), port = 5656)

client.connect() # this is for connecting the server

message = client.recv() # this will recieves the message from connection
print(message)
```