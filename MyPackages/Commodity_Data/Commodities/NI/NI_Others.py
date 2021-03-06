# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:18:01 2018

@author: Administrator
"""

import pandas as pd
from datetime import datetime
from .NI_Base import NI_Base
from ...Base.DataType_Base import Auto
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter
from . import NI_Macro

class others_base(NI_Base, Plot_Base):
    table_english_name = "Others"
    table_chinese_name = u"其他"
#    original_db_filepath = data_path + u"NIPP价格数据库.xlsx"

        

###########################################################################################################################
""" 增值税 """     
     
class ZengZhiShui(others_base, Auto):
    field_name = u"增值税"
    col_name = u"增值税"
    def get_ts(self):
        tmp_table_df = NI_Macro.JiQiHuiLv_MeiYuanDuiRenMinBi().get_ts()
        tmp_series = pd.Series([0.17] * len(tmp_table_df.index), index=tmp_table_df.index, name=u"增值税") 
        tmp_series.loc[tmp_series.index >= datetime(2018, 5, 1)] = 0.16    
        return tmp_series
    
