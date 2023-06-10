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
    for t in range(line if line > 0 else random.randint(3, 33)):
            yield line_create()

def download_data():
    from urllib.request import urlopen
    data_web = urlopen('https://raw.github.com/Expector-Hutch/e-poets/main/data.json')

def main(line=0):
    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        if input("找不到词库(>﹏<)\n是否从互联网上下载词库文件？\n(y/N) ") == 'y':
            download_data()

    for stc in create(line, data):
        print(stc)

if __name__ == '__main__':
    from sys import argv
    import getopt
    help_text = '''
命令格式：e-poet [-h]|[help] [-l]|[--line] <line>
    -h/help: 获取帮助
    -l/--line <line>: 写诗行数（默认随机）
    '''
    opts, args = getopt.getopt(argv[1:], 'hl:', ['help', 'line='])
    for arg in args:
        if arg == 'help':
            print(help_text)
    for opt, arg in opts:
        if opt in ('-l', '--line'):
            main(line=int(arg))
    main()
