# importing socket library
import socket

# creating socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# it can be anything between 0 and 65535
port = 12345

# binding (bağlamak) to specific address and port
# we did not give ip address
# all computer in the network can connect
s.bind(('', port))
print(f"Socket binded to {port}")

# starting to listening mode
# number is maximum unacceptable connection count
s.listen(5)
print("Socket is listening")

# a forever loop until we interrupt it
while True:
    # Establish connection with client.
    # accept() returns new socket object and address
    # c is a new socket object able to send and receive data
    # address is the address bound to the socket on the other end of the connection
    c, addr = s.accept()
    print(f"Got connection from {addr}")
    print(f"Socket object : {c}")

    # send a thank-you message to the client
    # encoding to send byte type.
    c.send('Thank you for connecting'.encode())

    # Close the connection with the client
    c.close()

    # Breaking once connection closed
    break
