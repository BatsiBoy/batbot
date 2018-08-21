#Name: Batbot - Network Variables
#Author: Batsi

#Any variables related to network connectivity and authentication.
#Configure these variables with your authorization credentials to use this bot for yourself.

#Credit to cormac-obrein of Instructables for the basis of this file.

HOST = "irc.chat.twitch.tv"          #Twitch uses IRC for chat, point to their server here
PORT = 6667                     #Twitch uses this port
NICK = "BatBot"
AUTH = "oath:xxx"               #Get your Oauth token here: https://twitchapps.com/tmi/
CHAN = "#channel"               #Twitch channel to live in

RATE = (20/30)                  #Twitch limits regular user rate to 20 messages per 30 seconds.