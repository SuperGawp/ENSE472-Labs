#Author: Aryan Chandra & Muhammad (Hasaan) Toor

from twisted.internet import reactor, protocol, endpoints

class UDPServer(protocol.DatagramProtocol):
    def __init__(self, users):
        self.users = users

    def connectionMade(self):
        print ("New Connection")
        self.users.append(self)
        print ("A new connection has been made. Geting name...")
        self.transport.write("Welcome to the Server, what is your name?".encode("utf-8"))

    def datagramReceived(self, data, addr):
        message = data.decode("utf-8")
        sender = None

        if addr in self.users:
            sender = self.users[addr]
        
        if sender:
            if message == "!Q":
                print(f"<{sender}> left the chat.")
                for user_addr, user_name in self.users.items():
                    if user_addr != addr:
                        self.transport.write(f"<{sender}> has left the chat!".encode("utf-8"), user_addr)
                del self.users[addr]
            else:
                print(f"<{sender}>: " + message)
                for user_addr, user_name in self.users.items():
                    if user_addr != addr:
                        self.transport.write(f"<{sender}>: ".encode("utf-8") + data, user_addr)
        else:
            if message == "!Q":
                print(f"Unnamed user left")
            else:
                self.users[addr] = message
                print(f"{message} has entered the chat")
                for user_addr, user_name in self.users.items():
                    if user_addr != addr:
                        self.transport.write(f"{message} has entered the chat".encode("utf-8"), user_addr)

if __name__ == "__main__":
    users = {}  # Dictionary to store user names with their addresses
    reactor.listenUDP(1234, UDPServer(users))
    reactor.run()
