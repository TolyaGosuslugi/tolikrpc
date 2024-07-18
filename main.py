import psutil
import random
import time
from pypresence import Presence

chill_img = random.choice(["https://i.imgur.com/v0SifzJ.gif", "https://i.imgur.com/0wRVS7T.gif"])
rndm_text = random.choice(["nya :3", "meow :D", "I'm a cute person", "u are so best", "suka blyat vodka", "tolik was here"])

client = Presence(1089811981009178775)

btns = [
    {
        "label": "Download",
        "url": "https://github.com/TolyaGosuslugi/tolikrpc"
    }
]

client.connect()

while True:
        
    if "csgo.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Counter-Strike: Global Offensive",
            details="Playing",
            buttons=btns,
            large_image="https://sun6-23.userapi.com/s/v1/if1/t6I2sTc5NiFMyBPWQR0j7g4Yd7WIGmvhm8eIe0qCkcwBQMI8dBmDXbjB5n6gNcnbSsN0V0Fw.jpg?size=1487x1487&quality=96&crop=203,232,1487,1487&ava=1",
            large_text=rndm_text,
        )
        
    if "cs2.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Counter-Strike 2",
            details="Playing",
            buttons=btns,
            large_image="https://i3.wp.com/media.moddb.com/images/downloads/1/210/209737/b10224ae75edd5debd06c44662cbcb30.png",
            large_text=rndm_text,
        )
        
    if "hl.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Half-Life",
            details="Playing",
            buttons=btns,
            large_image="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Half-Life_lambda_logo.svg/1200px-Half-Life_lambda_logo.svg.png",
            large_text=rndm_text,
        )
        
    if "ets2.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Euro Truck Simulator 2",
            details="Playing",
            buttons=btns,
            large_image="https://img.icons8.com/?size=256&id=MITxSnflsk3j&format=png",
            large_text=rndm_text,
        )
        
    if "hl2.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Half-Life 2",
            details="Playing",
            buttons=btns,
            large_image="https://logodix.com/logo/1687700.png",
            large_text=rndm_text,
        )
        
    if "HenryStikmin.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Henry Stickmin Collection",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/2LcKFZv.png",
            large_text=rndm_text,
        )
        
    if "gmod.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Garry's Mod",
            details="Playing",
            buttons=btns,
            large_image="https://sun6-22.userapi.com/s/v1/ig2/Q_uI0Sfk-bEHoR3-tTUxlrRjsDQbVsFzBjj8xSgFCY8poRErcFGCEm4ZuC6J_fXueTQsUL1SeREZmGGFfSUdVuah.jpg?size=1026x1026&quality=96&crop=1,1,1026,1026&ava=1",
            large_text=rndm_text,
        )
        
    if "The Jackbox Party Pack 2.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Jackbox Party Pack 2",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/LXKEFLU.png",
            large_text=rndm_text,
        )
        
    if "The Jackbox Party Pack 3.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Jackbox Party Pack 3",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/RTrlyx8.png",
            large_text=rndm_text,
        )
        
    if "The Jackbox Party Pack 4.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Jackbox Party Pack 4",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/AEvHZ1z.png",
            large_text=rndm_text,
        )
    
    if "The Jackbox Party Pack 5.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Jackbox Party Pack 5",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/ZaP12sS.png",
            large_text=rndm_text,
        )
        
    if "The Jackbox Party Pack 6.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Jackbox Party Pack 6",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/ub93Ywq.png",
            large_text=rndm_text,
        )
        
    if "The Jackbox Party Pack 7.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="The Jackbox Party Pack 7",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/L0BeN9g.png",
            large_text=rndm_text,
        )
        
    if "Teardown.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Teardown",
            details="Playing",
            buttons=btns,
            large_image="https://static.wikia.nocookie.net/logopedia/images/7/79/Teardown_2022_%28Icon%29.png/revision/latest?cb=20221215232436",
            large_text=rndm_text,
        )
        
    if "Lethal Company.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Lethal Company",
            details="Playing",
            buttons=btns,
            large_image="https://cdn2.steamgriddb.com/icon/5d29c687a58bc919bd4b28609e2f7134/32/512x512.png",
            large_text=rndm_text,
        )
        
    if "sandbox.exe" in (p.name() for p in psutil.process_iter()):
        client.update(
            state="Sand:box",
            details="Playing",
            buttons=btns,
            large_image="https://i.imgur.com/7x0jFUn.png",
            large_text=rndm_text,
        )
    
    else:
        client.update(
            details="Chilling",
            buttons=btns,
            large_image=chill_img,
            large_text=rndm_text,
        )