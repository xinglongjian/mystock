# -*- coding: UTF-8 -*-
from datetime import date
from datetime import timedelta
from datetime import datetime


def get_date(year,month,day):

    return date(year,month,day)


def get_date_str(date_temp):
    return date(date_temp.year, date_temp.month, date_temp.day).strftime('%Y-%m-%d')


def get_datetime_str(date_temp):
    return datetime(date_temp.year, date_temp.month, date_temp.day, date_temp.hour, date_temp.minute, date_temp.second) \
        .strftime('%Y-%m-%d %H:%M:%S')


def get_today():
    return date.today()


def get_today_str():
    return str(date.today().date)


def get_last_day(date_temp):
    """
    获取前一天
    :return:
    """
    return date_temp + timedelta(days=-1)


def get_quarter_name(date_temp):
    """
    根据date获取季度
    :param date_temp: 
    :return: 
    """

    year = date_temp.year
    month = date_temp.month

    if month == 1 or month == 2 or month == 3:
        column = "{}Q1".format(year)
    elif month == 4 or month == 5 or month == 6:
        column = "{}Q2".format(year)
    elif month == 7 or month == 8 or month == 9:
        column = "{}Q3".format(year)
    elif month == 10 or month == 11 or month == 12:
        column = "{}Q4".format(year)
    else:
        column = None

    return column

def get_last_quarter_name(date_temp):
    """
    根据date获取上一季度
    :param date_temp: 
    :return: 
    """

    year = date_temp.year
    last_year = year - 1
    month = date_temp.month

    if month == 1 or month == 2 or month == 3:
        column = "{}Q4".format(last_year)
    elif month == 4 or month == 5 or month == 6:
        column = "{}Q1".format(year)
    elif month == 7 or month == 8 or month == 9:
        column = "{}Q2".format(year)
    elif month == 10 or month == 11 or month == 12:
        column = "{}Q3".format(year)
    else:
        column = None

    return column
def year_qua(date):
    mon = date[5:7]
    mon = int(mon)
    return[date[0:4], _quar(mon)]
    

def _quar(mon):
    if mon in [1, 2, 3]:
        return '1'
    elif mon in [4, 5, 6]:
        return '2'
    elif mon in [7, 8, 9]:
        return '3'
    elif mon in [10, 11, 12]:
        return '4'
    else:
        return None
 
 
def today():
    day = datetime.datetime.today().date()
    return str(day) 


def get_year():
    year = datetime.datetime.today().year
    return year


def get_month():
    month = datetime.datetime.today().month
    return month

def get_hour():
    return datetime.datetime.today().hour
    
    
def today_last_year():
    lasty = datetime.datetime.today().date() + datetime.timedelta(-365)
    return str(lasty)


def day_last_week(days=-7):
    lasty = datetime.datetime.today().date() + datetime.timedelta(days)
    return str(lasty)


def get_now():
    return time.strftime('%Y-%m-%d %H:%M:%S')


def int2time(timestamp):
    datearr = datetime.datetime.utcfromtimestamp(timestamp)
    timestr = datearr.strftime("%Y-%m-%d %H:%M:%S")
    return timestr


def diff_day(start=None, end=None):
    d1 = datetime.datetime.strptime(end, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(start, '%Y-%m-%d')
    delta = d1 - d2
    return delta.days


def get_quarts(start, end):
    idx = pd.period_range('Q'.join(year_qua(start)), 'Q'.join(year_qua(end)),
                          freq='Q-JAN')
    return [str(d).split('Q') for d in idx][::-1]


def trade_cal():
    '''
            交易日历
    isOpen=1是交易日，isOpen=0为休市
    '''
    df = pd.read_csv(ct.ALL_CAL_FILE)
    return df


def is_holiday(date):
    '''
            判断是否为交易日，返回True or False
    '''
    df = trade_cal()
    holiday = df[df.isOpen == 0]['calendarDate'].values
    if isinstance(date, str):
        today = datetime.datetime.strptime(date, '%Y-%m-%d')

    if today.isoweekday() in [6, 7] or str(date) in holiday:
        return True
    else:
        return False


def last_tddate():
    today = datetime.datetime.today().date()
    today=int(today.strftime("%w"))
    if today == 0:
        return day_last_week(-2)
    else:
        return day_last_week(-1)
        

def tt_dates(start='', end=''):
    startyear = int(start[0:4])
    endyear = int(end[0:4])
    dates = [d for d in range(startyear, endyear+1, 2)]
    return dates
    
    
def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))

def get_q_date(year=None, quarter=None):
    dt = {'1': '-03-31', '2': '-06-30', '3': '-09-30', '4': '-12-31'}
    return '%s%s'%(str(year), dt[str(quarter)])