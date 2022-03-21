from pyautogui import *
import pyautogui
import time

time.sleep(1)

print("Looking for accept button...")
btnclicked = False
lockbtnclicked = False

while lockbtnclicked == False:
    acceptButton = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\league_accept.png", confidence=0.8)
    championban = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\darius.png", confidence=0.8)
    clearban = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\banbtn.png", confidence=0.8)
    banButton = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\ban_btn.png", confidence=0.6)
    jglane = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\jungle.png", confidence=0.8)
    clearlock = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\clearlock.png", confidence=0.8)
    dianaselect = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\diana.png", confidence=0.8)
    mundoselect = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\mundo.png", confidence=0.8)
    lockbutton = pyautogui.locateOnScreen(r"D:\Eugene\Code\FromDesktop\lockin.png", confidence=0.8)
    pick = pyautogui.locateOnScreen(r"D:\Program Files\Python\Projects\pick.png", confidence=0.9)
    if acceptButton != None:
        pyautogui.click(acceptButton)
        print("Clicked")
    if clearban != None:
        pyautogui.click(championban)
        print("clicked")
        time.sleep(1)
        pyautogui.click(banButton)
        print("banned")
        lockbtnclicked = True
        
print("Clicked!")