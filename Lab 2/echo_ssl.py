from twisted.internet import protocol, reactor, endpoints, ssl

class Echo(protocol.Protocol): # The brackets means we are extending their class
    def dataReceived(self, data): # This callback will run when we recieve data
        print(f"received {data!r}") #print it out!
        self.transport.write(data) # Write that data back to our transport!

class EchoFactory(protocol.Factory): # Rather than use a constructor, we will use a Factory
    def buildProtocol(self, addr):
        return Echo()

context = ssl.DefaultOpenSSLContextFactory("domain.key", "domain.crt")
reactor.listenSSL(1234, EchoFactory(), context)
reactor.run()
