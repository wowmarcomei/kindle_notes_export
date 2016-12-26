import re

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
    # words = open(makrdown,'a+',encoding='utf-8')
    with open(makrdown,'a+',encoding='utf-8') as words:
        # 以日期为标题，#h1格式
        words.write("#{}-{}-{}\n".format(year,month,day))
        # 写下markdown表格的标题部分
        words.write("| 单词 | 解释 | 例句 |\n| --------- | -------- | --------- |\n")

        # 由于kindle标记内容是5个为1行，所以其记事本的行数一定为5的倍数，取每个标记的话就用字典长度除以5即可
        for time in range(1,int(1+mywords_dict_len/5)):
            # 包含有日期数据的是字典中每一块的第2行，然后每次加5就得到下一次的数字行
            num_list = mywords_dict[1+(time-1)*5]
            # 使用正则表达式提取日期部分字符串，返回列表
            time_list = re.findall(r'\d{4}年\d{1,2}月\d{1,2}', num_list)
            # 使用正则表达式进一步提取日期，返回列表，
            selected_time = re.findall(r'[\d]+', str(time_list))

            # 判断年月日是否符合条件
            if int(selected_time[0]) == year and int(selected_time[1]) == month and int(selected_time[2]) == day:
                # 定义一个临时变量存储每行需要写入的单词或者语句（第4行）,加上markdown的表格标签"|",该变量最终是一个字符串
                word_line = "|"+mywords_dict[3+(time-1)*5]+"| - | - |"
                # 采用正则表达式去掉换行符号,但是返回结果是一个列表list,还需要将列表转换成字符串,采用join方法即可
                word_line_new = ''.join(re.split(r'[\n]+',word_line))
                # 写入markdown文件
                words.write(word_line_new+'\n')
            else:
                pass
        words.write('\n'*3)

parseWords(2016,12,2)
parseWords(2016,12,3)
parseWords(2016,12,5)
parseWords(2016,12,22)
parseWords(2016,12,23)
parseWords(2016,12,24)
parseWords(2016,12,25)
