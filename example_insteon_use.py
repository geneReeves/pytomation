from pytomation.interfaces import InsteonPLM, TCP

tcp = TCP('192.168.13.146', 9761)
insteon = InsteonPLM(tcp)
insteon.start()

# Turn on Light - Network: 49, ID: 3
response = insteon.on('19.05.7b')

# Turn off Light - Network: 49, ID: 3
response2 = insteon.off('19.05.7b')

# Check for success
if response:
    print "Message was successfully sent!"
else:
    print "Interface not responding"

# Code is down, we no longer need the interface
insteon.shutdown()
tcp.shutdown()