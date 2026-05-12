s = 'abcdefghijklmnopqrst'

# print(s[::-2])  #trpnljhfdb
# print(s[1:8:3]) #beh
# print(s[-1,-7,-2]) #trp
# print(s[10,3,-4]) #kg

# 回文练习
# "上海自来水来自海上"

content = input('请输入文字:')
if content == content[::-1]:
    print('是回文')
else:
    print('不是回文')