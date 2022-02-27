import logging
import re
import socket
import socketserver
import sys
import time
import sipfullproxy as sip


HOST, PORT = '0.0.0.0', 5060


def main():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info('Hosting IP: %s' % ipaddress)
    sip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    sip.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = socketserver.UDPServer((HOST, PORT), sip.UDPHandler)
    server.serve_forever()


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='MTAA_proxy.log', level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ---> PROXY START", time.localtime()))
    main()
