"""Custom topology example

Two directly connected switches plus a host for each switch:

   

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        hostOne = self.addHost( 'h1' )
        hostTwo = self.addHost( 'h2' )
        hostThree = self.addHost( 'h3' )
        hostFour = self.addHost( 'h4' )
        hostFive = self.addHost( 'h5' )
        hostSix = self.addHost( 'h6' )
        hostSeven = self.addHost( 'h7' )
        hostEight = self.addHost( 'h8' )

        switchOneHostOne = self.addSwitch( 's1h1' )
        switchTwoHostTwo = self.addSwitch( 's2h2' )
        switchThreeHostThree = self.addSwitch( 's3h3' )
        switchFourHostFour = self.addSwitch( 's4h4' )
        switchFiveLeft = self.addSwitch( 's5x1' )
        switchSixRight = self.addSwitch( 's6x2' )
        switchSeven = self.addSwitch( 's7' )
        switchEight = self.addSwitch( 's8' )
        switchNine = self.addSwitch( 's9' )
        switchTenHostSeven = self.addSwitch( 's10h7' )
        switchElevenHostEight = self.addSwitch( 's11h8' )

        # Add links
        self.addLink( hostOne, switchOneHostOne )
        self.addLink( hostTwo, switchTwoHostTwo )
        self.addLink( hostThree, switchThreeHostThree )
        self.addLink( hostFour, switchFourHostFour )

        self.addLink( switchOneHostOne, switchFiveLeft )
        self.addLink( switchTwoHostTwo, switchFiveLeft )

        self.addLink( switchThreeHostThree, switchSixRight )
        self.addLink( switchFourHostFour, switchSixRight )

        self.addLink( switchFiveLeft, switchSeven )
        self.addLink( switchSixRight, switchSeven )

        self.addLink( switchSeven, switchEight )

        self.addLink( hostFive, switchEight )
        self.addLink( hostSix, switchEight )

        self.addLink( switchEight, switchNine )

        self.addLink( switchNine, switchTenHostSeven )
        self.addLink( switchNine, switchElevenHostEight )

        self.addLink( switchTenHostSeven, hostSeven )
        self.addLink( switchElevenHostEight, hostEight )


topos = { 'mytopo': ( lambda: MyTopo() ) }
