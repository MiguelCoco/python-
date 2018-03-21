# coding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import datetime
import random
import re

#生成随机数种子
random.seed(datetime.datetime.now())
#创建函数，获取links列表
def get_links(article_url):
	try:
		html = urlopen("http://en.wikipedia.org" + article_url)
	#检查URLError，预防程序崩溃
	except URLError:
		print('URL is wrong!')
	try:	
		bs_obj = bs(html,'html5lib')
		#提取links
		links = bs_obj.find("div", {"id":"bodyContent"}).findAll("a",
			href=re.compile("^(/wiki/)((?!:).)*$"))
	#检查AttributeError,当bs_obj返回None时，bs_obj没有属性
	except AttributeError:
		return None
	#URLError出现时，html未定义，出现变量命名空间错误
	except UnboundLocalError:
		return None	
	return links
links_list = get_links("/wiki/Kevin_Bacon")
#links_list没有值时，返回TypeError
try:
	while len(links_list) > 0:
		try:
			#随机提取一条link
			newArticle = links_list[random.randint(0, len(links_list)-1)].attrs["href"]
		except AttributeError:
			print('attrs is not exist!')
		else:
			print(newArticle)
			links_list = get_links(newArticle)
except TypeError:
	print('links_list is not exist！')

	
	
