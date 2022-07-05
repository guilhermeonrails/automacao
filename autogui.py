import pyautogui 
from time import sleep

sleep(2)
# print(pyautogui.position())
pyautogui.moveTo(33, 37)
sleep(1)
pyautogui.click()
sleep(1)
pyautogui.click(1268, 10)
sleep(1)
pyautogui.write('visual', interval=0.5)
sleep(1)
pyautogui.press('enter')
sleep(1)