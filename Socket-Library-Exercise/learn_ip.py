# importing socket library
import socket

# using socket library function
# gethostbyname() returns host name
ip = socket.gethostbyname("www.google.com")
print(f"www.google.com ip address : {ip}")

ip = socket.gethostbyname("127.0.0.1")
print(f"localhost : {ip}")

# using gethostbyaddr() function
# returns detailed info about host
# gethostbyaddr(host) -> (name, alias list, address-list)
ip = socket.gethostbyaddr("www.google.com")
print(f"www.google.com detailed info: {ip}")

