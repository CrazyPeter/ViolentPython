import socket

socket.setdefaulttimeout(10)
s = socket.socket()
s.connect(('127.0.0.1',12345))
ans = s.recv(1024)
print ans



# >>> socket.setdefaulttimeout(2)
# >>> s = socket.socket()
# >>> s.connect(("192.168.95.148",21))
# >>> ans = s.recv(1024)
# >>> print ans
# 220 FreeFloat Ftp Server (Version 1.00).
