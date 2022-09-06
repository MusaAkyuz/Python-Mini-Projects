# importing socket library
import socket

# using socket function gethostbyname()
# taking parameter host name and return address
ip = socket.gethostbyname('www.google.com')
print(ip)

ip = socket.gethostbyname('127.0.0.1')
print(ip)

# using socket function gethostbyaddr()
# taking host name and return more detailed host name and ip address list
ip = socket.gethostbyaddr('www.google.com')
print(ip)

ip = socket.gethostbyaddr('221.43.21.43')
print(ip)
