# importing socket library
import socket

# creating INET raw socket object
# AF_INET means ipv4 address type
# SOCK_RAW means raw socket
# we will capture TCP packets
s = socket.socket(socket.AF_INET, socket.SOCK_RAW)

# initializing server info
port = 80  # port can be between 0 and 65535
ip_addr = '127.0.0.1'  # loopback/localhost


# creating open connection with server info
# which other computer on the network can establish
# s.bind((ip_addr, port))

while True:
    print(s.recvfrom())
# NOT WORKING I WILL CONTINUE
