# importing socket library
import socket

# creating socket object
s = socket.socket()

# initialize host info
port = 12345
ip = '127.0.0.1'

# connection the server
s.connect((ip, port))

# looking for receive any message and decode
# the number 4096 about buff size
print(s.recv(4096).decode())

# closing the object
s.close()
