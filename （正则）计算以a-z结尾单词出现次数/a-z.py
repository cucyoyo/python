from nltk.book import *
import re
import string

def fun(zimu):
    words = [w for w in text1 if re.search(zimu+'$',w)]
    print('以'+zimu+'结尾的单词出现的次数：'+str(len(words)))


for zimu in string.ascii_lowercase:
    fun(zimu)

