# -*- coding: UTF-8 -*-
from app import db

'''
股票的基本信息
'''
class Stock(db.Model):
    __tablename__ = 'stock'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20),doc='名称',index=True)
    industry = db.Column(db.String(20), doc='所属行业', index=True)
    area = db.Column(db.String(20), doc='地区', index=True)
    time_to_market = db.Column(db.String(10), doc='上市日期')

    def __init__(self, code, name, industry, area, time_to_market):
        self.code = code
        self.name = name
        self.industry = industry
        self.area = area
        self.time_to_market = time_to_market

    def __repr__(self):
        return '<Stock %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'industry': self.industry,
            'area':self.area,
            'time_to_market':self.time_to_market

        }