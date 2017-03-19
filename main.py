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

import sys
import getopt
from fetchNotes import parseFile,parseWords
from queryYoudao import words,explainations,sentences,extract_words_sentences,query_youdao,output_final_markdown

class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg

def main(argv=None):
    help = None
    date = None
    prefix = None
    input = None
    output = None
    if argv is None:
        argv = sys.argv
    try:
        # -------------------------------------------------------------------------------
        # 提取命令行的option选项与参数arguments, 注本例子中只采用opt,而没有使用args
        try:
            opts, args = getopt.getopt(argv[1:],'hp:t:i:o:',['help','prefix='])
            # opts是一个元祖列表
            for opt, value in opts:
                if opt in ('-h','--help'):
                    help = opt
                if opt in ('-p','--prefix'):
                    prefix = value
                if opt == '-t':
                    date = value.split('-')
                if opt == '-i':
                    input = value
                if opt == '-o':
                    output = value
        except getopt.error as msg:
            raise Usage(msg)
        # -------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------
        # 执行代码
        if help in ('-h','--help'):
            print("Usage:\n"
                  "-p, --a directory, to specify the prefix\n"
                  "-t, --select time, to specify the date\n"
                  "-i, --the source file, to specify the input which would be parsed\n"
                  "-o, --the output file, to specify the output which is markdwon file")
        elif len(date) < 3 or prefix==None or input==None or output==None:
            print("please input the right command, such as:\npython3 main.py -t 2016-12-26 --prefix=notes -i input.txt -o output.md \n\n\n"
                  "for help use --help")
        else:
            parseWords(int(date[0]), int(date[1]), int(date[2]), dict=parseFile(prefix+'/'+input),output=prefix+'/'+'tmp.md')
            print("1.Output the original markdown notes in: {}\n2.Prepare for next step and extract the explaination and sample sentences.\n".format(prefix+'/'+output))
        # -------------------------------------------------------------------------------
        #   将输出的原件整理为最终版本的markdown文件
            extract_words_sentences(prefix+'/'+'tmp.md', output_words=words,output_sentences=sentences)
            query_youdao(input=words)
            output_final_markdown(final_markdown=prefix + '/' + output)
            # print(words,sentences,sep='\n\n\n')

    except Usage as err:
        print(sys.stderr)
        print(err.msg)
        print("for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())