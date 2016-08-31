import socket
socket.setdefaulttimeout(2)
s = socket.socket()

try :
 s.connect(("192.168.95.149",21))
except Exception, e:
 print "[-] Error = "+str(e)


ans = s.recv(1024)
print ans
# if ("FreeFloat Ftp Server (Version 1.00)" in ans):
