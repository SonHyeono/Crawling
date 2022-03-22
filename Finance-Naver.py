import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/lastsearch2.naver'


def crawl_review(base_url):
    def no_space(text):
        text1 = re.sub('&nbsp;|&nbsp;|\n|\t|\r', '', text)
        text2 = re.sub('\n\n', '', text1)
        return text2
    res = requests.get(base_url)

    stocks_arr = []
    if res.status_code == 200:
        # html.parser 보다 lxml 이 빠름. 그러나 lxml은 따로 설치를 해야함.
        soup = BeautifulSoup(res.text, 'lxml')
        stocks = soup.select(
            'div.box_type_l table  tr td a')
        for st in stocks:
            stocks_arr.append(st.text)
    df = pd.DataFrame({"Stocks": stocks_arr})
    return df


def save_and_load(dataframe):
    basepath = 'C:/gitreposit/Crawling/Crawling_Data/'
    dataframe.to_csv(basepath+'검색상위종목.csv', index=False, encoding='utf-8-sig')


save_and_load(crawl_review(url))
