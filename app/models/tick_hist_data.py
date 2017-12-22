# -*- coding: UTF-8 -*-
from app import db

'''历史分笔
把过去每天每个时间的分笔数记录下来
'''


class TickHistData(db.Model):
    __tablename__ = 'tick_hist_data'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    date = db.Column(db.String(10),doc='日期',primary_key=True)
    time = db.Column(db.String(10), doc='时间', primary_key=True)
    price = db.Column(db.Float, doc='成交价格')
    change = db.Column(db.Float, doc='价格变动')
    volume = db.Column(db.Integer, doc='成交手')
    amount = db.Column(db.Integer, doc='成交金额(元)')
    type = db.Column(db.String(10), doc='买卖类型（买盘、卖盘、中性盘）')

    def __init__(self, code, date, time, price, change, volume, amount, type):
        self.code = code
        self.date = date
        self.time = time
        self.price = price
        self.change = change
        self.volume = volume
        self.amount = amount
        self.type = type

    def __repr__(self):
        return '<TickHistData %r>' % self.code

    __table_args__ = (
        # db.UniqueConstraint('code', 'date', 'time', name='ix_code_date_time'),
        db.Index('ix_code_date_time', 'code', 'date', 'time'),
    )

    def to_json(self):
        return {
            'code': self.code,
            'date': self.date,
            'time': self.time,
            'price': self.price,
            'change': self.change,
            'volume': self.volume,
            'amount': self.amount,
            'type': self.type
        }