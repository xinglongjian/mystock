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