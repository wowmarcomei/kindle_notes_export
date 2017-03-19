# /**
#  *   ┏┓　　　┏┓
#  * ┏┛┻━━━┛┻┓
#  * ┃　　　　　　　┃
#  * ┃　　　━　　　┃
#  * ┃　┳┛　┗┳　┃
#  * ┃　　　　　　　┃
#  * ┃　　　┻　　　┃
#  * ┃　　　　　　　┃
#  * ┗━┓　　　┏━┛
#  *    ┃　　　┃
#  *    ┃　　　┃
#  *    ┃　　　┗━━━┓
#  *    ┃　　　　　　　┣┓
#  *    ┃　　　　　　　┏┛
#  *    ┗┓┓┏━┳┓┏┛
#  *      ┃┫┫　┃┫┫
#  *      ┗┻┛　┗┻┛
#  *        神兽保佑
#  *        代码无BUG!
#  */

import requests
import bs4
import os
import time
import sys
import linecache
import re

words,explainations,sentences = [],[],[]

def extract_words_sentences(input=None,output_words=None,output_sentences=None):
    '''
    extract the words and sentences from the markdown files
    :param input: the source file
    :param output_words: come out with the words we need
    :param output_sentences: come out with the sentences we need
    :return: return the final sentences list: corresponding to each word
    '''
    file = open(input,'r',encoding='utf-8')
    print("正在解析单词与语句...\n")
    markdown_str = file.read()
    regex = [r'(?<=\|\*{2}).+?(?=\.?\,?\!?\:?\;?\"?\*{2}\|)',r'((?<=\|)[^\w\|]*(\w+\s+(?=\w+)[^\|]*))']

    temp=''
    temp_sentence = []

    for item in range(0,2):
        matches = re.finditer(regex[item],markdown_str)
        for matchNum, match in enumerate(matches):
            if item == 0:
                # 输出单词
                output_words.append(match.group(0))
            else:
                # 输出句子
                temp_sentence.append(match.group(0))
    print("解析单词语句结束...\n")

    # 从列表2(sentences)中找出包含列表1(words)的元素
    for i in range(0, len(output_words)):
        for j in range(0, len(temp_sentence)):
            if output_words[i] in temp_sentence[j]:
                temp = temp_sentence[j]
                break
            else:
                temp = '-'
        output_sentences.append(temp)

    file.close()

def query_youdao(input=None):
    '''
    查询有道词典,输入单词列表,返回单词解释
    :param input: None,后续传入为单词列表 words[]
    :return: explainations 单词释义列表
    '''
    rooturl = 'http://www.youdao.com/w/'

    print("正在查询有道词典...\n")

    for item in range(0,len(input)):
        url = rooturl + input[item]

        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text,'html.parser')

        chn2eng = soup.select('#phrsListTab > div.trans-container > ul > li')
        eng2eng = soup.select('#tEETrans > div > ul > li > ul > li > span')

        print("word {}: {}".format(item,input[item]))
        explaination = ''
        for i in range(0,len(chn2eng)):
            print("explaination {}: {}".format(i,chn2eng[i].get_text()))
            explaination = explaination+chn2eng[i].get_text()+"; "

        for i in range(0,len(eng2eng)):
            print("explaination {}: {}".format(i,eng2eng[i].get_text()))
            explaination = explaination+eng2eng[i].get_text()+"; "
        print("===============================================\n")
        # 将解释的单词放置在列表中
        explainations.append(explaination)
    print("查询有道词典结束...\n")

    return explainations


def output_final_markdown(final_markdown=None):
    print("正在生成最终markdown文件...\n")
    with open(final_markdown,'a+',encoding='utf-8') as markdown:
        markdown.write("| 单词 | 解释 | 例句 |\n| --------- | -------- | --------- |\n")
        for i in range(0,len(words)):
            markdown.write("|**{}**|{}|{}|\n".format(words[i],explainations[i],sentences[i]))
    print("Markdown文件生成完毕,主人请验证...\n")
