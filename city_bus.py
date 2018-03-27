# coding = 'utf-8'

import requests 
import json
import time
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
"""通过8684公交获取城市公交线路站点及站点坐标"""

#创建城市
city = 'beijing'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) + \
		AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}
url_1 = 'http://'+city+'.8684.cn'

#创建函数，获取各值开头的链接
def get_html_1(url_1,headers):
	try:
		#模拟浏览器Chrome
		html_1 = requests.get(url_1,headers=headers)
	except URLError:
		return None
	try:
		html_1_contents = bs(html_1.text,'html5lib')
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	try:
		bus_kt_r1 = html_1_contents.find('div',{'class':'bus_kt_r1'})
		bus_kt_r2 = html_1_contents.find('div',{'class':'bus_kt_r2'})
		#获取所有链接
		links_1_list = []
		for r1 in bus_kt_r1:
			links_1_list.append(r1['href'])
		for r2 in bus_kt_r2:
			links_1_list.append(r2['href'])
	except AttributeError:
		return None
	return links_1_list

#创建函数，获取某值开头的所有公交线路的链接
def get_html_2(url_2,headers):
	try:
		html_2 = requests.get(url_2,headers=headers)
	except URLError:
		return None
	try:
		html_2_contents = bs(html_2.text,'html5lib')
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	try:
		stie_list = html_2_contents.find('div',{'id':'con_site_1','class':'stie_list'})
		links_2_list = []
		for link in stie_list:
			links_2_list.append(link['href'])
	except AttributeError:
		return None
	return links_2_list


def get_html_3_up(url_3,headers):
	try:
		html_3 = requests.get(url_3,headers=headers)
	except URLError:
		return None
	try:
		html_3_contents = bs(html_3.text,'html5lib')
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	try:
		bus_line_txt = html_3_contents.findAll('div',{'class':'bus_line_txt'})
		bus_line_up = bus_line_txt[0].strong.get_text()	
		print(bus_line_up)
		bus_line_site = html_3_contents.findAll('div',{'class':'bus_site_layer'})
		bus_site_up = bus_line_site[0].findAll('a')
		bus_site_up_list = []
		for a in bus_site_up:
			bus_site_up_list.append(a.get_text())
	except AttributeError:
		return None
	return bus_site_up_list

#创建函数，获取具体公交线路下行站点名称			
def get_html_3_down(url_3,headers):
	try:
		html_3 = requests.get(url_3,headers=headers)
	except URLError:
		return None
	try:
		html_3_contents = bs(html_3.text,'html5lib')
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	try:
		bus_line_txt = html_3_contents.findAll('div',{'class':'bus_line_txt'})
		bus_line_down = bus_line_txt[1].strong.get_text()
		print(bus_line_down)
		bus_line_site = html_3_contents.findAll('div',{'class':'bus_site_layer'})
		bus_site_down = bus_line_site[1].findAll('a')
		bus_site_down_list = []
		for b in bus_site_down:
			bus_site_down_list.append(b.get_text())
	except IndexError:
		return None
	except AttributeError:
		return None
	return bus_site_down_list					

#创建函数，调用百度地图API，获取站点对应坐标
def get_x_y(address):
	url = 'http://api.map.baidu.com/geocoder/v2/?'
	params = {'address':'北京市'+address+'公交站',
			'city':'北京市',
			'ret_coordtype':'bd09ll',
			'ak':'G4rOuo*******************51oT4ho',
			'output':'json',
			}
	http_page = requests.get(url,params)
	http_contents = http_page.json()
	lng = http_contents['result']['location']['lng']
	lat = http_contents['result']['location']['lat']
	result = address + ':' + str(lng) + ',' + str(lat)
	print(result)

#嵌套循环，调用函数，获取城市所有公交线路名称、站点及坐标			
for a in get_html_1(url_1,headers):
	for b in get_html_2(url_1 + a,headers):
		try:
			for address in get_html_3_up(url_1 + b,headers):
				get_x_y(address)
			for address in get_html_3_down(url_1 + b,headers):
				get_x_y(address)
				#休眠3秒
				time.sleep(3) 
		#一股脑异常处理
		except TypeError:
			continue
		except KeyError:
			continue
		except AttributeError:
			continue

#不反爬，请求头较少
#未设置IP代理池
#没有写入文件/数据库
#部分异常处理不动脑
#3层for循环运行稍慢
