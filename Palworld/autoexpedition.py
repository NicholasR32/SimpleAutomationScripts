# Script to automate deploying and claiming expeditions in Palworld.
# By NerdyBlocks, 1/13/2025
import pyautogui as pag
import time

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
expedition1 = (0.38*X,0.3*Y) # Cave in the Grassland
expedition2 = (0.38*X,0.4*Y) # Forest's Secret Realm
expedition3 = (0.38*X,0.5*Y) # Volcanic Inferno Cave
expedition4 = (0.38*X,0.6*Y) # Hidden Ruins of the Desert
expedition5 = (0.38*X,0.7*Y) # Frozen Cave of the Snow Mountain
expedition6 = (0.38*X,0.8*Y) # Spirit Blossom Cave of Sakurajima
# TODO: add scrolling so 7th exp can be selected

# NOTICE: Upon starting, this script assumes that a destination hasn't been chosen yet.
#         If a destination already says 'Enrolled' on it, the station will go straight to
#         the pal assigning window when opened. The extra click shouldn't matter.
expeditions_completed = 0
print('Script started')
while True:
    print('Waiting 3 seconds for window focus...')
    time.sleep(3)
    print('Pressing F to open expedition station')
    pag.press('f') # Palworld eats this first input for some reason
    pag.press('f')
    time.sleep(1)
    print('Selecting chosen expedition')
    pag.moveTo(*expedition5,1)
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
    # At this point, you should be standing on the expedition station w/ the window closed.

    # By default, the time for each expedition is 30 min for expeditions 1-2, 45 min for 3-4, and 60 min for 5-7.
    # Change this depending on your pals' total firepower, which can reduce the time required.
    # Example: The first expedition can take as low as 5 minutes w/ high-level pals, which is useful for testing.
    print('Waiting for expedition to finish...')
    expedition_time_minutes = 48
    time.sleep(expedition_time_minutes*60+10)
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
    print(f'Expeditions completed: {expeditions_completed}')

# # small thing to grab position of cursor
# try:
#     while True:
#         x,y = pag.position()
#         print(f'{x/X},{y/Y}')
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('\n')