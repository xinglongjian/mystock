# -*- coding: UTF-8 -*-
from json import JSONEncoder

from flask import request, jsonify, make_response,json
from app.models import *
from app.api import api
from flask_jsontools import jsonapi
from util import AlchemyEncoder
import numpy as np
import json


@api.route('/apidemo', methods=['GET', 'POST'])
def api_demo():
    """返回一个json数据接口示例"""
    json_response = dict(errCode='1', errMsg="操作成功")
    response = jsonify(json_response)
    return response

@api.route("/stock_basic")
def select_stock_basic():
    """查询公司基本面情况"""
    code = request.args.get('code', '')
    date = request.args.get('date', '')
    page = request.args.get('page',1)
    page_size = request.args.get('pageSize',30)
    query = StockBasic.query
    if not date:
        date = db.session.query(db.func.max(StockBasic.date)).first()[0]
    query = query.filter_by(date = date).filter(StockBasic.pe > 0)
    result = query.paginate(page=int(page),per_page=int(page_size),error_out=False)
    json_items = [item.to_json() for item in result.items]
    response = {'total':result.total,'items':json_items}
    rst = make_response(jsonify(response))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    return rst