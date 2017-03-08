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

import re

def parseFile(path):
    '''
    获取文本文件,将其存入字典,注意open文件的时候一定要选择编码为utf-8
    :param path: path 文本文件
    :return: dict 字典变量
    '''
    with open(path,'r',encoding='utf-8') as file:
        dict = {key: value for key,value in enumerate(file)}
    return dict

def parseWords(year,month,day,dict=None,output=None):
    '''
    解析字典变量中对应时间后面的单词或者句子(适用于Kindle标记文件)
    :param year: 年
    :param month: 月
    :param day: 日
    :param dict: 字典
    :return: NULL
    '''
    # 注意,open文件的时候一定要选择编码为utf-8
    with open(output,'a+',encoding='utf-8') as words:
        # 以日期为标题，#h1格式,换行后写入表格标题
        words.write("#{}-{}-{}\n| 单词 | 解释 | 例句 |\n| --------- | -------- | --------- |\n".format(year,month,day))
        # 由于kindle标记内容是5行为1块，所以其记事本的行数一定为5的倍数，取每个标记的话就用字典长度除以5即可
        for time in range(1,int(1+len(dict)/5)):
            # 包含有日期数据的字符串是字典中每一块的第2行，然后每次加5就得到下一次的日期数据字符串; 使用正则表达式提取日期部分字符串，返回列表
            time_list = re.findall(r'\d{4}年\d{1,2}月\d{1,2}', dict[1+(time-1)*5])
            # 使用正则表达式进一步提取日期，返回列表，
            selected_time = re.findall(r'[\d]+', str(time_list))
            # 判断年月日是否符合条件
            if int(selected_time[0]) == year and int(selected_time[1]) == month and int(selected_time[2]) == day:
                # 定义一个临时变量存储每行需要写入的单词或者语句（第4行）,加上markdown的表格标签"|",该变量最终是一个字符串
                # 同时判断第一列是否是单个单词还是语句，如果是单个单词，则给单词加粗，否则是语句的话就不加粗（以是否包含空格' '为判断单词/语句的依据）
                if ' ' in dict[3+(time-1)*5]:
                    word_line = "|"+dict[3+(time-1)*5]+"| - | - |"
                else:
                    word_line = "|"+"**"+dict[3+(time-1)*5]+"**"+"| - | - |"
                # 采用正则表达式去掉换行符号,但是返回结果是一个列表list,还需要将列表转换成字符串,采用join方法即可
                word_extract = ''.join(re.split(r'[\n]+',word_line))
                # 写入markdown文件
                words.write(word_extract+'\n')
            else:
                pass
        words.write('\n'*3)
