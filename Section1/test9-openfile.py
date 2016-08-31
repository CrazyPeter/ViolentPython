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
    f = open("vuln_banners.txt",'r')
    for line in f.readlines():
        print 'line content is'+line
        if line.strip('\n') in banner:
            # print 'line content is'+line
            print "[+] Server is vulnerable: "+banner.strip('\n')

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
