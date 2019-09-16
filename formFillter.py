#! python3
# formFillter.py - automatically fills in the form.

import pyautogui, time

# set these to the correct coordinates坐标 for your computer.
nameFiled = (1212,430)
submitButton = (1261,619)
submitButtonColor = (106,162,224)

submitAnotherLink = (760,224)

formdata = [{'name':'hong','acount':'1234567','passowrd':'pppppp'},
            {'name':'fend','acount':'1234567','passowrd':'pppppp'},
            {'name':'yan','acount':'1234567','passowrd':'pppppp'}]

pyautogui.PAUSE = 0.5  # 在每次函数调用后等待半秒钟

for person in formdata:
    # give the user a chance to kill the script
    print('>>> 5 second pause to let user press ctrl-c <<<')
    time.sleep(5)

    # wait until the form page has loaded.
    while not pyautogui.pixelMatchsColor(submitButton[0], submitButton[1],submiButtonColor):
        time.sleep(0.5)

    print('enter %s info...' % (person['name']))
    pyautogui.click(nameField[0],nameField[1])

    # fill out the name field
    pyautogui.typewrite(person['name'] + '\t')  # \t模拟tab键

    # fill out the greatest fears field.
    pyautogui.typewrite(person['fear' + '\t'])

    # 处理选择列表和单选按钮
    if person['source'] == 'wand':
        pyautogui.typewrite(['down','\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down','down','\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down','down','down','\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down','down','down','down','\t'])

    if person['robocop'] == 1:
        pyautogui.typewrite([' ','\t'])  # 空格键，选择第一个
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right','\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right','right','\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right','right','right','\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right','right','right','right','\t'])

    # 提交表单并等待
    pyautogui.typewrite(person['comments'] + '\t')

    # clich submit
    pyautogui.press('enter')  # 按下回车键，提交表单

    # wait until form page has loaded
    print('clicked subit.')
    time.sleep(5)

    # click the submit another response link.
    pyautogui.click(submiAnotherLink[0],submitAnotherLink[1])

    

