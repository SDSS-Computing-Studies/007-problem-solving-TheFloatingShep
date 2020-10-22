#!python3

import time
import pyautogui as p 

p.mouseInfo()

x = 50

# Buys upgrades
def upgrades():
    p.moveTo(347,450)
    p.click(347,450)
    time.sleep(0.5)
    while True:
        if p.pixelMatchesColor(1060,590, (225,137,74)):
            p.moveTo(1060,590)
            p.click(1060,590)
            p.moveTo(1256,235)
            time.sleep(0.5)
        else:
            p.moveTo(1256,235)
            p.click(1256,235)
            break

# Buys managers
def managers():
    p.moveTo(347,520)
    p.click(347,520)
    time.sleep(0.5)
    while True:
        if p.pixelMatchesColor(1048,492, (151,191,212)):
            p.moveTo(1048,492)
            p.click(1048,492)
            p.moveTo(1256,235)
            time.sleep(0.5)
            while p.pixelMatchesColor(930,380, (176,219,126)):
                p.moveTo(930,380)
                p.click(930,380)
        else:
            p.moveTo(1256,235)
            p.click(1256,235)
            break

# Buys stuff
def buy():
    global x
    # Purchases
    if p.pixelMatchesColor(690,410, (224,139,78)):
        p.moveTo(690,410)
        p.click(690,410)
        x = 3
    if p.pixelMatchesColor(690,511, (224,139,78)):
        p.moveTo(690,511)
        p.click(690,511)
        x = 5
    if p.pixelMatchesColor(690,609, (224,139,78)):
        p.moveTo(690,609)
        p.click(690,609)
        x = 10
    if p.pixelMatchesColor(690,707, (224,139,78)):
        p.moveTo(690,707)
        p.click(690,707)
        x = 20

    if p.pixelMatchesColor(1043,327, (224,139,78)):
        p.moveTo(1043,327)
        p.click(1043,327)
        x = 30
    if p.pixelMatchesColor(1043,410, (224,139,78)):
        p.moveTo(1043,410)
        p.click(1043,410)
        x = 50
    if p.pixelMatchesColor(1043,511, (224,139,78)):
        p.moveTo(1043,511)
        p.click(1043,511)
        x = 90
    if p.pixelMatchesColor(1043,609, (224,139,78)):
        p.moveTo(1043,609)
        p.click(1043,609)
        x = 150
    if p.pixelMatchesColor(1043,707, (224,139,78)):
        p.moveTo(1043,707)
        p.click(1043,707)
        x = 500

    # Upgrades
    if p.pixelMatchesColor(347,450, (220,123,54)):
        upgrades()

    # Managers
    if p.pixelMatchesColor(347,520, (220,123,54)):
        managers()

    # All the stuff
    # Second line
    # OIL
    if p.pixelMatchesColor(1044,675, (115,105,96)):
        p.moveTo(1044,675)
        p.click(1044,675)
    if p.pixelMatchesColor(1100,710, (224,136,74)):
        p.moveTo(1100,700)
        p.click(1100,700)
    # BANK
    if p.pixelMatchesColor(1044,580, (115,105,96)):
        p.moveTo(1044,580)
        p.click(1044,580)
    if p.pixelMatchesColor(1100,610, (224,136,74)):
        p.moveTo(1100,610)
        p.click(1100,610)
    # MOVIE
    if p.pixelMatchesColor(1044,487, (115,105,96)):
        p.moveTo(1044,487)
        p.click(1044,487)
    if p.pixelMatchesColor(1100,510, (224,136,74)):
        p.moveTo(1100,510)
        p.click(1100,510)
    # HOCKEY
    if p.pixelMatchesColor(1044,393, (115,105,96)):
        p.moveTo(1044,393)
        p.click(1044,393)
    if p.pixelMatchesColor(1100,410, (224,136,74)):
        p.moveTo(1100,410)
        p.click(1100,410)
    # SHRIMP
    if p.pixelMatchesColor(1044,298, (115,105,96)):
        p.moveTo(1044,298)
        p.click(1044,298)
    if p.pixelMatchesColor(1100,330, (224,136,74)):
        p.moveTo(1100,330)
        p.click(1100,330)


    # First line
    # DONUT
    if p.pixelMatchesColor(677,675, (115,105,96)):
        p.moveTo(610,675)
        p.click(610,675)
    if p.pixelMatchesColor(730,710, (224,136,74)):
        p.moveTo(730,710)
        p.click(730,710)
    # PIZZA
    if p.pixelMatchesColor(677,580, (115,105,96)):
        p.moveTo(610,580)
        p.click(610,580)
    if p.pixelMatchesColor(730,610, (224,136,74)):
        p.moveTo(730,610)
        p.click(730,610)
    # CAR
    if p.pixelMatchesColor(677,487, (115,105,96)):
        p.moveTo(610,487)
        p.click(610,487)
    if p.pixelMatchesColor(730,510, (224,136,74)):
        p.moveTo(730,510)
        p.click(730,510)
    # NEWS
    if p.pixelMatchesColor(677,393, (115,105,96)):
        p.moveTo(610,393)
        p.click(610,393)
    if p.pixelMatchesColor(730,410, (224,136,74)):
        p.moveTo(730,410)
        p.click(730,410)
    # LEMONADE    
    if p.pixelMatchesColor(667,298, (115,105,96)):
        p.moveTo(610,298)
        p.click(610,298)
    if p.pixelMatchesColor(730,330, (224,136,74)):
        p.moveTo(730,330)
        p.click(730,330)
    
    # Popup tutorials
    while p.pixelMatchesColor(1191,205, (131,176,70)):
        p.moveTo(1249,198)
        p.click(1249,198)
        time.sleep(0.4)
    if p.pixelMatchesColor(1249,198, (224,139,78)):
        p.moveTo(1249,198)
        p.click(1249,198)
        time.sleep(0.4)

# Loops program
def run():
    global x
    while True:
        buy()
        time.sleep(x)

# Changes buy to MAX and then runs
def start():
    if p.pixelMatchesColor(1249,198, (224,139,78)):
        p.moveTo(1249,198)
        p.click(1249,198)
        time.sleep(0.4)
        start()
    else:
        run()
start()