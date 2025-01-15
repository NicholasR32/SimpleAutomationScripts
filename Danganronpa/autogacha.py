# Script to automate buying gift prizes from the gachapon machine in Danganronpa 1.
import pyautogui
import time

# Number of repetitions
iterations = 100

# Loop 100 times
for i in range(iterations):
    print(f"Iteration {i+1}/{iterations}")

    # Deposit Monocoins
    for j in range(100):
        pyautogui.press('s')
    # Spin
    pyautogui.click()
    # Wait for prize animation to play out
    time.sleep(5)

print("Task completed!")