# -*- coding: UTF-8 -*-
from .db import db

'''个股上榜统计
把近5、10、30、60日个股上榜统计数据

这里只获取5日的，然后后一天减去前一天的就是当天的变更
'''


class TopCaps(db.Model):
    __tablename__ = 'top_caps'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    date = db.Column(db.String(10), doc='日期', primary_key=True)
    name = db.Column(db.String(20),doc='名称')
    days = db.Column(db.Integer, doc='类型', primary_key=True)
    count = db.Column(db.Integer, doc='上榜次数')
    bamount = db.Column(db.Float, doc='累积购买额(万)')
    samount = db.Column(db.Float, doc='累积卖出额(万)')
    net = db.Column(db.Float, doc='净额(万)')
    bcount = db.Column(db.Integer, doc='买入席位数')
    scount = db.Column(db.Integer, doc='卖出席位数')

    def __init__(self, code, date, name, days, count, bamount, samount, net, bcount, scount):
        self.code = code
        self.date = date
        self.name = name
        self.days = days
        self.count = count
        self.bamount = bamount
        self.samount = samount
        self.net = net
        self.bcount = bcount
        self.scount = scount

    def __repr__(self):
        return '<TopCaps %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'date': self.date,
            'name': self.name,
            'days': self.days,
            'count': self.count,
            'bamount': self.bamount,
            'samount': self.samount,
            'net': self.net,
            'bcount': self.bcount,
            'scount': self.scount
        }