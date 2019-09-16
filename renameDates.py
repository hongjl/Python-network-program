#! python3
# renameDates.py - renames filenames with american mm-dd-yyyy date format
# to european dd-mm-yyyy.

import shutil, os, re

# create a regex that matches files with the american date format.
datePattern = re.compile(r"""^(.*?)  # 文件名前面一些字符
        ((0|1)?\d)-  # 匹配月份
        ((0|1|2|3)?\d)-  # 匹配日期
        ((19|20)\d\d)
        (.*?)$  # 非贪心匹配
        """,re.VERBOSE)

# loop over the files in the working directory
for amerFilename in os.listdir('.'):  # 获取当前目录的所有文件
    mo = datePattern.search(amerFilename)
    
    # skip files without a date.
    if mo == None:  # 跳过不匹配的文件
        continue
    # get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # form the european-style filename
    euroFilename = beforePart + dayPart + '-'+monthPart + '-'+yearPart + afterPart  # 将不同部分重新编排

    # get the full, absolte file paths.
    absWorkingDir = os.path.abspath('.')  # 获得当前目录的绝对路径
    amerFilename = os.path.join(absWorkingDir,amerFilename)  # 通过连接，获得文件的绝对路径
    euroFilename = os.path.join(absWorkingDir,euroFilename)

    # rename the files
    print('renaming "%s" to "%s"...'% (amerFilename,euroFilename))

    # shutil.move(amerFilename,euroFilename)  # 重命名
    
