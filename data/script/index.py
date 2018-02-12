# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
import datetime
import csv

pd.set_option('expand_frame_repr',False)
today=datetime.date.today()
print(today)

#股票列表
# stock_file="/Users/baidu/PycharmProjects/mystock/data/csv/stock/all_base_stock_%s.txt" % today
# df_stock= ts.get_stock_basics()
# df_stock.to_csv(stock_file, encoding='utf-8',index=True, index_label='code', decimal='.')

# df = pd.read_csv(stock_file, encoding='utf-8',dtype={'code': str})
# print(df.head(10))

#实时行情
today_file="/Users/baidu/PycharmProjects/mystock/data/csv/stock/today_sale_stock_%s.txt" % today
df_today= ts.get_today_all()
df_today.to_csv(today_file, encoding='utf-8',index=False)
exit()
