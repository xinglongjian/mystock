from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config import *

jobstores = {
    'default': SQLAlchemyJobStore(url=mysqlurl)
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}

def myfunc():
    print('hello')

scheduler = BackgroundScheduler(daemonic=False,executors=executors)
scheduler.add_job(myfunc, 'interval', minutes=2)

# @schedudler.cron_schedule(second='*', day_of_week='0-', hour='9-12,13-15')
# def quote_send_sh_job():
#     print('a simple cron job start at')


