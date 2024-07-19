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
import time
from pypresence import Presence

chill_img = random.choice(["https://i.imgur.com/v0SifzJ.gif", "https://i.imgur.com/0wRVS7T.gif"])
#rndm_text = random.choice(["nya :3", "meow :D", "I'm a cute person", "u are so best", "suka blyat vodka", "tolik was here"])

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

while True:

    rndm_text = random.choice(["nya :3", "meow :D", "Rise and Shine, mister Freeman", "u are so best", "suka blyat vodka", "tolik was here", "It starts with one(one thing) I dont know why", "Welkom in Europa, jongen!", "私は猫です", "print(Hello, World!)"])

    if check("csgo.exe"):
        client.update(
            state="Counter-Strike: Global Offensive",
            details="Playing",
            large_image="https://sun6-23.userapi.com/s/v1/if1/t6I2sTc5NiFMyBPWQR0j7g4Yd7WIGmvhm8eIe0qCkcwBQMI8dBmDXbjB5n6gNcnbSsN0V0Fw.jpg?size=1487x1487&quality=96&crop=203,232,1487,1487&ava=1",
            large_text=rndm_text,
        )
        
    elif check("cs2.exe"):
        client.update(
            state="Counter-Strike 2",
            details="Playing",
            large_image="https://i3.wp.com/media.moddb.com/images/downloads/1/210/209737/b10224ae75edd5debd06c44662cbcb30.png",
            large_text=rndm_text,
        )
        
    elif check("hl.exe"):
        client.update(
            state="Half-Life",
            details="Playing",
            large_image="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Half-Life_lambda_logo.svg/1200px-Half-Life_lambda_logo.svg.png",
            large_text=rndm_text,
        )
        
    elif check("ets2.exe"):
        client.update(
            state="Euro Truck Simulator 2",
            details="Playing",
            large_image="https://img.icons8.com/?size=256&id=MITxSnflsk3j&format=png",
            large_text=rndm_text,
        )
        
    elif check("hl2.exe"):
        client.update(
            state="Half-Life 2",
            details="Playing",
            large_image="https://steamsolo.com/wp-content/uploads/2021/07/how-to-keep-your-car-in-chapter-11-sandtraps-half-life-2.jpg",
            large_text=rndm_text,
        )
        
    elif check("HenryStickmin.exe"):
        client.update(
            state="The Henry Stickmin Collection",
            details="Playing",
            large_image="https://i.imgur.com/2LcKFZv.png",
            large_text=rndm_text,
        )
        
    elif check("gmod.exe"):
        client.update(
            state="Garry's Mod",
            details="Playing",
            large_image="https://sun6-22.userapi.com/s/v1/ig2/Q_uI0Sfk-bEHoR3-tTUxlrRjsDQbVsFzBjj8xSgFCY8poRErcFGCEm4ZuC6J_fXueTQsUL1SeREZmGGFfSUdVuah.jpg?size=1026x1026&quality=96&crop=1,1,1026,1026&ava=1",
            large_text=rndm_text,
        )
        
    elif check("The Jackbox Party Pack 2.exe"):
        client.update(
            state="The Jackbox Party Pack 2",
            details="Playing",
            large_image="https://i.imgur.com/LXKEFLU.png",
            large_text=rndm_text,
        )
        
    elif check("The Jackbox Party Pack 3.exe"):
        client.update(
            state="The Jackbox Party Pack 3",
            details="Playing",
            large_image="https://i.imgur.com/RTrlyx8.png",
            large_text=rndm_text,
        )
        
    elif check("The Jackbox Party Pack 4.exe"):
        client.update(
            state="The Jackbox Party Pack 4",
            details="Playing",
            large_image="https://i.imgur.com/AEvHZ1z.png",
            large_text=rndm_text,
        )
    
    elif check("The Jackbox Party Pack 5.exe"):
        client.update(
            state="The Jackbox Party Pack 5",
            details="Playing",
            large_image="https://i.imgur.com/ZaP12sS.png",
            large_text=rndm_text,
        )
        
    elif check("The Jackbox Party Pack 6.exe"):
        client.update(
            state="The Jackbox Party Pack 6",
            details="Playing",
            large_image="https://i.imgur.com/ub93Ywq.png",
            large_text=rndm_text,
        )
        
    elif check("The Jackbox Party Pack 7.exe"):
        client.update(
            state="The Jackbox Party Pack 7",
            details="Playing",
            large_image="https://i.imgur.com/L0BeN9g.png",
            large_text=rndm_text,
        )
        
    elif check("Teardown.exe"):
        client.update(
            state="Teardown",
            details="Playing",
            large_image="https://static.wikia.nocookie.net/logopedia/images/7/79/Teardown_2022_%28Icon%29.png/revision/latest?cb=20221215232436",
            large_text=rndm_text,
        )
        
    elif check("Lethal Company.exe"):
        client.update(
            state="Lethal Company",
            details="Playing",
            large_image="https://cdn2.steamgriddb.com/icon/5d29c687a58bc919bd4b28609e2f7134/32/512x512.png",
            large_text=rndm_text,
        )
        
    elif check("sandbox.exe"):
        client.update(
            state="Sand:box",
            details="Playing",
            large_image="https://i.imgur.com/7x0jFUn.png",
            large_text=rndm_text,
        )
        
    elif check("Solitaire.exe"):
        client.update(
            state="Microsoft Solitaire",
            details="Playing",
            large_image="https://cdn.discordapp.com/app-assets/1221433085829185598/1221434157293633586.png",
            large_text=rndm_text,
        )
    
    else:
        client.update(
            details="Chilling",
            large_image=chill_img,
            large_text=rndm_text,
        )
time.sleep(3)