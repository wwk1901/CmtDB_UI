# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:48:24 2018

@author: 李弘一萌
"""

import pandas as pd
from datetime import datetime
from .I_Base import I_Base
from . import I_SpotPrice, I_Upstream, I_FuturesPrice, I_Macro
from ...Base.Spread_Generate import main_month_quote_2_spread_series
from ...Base.DataType_Base import Manual, Computed, WindData
from ...Base.Plot_Base import Plot_Base
from matplotlib.ticker import FuncFormatter

class spread_base(I_Base, Plot_Base):
    table_english_name = "Spread"
    table_chinese_name = u"价差"
#    original_db_filepath = data_path + u"LPP价格数据库.xlsx"
    
    def output(self):
        print("Spread")
    
    def get_relevant_df(self, col_list):
        ts_list = [eval(I_Base.get_table_class_full_variable(x))().get_ts() for x in col_list]
        tmp_table_df = pd.concat(ts_list, axis=1).dropna(how="all")
        return tmp_table_df  
    

    
###########################################################################################################################
""" 基差(计算指标) """ 


class TieKuangJiCha_01HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"铁矿基差_01合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"铁矿车板价_澳大利亚金布巴粉61%_青岛港", u"I01合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)        
        tmp_total[self.col_name] = tmp_total[u"铁矿车板价_澳大利亚金布巴粉61%_青岛港"] / 0.93 + 25 - tmp_total[u"I01合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TieKuangJiCha_01HeYue, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
class TieKuangJiCha_05HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"铁矿基差_05合约"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"铁矿车板价_澳大利亚金布巴粉61%_青岛港",  u"I05合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)        
        tmp_total[self.col_name] = tmp_total[u"铁矿车板价_澳大利亚金布巴粉61%_青岛港"] / 0.93 + 25 - tmp_total[u"I05合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TieKuangHeYueJiaCha_5_9, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis

class TieKuangJiCha_09HeYue(spread_base, Computed):
    field_name = u"基差"
    col_name = u"铁矿基差_09合约"
    axhline = 0
    
    def get_ts_whole_progress(self):
        relevant_col_list = [u"铁矿车板价_澳大利亚金布巴粉61%_青岛港",  u"I09合约收盘价"]
        tmp_total = self.get_relevant_df(relevant_col_list)        
        tmp_total[self.col_name] = tmp_total[u"铁矿车板价_澳大利亚金布巴粉61%_青岛港"] / 0.93 + 25 - tmp_total[u"I09合约收盘价"]
        return tmp_total
    
    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TieKuangHeYueJiaCha_9_1, self).seasonal_plot(title=self.col_name, axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis
    
    
###########################################################################################################################
""" 月间价差(计算指标) """ 

class TieKuangHeYueJiaCha_1_5(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"铁矿合约价差_1_5"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["01", "05"]
        all_main_quote_df = I_Base.get_I_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TieKuangHeYueJiaCha_1_5, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[1, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 1)
        return tmp_df_interpolated, fig, axis    
      

class TieKuangHeYueJiaCha_5_9(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"铁矿合约价差_5_9"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["05", "09"]
        all_main_quote_df = I_Base.get_I_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TieKuangHeYueJiaCha_5_9, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[5, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 5)
        return tmp_df_interpolated, fig, axis   

class TieKuangHeYueJiaCha_9_1(spread_base, Computed):
    field_name = u"月间价差"
    col_name = u"铁矿合约价差_9_1"
    axhline = 0
    start_year = 2015
    def get_ts_whole_progress(self):
        month_list = ["09", "01"]
        all_main_quote_df = I_Base.get_I_main_month_quote_df()
        spread_series = main_month_quote_2_spread_series(month_list, all_main_quote_df)
        tmp_df = pd.DataFrame([spread_series], index=[self.col_name]).T
        return tmp_df

    def seasonal_plot(self, title=None, start_year=None, axhline=None):
        tmp_df_interpolated, fig, axis = super(TieKuangHeYueJiaCha_9_1, self).seasonal_plot(title=self.col_name, start_year = self.start_year, 
                                              axhline=self.axhline, date_constraint=[9, 17])
        axis = Plot_Base.add_month_span(axis, tmp_df_interpolated, 9)
        return tmp_df_interpolated, fig, axis


###########################################################################################################################
""" 现货价差(计算指标) """ 

class TieKuangXianHuoJiaCha_PBKuai_PBFen_QingDaoGang(spread_base, Computed):
    field_name = u"现货价差"
    col_name = u"铁矿现货价差_PB块-PB粉_青岛港"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"铁矿车板价_澳大利亚PB块矿62.5%_青岛港", "铁矿车板价_澳大利亚PB粉矿61.5%_青岛港"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"铁矿车板价_澳大利亚PB块矿62.5%_青岛港"] - tmp_total[u"铁矿车板价_澳大利亚PB粉矿61.5%_青岛港"]
        return tmp_total


class TieKuangXianHuoJiaCha_PBFen_YangDiFen_QingDaoGang(spread_base, Computed):
    field_name = u"现货价差"
    col_name = u"铁矿现货价差_PB粉-杨迪粉_青岛港"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"铁矿车板价_澳大利亚PB粉矿61.5%_青岛港", "铁矿车板价_澳大利亚杨迪粉58%_青岛港"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"铁矿车板价_澳大利亚PB粉矿61.5%_青岛港"] - tmp_total[u"铁矿车板价_澳大利亚杨迪粉58%_青岛港"]
        return tmp_total

class TieKuangXianHuoJiaCha_KaLaJiaSiFen_PBFen_QingDaoGang(spread_base, Computed):
    field_name = u"现货价差"
    col_name = u"铁矿现货价差_卡拉加斯粉-PB粉_青岛港"
    axhline = 0
    def get_ts_whole_progress(self):
        relevant_col_list = [u"铁矿车板价_澳大利亚PB粉矿61.5%_青岛港", "铁矿车板价_巴西卡拉加斯粉65%_青岛港"]
        tmp_total = self.get_relevant_df(relevant_col_list)
        tmp_total[self.col_name] = tmp_total[u"铁矿车板价_巴西卡拉加斯粉65%_青岛港"] - tmp_total[u"铁矿车板价_澳大利亚PB粉矿61.5%_青岛港"]
        return tmp_total














if __name__ == "__main__":
#    df = PISpread9_1().get_ts()
    df, fig, axis = LuoWenQiHuoJiaCha_1_5().seasonal_plot()
    
    
    
    
    
    
    
    
    
    
    
    
    
    