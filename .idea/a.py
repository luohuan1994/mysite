import re
tt = "this is a good girl, she is cool,clever, and so on...."
rr = re.compile(r'\w+oo\w+')    # 查找所有包含oo的单词
print (rr.findall(tt))
print(re.findall(r'(\w)*oo(\w)+',tt))

"""
print(re.match('com','comwww.runbo').group())
print(re.match('com','cohhhh.rungggg',re.I).group())
"""
print ("----------------------")
#print (re.search('\dcom','www.4comrunoob.5com').group())
a = "12345abc6789"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group())
#print(re.search("([0-9]*)([a-z]*)(0-9)",a).group(1))
#print(re.search("([0-9]*)([a-z]*)(0-9)",a).group(2))
#print(re.search("([0-9]*)([a-z]*)(0-9)",a).group(3))

print(re.split('\d+','one1two2three3four4five5'))

