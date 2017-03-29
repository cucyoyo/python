from nltk.book import *
import re

e = [w for w in text1 if re.search('e$',w)]
print('以e结尾的单词出现的次数：'+str(len(e)))
len_e = 0
count_e = 0
for w in e:
	len_e += len(w)
	count_e += 1
arra_e = len_e/count_e
print('以e结尾的单词平均长度为：'+str(arra_e))

x = [w for w in text1 if re.search('x$',w)]
print('以x结尾的单词出现的次数：'+str(len(x)))
len_x = 0
count_x = 0
for w in x:
	len_x += len(w)
	count_x += 1
arra_x = len_x/count_x
print('以x结尾的单词平均长度为：'+str(arra_x))

