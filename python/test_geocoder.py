# 根据文字查坐标
import json
from urllib.request import urlopen, quote
import requests
# def getlnglat(address):
#     url = 'https://api.map.baidu.com/geocoding/v3/'
#     output = 'json'
#     ak = 'f247cdb592eb43ebac6ccd27f796e2d2' # 你申请的ak
#     address = quote(address) # 由于本文地址变量为中文，为防止乱码，先用quote进行编码
#     uri = url + '?' + 'address=' + address  + '&output=' + output + '&ak=' + ak +""
#     req = urlopen(uri)
#     res = req.read().decode() 
#     print(res)
#     temp = json.loads(res)
#     print(temp)

#     # result = temp['result']
#     # lat = result['location']['lat']
#     # lng = result['location']['lng']
#     # print(result['precise'],result['confidence'],result['comprehension'],result['level'])
#     # return (lat, lng),(lng,lat)
# getlnglat('特克斯县的中心太极坛')

# import requests

# addr="上海市浦东新区世博园区"
# key="f247cdb592eb43ebac6ccd27f796e2d2"
# url= f'http://api.map.baidu.com/geocoder?address={addr}&output=json&key={key}'
# ret = requests.get(url).json()

# print("**************************************")
# print("【地址转经纬度】：", ret)
# print(ret['result']['location'])

# lng_lat=[121.498794,31.182546]
# key="f247cdb592eb43ebac6ccd27f796e2d2"
# url=f"http://api.map.baidu.com/geocoder?callback=renderReverse&location={lng_lat[1]},{lng_lat[0]}&output=json&pois=1&key={key}"
# ret = requests.get(url).json()
# print("**************************************")
# print("【经纬度转地址】：", ret)

# import requests
# def geocoding(addr):
#     key="f247cdb592eb43ebac6ccd27f796e2d2"
#     url= f'http://api.map.baidu.com/geocoder?address={addr}&output=json&key={key}'
#     hjson=requests.get(url).json()
#     lng = hjson['result']['location']['lng'] # 经度
#     lat = hjson['result']['location']['lat'] # 纬度
#     #lng_lat = [lng, lat]
#     #因为要用于UDF，所以这里返回字符串而非列表
#     return f"{lng},{lat}"

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
# geolocator = Nominatim(user_agent="test",timeout=None)
# result = geolocator.geocode("浙江省浙江大学")
# if result != None:
#     print(result)
#     print("latitude: ", result.latitude)
#     print("longitude: ", result.longitude)
#     print("address: ", result.address)
#     print("altitude: ", result.altitude)
#     print("point: ", result.point)
# else:
#     print("No data.")

# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="test",timeout=None)
# lat = 30.2768278
# lon = 120.13663990955736
# print('.....{}, {}........'.format(lat, lon))
# result = geolocator.reverse([lat, lon])
# if result != None:
#     print(result)
#     print("latitude: ", result.latitude)
#     print("longitude: ", result.longitude)
#     print("address: ", result.address)
#     print("altitude: ", result.altitude)
#     print("point: ", result.point)
#     print("raw: ", result.raw)
# else:
#     print("No data.")



# rectangles_df=df["LatLong"].head(2)
# location=rectangles_df.apply(geolocator.reverse)

# import geocoder
# g = geocoder.arcgis('Harvard University')
# print(g.latlng)
# print(g.geojson)
# print(g.json)
# print(g.wkt)
# print(g.osm)

# import geocoder
# g = geocoder.arcgis([31.18698, 121.48482], method='reverse')
# print(g.address)
# print(g.json)

# import geocoder
# g = geocoder.osm("453 Booth Street, Ottawa ON")
# print(g.housenumber)
# print(g.postal)
# print(g.street)

# import geocoder
# g = geocoder.osm("Harvard University")
# print(g.bbox)
# # print(g.geojson['bbox'])
# print(g.southwest)

# import requests
 
# url = 'https://nominatim.openstreetmap.org/search.php?q=哈佛大学&format=jsonv2'
# response = requests.get(url)
# print(response.text)
# # print(response.json())
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)

# import requests

# url = 'https://nominatim.openstreetmap.org/reverse.php?lat=42.36790855&lon=-71.12678237443698&zoom=18&format=jsonv2'
# response = requests.get(url)
# print(response.text)
# print(response.json())

# import requests
# url = 'https://nominatim.openstreetmap.org/search.php'
# params = {'q': '哈佛大学', 'format': 'jsonv2'}
# response = requests.get(url, params=params)
# print(response.text)

# import requests
# url = 'https://nominatim.openstreetmap.org/reverse.php'
# params = {'lat': '42.36790855', 'lon': '-71.12678237443698', 'format': 'jsonv2'}
# response = requests.get(url, params=params)
# print(response.text)

import geocoder
print(dir(geocoder))