#! python3
'''
强口令： 长度不少于8个字符，同时包含大写和小写字符，至少有一个数字
'''
import re




text = ['SLKJDFSLDKF','laksfdlksd','8378373849999','asdf','sdfkjSDLFK','aslkdfj89899','SLKDFJSLDKF89687','asdfkSDKF78799']  # 测试，只有一个符合条件

def checkStrongPassword(pwList):
    
    # castAndNum = re.compile(r'\w*?[0-9A-Z]*[a-z]+\w*')
    lowCast = re.compile(r'[^a-z]*[a-z]+[^a-z]*')  # 包含小写字母
    uppCast = re.compile(r'[^A-Z]*[A-Z]+[^A-Z]*')  # 包含大写字母
    num = re.compile(r'\D*\d+\D*')  # 包含至少一个数字
    beyond8 = re.compile(r'\w{8,}')  # 至少8个字符
    
    for pw in pwList:
        if(lowCast.search(pw) != None and uppCast.search(pw) != None 
           and num.search(pw) != None and beyond8.search(pw) != None):
            print(pw)


checkStrongPassword(text)
