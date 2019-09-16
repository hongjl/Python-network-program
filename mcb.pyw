#! python3

# pyw mcb.py save <key-word> 按关键字将剪贴板的内容保存
# pyw mcb.py <key-word> 将关键字对应的内容放到剪贴板中
# pyw mcb.py list 列出所有关键字

import shelve, sys, pyperclip
# shelve用来保存字典，启动文件就能够读取内容
# sys 用来sys.argv
# pyperclip 用来获取剪贴板的内容和修改剪贴板的内容

mcbshelf = shelve.open('mcb')  # 创建shelf文件

'''
if sys.argv[1].lower == 'save':  # 可处理大小写
    # 按关键字将剪贴板的内容保存
    shelfFile[sys.argv[2]] = pyperclip.paste()

elif sys.argv[1].lower() == 'list':
    # 列出所有关键字
    # for keyname in shelfFile['data']:  遍历字典的键
    pyperclip.copy(shelfFile.keys())  # 将所有关键字存放到剪切板中

else:
    # 将关键字对应的内容放到剪贴板中
    pyperclip.copy(shelfFile[sys.argv[1]])

'''
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
    
mcbshelf.close()



def Mymcb(argv,keyname = None):
    mcbshelf = shelve.open('mcb')  # 创建shelf文件

    if keyname != None and argv.lower() == 'save':
        mcbshelf[keyname] = pyperclip.paste()
    elif keyname == None:
        if argv.lower() == 'list':
            pyperclip.copy(str(list(mcbshelf.keys())))
        elif argv in mcbshelf:
            pyperclip.copy(mcbshelf[argv])
        
    mcbshelf.close()





























