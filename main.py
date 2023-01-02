import pyautogui
import time

print("It works")

def SendMessage():
    message = input("Input your message")
    amount = int(input("Inout your numbers of spam"))
    time.sleep(6)

    for i in range(amount):
        pass

    while amount > 0:
        amount-=1

        pyautogui.typewrite(message.strip())
        pyautogui.press("enter")

SendMessage()