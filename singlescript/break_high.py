#-*-coding=utf-8-*-
#获取破指定天数内的新高 比如破60日新高
import tushare as ts
import datetime
import time

stocks=ts.get_stock_basics()


def loop_all_stocks():
    stocks_pe = stocks[(stocks.pe>1) & (stocks.pe <20)]
    print(len(stocks_pe))
    for EachStockID in stocks_pe.index:
        try:
            if is_break_high(EachStockID, 10):
                print("High price on")
                print(EachStockID)
                print(stocks.ix[EachStockID]['name'])
                time.sleep(2)
        except Exception as e:
            pass



def is_break_high(stockID,days):
    end_day=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
    days=days*7/5
    start_day=end_day-datetime.timedelta(days)

    start_day=start_day.strftime("%Y-%m-%d")
    end_day=end_day.strftime("%Y-%m-%d")
    df=ts.get_h_data(stockID,start=start_day,end=end_day)

    period_high=df['high'].max()
    today_high=df.iloc[0]['high']
    if today_high>=period_high:
        return True
    else:
        return False

loop_all_stocks()