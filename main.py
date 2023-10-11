import pyautogui, time

file = open("send.txt", "r")
for word in file:
    pyautogui.typewrite(word)
    time.sleep(2)
    pyautogui.press("enter")