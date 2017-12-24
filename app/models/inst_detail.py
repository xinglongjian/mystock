# -*- coding: UTF-8 -*-
from .db import db

'''机构成交明细
获取最近一个交易日机构席位成交明细统计情况

每个交易日获取一次
'''


class InstDetail(db.Model):
    __tablename__ = 'inst_detail'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20), doc='名称')
    date = db.Column(db.String(10),doc='日期',primary_key=True)
    bamount = db.Column(db.Float, doc='机构席位买入额(万)')
    samount = db.Column(db.Float, doc='机构席位卖出额(万)')
    type = db.Column(db.String(50), doc='类型')

    def __init__(self, code, name, date, bamount, samount, type):
        self.code = code
        self.name = name
        self.date = date
        self.bamount = bamount
        self.samount = samount
        self.type = type

    def __repr__(self):
        return '<InstDetail %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'date': self.date,
            'bamount': self.bamount,
            'samount': self.samount,
            'type': self.type
        }