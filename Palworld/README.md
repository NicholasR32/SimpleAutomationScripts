#### How to automate expeditions when AFK:
1. **Install stuff for the script to work**
    1. Install [Python](https://www.python.org/downloads/). This also installs pip, Python's package manager.
    2. Open Command Prompt or any terminal.
    3. Run `pip install pyautogui`. This package allows the script to control your mouse and keyboard.
2. **Play Palworld (the fun part!)**
    1. Enter a world and go to your base.
    2. Choose an expedition, and see how long it takes when you Auto-Assign. Note this time for later. Then cancel the expedition.
    3. Stand in front of the expedition station so you can interact with it, but don't open the station's interface.
3. **Run the script**
    1. Download `autoexpedition.py`.
    2. Assuming the file is in your Downloads folder, run `cd Downloads` to navigate to that folder, so the script can be accessed. (cd = change directory)
    3. Run the script with `python autoexpedition.py`.
    4. In the terminal, it will ask :
        1. Which expedition you are running (so it knows which button to click)
        2. How long the expedition will take (which depends on the difficulty level and your pals), and 
        3. Whether an expedition is currently in progress, since you'll have to wait for that one to finish first.
    5. Answer these prompts in the terminal so the script can account for those situations.
    6. Done! It should be fine to leave your computer, and the script will automatically claim and deploy new expeditions when the timer finishes. It is safe to use your mouse and keyboard while it is running, just ensure that Palworld is focused again when the timer finishes so the clicks reach the game properly. Otherwise, you'll have to rerun the script.
4. **Making sure it works**
    1. Before AFKing on a long 1-hour expedition, I highly recommend testing it with the first expedition, which can take as low as 5 minutes with level 30+ pals. Repeat the steps above with the first expedition, making sure to input how long it will take when you auto-assign.
    2. Once it finishes, verify that the script uses your mouse to claim the rewards and then deploy another one.
    3. If it works, you can AFK with a longer expedition. If it doesn't, please reach out to me with any issues.