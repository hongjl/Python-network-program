#! python3
'''
Mymcb save <key-word>
Mymcb list
Mymcb <key-word>
Mymcb delete <key-word>
'''

import sys, pyperclip, shelve

mymcb = shelve.open('mymcb')  # 创建shelve文件

if len(sys.argv) == 3:
    if sys.argv[1] == 'save':
        mymcb[sys.argv[2]] = pyperclip.paste()  # 从剪切板获取内容
        
    elif sys.argv[1] == 'delete':  # 删除对应的值
        if sys.argv[2] in mymcb:
            del mymcb[sys.argv[2]]
            pyperclip.copy('have delete {}'.format(sys.argv[2]))
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(mymcb.keys())))  # 将所有键的值复制到剪贴板中
    elif sys.argv[1] in mymcb:  # 判断mymcb中是否有这键
        pyperclip.copy(mymcb[sys.argv[1]])
        
