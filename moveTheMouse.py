#! python3
# 移动鼠标，将鼠标订到左上角抛出异常，也能结束程序

import pyautogui,time
screenWidth, screenHeight = pyautogui.size()  # 获取屏幕大小

x_move = 3

# 这段是整个屏幕移动

"""
try:  # 捕获Ctrl c 产生的异常
    while True:
    # for i in range(40):  # 用于测试
        p = pyautogui.position()  # 获取当前鼠标的位置
        if p[0] > screenWidth - 50 or p[0] < 50:
            x_move = -x_move  # 鼠标转向
        pyautogui.moveRel(x_move,0,duration=0.2)
        time.sleep(10)
except KeyboardInterrupt:
    print('Done!')
"""

try:  # 捕获Ctrl c 产生的异常
    while True:
        pyautogui.moveRel(x_move,0,duration=0.2)
        x_move = -x_move  # 鼠标转向，让他在左右很小的范围内移动
        time.sleep(10)
except KeyboardInterrupt:
    print('Done!')
