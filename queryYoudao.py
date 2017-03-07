import requests
import bs4
import os
import time
import sys
import linecache
import re

words,sentences = [],[]

def extract_Words_Sentences(input=None,output_words=None,output_sentences=None):
    '''
    extract the words and sentences from the markdown files
    :param input: the source file
    :param output_words: come out with the words we need
    :param output_sentences: come out with the sentences we need
    :return: NULL
    '''
    file = open(input,'r',encoding='utf-8')

    markdown_str = file.read()

    regex = [r'(?<=\|\*{2}).+?(?=\.?\,?\!?\:?\;?\"?\*{2}\|)',r'((?<=\|)[^\w\|]*(\w+\s+(?=\w+)[^\|]*))']

    for item in range(0,2):
        matches = re.finditer(regex[item],markdown_str)
        for matchNum, match in enumerate(matches):
            if item == 0:
                output_words.append(match.group(0))
            else:
                output_sentences.append(match.group(0))

    file.close()

extract_Words_Sentences(input='static'+'/'+'words_chapters_mxh.md',output_words=words,output_sentences=sentences)

print('====' * 10 + '\n')
print('globle variables are:\n words:{}\nsentences:{}'.format(words,sentences))

def queryYoudao(input=None,output=None):
    with open(output, 'a+', encoding='utf-8') as finalmk:
        print("到有道词典网站查询单词单词,抓取释义!")

        rooturl = 'http://www.youdao.com/w/'
        url = rooturl + 'biscuits'
        result = {}

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        word = soup.select('.keyword')[0].get_text()

        res_num_chn2chn = len(soup.select('#phrsListTab > div.trans-container > ul > li'))

        print("查询出{}条英中结果".format(res_num_chn2chn))
        for i in range(1,res_num_chn2chn+1):
            print("第{}次".format(i))
            print(soup.select('#phrsListTab > div.trans-container > ul > li')[i-1].get_text())
            finalmk.write(" **英中:** ({})".format(i)+soup.select('#phrsListTab > div.trans-container > ul > li')[i-1].get_text())

        res_num_eng2eng = len(soup.select('#tEETrans > div > ul > li > ul > li > span'))
        print("查询出{}条中英结果".format(res_num_eng2eng))
        for i in range(1,res_num_eng2eng+1):
            print("第{}次".format(i))
            # print(soup.select('#tEETrans > div > ul > li > span')[i-1].get_text())
            print(soup.select('#tEETrans > div > ul > li > ul > li > span')[i-1].get_text())
            finalmk.write(" **英英:** ({})".format(i)+soup.select('#tEETrans > div > ul > li > ul > li > span')[i - 1].get_text())

queryYoudao(output='static'+'/'+'final.md')
