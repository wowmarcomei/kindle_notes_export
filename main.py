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
from fetchNotes import parseWords

class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg

def main(argv=None):
    date = None

    if argv is None:
        argv = sys.argv
    try:

        # -------------------------------------------------------------------------------
        # 提取命令行的option选项与参数arguments, 注本例子中只采用opt,而没有使用args
        try:
            opts, args = getopt.getopt(argv[1:],'ht:o:',['help'])
            # opts是一个元祖列表
            for opt, value in opts:
                if opt in ('-h','--help'):
                    print("Usage: please input the date such as:\npython3 main.py -t 2016-12-26")
                if opt == '-t':
                    date = value.split('-')
        except getopt.error as msg:
            raise Usage(msg)
        # -------------------------------------------------------------------------------

        # -------------------------------------------------------------------------------
        # 执行代码
        if len(date) < 3:
            print("input date and output correctly please, for help use --help")
        else:
            parseWords(int(date[0]), int(date[1]), int(date[2]))
            print("parse the words noted in {}".format(value))
        # -------------------------------------------------------------------------------

    except Usage as err:
        print(sys.stderr)
        print(err.msg)
        print("for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
