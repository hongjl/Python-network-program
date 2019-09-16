#! python3
# pw.py - An insecure password locker program
# 密码管理
# 可以添加查询菜单功能

PASSWORDS = {'email':'honghong',
             'blog':'sdflkkaf',
             'school':'asdfekk'}

import sys
import pyperclip

def pw():
    if len(sys.argv) < 2:
        print('Usage: python pw.py [account] - copy account password.')
        sys.exit()

    account = sys.argv[1]  # first command line arg is the account name

    if account in PASSWORDS:
        pyperclip.copy(PASSWORDS[account])
        print('Password for ' + account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)

if __name__ == '__main__':
    pw()