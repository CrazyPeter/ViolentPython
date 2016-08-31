import socket

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(10)
        s=socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
            print '[+] FreeFloat FTP Server is vulnerable.'
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
            print '[+] 3CDaemon FTP Server is vulnerable.'
    elif 'Ability Server 2.34' in banner:
            print '[+] Ability FTP Server is vulnerable.'
    elif 'Sami FTP Server 2.0.2' in banner:
            print '[+] Sami FTP Server is vulnerable.'
    else:
            print '[-] FTP Server is not vulnerable.'
            return

def main():
    ip1 = '127.0.0.1'
    ip2 = '192.168.95.149'
    port = 12345

    banner1 = retBanner(ip1,port)
    if banner1:
        print '[+] ' + ip1 + ': ' + banner1
        checkVulns(banner1)
    banner2 = retBanner(ip2, port)
    if banner2:
        print '[+] ' + ip2 + ': ' + banner2
        checkVulns(banner2)


if __name__ == '__main__':
    main()
