import gdshortener
import os
import time

def ascii():
    print("_  _ ____ _       ____ ___  ____ ____ ____ _ _  _ ____")
    print("|  | |__/ |       [__  |__] |  | |  | |___ | |\ | | __")
    print("|__| |  \ |___    ___] |    |__| |__| |    | | \| |__]")
    print("")
    print("Masteer-V")
    print("")
    print(" ███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃")
    print(" ▂▄▅█████████▅▄▃▂")
    print(" I███████████████████].")
    print(" ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...")
    print("")
    print("")
    print("")

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def load():
    print("Generating url...")

clear()
ascii()

s = gdshortener.ISGDShortener()

url = input("Enter a URL >>> ")
    
surl = input("Enter custom part >>> ")

load()
time.sleep(2)

fin = s.shorten(url)

newurl = fin[0]

truesurl = "https://" + surl + "@"

trueurl = newurl.replace("https://", truesurl)

print("New url > > > " + trueurl)