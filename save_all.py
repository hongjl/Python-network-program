import pyperclip
# 本来用意：为笔记制作目录，所以为将每个小节的标题获取下来，
# 将拷贝的字符串存放到指定文件下，之后就可以很快的获取到这些标题，而不用
# 不停的复制粘贴

def all_save():
    with open('all_save.txt','a',encoding='utf-8') as f:  # 使用 a 模式，文件不存在会创建
        f.write(pyperclip.paste()+'\n')  # 将剪贴板的内容放到文件中
        pyperclip.copy('')


def all_print(content:list):  # 默认传入一个列表
    content.append(pyperclip.paste())


content = []
while True:
    if pyperclip.paste() != '':
        # all_save()
        # all_print(content)
        print(pyperclip.paste())  # 直接在屏幕输出更加方便
        pyperclip.copy('')  # 重置剪贴板内容
