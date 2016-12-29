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

class Usage(Exception):
    def __init__(self,msg):
        self.msg = msg

def main(argv=None):
    date = None
    output = None

    if argv is None:
        argv = sys.argv
    try:
        try:
            # 提取命令行的option选项与参数arguments
            opts, args = getopt.getopt(argv[1:],'ht:o:',['help'])
            # opts是一个元祖列表
            for opt, value in opts:
                if opt in ('-h','--help'):
                    print("Usage: please input the date and output fine name, such as:\npython3 main.py -t 20161226 -o words.md")
                if opt == '-t':
                    date = value
                    print(date)
                if opt == '-o':
                    output = value
                    print(output)
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
        if date == None or output == None:
            print("input date and output completely please, for help use --help")
    except Usage as err:
        # print(sys.stderr + err.msg)
        print(sys.stderr)
        print(err.msg)
        print("for help use --help")
        return 2

if __name__ == "__main__":
    sys.exit(main())
