# kindle_notes_export

> 用于将Kindle电子书上标注的单词，语句自动导出并整理成Markdown格式的表格形式。

## 使用步骤:
1. 当然是在Kindle看书时自己对想要学习的单词或者语句进行标记,Kindle会将这些记录写入记事本文件 My Clippings.txt
2. 将该文件导出到电脑,重新命名为My_Clippings.txt,主要是为了去掉文件名的空格
3. 在fetchNotes.py中指定日期,如parseWords(2016,12,2)来导出12月1日的标记为markdown文件
3. 运行fetchNotes.py文件: python3 fetchNotes.py就会在static目录下生成words.md文件