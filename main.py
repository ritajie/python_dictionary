"""就是简单地抓取该翻译网站的信息
2018/1/11 路小鹿"""
from bs4 import BeautifulSoup
import requests


def tran(word):
    """参数一个字符串单词 return字符串翻译结果"""
    url = "http://dict.cn/" + word
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    lis = soup.select(".basic.clearfix ul li")
    # 最终答案
    ans = ""
    for li in lis[:-1]:
        text = li.text.strip().replace("\n", "\t")
        ans += (text + "\n")

    if len(ans) == 0:
        ans = "没找到这个词\n"

    return ans


def HasZh(str):
    """判断str有无中文"""
    for c in str:
        if ('\u4e00' <= c <= '\u9fa5'):
            return True
    return False


if __name__ == '__main__':
    word = input("input your word: ")
    while word != "exit":
        if HasZh(word):
            print("暂不支持中译英", end="\n\n")
        else:
            try:
                print(tran(word))
            except Exception:
                print("没找着这个词", end="\n\n")
        word = input("input your word: ")
