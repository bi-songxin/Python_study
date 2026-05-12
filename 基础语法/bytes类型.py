# bytes 是python中最小的数据单位

# s = '中国' #内存中使用的是unicode

# encode编码
# print(s.encode('utf-8')) #b'\xe4\xb8\xad\xe5\x9b\xbd'

# bytes类型
# utf-8
# bs = b'\xe4\xb8\xad\xe5\x9b\xbd' # 每个\x是一个字节
# print(type(bs))

#gbk
# print(s.encode('gbk')) #b'\xd6\xd0\xb9\xfa'
# print(type(s.encode('gbk'))) #bytes

# 把bytes转化为字符串
# decode解码
bss = b'\xd6\xd0\xb9\xfa'
# 用gbk解码
s1 = bss.decode('gbk')
print(s1)

# 不同编码之间是不能直接转换的
# 转换成utf-8字节
print(s1.encode('utf-8'))
