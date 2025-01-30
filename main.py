#!/usr/bin/env python

from requests import get
from json import dumps, load
#from art import text2art
from time import sleep
from sys import stdout


titleArt1 = r"""
  __  __                                    _____      _ 
 |  \/  | ___ _ __  ___  __ _  __ _ _ __   |_   _|   _(_)
 | |\/| |/ _ \ '_ \/ __|/ _` |/ _` | '__|____| || | | | |
 | |  | |  __/ | | \__ \ (_| | (_| | | |_____| || |_| | |
 |_|  |_|\___|_| |_|___/\__,_|\__,_|_|       |_| \__,_|_|
                                                         
"""

titleArt2 = r"""
  ____       _           _ _           _ 
 / ___|  ___| |__  _ __ (_) |_ _______| |
 \___ \ / __| '_ \| '_ \| | __|_  / _ \ |
  ___) | (__| | | | | | | | |_ / /  __/ |
 |____/ \___|_| |_|_| |_|_|\__/___\___|_|
                                         
"""


def typewriter_print(text, delay=0.01, end="\n"):
    for char in text:
        stdout.write(char)
        stdout.flush()
        sleep(delay)
    print(f"{end}", end="")  # Move to the next line after the text is printed

def colored(text, color_code=None, bold=False):
    # Start with the escape code for bold if requested
    start_code = "\033[1m" if bold else ""
    # Add the color code if provided
    if color_code:
        start_code += f"\033[{color_code}m"
    # End code to reset formatting
    end_code = "\033[0m"

    return f"{start_code}{text}{end_code}"

def clickable_link(text, url):
    # ANSI escape sequence for a clickable link
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def getJsonData(URL):
    response = get(URL)

    if response.status_code == 200:
        json_data = response.json()
        with open("out.json", "w") as file:
            file.write(dumps(json_data, indent=4))

def readJsonData():
    with open("out.json", "r") as file:
        json_data = load(file)
        file.close()

    print_output = ""

    
    # print mensaar artwork
    #Art = text2art("Mensaar")
    titel_artwork = colored(titleArt1, "33", bold=True) + "\n"



    day = 0
    for i in range(len(json_data["days"])):
        if json_data["days"][day]["isPast"]:
            day += 1

    counters = json_data["days"][day]["counters"]


    max_meal_name_len = 0
    for i in range(min(len(counters), 4)):
        max_meal_name_len = max(max_meal_name_len, len(counters[i]["meals"][0]["name"]))



    schnitzel = False
    for i in range(min(len(counters), 4)):
        menuType = [
            colored(f'Menu 1:      ', "34", bold=True),
            colored(f'Menu 2:      ', "31", bold=True),
            colored(f'Wahlessen:   ', "33", bold=True),
            colored(f'Mensacafé:   ', "32", bold=True),
            ]
        menu_Type_Color = ["34", "31", "33", "32"]


        print_output_menu = ""
        # print menu type
        print_output_menu += menuType[i]

        # print menu name
        print_output_menu += f"\t{colored(clickable_link(counters[i]['meals'][0]['name'], "https://www.google.com/search?q="+counters[i]['meals'][0]['name'],), menu_Type_Color[i], bold=True)}    {' '*(max_meal_name_len - len(counters[i]['meals'][0]['name']))} - "

        # print Description
        print_output_menu += f"{colored(counters[i]['description'], '90')}   \t"


        # print menu price
        prices = counters[i]["meals"][0]["prices"]
        for p in prices:
            print_output_menu += f"{p}: {prices[p]}€  "
        print_output_menu += "\n"

        # print menu components
        components = counters[i]["meals"][0]["components"]
        max_component_name_len = 0

        for j in range(len(components)): #get max component length
            max_component_name_len = max(len(components[j]["name"]), max_component_name_len)

        for j in range(len(components)):
            print_output_menu += f'\t\t| {components[j]["name"]} \n'

        print_output_menu += "\n"

        # make menu blink when schnitzel
        # check if schnitzel is contained
        if "Schnitzel" in counters[i]['meals'][0]['name']:
            print_output += print_output_menu

             # print schnitzel artwork
            #Art = text2art("Schnitzel")
            titel_artwork = colored(colored(titleArt2, "33", bold=True) + "\n", "5")
        else:
            print_output += print_output_menu



    # print output string
    typewriter_print(titel_artwork + print_output, delay=0.001)



if __name__ == "__main__":
    getJsonData("https://mensaar.de/api/2/TFtD8CTykAXXwrW4WBU4/1/de/getMenu/sb")
    readJsonData()
    print("\nGet more infomation " + clickable_link("here", "https://mensaar.de/#/menu/sb"))
