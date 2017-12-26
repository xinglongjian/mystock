# -*- coding: UTF-8 -*-
from urllib.error import HTTPError


from app.models import TickHistData,Stock
import tushare as ts
from app import db
from util.date_util import *
from log import *

'''历史分笔数据任务

'002065','600243','600366'
到2016-11-21
'''


def start():

    start_date = get_date(2017,7,11)
    end_date = get_date(2017,7,11)
    code = '600243'

    while start_date >= end_date:
        date_str = str(start_date)
        #如果是节假日就返回
        if ts.is_holiday(date_str):
            start_date = get_last_day(start_date)
            continue

        try:
            df = ts.get_tick_data(code, date_str)
            is_empty = '当天没有数据' in df['time'][0]
            if is_empty :
                start_date = get_last_day(start_date)
                continue
            df = df.fillna(0)
            df = df.replace('--',0)
            df = df.sort_values(by='time', ascending=True)
            for index, row in df.iterrows():
                add_to_db(code, row, date_str)
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


def add_to_db(code, item, date_str):

    #查看tick_data里是不是有
    tick_is_exist = TickHistData.query.filter_by(code=code, date=date_str, time=item.time).first()
    if tick_is_exist is None:
        tick_new = TickHistData(code=code, date=date_str, time=item['time'], price=item['price'], change=item['change'],
                                 volume=item['volume'], amount=item['amount'], type=item['type'])
        db.session.add(tick_new)


def commit_to_db():
    db.session.commit()
