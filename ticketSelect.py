#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 18:33
# @Author  : 彦小明IT
# @File    : ticketSelect.py
# @Software: PyCharm
# @description： 实现火车票查询 输入：重庆 成都 2020-08-03
				# 爬虫项目，requests(不要)，selenium的webdriver
				# 1.入口页面
				# 2.信息如何填充
				# 3.获取信息， 如何展示

from selenium import webdriver
import time
from lxml import etree
from prettytable import PrettyTable
from color import Colored


# 判断元素是否存在,返回对应的文本
def getSeatInfo(target):
	t = target.xpath('./div')
	if t:
		return t[0].xpath('./text()')
	else:
		return target.xpath('./text()')


# 获取票信息
def getTicketInfo(start, end, date):
	color = Colored()
	info = []
	options = webdriver.ChromeOptions()
	options.add_argument('headless')  # 设置后台运行
	options.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36')
	driver = webdriver.Chrome(options=options)
	driver.get(r'https://www.12306.cn/index/')
	time.sleep(5)  # 可以等待相应元素出现之后，在进行接下来的逻辑操作
	# 模拟出发地点击
	driver.find_element_by_xpath('//*[@id="fromStationText"]').clear()
	driver.find_element_by_xpath('//*[@id="fromStationText"]').click()
	driver.find_element_by_xpath('//*[@id="fromStationText"]').send_keys(start)
	from_text = driver.find_elements_by_class_name('ralign')  # 使用tab键
	# 模拟输入城市，会产生推荐城市名的选择
	for i in from_text:
		if i.text == start:
			i.click()
			break
	# 模拟目的地点击
	driver.find_element_by_xpath('//*[@id="toStationText"]').clear()
	driver.find_element_by_xpath('//*[@id="toStationText"]').click()
	driver.find_element_by_xpath('//*[@id="toStationText"]').send_keys(end)
	from_text = driver.find_elements_by_class_name('ralign')
	for i in from_text:
		if i.text == end:
			i.click()
			break
	# 模拟日期
	t = driver.find_element_by_xpath('//*[@id="train_date"]')
	driver.execute_script('arguments[0].removeAttribute(\"readonly\")', t);
	t.clear()
	t.send_keys(date)
	# 单击查询按钮，使用js脚本进行单击
	t = driver.find_element_by_xpath('//*[@id="search_one"]')
	# t.click()
	driver.execute_script("arguments[0].click();", t)
	# 会产生新的页面，切换到数据页
	windows = driver.window_handles
	driver.close()
	driver.switch_to.window(windows[-1])
	time.sleep(5)
	# 解析页面，获取所需的数据
	selector = etree.HTML(driver.page_source)
	trs = selector.xpath('/html/body/div[8]/div[7]/table/tbody[1]/tr')
	for tr in trs[::2]:
		tds = tr.xpath('./td')
		trainNO = tds[0].xpath('./div/div[1]/div/a/text()')
		fromStation = tds[0].xpath('./div/div[2]/strong[1]/text()')
		toStation = tds[0].xpath('./div/div[2]/strong[2]/text()')
		fromTime = tds[0].xpath('./div/div[3]/strong[1]/text()')
		toTime = tds[0].xpath('./div/div[3]/strong[2]/text()')
		totalTime = tds[0].xpath('./div/div[4]/strong[1]/text()')
		timeDesc = tds[0].xpath('./div/div[4]/span/text()')
		specialSeat = getSeatInfo(tds[1])
		firstSeat = getSeatInfo(tds[2])
		secondSeat = getSeatInfo(tds[3])
		softSleeper = getSeatInfo(tds[4])
		firstSleeper = getSeatInfo(tds[5])
		moveSleeper = getSeatInfo(tds[6])
		secondSleeper = getSeatInfo(tds[7])
		softSeat = getSeatInfo(tds[8])
		hardSeat = getSeatInfo(tds[9])
		noSeat = getSeatInfo(tds[10])
		remark = tds[12].xpath('./a')
		if remark:
			remark = remark[0].xpath('./text()')
		else:
			remark = tds[12].xpath('./text()')
		trainNO = [color.blue(trainNO[0])]
		fromToStation = [color.green(fromStation[0])+'\n'+color.red(toStation[0])]
		fromToTime = [color.green(fromTime[0])+'\n'+color.red(toTime[0])]
		totalTime = [totalTime[0]+'\n'+ color.dim(timeDesc[0])]
		info.append(trainNO+fromToStation+fromToTime+totalTime+specialSeat+
		      firstSeat+secondSeat+softSleeper+firstSleeper+moveSleeper+secondSleeper+softSeat+hardSeat+noSeat+remark)
	# print(info)
	return info


if __name__ == '__main__':
	print("请输入查询车次（示例：重庆 成都 2020-07-15）")
	t = input()
	t = t.split(" ")
	if len(t) == 3:
		ticketInfo = getTicketInfo(t[0], t[1], t[2])
		table = PrettyTable()
		table.valign = 'm'
		table.field_names = ['车次', '出发站/终到站', '出发时间/到达时间', '历时', '特等座', '一等座',
	                         '二等座', '软卧', '一等卧', '动卧', '二等卧', '软座', '硬座', '无座', '备注']
		for info in ticketInfo:
			if len(info) == len(table.field_names):
				table.add_row(info)
				table.add_row([" "]*len(info))
		print(table)
	else:
		print("输入信息有误......")

