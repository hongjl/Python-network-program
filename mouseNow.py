#! python3

# 获得鼠标的位置
import pyautogui

print('Ctrl-c to quit the program.')


try:
    while True:
        x,y = pyautogui.position()  # 获得鼠标位置
        position = 'X:'+str(x).rjust(4)+' \tY:'+str(y).rjust(4)
        pixelColor = pyautogui.screenshot().getpixel((x,y))
        position += ' RGB: (' + str(pixelColor[0]).rjust(3)
        position += ','+str(pixelColor[1]).rjust(3)
        position += ','+str(pixelColor[2]).rjust(3)+')'
        print(position,end='')
        print('\b'*len(position),end='',flush=True)  # 檫除之前的数据
except KeyboardInterrupt:
    print('\nDone')
