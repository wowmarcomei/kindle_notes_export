# kindle_notes_export

## Update: 
(1) 19-3-2017:
- 增加单词自动查询并返回注释功能,爬取网易有道词典网站
- 整理markdown表格内容,单词加粗显示

(2) 29-12-2016:
- 完成基本功能,将Kindle上的标记自动整理成markdown格式文件,便于自己统计学习
  

## 使用步骤:

### 1.准备工作
1. 当然是在Kindle看书时自己对想要学习的单词或者语句进行标记,Kindle会将这些记录写入记事本文件 My Clippings.txt
2. 将该文件导出到电脑,重新命名为My_Clippings.txt,主要是为了去掉文件名的空格

### 2.运行程序输出markdown文件
```shell
 python3 main.py --prefix=static -t 2017-2-25 -i My_Clippings.txt -o words_chapters_9.md
```
>其中 
 - --prefix为指定源目录为static,当然也可以指定别的目录,但是需要将My_Clippings.txt文件将其移动到相应目录里,
 - -t 为选择时间
 - -i 为指定输入源文件,即目录中的txt文件
 - -o 为指定输出源文件,即输出的markdown文件

