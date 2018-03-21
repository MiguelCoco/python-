# coding = utf-8
import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

#创建downloaded文件夹
download_directory = 'downloaded'
base_url = "http://pythonscraping.com"
#创建函数，规范和标准化url
def get_absolute_url(base_url,source):
	if source.startswith('http://www.'):
		url = 'http://' + source[11:]
	elif source.startswith('http://'):
		url = source
	elif source.startswith('www.'):
		url = 'http://' + source[4:]
	else:
		url = base_url + '/' + source
	if base_url not in url:
		return None
	return url
#创建函数，os模块建立完整路径
def get_download_path(base_url,absolute_url,download_directory):
	path = absolute_url.replace('www.',"")
	path = path.replace(base_url,"")
	path = download_directory + path
	directory = os.path.dirname(path)

	if not os.path.exists(directory):
		os.makedirs(directory)

	return path

html = urlopen('http://pythonscraping.com')
bs_obj = bs(html,'html5lib')
download_list = bs_obj.findAll(src=True)

for download in download_list:
	file_url = get_absolute_url(base_url,download['src'])
	if file_url is not None:
		print(file_url)
urlretrieve(file_url,get_download_path(base_url,file_url,download_directory))