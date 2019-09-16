#! python3
# per10second

'''
每个10秒稍微动一下鼠标
'''
import pyautogui, datetime

location = 50
threeSecond = datetime.timedelta(seconds=3)
print('每个10秒稍微动一下鼠标,ctrl-c结束.')
try:
    now = datetime.datetime.now()
    while True:
        if now + threeSecond < datetime.datetime.now():  # 当过了3秒时
            pyautogui.moveRel(location,0,duration=0.2)  # 移动鼠标
            location = -location
            now = datetime.datetime.now()
            
            
        
except KeyboardInterrupt:  # 捕获ctrl-c产生的异常
    print('Done.')
