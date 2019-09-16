#! python3

# myfind - 编写一个程序，打开文件夹中所有的.txt文件，
# 查找匹配用户提供的正则表达式的所有行，将结果打印到屏幕

import os, re

userRegex = re.compile(r'\d{7,}')

for filename in os.listdir('.'):  # 列出当前目录所有文件
    if filename.endswith('.txt'):  # 找出.txt文件
        file = open(filename)  # 打开文件
        flag = False  # 用于显示文件名
        for line in file.readlines():  # 遍历每一行
            if userRegex.search(line) is not None:
                if flag == False:  # 该文件第一次有匹配上
                    print('-'*10+filename+'-'*10)
                    flag = True
                print(line)  # 在屏幕上打印符合的语句
        file.close()  # 安全关闭文件
