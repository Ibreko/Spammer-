import time, pyautogui, keyboard

time.sleep(5)
text = open('text_spammer.txt', 'r')

for line in text:
    if not keyboard.is_pressed('space'):
        pyautogui.typewrite(line)
        pyautogui.press('enter')
    else:
        break


