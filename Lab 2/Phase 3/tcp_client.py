#Author: Aryan Chandra & Muhammad (Hasaan) Toor

import socket
from twisted.internet import reactor, protocol, endpoints

class UDPClient(protocol.DatagramProtocol):
    def startProtocol(self):
        self.server_address = (socket.gethostbyname('localhost'), 1234)
        reactor.callInThread(self.send_data)

    def datagramReceived(self, data, addr):
        data = data.decode("utf-8")
        print(data)

    def send_data(self):
        while True:
            message = input()
            self.transport.write(message.encode("utf-8"), self.server_address)

            if message == "!Q":
                reactor.stop()
                break

if __name__ == "__main__":
    reactor.listenUDP(0, UDPClient())  # Start listening on a random local port
    reactor.run()
