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
    def __init__(self, msg):
        self.msg = msg

def usage():
    print("Usage:{} [-a|-o|-c] [--help|--output] args...." .format(sys.argv[0]));

def main(argv=None):
    if argv is None:
        # 获取命令行参数列表,如执行函数时:python main.py 2016,可以得到列表argv为['main.py', '2016']
        argv = sys.argv

    try:
        # 提取命令行参数列表,过滤掉第一个参数,因为第一个参数一般为文件本身
        # opts, args = getopt.getopt(argv[1:], "h", ["help"])

        opts, args = getopt.getopt(sys.argv[1:], "ao:c", ["help", "output="])
        print("============ opts ==================")
        print(opts)
        print("============ args ==================")
        print(args)

        # check all param
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                usage();
                sys.exit(1);
            elif opt in ("-t", "--test"):
                print("for test option");
            else:
                print("{}  ==> {}".format(opt, arg))

    except getopt.GetoptError:
        print("getopt error!");
        usage();
        sys.exit(1);

if __name__ == "__main__":
    sys.exit(main())