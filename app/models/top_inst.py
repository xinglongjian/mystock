# -*- coding: UTF-8 -*-
from .db import db

'''机构席位追踪
获取机构近5、10、30、60日累积买卖次数和金额情况

这里只获取5日
'''


class TopInst(db.Model):
    __tablename__ = 'top_inst'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20), doc='名称')
    date = db.Column(db.String(10),doc='日期',primary_key=True)
    days = db.Column(db.Integer, doc='类型', primary_key=True)
    bamount = db.Column(db.Float, doc='累积买入额(万)')
    bcount = db.Column(db.Integer, doc='买入次数')
    samount = db.Column(db.Float, doc='累积卖出额(万)')
    scount = db.Column(db.Integer, doc='卖出次数')
    net = db.Column(db.Float, doc='净额(万)')

    def __init__(self, code, name, date, days, bamount, bcount, samount, scount, net):
        self.code = code
        self.name = name
        self.date = date
        self.days = days
        self.bamount = bamount
        self.bcount = bcount
        self.samount = samount
        self.scount = scount
        self.net = net

    def __repr__(self):
        return '<TopInst %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'date': self.date,
            'days': self.days,
            'bamount': self.bamount,
            'bcount': self.bcount,
            'samount': self.samount,
            'scount': self.scount,
            'net': self.net
        }