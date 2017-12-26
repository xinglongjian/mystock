# -*- coding: UTF-8 -*-
from urllib.error import HTTPError

from sqlalchemy import Float

from app.models import StockBasic, Stock
import tushare as ts
from app import db
from datetime import datetime
from util.date_util import *
from log import *

'''股票基本面数据
每个交易日都会获取，两个表：stock 和 stock_basics

从2017-07-11开始往前

从2016-11-21开始之前的包含的列不全
'''


def start():

    start_date = get_date(2017,7,10)
    end_date = get_date(2017,12,26)

    while start_date >= end_date:
        date_str = str(start_date)
        #如果是节假日就返回
        if ts.is_holiday(date_str):
            start_date = get_last_day(start_date)
            continue

        try:
            df = ts.get_stock_basics(date_str)
            df = df.fillna(0)
            # df['esp'] = df['esp'].astype('float')
            for index, row in df.iterrows():

                if '㈢' in str(row['esp']):
                    row['esp'] = row['esp'].replace('㈢','')
                if '㈠' in str(row['esp']):
                    row['esp'] = row['esp'].replace('㈠','')
                if '㈣' in str(row['esp']):
                    row['esp'] = row['esp'].replace('㈣','')
                # row['totalAssets'] = row['totalAssets'].astype('float')
                # row['liquidAssets'] = row['liquidAssets'].astype('float')
                # row['reserved'] = row['reserved'].astype('float')
                add_to_db(index, row, date_str)
                try:
                    commit_to_db()
                except Exception as e:
                    logging.error("error:date_str:%s,caused by:%s,row:%s", date_str, e.args[0], row)
        except HTTPError as ex:
            logging.error("error:date:%s Not Found",date_str)
            start_date = get_last_day(start_date)
            continue
        except Exception as ex:
            logging.error("error:date_str:%s,caused by:%s,row:%s",date_str, ex.args[0],row)
            break
        logging.info("finsish :%s",start_date)
        start_date = get_last_day(start_date)

    logging.info("all finsish")


def add_to_db(index, item, date_str):

    #查看stock里是不是有
    stock_is_exist = Stock.query.filter_by(code=index).first()
    if stock_is_exist is None:
        stock_new = Stock(code=index, name=item['name'], industry=item['industry'], area=item['area'],
                          time_to_market=item['timeToMarket'])
        db.session.add(stock_new)

    basic_is_exist = StockBasic.query.filter_by(code=index, date=date_str).first()
    if basic_is_exist is None:
        stock_basic = StockBasic(index, item['name'], date_str, item['pe'], item['outstanding'], item['totals'],
                                 item['totalAssets'],item['liquidAssets'], item['fixedAssets'], item['reserved'],
                                 item['reservedPerShare'], item['esp'],item['bvps'], item['pb'], item['undp'],
                                 item['perundp'], item['rev'], item['profit'], item['gpr'], item['npr'], item['holders'])
        db.session.add(stock_basic)

def commit_to_db():
    db.session.commit()

if __name__ == '__main__':
    start()