import select

from pytomation.interfaces import UPB, InsteonPLM, TCP, Serial, Stargate

###################### INTERFACE CONFIG #########################
upb = UPB(Serial('/dev/ttyMI0', 4800))
upb.start()

insteon = InsteonPLM(TCP('192.168.13.146', 9761))
insteon.start()

sg = Stargate(Serial('/dev/ttyMI2', 9600))
sg.start()

###################### DEVICE CONFIG #########################


# Turn on Light - Address 19.05.7b
response = insteon.on('19.05.7b')

# Turn off Light - Address 19.05.7b
response2 = insteon.off('19.05.7b')

# Turn on Light - Network: 49, ID: 3
response = upb.on((49, 3))

# Turn off Light - Network: 49, ID: 3
response2 = upb.off((49, 3))

def on_digital_input(command=None, address=None):
    print "Digital Input #" + str(address) + " -> " + str(command)

# Listen for changes on Digital Input #1 on Stargate
sg.onCommand(callback=on_digital_input, address='D1')

# sit and spin - Let the magic flow
select.select([],[],[])