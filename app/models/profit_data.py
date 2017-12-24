# -*- coding: UTF-8 -*-
from .db import db

'''分配预案'''


class ProfitData(db.Model):
    __tablename__ = 'profit_data'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20),doc='名称',index=True)
    year = db.Column(db.Integer, doc='年份', primary_key=True)
    report_date = db.Column(db.String(10), doc='公布日期')
    divi = db.Column(db.Float, doc='分红金额')
    shares = db.Column(db.Integer, doc='转赠和送股数')

    def __init__(self, code, name, year, report_date, divi, shares):
        self.code = code
        self.name = name
        self.year = year
        self.report_date = report_date
        self.divi = divi
        self.shares = shares

    def __repr__(self):
        return '<ProfitData %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'year': self.year,
            'report_date':self.report_date,
            'divi':self.divi,
            'shares':self.shares
        }