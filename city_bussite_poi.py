# coding ='utf-8'
import requests 
import json

#loc_1和loc_2是城市行政区左下坐标和右上坐标
loc_1 =[39.379134,115.446316]
loc_2 = [41.085189,117.900402]

#步长根据测试选择相对合适的值
step = 0.08
#for循环嵌套，获取loc_2与loc_1间步长0.08的矩形区域列表
loc_fin = []
for a in range(1,int((loc_2[0]-loc_1[0])/step+1)+1):
	for b in range(1,int((loc_2[1]-loc_1[1])/step+1)+1):
		lat_1 = round((loc_1[0]+step*a),6)
		lon_1 = round((loc_1[1]+step*b),6)
		lat_2 = round((lat_1-step),6)
		lon_2 = round((lon_1-step),6)
		loc_fin.append(str(lat_2)+","+str(lon_2)+','+str(lat_1)+','+str(lon_1))
#print(loc_fin)

url = 'http://api.map.baidu.com/place/v2/search?'
#for循环遍历loc_2与loc_1间步长0.08的矩形区域列表
for loc in loc_fin:
	params = {
		'query':'公交车站',
		'bounds':loc,
		'output':'json',
		'page_size':'20',
		'ak':'G4rOuo6mHVvNtSU7PpRLTsWdz51oT4ho'
		}
	http_page = requests.get(url,params)
	result = http_page.json()
	#剔除为空返回结果
	if result['total'] != 0:
		total = result['total']
		result_list = result['results']
		for a in result_list:
			name = a['name']
			lat = a['location']['lat']
			lng = a['location']['lng']
			info = name+','+str(lat)+','+str(lng)+'\n'
			with open('city_bus_poi.txt','a') as f:
				f.write(info)
			print(info)
