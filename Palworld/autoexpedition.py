# Script to automate deploying and claiming expeditions in Palworld.
# By NerdyBlocks, 1/13/2025
import pyautogui as pag
import time


if __name__ == '__main__':
    # Get your screen's resolution.
    resolution = pag.size()
    X = resolution[0]
    Y = resolution[1]

    # The position of each button as a percentage of your screen's X and Y.
    auto_assign_button_pos = (0.275*X,0.83*Y)
    start_button_pos = (0.5*X,0.83*Y)
    collect_button_pos = (0.8*X,0.197*Y)

    # Positions of each expedition destination button.
    # Conveniently, each button takes about 10% of the screen's height.
    exp_buttons = [
                  [0.37*X,0.3*Y], # Cave in the Grassland
                  [0.37*X,0.4*Y], # Forest's Secret Realm
                  [0.37*X,0.5*Y], # Volcanic Inferno Cave
                  [0.37*X,0.6*Y], # Hidden Ruins of the Desert
                  [0.37*X,0.7*Y], # Frozen Cave of the Snow Mountain
                  [0.37*X,0.8*Y]  # Spirit Blossom Cave of Sakurajima
                ]
    # TODO: add scrolling so 7th exp can be selected
    # NOTICE: Upon starting, this script assumes that a destination hasn't been chosen yet.
    #         If a destination already says 'Enrolled' on it, the station will go straight to
    #         the pal assigning window when opened. The extra click shouldn't matter.
    expeditions_completed = 0
    print('Script started')
    exp_id = int(input('Which expedition are you running? 1 = Cave in the Grassland, 2 = Forest\'s Secret Realm, etc.\n'))
    exp_time = int(input('Click Auto-Assign. How long will it take, in minutes?\n'))
    in_progress = input('Is an expedition already in progress? [Y/N]\n')
    if in_progress in ['Y','y']:
        time_to_wait = int(input('How much longer, in minutes? Round up to nearest minute.\n'))
        print('Script activated! Please make sure Palworld is focused when the timer ends.')
        time.sleep(time_to_wait*60+10)
        print('Expedition done!')
        expeditions_completed += 1
        # Reopen station
        print('Pressing F to open expedition station')
        pag.press('f')
        pag.press('f')
        time.sleep(1)
        print('Pressing button to collect rewards')
        pag.moveTo(*collect_button_pos,1)
        pag.click()
        time.sleep(1)
        print('Exiting expedition window')
        pag.press('esc')
        time.sleep(1)
        expeditions_completed+=1
        print(f'Expeditions completed: {expeditions_completed}')
        print('Now entering full AFK expedition loop.')

    while True:
        print('Please refocus on Palworld.')
        print('Waiting 3 seconds for window focus...')
        time.sleep(3)
        print('Pressing F to open expedition station')
        pag.press('f') # Palworld eats this first input for some reason
        pag.press('f')
        time.sleep(3)
        print('Selecting chosen expedition')
        pag.moveTo(*exp_buttons[exp_id-1],1)
        pag.click()
        time.sleep(1)
        print('Pressing Auto-Assign button')
        pag.moveTo(*auto_assign_button_pos, 1)
        pag.click()
        time.sleep(3)
        print('Pressing Start button')
        pag.moveTo(*start_button_pos, 1)
        pag.click()
        time.sleep(1)
        print('Expedition started! It is safe to use your mouse and keyboard while it finishes.\n')
        if expeditions_completed < 2:
            print('NOTE: Please make sure the right expedition was selected. You may have to manually enroll in the correct one beforehand.\n')
        # By default, the time for each expedition is 30 min for expeditions 1-2, 45 min for 3-4, and 60 min for 5-7.
        # Change this depending on your pals' total firepower, which can reduce the time required.
        # Example: The first expedition can take as low as 5 minutes w/ high-level pals, which is useful for testing.
        print('Waiting for expedition to finish...')
        print('Please ensure Palworld is focused and you are in the correct position when the expedition timer ends.\n')
        time.sleep(exp_time*60+10)
        # It is safe to use your computer during this waiting phase,
        # just ensure Palworld is focused and the expedition station is in range when the timer ends.
        print('Expedition done!')

        # Reopen station
        print('Pressing F to open expedition station')
        pag.press('f')
        pag.press('f')
        time.sleep(1)
        print('Pressing button to collect rewards')
        pag.moveTo(*collect_button_pos,1)
        pag.click()
        time.sleep(1)
        print('Exiting expedition window')
        pag.press('esc')
        time.sleep(1)
        expeditions_completed+=1
        print(f'Expeditions completed: {expeditions_completed}\n')
