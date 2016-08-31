import socket
socket.setdefaulttimeout(100)
s = socket.socket()

try :
 s.connect(("127.0.0.1",12345))
except Exception, e:
 print "[-] Error = "+str(e)


ans = s.recv(1024)
print ans
# if ("FreeFloat Ftp Server (Version 1.00)" in ans):
