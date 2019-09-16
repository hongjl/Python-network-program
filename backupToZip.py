#! python3
# backupToZip.py - copies an entire folder and its contents into
# a zip file whose filename increments  自增

import zipfile, os

def backupToZip(folder):
    # backup the entire contents of folder into a zip file
    folder = os.path.abspath(folder)  # 确保路径是绝对路径

    # figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):  # 确保不会重名
            break
        number = number + 1

    # create the zip file
    print('creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')  # 创建压缩文件

    # walk the entire folder tree and compress the files in each folder.
    # 压缩子文件夹
    for foldername, subfolders, filenames in os.walk(folder):
        print('adding files in %s...' %(foldername))
        # add the current folder to the zip file.
        backupZip.write(foldername)

    # add all the files in this folder to the zip file
    # 压缩当前文件夹内的文件，并跳过当前已有的备份文件
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # 不备份之前的备份文件
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('done.')


backupToZip('C:\\MyPythonScripts')
    
