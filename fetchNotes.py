import re

path = './My_Clippings_20161224.txt'

def parseFile(path):
    '''
    获取文本文件,将其存入字典
    :param path: path 文本文件
    :return: words_dict 字典变量
    '''
    with open(path,'r',encoding='utf-8') as file:
        words_dict = {num: value for num,value in enumerate(file)}
    return words_dict

mywords_dict = parseFile(path)
mywords_dict_len = len(mywords_dict)

def parseWords():
    for time in range(1,int(1+mywords_dict_len/5)):
        num_list = mywords_dict[1+(time-1)*5]
        print(re.findall(r"[\d]+",num_list))
        print("word/sentence is: {}".format(mywords_dict[1+(time-1)*5+2]))

parseWords()

# date = mywords_dict[6]
# print(re.findall(r"[\d]+",date))
#
#
# for i in range(1,6):
#     print("{} of {} is: {}\n".format(i,len(mywords_dict),mywords_dict[i-1]))