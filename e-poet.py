import random
import json

def create(line: int = 0, data: dict = {}) -> str:
    if not data:
        return ''
    def line_create():
        sentence = random.choice(data['sentences'])
        for sign in data['words']:
            sentence = sentence.replace(sign,
                           random.choice(data['words'][sign]))
        return sentence
    for t in range(line if line > 0 else random.randint(3, 33)):
            yield line_create()

def download_data():
    ...

def main():
    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        if input("找不到词库(>﹏<)\n是否从互联网上下载词库文件？\n(y/N) ") == 'y':
            download_data()
        
    for stc in create(int(input("创作行数: ")), data):
        print(stc)

if __name__ == '__main__':
    import getopt
    help_text = '''
命令格式：e-poet [-h]|[help] [-l]|[--line] <line>
    -h/help: 获取帮助
    -l/--line <line>: 写诗行数（默认随机）
    '''
    opts, args = getopt.getopt(__import__('sys').argv[1:], 'hl:', ['help', 'line='])
    for arg in args:
        if arg == 'help':
            print(help_text)
    for opt, arg in opts:
        ...
    main()
