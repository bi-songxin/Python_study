"""练习10-4:访客名单编写一个while循环，提示用户输入名字。用户输入名字后，在屏幕上打印一句问候语并将一条到访记录添加到文件guest_book.txt中。
确保这个文件中的每条记录都独占一行。"""

while True:
    name = input('输入您的姓名(按回车键退出)：')
    if name == "":
        print('over!')
        break
    with open('guest_book.txt','a',encoding='utf-8') as f:
        # f.write(f'{name}\n')
        f.write(name+'\n')
        print(f'欢迎{name}!并新增一条记录！')
