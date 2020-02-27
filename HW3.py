# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 15:25:40 2018

@author: USER
"""

import matplotlib.pyplot as plt
import numpy as np
import jieba.analyse
import codecs
from wordcloud import WordCloud

# 每首歌的前10大tag
#with open("再會中港路.txt", "r",encoding="utf-8") as f1:
#   for line in f1:
#        words = jieba.analyse.extract_tags(line,10)
#        print(",".join(words))
#f1.close()

# 把所有歌的10大tags取N個tags
with open("再會中港路.txt", "r",encoding="utf-8") as f2:
    for line in f2:
        tags = jieba.analyse.extract_tags(line,15) #取Ｎ個tags
        print(",".join(tags))
f2.close()


# 讀取欲透過文字雲計算詞頻的檔案
text = open("再會中港路.txt",encoding="utf-8").read()
# 建立停用字
stopwords = {}.fromkeys(["啦啦啦啦啦"])  

wc = WordCloud(font_path="simfang.ttf", #設置字體
               background_color="black", #背景顏色
               max_words = 30 , #文字雲顯示最大詞數
               stopwords=stopwords) #停用字詞


# 產生文字雲
wc.generate(text)

# 視覺化
plt.imshow(wc)
plt.axis("off")
plt.figure(figsize=(10,6), dpi = 100)
plt.show()

# 存檔
#wc.to_file("lyrics/wordcloud1.jpg")