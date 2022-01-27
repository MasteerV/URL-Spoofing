import gdshortener
import os
import time

def ascii():
    print(" _  _ ____ _       ____ ___  ____ ____ ____ _ _  _ ____")
    print(" |  | |__/ |       [__  |__] |  | |  | |___ | |\ | | __")
    print(" |__| |  \ |___    ___] |    |__| |__| |    | | \| |__]")
    print("")
    print(" Masteer-V")
    print("")
    print(" ███۞███████ ]▄▄▄▄▄▄▄▄▄▄▄▄▃")
    print(" ▂▄▅█████████▅▄▃▂")
    print(" I███████████████████].")
    print(" ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...")
    print("")
    print("")


#function to clean screen
def clear():
    #to Windows
    if os.name == "nt":
        os.system("cls")
    #to Linux
    else:
        os.system("clear")

def load():
    print("Generating url...")

#Main 
def get_url_shortened():
    #We create the object with the imported class 'gdshortener'
    request_gdshortener = gdshortener.ISGDShortener()
    #Enter url to which we will be redirected
    url = input("Enter a URL >>> ")
    #Enter the custom part
    custom_url_part = input("Enter custom part >>> ")
    true_custom_url_part = "https://" + custom_url_part + "@"
    load()
    time.sleep(1)
    #Shorten the url entered
    shortened_url = request_gdshortener.shorten(url)
    #We take position 0 because 'shortened_url' returns a tuple
    newurl = shortened_url[0]
    #Finally we replace the 'https://' of shorten url for the custom part
    final_url = newurl.replace("https://", true_custom_url_part)
    print("New url > > > " + final_url)

clear()
ascii()
get_url_shortened()