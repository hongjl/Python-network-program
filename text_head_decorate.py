#! python3
# text_head_decorate.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

"""
asdlkfsldf
aksjdflsjdf
lakdfksdf
* asdlkfsldf
* aksjdflsjdf
* lakdfksdf
"""

import pyperclip

# 用于修饰剪贴板文本
def text_head_decorate(pattern='*'):  # 设置它的默认值
    text = pyperclip.paste()  # 从剪贴板上获取内容
    next_text = []

    for line in text.split('\n'):  # 分开每一行,split会返回一个列表
        next_text.append( pattern+ line)  # 在行首加上一些符号

    pyperclip.copy('\n'.join(next_text))


if __name__ == '__main__':
    text_head_decorate('#')