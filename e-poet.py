import random
import json

def create(line: int = 0, data: dict = {}) -> str:
    if not data:
        return ''
    def line_create():
        sentence = random.choice(data['sentences'])
        for sign in data['words']:
            while sign in sentence:
                sentence = sentence.replace(sign,
                    random.choice(data['words'][sign]), 1)
        return sentence
    for t in range(line):
            yield line_create()

def download_data():
    from urllib import error
    from urllib.request import urlopen
    try:
        data_web = urlopen('https://raw.githubusercontent.com/Expector-Hutch/e-poets/main/data.json')
    except error.HTTPError as e:
        print(f'链接网络数据失败，错误码{e.code}')
        exit(e.code)
    if data_web.status == 200:
        print('已链接到网络数据...', end='')
    data_local = open('./data.json', 'wb')
    data = data_web.read()
    print('\r已完成数据读取...        ', end='')
    data_local.write(data)
    print('\r数据保存完成，正在等待关闭...', end='')
    data_local.close()
    print('\r🉐词库数据恢复成功!          ')

def main(line=0):
    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        if input("找不到词库(>﹏<)\n是否从互联网上下载词库文件？\n(y/N) ") == 'y':
            download_data()
        else:
            exit(-1)

    for stc in create(line, data):
        print(stc)

if __name__ == '__main__':
    from sys import argv
    import getopt
    help_text = '''
命令格式：e-poet [h]|[help] [-r]|[--restore] [-l]|[--line] <line>
    h/help: 获取帮助
    -r/--restore: 恢复词库数据
    -l/--line <line>: 写诗行数
    '''
    opts, args = getopt.getopt(argv[1:], 'hrl:', ['help', 'restore', 'line='])
    for arg in args:
        if arg in ('h', 'help'):
            print(help_text)
            exit()
    for opt, arg in opts:
        if opt in ('-l', '--line'):
            main(line=int(arg))
        elif opt in ('-r', '--restore'):
            download_data()
