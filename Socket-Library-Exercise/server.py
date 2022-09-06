import socket

# creating socket object
s = socket.socket()

# initializing server info
port = 12345  # port can be between 0 and 65535
ip_addr = '127.0.0.1'  # loopback/localhost

# creating open connection with server info
# which other computer on the network can establish
s.bind((ip_addr, port))

# listening the connection
s.listen(5)

while True:
    # c is new socket object includes information about connection
    # addr is computer ip address which connect the open connection
    # accept() starts the connection
    # also c can send or receive a message
    # between other computer which established
    c, addr = s.accept()

    # you must encode byte to send across the network
    c.send("You are in!".encode())

    c.close()

    break
