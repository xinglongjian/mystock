# -*- coding: UTF-8 -*-
from .db import db

'''每日龙虎榜列表
按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现多条数据
'''


class TopTickList(db.Model):
    __tablename__ = 'top_tick_list'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20), doc='名称')
    date = db.Column(db.String(10),doc='日期',primary_key=True)
    reason = db.Column(db.String(100), doc='原因', primary_key=True)
    pchange = db.Column(db.Float, doc='当日涨跌幅')
    amount = db.Column(db.Float, doc='龙虎榜成交额(万)')
    buy = db.Column(db.Float, doc='买入额(万)')
    bratio = db.Column(db.Float, doc='买入占总成交比例')
    sell = db.Column(db.Float, doc='卖出额(万)')
    sratio = db.Column(db.Float, doc='卖出占总成交比例')

    def __init__(self, code, name, date, reason, pchange, amount, buy, bratio, sell, sratio):
        self.code = code
        self.name = name
        self.date = date
        self.reason = reason
        self.pchange = pchange
        self.amount = amount
        self.buy = buy
        self.bratio = bratio
        self.sell = sell
        self.sratio = sratio

    def __repr__(self):
        return '<TopTickList %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'date': self.date,
            'reason': self.reason,
            'pchange': self.pchange,
            'amount': self.amount,
            'buy': self.buy,
            'bratio': self.bratio,
            'sell': self.sell,
            'sratio': self.sratio
        }