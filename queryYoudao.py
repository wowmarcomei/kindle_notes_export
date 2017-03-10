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
                # 输出单词
                output_words.append(match.group(0))
            else:
                # 输出句子
                output_sentences.append(match.group(0))
    file.close()

def queryYoudao(input=None,output=None):
    with open(output, 'w', encoding='utf-8') as finalmk:
        print("到有道词典网站查询单词单词,抓取释义!")

        rooturl = 'http://www.youdao.com/w/'

        for item in range(0,len(input)):
            url = rooturl + input[item]

            response = requests.get(url)
            soup = bs4.BeautifulSoup(response.text,'html.parser')

            chn2eng = soup.select('#phrsListTab > div.trans-container > ul > li')
            eng2eng = soup.select('#tEETrans > div > ul > li > ul > li > span')

            shiyi = ''
            for i in range(0,len(chn2eng)):
                # print("shiyi {}: {}".format(i,chn2eng[i].get_text()))
                shiyi = shiyi+chn2eng[i].get_text()+ "  |  "

            for i in range(0,len(eng2eng)):
                # print("shiyi {}: {}".format(i,eng2eng[i].get_text()))
                shiyi = shiyi+eng2eng[i].get_text()+ "  |  "
            print("============================\n查出{}个中文释义,{}个英文释义\n".format(len(chn2eng),len(eng2eng)))
            print("单词: {}\n释义: {}\n".format(input[item],shiyi))
            print("****************************\n")

def output_final_markdown():
    '''
    输出最终的markdown文件
    :return:
    '''
    # 找出单词所在的句子
    for i in range(0, len(words)):
        for j in range(0, len(sentences)):
            if words[i] in sentences[j]:
                print("word:'{}' is in the sentence:{}\n".format(words[i], sentences[j]))

extract_Words_Sentences(input='static'+'/'+'words_chapters_mxh.md',output_words=words,output_sentences=sentences)

print("words are: {}\nsentences are: {}".format(words,sentences))

queryYoudao(input=words,output='static'+'/'+'final.md')