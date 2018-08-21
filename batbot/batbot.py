#Name: BatBot
#Author: Batsi

#This is a general-purpose Twitch and Discord chatbot for moderation and entertainment.
#This project exists mostly as a playground to implement an interactive daemon with various features.
#I expect a number of dramatic reworks and bugs, hang on for the ride.

#Feel free to pull/branch/fork.

import netcfg as nc                                          #Configuration module containing network variables
import writing as wr                                         #Text fragments for responding.
import netfuncs as nf                                        #Repeatedly used functions for network connection.
import socket                                                #Establish connections for network activity 
import re                                                    #Parse raw chat with regular expressions.
import nltk                                                  #Language processing toolkit for chat interactivity.
from time import sleep                                       #For pacing the blocking loop

mainsck = socket.socket()
mainsck.connect((nc.HOST,nc.PORT))                           #Create the socket for connecting to the chat server.
mainsck.send("PASS {}\r\n".format(nc.AUTH).encode("utf-8"))  #OAuth token for your credentials.
mainsck.send("NICK {}\r\n".format(nc.NICK).encode("utf-8"))  #Desired nickname, must be unique in your chat.
mainsck.send("JOIN {}\r\n".format(nc.CHAN).encode("utf-8"))  #The channel to join.

"""
Message parsing objects
Chat messages look like this: 
   :nickname!nickname@nickname.tmi.twitch.tv PRIVMSG #channel :message
All other messages are users coming and going and not needed yet
This object gets the author (3 times) and message info from the message syntax
"""

msg_parse = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
#This object gets the first username out of the above line.
msg_split = re.compile(r"^:\w+!")
#Check for the !batbot command
cmd_about = re.compile(r"^!batbot\b")
#This object checks for the phrase "BatBot" as a standalone word
ph_mention = re.compile(r"\bbatbot\b",re.IGNORECASE)

#Placeholder blocking function for body
while True:
    response = mainsck.recv(1024).decode("utf-8")            #Read in some messages
    if response == "PING :tmi.twitch.tv\r\n":                #The server sends this PING to ensure the bot is active
        mainsck.send("PONG :tmi.twitch.tv\r\n").encode("utf-8")  #Respond with a PONG
    elif msg_parse.match(response):                          #If this is not None, then the response was a chat message.
        username = msg_split.search(response)[1:-1]          #Match the first username and trim off extra characters
        msg = msg_parse.sub("",response)                     #Everything after msg_parse is the message, so this trims it            
        if cmd_about.match(msg):
            nf.chat(mainsck,nc.CHAN, wr.whoami)
        elif ph_mention.match(msg):
            nf.chat(mainsck,nc.CHAN, wr.retort)                                    
    sleep(1 / nc.RATE)                                       #Sleep until the rate limit will allow another message.



    