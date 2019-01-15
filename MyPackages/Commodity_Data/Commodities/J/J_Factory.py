# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:13:28 2018

@author: 李弘一萌
"""

import pandas as pd
from .J_Base import J_Base
from . import J_SpotPrice, J_FuturesPrice
from . import J_Inventory, J_Spread, J_SupplyDemandBalance
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy import and_



class J_Factory(object):
    @staticmethod
    def getobj(col):
        class_name, table_module_name = J_Base.get_col_class_table(col)
        tmp_obj = eval(table_module_name + "." + class_name)()
        return tmp_obj

    @staticmethod
    def getBaseObj():
        return J_Base()
        
if __name__ == "__main__":
    col_list = [u"PP拉丝价格_华东"]
    col = u"PP拉丝价格_华东"
    a = J_Factory().getobj(col)
    print(a.col_name)
#    bbb = a.get_ts()