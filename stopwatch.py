#! python3
# stopwatch.py - a simple stopwatch program

import time, pyperclip

# display the program's instructions
print('''press enter to begin.afterwards,press enter to "click" the stopwatch.
      press Ctrl-C to quit.''')

input()  # press enter to begin
print('started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1  # 计算多少段时间

# 这里以写方式创建一个，这样每次都会只保存新的内容
with open('stopwatch.txt','w') as f:
    f.write('------------time message------------\n')


# start tracking the lap times.
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - startTime,2)
        timemesg = 'lap #{:>4}: {:>6} ({:>4}) '.format(lapNum, totalTime,lapTime)

        with open('stopwatch.txt','a') as f:  # 将内容写到文件中去
            f.write(timemesg+'\n')
            
        print(timemesg,end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # handle the ctrl-c exception to keep its error message from displaying.
    with open('stopwatch.txt','r') as f:  # 将文件内容写到剪贴板上
        pyperclip.copy(f.read())  # 复制
    print('\nDone.')
