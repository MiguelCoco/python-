#coding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import re

#创建函数，获取img相对路径
def get_img_path(url):
	try:
		html = urlopen(url)
	except URLError:#检查URLError，预防程序崩溃
		print('URL is wrong!')
	try:
		bs_boj = bs(html,'html5lib')
		#正则表达式表达"../img/gifts/img1.jpg"
		images = bs_boj.findAll('img',{'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')}) 
	except AttributeError:#检查AttributeError,当bs_obj返回None时，bs_obj将没有h1属性
		return None
	except UnboundLocalError:#URLError出现时，html未定义，则出现错误
		return None
	for image in images:#for循环，打印所有img相对路径
		print(image)
get_img_path("http://www.pythonscraping.com/pages/page3.html")