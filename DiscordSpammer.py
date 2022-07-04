import pyautogui
import webbrowser
import time

message = input("spam message : ")
repeats = int(input("number : "))
delay = int(input("wait time : "))

isLoaded = input("press enter")


print("5 seconds before spam starts")

time.sleep(5)

for i in range (0,repeats):
    if message !="":
      pyautogui.typewrite(message)
      pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

    time.sleep(delay/1000)

print("  Done")