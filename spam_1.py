import time, pyautogui, keyboard

time.sleep(5)
text = open('text_spammer.txt', 'r')
for line in text:
    time.sleep(50)
    if not keyboard.is_pressed('space'):
        pyautogui.typewrite(line)
        time.sleep(50)
        pyautogui.press('enter')
    else:
        break

