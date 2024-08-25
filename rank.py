#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#  @Time   :2024/8/21 14:02
#  @Author :Zhd
#  @File   :rank.py
import pandas as pd
from lxml import etree
from selenium import webdriver
#启动谷歌浏览器
driver = webdriver.Chrome()

url = "https://www.shanghairanking.cn/rankings/bcur/202411"
#访问URL
driver.get(url)
#浏览器最大化
driver.maximize_window()
#隐式等待
driver.implicitly_wait(10)
#保存结果的容器
contents = []
#获取全部的网页信息
html1 = driver.page_source

root = etree.HTML(html1)

#使用XPath 选择tbody下的所有tr节点
school_info_list = root.xpath('//tbody/tr')

for school_info in school_info_list:
    contents.append([
        school_info.xpath('./td[1]/div/text()')[0].replace('\n','').replace(' ',''),
        school_info.xpath('./td[2]/div/div[2]/div/div/div/span/text()')[0].replace('\n', '').replace(' ', ''),
        school_info.xpath('./td[3]/text()')[0].replace('\n', '').replace(' ', ''),
        school_info.xpath('./td[4]/text()')[0].replace('\n', '').replace(' ', ''),
        school_info.xpath('./td[5]/text()')[0].replace('\n', '').replace(' ', ''),
        school_info.xpath('./td[6]/text()')[0].replace('\n', '').replace(' ', ''),
    ])
print(contents)
first_name = ["排名","学校名称","省市","类型","总分","办学层次"]
rank = pd.DataFrame(contents, columns=first_name)
rank["排名"] = rank["排名"].astype(int)
rank["总分"] = rank["总分"].astype(float)
rank["办学层次"] = rank["办学层次"].apply(pd.to_numeric, errors = 'coerce')
print(rank.head(3))
rank.to_excel("2024中国大学排名.xlsx",index = False)
print("保存成功！")
driver.quit()