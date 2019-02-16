# -*- coding: utf-8 -*-
from logging import getLogger, DEBUG
import urllib.request
import json
import binascii

# ログの設定
logger = getLogger(__name__)
logger.setLevel(DEBUG)

# 定数です
NUM_SPHERE = 4
NUM_TRYSAIL = 3


def main():
    a = 'test'
    logger.debug("mainの開始")
    
    if a != 'test':
        func_fugafuga(1)
    else:
        print(a)
        
    #ここからちゃんと書くべ
    #まずはitunesにGETリクエストを投げるよ
    #url 初期化
    url = ''
    
    #urlは構造で分解する必要がある
    protocol = 'https://'
    domain = 'itunes.apple.com/search?term='
    word = 'Mr\.children'#検索キーワードさ
    query_string = '&media=music'
    
    url = protocol + domain + word + query_string
    print(url)
    
#     req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)))
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        json_txt = json.load(res)  #JSON形式での取得

#     print(body)
    
    #JSONの解析
    #musicのdict
    keyList = json_txt.keys()
#     print(keyList)
    
    valList = json_txt.values()
    print(valList)
    
    
def func_fugafuga(parm1):
    logger.error("エラーです！！")

class MyClass:

    def __init__(self):
        self._pv_v = "インスタンス変数"

    def process(self, parm1):
        logger.debug("process")

    def _pv_process(self):
        logger.debug("_pv_process")


if __name__ == "__main__":
    main()
