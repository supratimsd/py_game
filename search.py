import time
import datetime
import os
import sys

windows = lambda: os.system('cls')

TGREEN = '\x1b[5;30;42m'
TWHITE = '\x1b[0m'
flag = 1
while flag:
    print('Select Website:')
    print('1. Shopee')
    print("Enter selected number:", end="")
    web = input()
    if web == '1':
        web = 'shopee'
    print('Select Website:')
    print('1. Malaysia')
    print('2. Singapore')
    print('3. Philippines')
    print('4. Indonesia')
    print("Enter selected number:", end="")
    country = input()
    if country == "1":
        country = 'malaysia'
    elif country == "2":
        country = 'singapore'
    elif country == "3":
        country = 'philippines'
    elif country == "4":
        country = 'indonesia'
    windows()
    print(TWHITE + 'Your selection is ' + TGREEN + web.capitalize() + " - " + country.capitalize() + TWHITE)
    print(TWHITE + "Confirm selection [y/n]:", end="")
    selc = input()
    if selc == 'Y' or selc == 'y':
        flag = 0
    windows()
flag = 1
while flag:
    print(TGREEN + web.capitalize() + " - " + country.capitalize() + TWHITE)
    print("Select Scraping Type:")
    print('1. New Keywords')
    print('2. Tokens')
    print('3. Empty Keys')
    print("Enter selected number:", end="")
    type = input()
    if type == "1":
        type = 'New Keywords'
    elif type == "2":
        type = 'Tokens'
    elif type == "3":
        type = 'Empty Keys'
    windows()
    print(TWHITE + 'Your selection is ' + TGREEN + type.capitalize() + TWHITE)
    print(TWHITE + "Confirm selection [y/n]:", end="")
    selc = input()
    if selc == 'Y' or selc == 'y':
        flag = 0
    windows()
print(TGREEN + web.capitalize() + " - " + country.capitalize() + '>' + type + TWHITE)
