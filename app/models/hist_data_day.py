# -*- coding: UTF-8 -*-
from .db import db

'''历史数据-日'''


class HistDataDay(db.Model):
    __tablename__ = 'hist_data_day'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    date = db.Column(db.String(20),doc='日期',primary_key=True)
    open = db.Column(db.Float, doc='开盘价')
    high = db.Column(db.Float, doc='最高价')
    close = db.Column(db.Float, doc='收盘价')
    low = db.Column(db.Float, doc='最低价')
    volume = db.Column(db.Float, doc='成交量')
    price_change = db.Column(db.Float, doc='价格变动')
    p_change = db.Column(db.Float, doc='涨跌幅')
    ma5 = db.Column(db.Float, doc='5日均价')
    ma10 = db.Column(db.Float, doc='10日均价')
    ma20 = db.Column(db.Float, doc='20日均价')
    v_ma5 = db.Column(db.Float, doc='5日均量')
    v_ma10 = db.Column(db.Float, doc='10日均量')
    v_ma20 = db.Column(db.Float, doc='20日均量')
    turnover = db.Column(db.Float, doc='换手率')

    def __init__(self):
        pass

    def __repr__(self):
        return '<ProfitData %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'date': self.date,
            'open': self.open,
            'high':self.high,
            'close':self.close,
            'volume':self.volume,
            'price_change': self.price_change,
            'p_change': self.p_change,
            'ma5':self.ma5,
            'ma10': self.ma10,
            'ma20': self.ma20,
            'v_ma5':self.v_ma5,
            'v_ma10': self.v_ma10,
            'v_ma20': self.v_ma20,
            'turnover':self.turnover
        }