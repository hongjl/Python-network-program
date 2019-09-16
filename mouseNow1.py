#! python3

import pyautogui

print('press ctrl-c to quit.')

try:
    while True:
        x,y = pyautogui.position()
        position = 'X:'+str(x).rjust(4)+' Y:'+str(y).rjust(4)
        print(position,end='')
        print('\b'*len(position),end='')
except KeyboardInterrupt:
    print('have done.')
