import re
from datetime import datetime

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

def parseWords(year,month,day):
    for time in range(1,int(1+mywords_dict_len/5)):
        num_list = mywords_dict[1+(time-1)*5]
        # time_list = re.findall(r"[\d]+",num_list)
        time_list = re.findall(r'\d{4}年\d{1,2}月\d{1,2}', num_list)
        # print(time_list)
        selected_time = re.findall(r'[\d]+', str(time_list))
        # if int(selected_time[0]) == 2016 and int(selected_time[1]) == 7:
        #     print("yes,2016 07.")
        # # print(int(selected_time[0]))

        if int(selected_time[0]) == year and int(selected_time[1]) == month and int(selected_time[2]) == day:
            print("{} - {} - {}\n{}".format(year,month,day,mywords_dict[1+(time-1)*5+2]))


        # print("word/sentence is: {}".format(mywords_dict[1+(time-1)*5+2]))

parseWords(2016,12,22)
