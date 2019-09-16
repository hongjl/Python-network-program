#! python3
# countdown.py - asimple countdown script.

import time, subprocess

timeLeft = 6

while timeLeft > 0:
    print(timeLeft,end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# at the end of the countdown,play a sound file
subprocess.Popen(['start','C:\\MyPythonScripts\\alarm.wav'],shell=True)
