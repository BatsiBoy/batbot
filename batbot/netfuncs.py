#Name: Batbot - Network Interaction Functions
#Author: Batsi

#Break out general functions from main integration bot for housekeeping.

def chat(sck, chan, msg):
    """ Send a message (msg) to chat over the chosen socket (sck) """
    sck.send("PRIVMSG #{} :{}".format(chan, msg))
    return