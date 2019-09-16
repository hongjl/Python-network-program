#! python3
"""
选择性拷贝
编写一个程序，遍历一个目录树，查找特定扩展名的文件(诸如.pdf或.jpg)
不论这些文件的位置在哪里，将它们拷贝到一个新的文件夹中
"""

import shutil, os, re  # shutil用于移动，复制文件

def copySomething(path, fileType = None,despath=None):  # path 哪里的目录，fileType什么类型的文件
    # 获得绝对路径
    abspath = os.path.abspath(path)
    if despath == None:
        despath = 'C:\\MyPythonScripts\\something'
    

    # 默认拷贝.txt文件，使用os.walk，以及循环
    if fileType == None:
        fileType = ['txt']  # 一个列表，表示可以查找多种类型的文件
        
    fileRegex = re.compile(r'(.*?)\.({})$'.format('|'.join(fileType)))

    for folder, subfolders, filenames in os.walk(abspath):
        
        for file in filenames:
            if fileRegex.search(file) == None:  # 跳过不合适的文件
                continue
            shutil.copy(os.path.join(abspath,file),despath)  # 复制到指定目录
            print(os.path.join(abspath,file),'->',despath)
            
    
   

