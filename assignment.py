#!python3

import time
import pyautogui as p 

p.mouseInfo()

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
            p.click(1256,235)
            break

# Buys stuff
def buy():
    # Upgrades
    if p.pixelMatchesColor(347,450, (220,123,54)):
        upgrades()

    # Managers
    if p.pixelMatchesColor(347,520, (220,123,54)):
        managers()

    # All the stuff
    # Second line
    if p.pixelMatchesColor(1037,675, (115,105,96)):
        p.moveTo(1037,675)
        p.click(1037,296)
    if p.pixelMatchesColor(1100,710, (224,136,74)):
        p.moveTo(1100,700)
        p.click(1100,700)

    if p.pixelMatchesColor(1037,582, (115,105,96)):
        p.moveTo(1037,582)
        p.click(1037,582)
    if p.pixelMatchesColor(1100,610, (224,136,74)):
        p.moveTo(1100,610)
        p.click(1100,610)

    if p.pixelMatchesColor(1037,487, (115,105,96)):
        p.moveTo(1037,487)
        p.click(1037,487)
    if p.pixelMatchesColor(1100,510, (224,136,74)):
        p.moveTo(1100,510)
        p.click(1100,510)

    if p.pixelMatchesColor(1037,393, (115,105,96)):
        p.moveTo(1037,393)
        p.click(1037,393)
    if p.pixelMatchesColor(1100,410, (224,136,74)):
        p.moveTo(1100,410)
        p.click(1100,410)

    if p.pixelMatchesColor(1037,300, (115,105,96)):
        p.moveTo(1037,300)
        p.click(1037,300)
    if p.pixelMatchesColor(1100,330, (224,136,74)):
        p.moveTo(1100,330)
        p.click(1100,330)


    # First line
    if p.pixelMatchesColor(664,675, (115,105,96)):
        p.moveTo(610,675)
        p.click(610,296)
    if p.pixelMatchesColor(730,710, (224,136,74)):
        p.moveTo(730,710)
        p.click(730,710)

    if p.pixelMatchesColor(664,582, (115,105,96)):
        p.moveTo(610,582)
        p.click(610,582)
    if p.pixelMatchesColor(730,610, (224,136,74)):
        p.moveTo(730,610)
        p.click(730,610)

    if p.pixelMatchesColor(664,487, (115,105,96)):
        p.moveTo(610,487)
        p.click(610,487)
    if p.pixelMatchesColor(730,510, (224,136,74)):
        p.moveTo(730,510)
        p.click(730,510)

    if p.pixelMatchesColor(664,393, (115,105,96)):
        p.moveTo(610,393)
        p.click(610,393)
    if p.pixelMatchesColor(730,410, (224,136,74)):
        p.moveTo(730,410)
        p.click(730,410)

    if p.pixelMatchesColor(664,300, (115,105,96)):
        p.moveTo(610,300)
        p.click(610,300)
    if p.pixelMatchesColor(730,330, (224,136,74)):
        p.moveTo(730,330)
        p.click(730,330)

# Loops program
def run():
    while True:
        buy()
        time.sleep(15)

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