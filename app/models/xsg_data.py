# -*- coding: UTF-8 -*-
from app import db

'''限售解禁股'''


class XsgData(db.Model):
    __tablename__ = 'xsg_data'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20),doc='名称')
    year = db.Column(db.Integer, doc='年份', primary_key=True)
    month = db.Column(db.Integer, doc='月份', primary_key=True)
    date = db.Column(db.String(10), doc='解禁日期')
    count = db.Column(db.Float, doc='解禁数量(万股)')
    ratio = db.Column(db.Float, doc='占总盘比率')

    def __init__(self, code, name, year, month, date, count, ratio):
        self.code = code
        self.name = name
        self.year = year
        self.month = month
        self.date = date
        self.count = count
        self.ratio = ratio

    def __repr__(self):
        return '<XsgData %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'year': self.year,
            'month': self.month,
            'date':self.date,
            'count':self.count,
            'ratio':self.ratio
        }