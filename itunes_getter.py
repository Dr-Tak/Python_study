# -*- coding: utf-8 -*-
from logging import getLogger, DEBUG
import urllib.request
import json
import binascii

# ログの設定
logger = getLogger(__name__)
logger.setLevel(DEBUG)

def main():
    logger.debug("mainの開始")
    
    #url 初期化
    url = ''
    
    #urlは構造で分解する必要がある
    protocol = 'https://'
    domain = 'itunes.apple.com/search?term='
    word = 'Mr\.children'#検索キーワード　HTMLから値をもらってくる箇所(いずれ変数化する)
    query_string = '&media=music'
    
    url = protocol + domain + word + query_string
    print(url)
    
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        json_txt = json.load(res)  #JSON形式での取得

    #JSONの解析
    #musicのdict
    for one in json_txt['results']:  #普通に配列へのアクセスで取れたわ・・・
        print(
            one['artistName'],
            one['collectionName'],
            one['trackName'],
            one['artworkUrl100'],
            one['trackNumber'],
            one['country']
        )
    
def func_erroe(parm1):
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
