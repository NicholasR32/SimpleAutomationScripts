# Script to automate deploying and claiming expeditions in Palworld.
# By NerdyBlocks, 1/13/2025
import pyautogui as pag
import time

# Convert a time in format MM:SS to seconds.
def to_seconds(duration):
    clock = duration.split(':')
    return int(clock[0]) * 60 + int(clock[1])

def claim_expedition(claim_button_pos):
    # Open station
    print('Pressing F to open expedition station')
    pag.press('f')
    pag.press('f')
    time.sleep(1)
    print('Pressing button to collect rewards')
    pag.moveTo(*claim_button_pos,1)
    pag.click()
    time.sleep(1)
    print('Exiting expedition window')
    pag.press('esc')
    time.sleep(1)

def deploy_expedition(exp_button_pos, auto_assign_button_pos, start_button_pos):
    print('Pressing F to open expedition station')
    pag.press('f') # Palworld eats this first input for some reason
    pag.press('f')
    time.sleep(3)
    print('Selecting chosen expedition')
    pag.moveTo(*exp_button_pos,1)
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

def wait_expedition(time_to_wait):
    print(f'Waiting {time_to_wait // 60} minute(s) {time_to_wait % 60} seconds')
    time.sleep(time_to_wait)
    # while time_to_wait > 0:
    #     wait = min(time_to_wait, 600) # Print status every 10 minutesff
    #     print(f'{time_to_wait // 60}:{time_to_wait % 60} left')
    #     time.sleep(wait)
    #     time_to_wait -= wait
    print(f'Waiting an extra 10 seconds...')
    time.sleep(10)


if __name__ == '__main__':
    # Get your screen's resolution.
    resolution = pag.size()
    X = resolution[0]
    Y = resolution[1]

    # The position of each button as a percentage of your screen's X and Y.
    auto_assign_button_pos = (0.275*X,0.83*Y)
    start_button_pos = (0.5*X,0.83*Y)
    claim_button_pos = (0.8*X,0.197*Y)

    # Positions of each expedition destination button.
    # Conveniently, each button takes about 10% of the screen's height.
    exp_buttons = [
                  [0.35*X,0.3*Y], # Cave in the Grassland
                  [0.35*X,0.4*Y], # Forest's Secret Realm
                  [0.35*X,0.5*Y], # Volcanic Inferno Cave
                  [0.35*X,0.6*Y], # Hidden Ruins of the Desert
                  [0.35*X,0.7*Y], # Frozen Cave of the Snow Mountain
                  [0.35*X,0.8*Y]  # Spirit Blossom Cave of Sakurajima
                  ]
    # TODO: add scrolling so 7th exp can be selected
    # NOTICE: Upon starting, this script assumes that a destination hasn't been chosen yet.
    #         If a destination already says 'Enrolled' on it, the station will go straight to
    #         the pal assigning window when opened. The extra click shouldn't matter.
    expeditions_completed = 0
    exp_id = int(input('Which expedition are you running? 1 = Cave in the Grassland, 2 = Forest\'s Secret Realm, etc.\n'))
    exp_time_raw = input('Click Auto-Assign. How long will it take? Enter in format MM:SS. (Example: 48:30 = 48 minutes 30 seconds.)\n')
    exp_time = to_seconds(exp_time_raw)

    in_progress = input('Is an expedition already in progress? [Y/N]\n')
    if in_progress in ['Y','y']:
        duration_raw = input('How much longer, in minutes? Enter in format MM:SS.\n')
        duration = to_seconds(duration_raw)

        print('Script activated! Please make sure Palworld is focused when the timer ends.')
        wait_expedition(duration)

        print('Expedition done!')
        expeditions_completed += 1
        claim_expedition(claim_button_pos)
        print(f'Expeditions completed: {expeditions_completed}')
        print('Now entering full AFK expedition loop.')

    while True:
        print('Please refocus on Palworld.')
        print('Waiting 3 seconds for window focus...')
        time.sleep(3)
        deploy_expedition(exp_buttons[exp_id-1],auto_assign_button_pos,start_button_pos)
        print('Expedition started! It is safe to use your mouse and keyboard while it finishes.\n')

        if expeditions_completed < 1:
            print('NOTE: Please make sure the right expedition was selected. You may have to manually enroll in the correct one beforehand.\n')

        print('Waiting for expedition to finish...')
        print('Please ensure Palworld is focused and you are in the correct position when the expedition timer ends.\n')
        wait_expedition(exp_time)

        print('Expedition done!')
        claim_expedition(claim_button_pos)
        expeditions_completed+=1
        print(f'Expeditions completed: {expeditions_completed}\n')

