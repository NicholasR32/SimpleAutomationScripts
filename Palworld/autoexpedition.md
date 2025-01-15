#### How to automate expeditions when AFK:
1. Installing stuff for the script to work
    1. Install [Python](https://www.python.org/downloads/). This also installs pip, Python's package manager.
    2. Open Command Prompt or whatever terminal you prefer.
    3. Run `pip install pyautogui`. This package allows the script to control your mouse and keyboard.
2. Playing Palworld (the fun part!)
    1. Assuming you are in game, stand in front of the expedition station so you can interact with it, but don't open the station's interface.
3. Running the script
    1. Download `autoexpedition.py` and move it to a directory of your choice.
    2. If you open the script in an IDE or text editor with a running feature, you can use that.
    3. Otherwise, to run the script in the terminal, [navigate](https://linuxblog.io/navigating-the-linux-file-system-with-the-cd-command/) to the directory where you put the script.
    4. Run the script with `python autoexpedition.py` or through your IDE.
    5. In the terminal, it will ask :
        1. How long the expedition will take (which depends on the difficulty level and your pals), and 
        2. Whether an expedition is currently in progress, since you'll have to wait that one out first.
    6. Enter in answers so the script can account for those situations.
    7. Done! It should be fine to leave your computer, and the script will automatically claim and deploy new expeditions when the timer finishes. It is safe to use your mouse and keyboard while it is running, just ensure that Palworld is focused again when the timer finishes so the clicks register. Otherwise, you'll have to rerun the script.