#!python3

import time
import pyautogui as p 

p.mouseInfo()

def run():
    # Upgrades
    if p.pixelMatchesColor(347,450, (220,123,54)):
        p.moveTo(347,450)
        p.click(347,450)
        while True:
            if p.pixelMatchesColor(1060,590, (224,136,74)):
                p.moveTo(1060,590)
                p.click(1060,590)

    # Managers
    if p.pixelMatchesColor(347,520, (220,123,54)):
        p.moveTo(347,520)
        p.click(347,520)

    p.moveTo(980,675)
    if p.pixelMatchesColor(1100,710, (224,136,74)):
        p.moveTo(1100,700)
        p.click(1100,700)

    p.moveTo(980,580)
    if p.pixelMatchesColor(1100,610, (224,136,74)):
        p.moveTo(1100,610)
        p.click(1100,610)

    p.moveTo(980,490)
    if p.pixelMatchesColor(1100,510, (224,136,74)):
        p.moveTo(1100,510)
        p.click(1100,510)

    p.moveTo(980,410)
    if p.pixelMatchesColor(1100,410, (224,136,74)):
        p.moveTo(1100,410)
        p.click(1100,410)

    p.moveTo(980,296)
    if p.pixelMatchesColor(1100,330, (224,136,74)):
        p.moveTo(1100,330)
        p.click(1100,330)


    p.moveTo(610,675)
    if p.pixelMatchesColor(730,710, (224,136,74)):
        p.moveTo(730,710)
        p.click(730,710)

    p.moveTo(610,580)
    if p.pixelMatchesColor(730,610, (224,136,74)):
        p.moveTo(730,610)
        p.click(730,610)

    p.moveTo(610,490)
    if p.pixelMatchesColor(730,510, (224,136,74)):
        p.moveTo(730,510)
        p.click(730,510)

    p.moveTo(610,410)
    if p.pixelMatchesColor(730,410, (224,136,74)):
        p.moveTo(730,410)
        p.click(730,410)

    p.moveTo(610,296)
    if p.pixelMatchesColor(730,330, (224,136,74)):
        p.moveTo(730,330)
        p.click(730,330)

run()