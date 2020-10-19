#!python3

import time
import pyautogui as p 

p.mouseInfo()

def run():
    p.moveTo(980,675)
    if p.pixelMatchesColor(1100,700, (220,123,54)):
        p.click(1100,700)

    p.moveTo(980,580)
    if p.pixelMatchesColor(1100,, (220,123,54)):
        p.click(1100,)

    p.moveTo(980,490)
    if p.pixelMatchesColor(1100,, (220,123,54)):
        p.click(1100,)

    p.moveTo(980,410)
    if p.pixelMatchesColor(1100,, (220,123,54)):
        p.click(1100,)

    p.moveTo(980,296)
    if p.pixelMatchesColor(1100,, (220,123,54)):
        p.click(1100,)


    p.moveTo(610,675)
    if p.pixelMatchesColor(730,710, (220,123,54)):
        p.click(730,710)

    p.moveTo(610,580)
    if p.pixelMatchesColor(730,610, (220,123,54)):
        p.click(730,610)

    p.moveTo(610,490)
    if p.pixelMatchesColor(730,510, (220,123,54)):
        p.click(730,510)

    p.moveTo(610,410)
    if p.pixelMatchesColor(730,410, (220,123,54)):
        p.click(730,410)

    p.moveTo(610,296)
    if p.pixelMatchesColor(730,330, (220,123,54)):
        p.click(730,330)

run()