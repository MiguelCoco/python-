# coding = 'utf-8'

import urllib.request as ur
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import time
import random

headers = [{ 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/39.0.2171.95 Safari/537.36',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
			{'User-Agent':'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
			{'User-Agent':'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
			{'User-Agent':'Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
			{'User-Agent':'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
			{'User-Agent':'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}]

#创建函数，从去哪网上海景点页面获取所有景点对应的link
def get_links(url,headers):
	try:
		#模拟浏览器，随机选取一个请求头
		headers = random.choice(headers)
		req = ur.Request(url,headers=headers)
		html = ur.urlopen(req)
	except URLError:
		return None
	try:
		bs_obj = bs(html,'html5lib')
		#使用两个属性，筛掉重复项
		link_list = bs_obj.findAll('a',{'class':'titlink','data-beacon':"poi"})
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	links = []
	try:
		for link in link_list:
			links.append(link['href'])
	except AttributeError:
		return None
	return links

#创建函数，获取景点具体内容
def get_contents(url,headers):
	try:
		headers = random.choice(headers)
		req = ur.Request(url,headers=headers)
		html = ur.urlopen(req)
	except URLError:
		return None
	try:
		bs_obj = bs(html,'html5lib')
		title = bs_obj.find('h1',{'class':'tit'}).get_text()
		rating = bs_obj.find('span',{'class':'sum'}).get_text()
		description = bs_obj.find('p',{'style':'text-indent: 2em'}).get_text()
		address = bs_obj.tbody.span.get_text()
		open_time = bs_obj.find('td',{'class':'td_r'}).get_text()
		charge = bs_obj.find('div',{'class':'e_db_content_box e_db_content_dont_indent'}).get_text()
		content = title+'\n' + rating+'\n' + description+'\n' + address+'\n' + open_time+'\n' + charge+'\n'
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	return print(content)

#创建循环，获取所有link和景点内容
i = 1
while i < 201:
	#上海景点URL
	url ='http://travel.qunar.com/p-cs299878-shanghai-jingdian-1-{}'.format(i)
	i += 1
	get_links(url,headers)
	for new_url in get_links(url,headers):
		print(get_contents(new_url,headers))
		#睡眠5秒，减轻服务器压力
		time.sleep(3)
