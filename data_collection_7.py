# coding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.error import URLError
import string
import re

#创建函数，获取网站页面所有文本
def get_contents(url):
	try:
		html = urlopen(url)
	except URLError:
		print('URL is wrong!')
	try:
		bs_obj = bs(html,'html5lib')
		contents = bs_obj.find('div',{'id':'mw-content-text'}).get_text()
	except AttributeError:
		return None
	except UnboundLocalError:
		return None
	return contents

#创建函数，清洗文本
def clean_words(words):
	#re.sub(要替换,替换为,需替换的字符串)
	words = re.sub('\n+',' ',words)
	words = re.sub(' +',' ',words)
	words = re.sub('\[[0-9]*\]','',words)
	#编码为utf-8,解码为ascii
	words = bytes(words,'utf-8')#
	words = words.decode('ascii', 'ignore')
	clean_words = []
	#split()空格切片文本，返回列表
	words = words.split(' ')
	for item in words:
		#strip()清除字符串两边所有标点符号
		item = item.strip(string.punctuation)
		if len(item) > 1 or (item.lower()) == 'a' or (item.lower()) == 'i':
			clean_words.append(item)
	return clean_words

#创建函数，建立n-gram模型
def n_grams(words,n):
	words = clean_words(words)
	output = []
	for i in range(len(words)-n+1):
		output.append(words[i:i+n])
	return output


url ="http://en.wikipedia.org/wiki/Python_(programming_language)"
#调用函数，获取url包含文本
contents = get_contents(url)
#调用n-gram函数并打印n-gram模型结果
print(n_grams(contents,2))