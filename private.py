import pyautogui
import time
import pyperclip

x, y = 2225, 2022  #Using ShareX is a good way to know coordinates.
time.sleep(1)

repetitions = 500  # Change this to None for an infinite loop

delay = 61
def send_heart():
    pyautogui.click(2136,34)
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.click(2448,34)
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.click(2749,34)
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.click(3025,34)
    pyautogui.press("3")
    pyautogui.press("3")
    pyautogui.press("3")
    return None

#LOOP!
count = 0
while count < repetitions:
    text = "오프라인 광고를 혁신하는 카멜레온입니다! \n궁금한점 있으시면 바로 문의해주세요‼️\n후기 남겨주세요~~🔥⭐❣️😁\n후기는 저희에게 큰 힘이 됩니다🔥🔥🔥\n\nhttps://www.chamelneon.net/"
    send_heart()
    pyautogui.click(3347,34)
    pyperclip.copy(text)  #to ensure reload clipboard
    pyautogui.click(x, y)  #Click!
    pyautogui.hotkey("ctrl", "v")  #Paste!
    pyautogui.press("enter")  #Send!
    for i in range(12):
        time.sleep(5)       #Wait counter to know when it loops
        print(60-5*i)
    count += 1

print("Over!")
