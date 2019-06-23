# -*- coding:utf-8 -*-

import os
import sys
import urllib
from urllib import request
from bs4 import BeautifulSoup

papers_url = 'http://proceedings.mlr.press/v97/'

def get_title_list():
    html = urllib.request.urlopen(papers_url)
    soup = BeautifulSoup(html, "html.parser")

    papers = soup.find_all('div', attrs={'class': 'paper'})
    ret = []
    for paper in papers:
        title = paper.find('p', attrs={'class': 'title'}).text
        try:
            print(title)
            ret.append(title)
        except:
            continue
    return ret

if __name__ == '__main__':
    paper_titles = get_title_list()
    with open('title.txt', 'w') as f:
        f.write('\n'.join(paper_titles))
        
