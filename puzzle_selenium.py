from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from ejer07_puzzlev2 import *
import time

driver = webdriver.Chrome('driver/chromedriver.exe')
wait_page = WebDriverWait(driver, 100)
driver.maximize_window()

driver.get('http://www.artbylogic.com/puzzles/numSlider/numberShuffle.htm?rows=3&cols=3&sqr=1')

time.sleep(3)
elem = []
puzzles_values = driver.find_elements_by_class_name('dragWrapper')

convert = dict()
convert["left: 0px; top: 0px;"] = 1
convert["left: 79px; top: 0px;"] = 2
convert["left: 158px; top: 0px;"] = 3
convert["left: 0px; top: 84px;"] = 4
convert["left: 79px; top: 84px;"] = 5
convert["left: 158px; top: 84px;"] = 6
convert["left: 0px; top: 168px;"] = 7
convert["left: 79px; top: 168px;"] = 8
convert["left: 158px; top: 168px;"] = 9

convert["block0_0"] = 1
convert["block0_1"] = 2
convert["block0_2"] = 3
convert["block1_0"] = 4
convert["block1_1"] = 5
convert["block1_2"] = 6
convert["block2_0"] = 7
convert["block2_1"] = 8

reverse_convert = dict()
reverse_convert['1'] = "block0_0"
reverse_convert['2'] = "block0_1"
reverse_convert['3'] = "block0_2"
reverse_convert['4'] = "block1_0"
reverse_convert['5'] = "block1_1"
reverse_convert['6'] = "block1_2"
reverse_convert['7'] = "block2_0"
reverse_convert['8'] = "block2_1"

numbers = dict()

for elem in puzzles_values:
    id = elem.get_attribute('id')
    style = elem.get_attribute('style')
    try:
        position = convert[style]
        value = convert[id]
        numbers[position] = str(value)
        print(numbers[position])
        #print(position, value, style, id)
    except:
        print(style, id)
        print("except")
        continue

for i in range(8):
    position = i + 1
    if position not in numbers:
        numbers[position] = "e"

INITIAL = numbers[1] + "-" + numbers[2] + "-" + numbers[3] + "\n" + numbers[4] + "-" + numbers[5] + "-" + numbers[6] + "\n" + numbers[7] + "-" + numbers[8] + "-" + numbers[9]

print('INICIAL: ', INITIAL)

'''result = astar(EigthPuzzleProblem(INITIAL))

actions = []
for action, state in result.path():
    if action is not None:
        print('Mover número: ', action)
        print('Mover elemento: ', reverse_convert[action])
        actions.append(reverse_convert[action])
        print(state)

# MOVE PIECES
counter = 0
print(len(actions))
while counter < len(actions):
    print(counter, actions[counter])
    driver.find_element_by_id(actions[counter]).click()
    time.sleep(2)
    counter += 1

print(actions)
print(len(actions))'''
