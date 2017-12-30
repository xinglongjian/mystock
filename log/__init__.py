# -*- coding: UTF-8 -*-
import logging
import logging.handlers

log_filename = 'stock.log'


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='stock.log',
                    filemode='w')
logging.getLogger('apscheduler').setLevel(logging.DEBUG)