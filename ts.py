#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#  @Time   :2025/2/22 15:52
#  @Author :Zhd
#  @File   :ts.py
ts_list = ['fnd17_oxlcxspebq', 'fnd17_shsoutbs', 'fnd28_value_05191q', 'fnd28_value_05301q', 'fnd28_value_05302q', 'fnd17_pehigh','fnd17_pelow', 'fnd17_priceavg150day', 'fnd17_priceavg200day', 'fnd17_priceavg50day', 'fnd17_pxedra', 'fnd28_newa3_value_18191a', 'fnd28_value_02300a', 'mdl175_ebitda', 'mdl175_pain']
count =0
for i in range(len(ts_list)-1):
    for j in range(len(ts_list)-i-1):
        print('s_regression(ts_zscore('+ts_list[i]+', 500), ts_zscore('+ts_list[i+j+1]+', 500), 500)')

        count=count+1
print(count)


