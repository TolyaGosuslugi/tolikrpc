# MIT License
# 
# Copyright (c) 2024 Nikita Belov
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import psutil
import random
import json
import time
from pypresence import Presence

chill_img = random.choice(["https://i.imgur.com/v0SifzJ.gif", "https://i.imgur.com/0wRVS7T.gif", "https://media1.tenor.com/m/90koS7WCDO4AAAAC/skill-issue-skills.gif"])

client = Presence(1089811981009178775)
client.connect()

def check(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
    
data = json.load(open("progs.json"))

while True:

    rndm_text = random.choice(["nya :3", "meow :D", "Rise and Shine, mister Freeman", "u are so best", "suka blyat vodka", "tolik was here", "It starts with one(one thing) I dont know why", "Welkom in Europa, jongen!", "私は猫です", "print(Hello, World!)"])
    
    found = False
    for process, details in data.items():
        if check(process):
            client.update(
                details="Playing",
                state=details['name'],
                large_image=details['icon'],
                large_text=rndm_text,
            )
            found = True
            break
    
    else:
        client.update(
            details="Chilling",
            large_image=chill_img,
            large_text=rndm_text,
        )
        
    time.sleep(3)