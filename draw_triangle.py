# 画三角形
# 时常自己动手做些小东西，添加一些乐趣，和古人有空做做诗是一样的

import pyautogui, time

time.sleep(4)

distance = 100

x,y = pyautogui.position()  # 获取当前鼠标的值

while distance > 0:
    pyautogui.dragRel(distance,distance,duration=0.2)  # 向右下画
    distance -= 5
    pyautogui.dragRel(-2*distance,0,duration=0.2)  # 向左
    distance -=5
    pyautogui.dragRel(distance,-distance,duration=0.2)  # 向上
    distance -=10

