from flask import Blueprint

models = Blueprint('models', __name__)

from .stock import *
from .stock_basic import *
from .profit_data import *
from .hist_data_5 import *
from .hist_data_15 import *
from .hist_data_30 import *
from .hist_data_60 import *
from .hist_data_day import *
from .hist_data_week import *
from .hist_data_month import *
from .inst_detail import *
from .realtime_quotes import *
from .tick_hist_data import *
from .tick_today_data import *
from .top_caps import *
from .top_inst import *
from .top_tick_list import *
from .xsg_data import *