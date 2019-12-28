import re


def main():
    lines = []
    with open('test.txt', 'r', encoding='utf-8') as f:
        for line in f:
            purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                              '*', line, flags=re.IGNORECASE)
            print(purified)  # 你丫是*吗? 我*你大爷的. * you.
            lines.append(purified)
        f.close()
    with open('test.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)


if __name__ == '__main__':
    main()
