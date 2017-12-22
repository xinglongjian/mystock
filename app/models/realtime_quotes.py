# -*- coding: UTF-8 -*-
from app import db

'''实时分笔
可以监控单个股票实时价格情况
'''


class RealtimeQuotes(db.Model):
    __tablename__ = 'realtime_quotes'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20), doc='名称')
    date = db.Column(db.String(10),doc='日期',primary_key=True)
    time = db.Column(db.String(10), doc='时间', primary_key=True)
    open = db.Column(db.Float, doc='今日开盘价')
    pre_close = db.Column(db.Float, doc='昨日收盘价')
    price = db.Column(db.Float, doc='当前价格')
    high = db.Column(db.Float, doc='今日最高')
    low = db.Column(db.Float, doc='今日最低')
    bid = db.Column(db.Float, doc='竞买价，即买一报价')
    ask = db.Column(db.Float, doc='竞卖价，即卖一报价')
    volume = db.Column(db.Integer, doc='成交量,需要/100')
    amount = db.Column(db.Integer, doc='成交金额(元)')
    b1_v = db.Column(db.Integer, doc='委买一笔数')
    b1_p = db.Column(db.Float, doc='委买一价格')
    b2_v = db.Column(db.Integer, doc='委买二笔数')
    b2_p = db.Column(db.Float, doc='委买二价格')
    b3_v = db.Column(db.Integer, doc='委买三笔数')
    b3_p = db.Column(db.Float, doc='委买三价格')
    b4_v = db.Column(db.Integer, doc='委买四笔数')
    b4_p = db.Column(db.Float, doc='委买四价格')
    b5_v = db.Column(db.Integer, doc='委买五笔数')
    b5_p = db.Column(db.Float, doc='委买五价格')
    a1_v = db.Column(db.Integer, doc='委卖一笔数')
    a1_p = db.Column(db.Float, doc='委卖一价格')
    a2_v = db.Column(db.Integer, doc='委卖二笔数')
    a2_p = db.Column(db.Float, doc='委卖二价格')
    a3_v = db.Column(db.Integer, doc='委卖三笔数')
    a3_p = db.Column(db.Float, doc='委卖三价格')
    a4_v = db.Column(db.Integer, doc='委卖四笔数')
    a4_p = db.Column(db.Float, doc='委卖四价格')
    a5_v = db.Column(db.Integer, doc='委卖五笔数')
    a5_p = db.Column(db.Float, doc='委卖五价格')

    def __init__(self, code, name,date, time, open, pre_close, price, high, low, bid, ask, volume, amount, b1_v, b1_p,
                 b2_v, b2_p, b3_v, b3_p, b4_v, b4_p, b5_v, b5_p, a1_v, a1_p, a2_v, a2_p, a3_v, a3_p, a4_v, a4_p, a5_v, a5_p):
        self.code = code
        self.name = name
        self.date = date
        self.time = time
        self.open = open
        self.pre_close = pre_close
        self.price = price
        self.high = high
        self.low = low
        self.bid = bid
        self.ask = ask
        self.volume = volume
        self.amount = amount
        self.b1_v = b1_v
        self.b1_p = b1_p
        self.b2_v = b2_v
        self.b2_p = b2_p
        self.b3_v = b3_v
        self.b3_p = b3_p
        self.b4_v = b4_v
        self.b4_p = b4_p
        self.b5_v = b5_v
        self.b5_p = b5_p
        self.a1_v = a1_v
        self.a1_p = a1_p
        self.a2_v = a2_v
        self.a2_p = a2_p
        self.a3_v = a3_v
        self.a3_p = a3_p
        self.a4_v = a4_v
        self.a4_p = a4_p
        self.a5_v = a5_v
        self.a5_p = a5_p

    def __repr__(self):
        return '<RealtimeQuotes %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'date': self.date,
            'time': self.time,
            'open': self.open,
            'pre_close': self.pre_close,
            'price': self.price,
            'high': self.high,
            'low': self.low,
            'bid': self.bid,
            'ask': self.ask,
            'volume': self.volume,
            'amount': self.amount,
            'b1_v': self.b1_v,
            'b1_p': self.b1_p,
            'b2_v': self.b2_v,
            'b2_p': self.b2_p,
            'b3_v': self.b3_v,
            'b3_p': self.b3_p,
            'b4_v': self.b4_v,
            'b4_p': self.b4_p,
            'b5_v': self.b5_v,
            'b5_p': self.b5_p,
            'a1_v': self.a1_v,
            'a1_p': self.a1_p,
            'a2_v': self.a2_v,
            'a2_p': self.a2_p,
            'a3_v': self.a3_v,
            'a3_p': self.a3_p,
            'a4_v': self.a4_v,
            'a4_p': self.a4_p,
            'a5_v': self.a5_v,
            'a5_p': self.a5_p

        }