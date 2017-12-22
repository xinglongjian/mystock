# -*- coding: UTF-8 -*-
from app import db


class StockBasic(db.Model):
    __tablename__ = 'stock_basics'

    code = db.Column(db.String(10),doc='代码', primary_key=True)
    name = db.Column(db.String(20),doc='名称',index=True)
    date = db.Column(db.String(10), doc='日期', primary_key=True)
    pe = db.Column(db.Float, doc='市盈率')
    outstanding = db.Column(db.Float, doc='流通股本(亿)')
    totals = db.Column(db.Float, doc='总股本(亿)')
    total_assets = db.Column(db.Float, doc='总资产(万)')
    liquid_assets = db.Column(db.Float, doc='流动资产')
    fixed_assets = db.Column(db.Float, doc='固定资产')
    reserved = db.Column(db.Float, doc='公积金')
    reserved_per_share = db.Column(db.Float, doc='每股公积金')
    esp = db.Column(db.Float, doc='每股收益')
    bvps = db.Column(db.Float, doc='每股净资')
    pb = db.Column(db.Float, doc='市净率')
    undp = db.Column(db.Float, doc='未分利润')
    perundp = db.Column(db.Float, doc='每股未分配')
    rev = db.Column(db.Float, doc='收入同比(%)')
    profit = db.Column(db.Float, doc='利润同比(%)')
    gpr = db.Column(db.Float, doc='毛利率(%)')
    npr = db.Column(db.Float, doc='净利润率(%)')
    holders = db.Column(db.Integer, doc='股东人数')

    def __init__(self, code, name, date, pe, outstanding, totals, total_assets, liquid_assets, fixed_assets, reserved,
                 reserved_per_share, esp, bvps, pb, undp, perundp, rev, profit, gpr, npr, holders):
        self.code = code
        self.name = name
        self.date = date
        self.pe = pe
        self.outstanding = outstanding
        self.totals = totals
        self.total_assets = total_assets
        self.liquid_assets = liquid_assets
        self.fixed_assets = fixed_assets
        self.reserved = reserved
        self.reserved_per_share = reserved_per_share
        self.esp = esp
        self.bvps = bvps
        self.pb = pb
        self.undp = undp
        self.perundp = perundp
        self.rev = rev
        self.profit = profit
        self.gpr = gpr
        self.npr = npr
        self.holders = holders


    def __repr__(self):
        return '<StockBasic %r>' % self.code

    def to_json(self):
        return {
            'code': self.code,
            'name': self.name,
            'date':self.date,
            'pe':self.pe,
            'outstanding':self.outstanding,
            'totals': self.totals,
            'total_assets': self.total_assets,
            'liquid_assets': self.liquid_assets,
            'fixed_assets': self.fixed_assets,
            'reserved':self.reserved,
            'reserved_per_share':self.reserved_per_share,
            'esp':self.esp,
            'bvps':self.bvps,
            'pb':self.pb,
            'undp': self.undp,
            'perundp': self.perundp,
            'rev':self.rev,
            'profit':self.profit,
            'gpr':self.gpr,
            'npr':self.npr,
            'holders':self.holders

        }