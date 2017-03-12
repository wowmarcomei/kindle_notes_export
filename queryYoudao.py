import requests
import bs4
import os
import time
import sys
import linecache
import re

words,explainations,sentences = [],[],[]

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

def queryYoudao(input=None):
    '''
    查询有道词典,输入单词列表,返回单词解释
    :param input:
    :return:
    '''
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
        # 将解释的单词放置在列表中
        explainations.append(shiyi)
    # print("length is: {}\nexplaination is: {}\n".format(len(explaination),explaination))

extract_Words_Sentences(input='static'+'/'+'words_chapters_mxh.md',output_words=words,output_sentences=sentences)

queryYoudao(input=words)

def output_final_markdown():
    word_in_sentences = False
    for i in range(0, len(words)):
        print("========word[{}]=========\n".format(i+1))
        for j in range(0, len(sentences)):
            if words[i] in sentences[j]:
                print("word: {}\nexplaination: {}\nsentences: {}\n========end[{}]=========\n".format(words[i], explainations[i],sentences[j],i+1))
                # print("========end[{}]=========\n".format(i + 1))
            else:
                word_in_sentences = True
        if word_in_sentences:
            word_in_sentences = False
            print("word: {}\nexplaination: {}\n========end[{}]=========\n".format(words[i], explainations[i],i+1))
            # print("========end[{}]=========\n".format(i + 1))

output_final_markdown()