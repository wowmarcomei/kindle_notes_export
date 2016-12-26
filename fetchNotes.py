import re
from datetime import datetime

path = './My_Clippings.txt'
makrdown = './words.md'

def parseFile(path):
    '''
    获取文本文件,将其存入字典,注意open文件的时候一定要选择编码为utf-8
    :param path: path 文本文件
    :return: words_dict 字典变量
    '''
    with open(path,'r',encoding='utf-8') as file:
        words_dict = {num: value for num,value in enumerate(file)}
    return words_dict

mywords_dict = parseFile(path)
mywords_dict_len = len(mywords_dict)

def parseWords(year,month,day):
    # 注意,open文件的时候一定要选择编码为utf-8
    words = open(makrdown,'a+',encoding='utf-8')
    words.write("| 单词 | 解释 | 例句 |\n| --------- | -------- | --------- |\n")

    for time in range(1,int(1+mywords_dict_len/5)):
        num_list = mywords_dict[1+(time-1)*5]
        # time_list = re.findall(r"[\d]+",num_list)
        time_list = re.findall(r'\d{4}年\d{1,2}月\d{1,2}', num_list)
        # print(time_list)
        selected_time = re.findall(r'[\d]+', str(time_list))
        # print(selected_time)

        if int(selected_time[0]) == year and int(selected_time[1]) == month and int(selected_time[2]) == day:
            #print("{} - {} - {}\n{}".format(year,month,day,mywords_dict[1+(time-1)*5+2]))
            # 定义一个临时变量存储每行需要写入的单词或者语句,用于后续去掉字符串的换行符号
            word_line = "|"+mywords_dict[1+(time-1)*5+2]+"| - | - |"
            # 采用正则表达式去掉换行符号,但是返回结果是一个列表list,还需要将列表转换成字符串,采用join方法即可
            word_line_new = ''.join(re.split(r'[\n]+',word_line))
            # str1 = ''.join(word_line_new)
            print(word_line_new)
            # print(str(word_line_new))
            # words.write(word_line+"\n")
        else:
            pass

    words.close()

        # print("word/sentence is: {}".format(mywords_dict[1+(time-1)*5+2]))

parseWords(2016,12,25)
