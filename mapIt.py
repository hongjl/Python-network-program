#! python3
# mapIt.py - lauches a map in the brower using an address from the
# command line or clipboard

import webbrowser, sys, pyperclip

"""
if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])  # 取后几个参数
else:
    # get address from clipboard.
    address = pyperclip.paste()  # 从剪贴板中获得地址

webbrowser.open('https://map.baidu.com/'+address)
"""
def mapIt(address):
    webbrowser.open('https://map.baidu.com/search/'+address)
