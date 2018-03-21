#coding = utf-8 
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
#创建函数get_title(),获取网页标题
def get_title(url):
	try:
		html = urlopen(url)
	except URLError:#检查URLError
		return None
	try:
		bs_obj = bs(html,'html5lib')
		title = bs_obj.h1
	except AttributeError:#检查AttributeError,当bs_obj返回None时，bs_obj将没有h1属性
		return None
	return title
title = get_title("http://www.pythonscraping.com/pages/page1.html")
if title == None:
	print('Title could not be found!')
else:
	print(title)
