# -*- coding: UTF-8 -*-
from app import db

'''当日分笔
当日的分笔情况，每次都清空
'''


class TickTodayData(db.Model):
    __tablename__ = 'tick_today_data'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    time = db.Column(db.String(10), doc='时间', primary_key=True)
    price = db.Column(db.Float, doc='成交价格')
    change = db.Column(db.Float, doc='价格变动')
    volume = db.Column(db.Integer, doc='成交手')
    amount = db.Column(db.Integer, doc='成交金额(元)')
    type = db.Column(db.String(10), doc='买卖类型（买盘、卖盘、中性盘）')

    def __init__(self, code, time, price, change, volume, amount, type):
        self.code = code
        self.time = time
        self.price = price
        self.change = change
        self.volume = volume
        self.amount = amount
        self.type = type

    def __repr__(self):
        return '<TickTodayData %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'time': self.time,
            'price': self.price,
            'change': self.change,
            'volume': self.volume,
            'amount': self.amount,
            'type': self.type
        }