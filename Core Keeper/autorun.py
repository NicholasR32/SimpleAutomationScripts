# Really simple script to automate running back and forth
# for running xp in Core Keeper (pre update 1.0)
import pyautogui, time

time.sleep(3)

while True:
    with pyautogui.hold('left'):
        pyautogui.sleep(1)

    with pyautogui.hold('right'):
        pyautogui.sleep(1)