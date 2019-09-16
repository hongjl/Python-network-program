import pyautogui, time
time.sleep(3)

pyautogui.click()
distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, duration=0.2)  # move right
    distance = distance -10
    pyautogui.dragRel(0, distance, duration=0.2)  # move down
    pyautogui.dragRel(-distance,0,duration=0.2)  # move left
    distance = distance - 10
    pyautogui.dragRel(0,-distance,duration=0.2)  # move up

print('Done!')
