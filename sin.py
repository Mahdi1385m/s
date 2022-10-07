from requests import get
from re import findall
import os
import glob
from Arsein import Robot_Rubika
import requests
from gtts import gTTS
from mutagen.mp3 import MP3
import json
from datetime import datetime
from json import loads , dumps
import time
from time import sleep
import random
import urllib.request
import io
from random import choice,randint
from PIL import Image
from colorama import Fore
green = '\033[32m' 
red = '\033[31m' 
blue = '\033[36m' 
pink = '\033[35m' 
yellow = '\033[93m' 
darkblue = '\033[34m' 
white = '\033[00m'

bot = Robot_Rubika("ynhczsukhidqxmqlnjquovpmwpdvppun")

channell_sin_tabl = ["c0HhAr0dd2a2b3e454b99afd5b02a995","c0qg2R078ef0adfb63adffdfe8d2dfd7","c0Os2U04e474afa9d597a71959dc8b7e","c0BTXy05d5dbf4aa17e8c92e7e260973","c0Btyq095a83abe72ecf41080c6f1c35"]
channells = choice(channell_sin_tabl)


answered, sleeped, retries,forward_Channell, answer,lock_fosh,st,list_gap,sttab2,st_tabl,deletergap = [] , False , {} , True , [] , False , False , [] , False , False , True
alerts, blacklist, stars, alert_stickers, alert_Gif, lock_GIF,lock_Sticker,star_sinza,sin_time,tab_time = [] , [] , [] , [] , [] , False , False , False , False , False



#m = input("your post link \n")
post_link = "https://rubika.ir/m_GIF_0_o/CJCADFFEGCHBIBG"
sum = 0
while True:
    try:
        bot.joinChannelAction(channells)
        res = bot.getLinkFromAppUrl(post_link)
        k = res["object_guid"]
        m = res["message_id"]
        last_chat = bot.getChannelInfo(channells)["data"]["chat"]["last_message_id"]
        messages_channell = bot.getMessages(channells,last_chat)
        for chat in messages_channell:
        					try:
        					    chat = chat['text']
        					    link_Group = findall(r"https://rubika.ir/joing/\w{32}", chat)
        					    for linkes in link_Group:
        					        list_gap.append(linkes)
        					        randomli = choice(list_gap)
        					        tabeligh = bot.joinGroup(randomli)
        					        tabrligh = tabeligh['data']['group']['group_guid']
        					        info = tabeligh['data']['group']['group_title']
        					        momber = tabeligh['data']['group']['count_members']
        					        sum += 1
        					        bot.forwardMessages(k,[m],tabrligh)
        					        print(green+f" forward mag : <{randomli}> \n {blue}name gap : <{info}> \n {yellow}forward : <{sum}> \n {blue}momber group : <{momber}>")
        					        bot.leaveGroup(tabrligh)
        					except:continue  
    except:pass
