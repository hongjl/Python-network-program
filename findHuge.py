#! python3

"""
删除不需要的文件
编写一个程序，遍历一个目录树，查找特别大的文件或文件夹，比方说，超过100MB的文件
os.path.getsize()
将这些文件的绝对路径打印到屏幕上
"""
import os


def findHuge(path,size,delete=False):
    # 获取绝对路径
    abspath = os.path.abspath(path)

    # os.walk  循环遍历,判断大小打印出文件的绝对路径
    for folder, subfolders, filenames in os.walk(abspath):
        for file in filenames:
            filepath = os.path.join(abspath,file)
            if os.path.getsize(filepath) < size:
                continue
            print(filepath)  # 绝对路径
            if delete == False:
                continue
            # delete若为True,注释两种删除，一种直接删除，2放到回收站中
            # os.unlink(filepath)  # 删除文件
            # import send2trash  # 丢到回收站中
            # send2trash.send2trash(filepath)

    

  
