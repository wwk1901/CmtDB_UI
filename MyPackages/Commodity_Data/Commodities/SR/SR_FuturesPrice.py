# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:20:08 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .SR_Base import SR_Base
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

def month_quote_df_2_series(df):
    ts_list = []
    for col in df.columns.tolist():
        tmp_series = df[col].dropna()
        ts_list.append(tmp_series)
    result = pd.concat(ts_list)
    result = result[~result.index.duplicated()]
    return result

class futures_price_base(SR_Base, Plot_Base):
    table_english_name = "FuturesPrice"
    table_chinese_name = u"期货数据"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("FuturesPrice")
    
    def get_relevant_df(self, col_list):
        local_col_name_list = futures_price_base.get_all_table_classname()
        col_cls_list = []
        for x in col_list:
            col_cls_name = str(SR_Base.get_class_name(x))
            if col_cls_name not in local_col_name_list:
                col_cls_list.append(eval(SR_Base.get_table_class_full_variable(x)))
            else:
                col_cls_list.append(eval(col_cls_name))
        ts_list = [x().get_ts() for x in col_cls_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df 
    
    
        
###########################################################################################################################
""" 国内期货价格 """     

    
class SR01HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"国内期货价格"
    col_name = u"SR01合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_SR_quote_df(month=1)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class SR05HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"国内期货价格"
    col_name = u"SR05合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_SR_quote_df(month=5)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name
        return quote_ts.to_frame()


class SR09HeYueShouPanJia(futures_price_base, Computed):
    field_name = u"国内期货价格"
    col_name = u"SR09合约收盘价"
    def get_ts_whole_progress(self):
        quote_df = self.get_SR_quote_df(month=9)
        quote_ts = month_quote_df_2_series(quote_df)
        quote_ts.name = self.col_name  
        return quote_ts.to_frame()
    

###########################################################################################################################
""" 持仓数量 """ 

class No11TangFeiShangYeDuoTouChiCangLiang_ICE(futures_price_base, WindData):
    field_name = u"持仓数量"
    col_name = u"11号糖非商业多头持仓量_ICE"    
    wind_code = "S0107896"

class No11TangFeiShangYeKongTouChiCangLiang_ICE(futures_price_base, WindData):
    field_name = u"持仓数量"
    col_name = u"11号糖非商业空头持仓量_ICE"    
    wind_code = "S0107897"
    
class No11TangFeiShangYeTaoLiChiCangLiang_ICE(futures_price_base, WindData):
    field_name = u"持仓数量"
    col_name = u"11号糖非商业套利持仓量_ICE"    
    wind_code = "S0107898"
    
    
###########################################################################################################################
""" 外盘期货价格 """ 

class YuanTangJinYueHeYueJiaGe_ICE(futures_price_base, WindData):
    field_name = u"外盘期货价格"
    col_name = u"原糖近月合约价格_ICE"
    wind_code = "SBV18E.NYB"





    
if __name__ == "__main__":
    df = SR12HeYueShouPanJia().get_ts()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    