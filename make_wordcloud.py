# -*- coding:utf-8 -*-

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS
from get_titles import get_title_list

if __name__ == '__main__':
    #text = open('title.txt', 'r').read()
    text = ' '.join(get_title_list())
    ICML_mask = np.array(Image.open("ICML_mask.png"))
    
    wordcloud = WordCloud(max_font_size=64, max_words=300, 
                          width=1280, height=640,
                          background_color="white",
                          mask=ICML_mask).generate(text)
    plt.figure(figsize=(16, 8), frameon=False)
    plt.imshow(ICML_mask)
    plt.imshow(wordcloud, interpolation="bilinear",  alpha=.7)
    plt.axis("off")
    plt.savefig('wordcloud.png')
    #plt.show()
