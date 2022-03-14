# from osgeo import gdal
# from osgeo.gdalconst import *
# import numpy as np


# gdal.AllRegister()
# driver = gdal.GetDriverByName('GTiff')
# print(driver)

# drv_count = gdal.GetDriverCount()
# print(drv_count)

# for idx in range(drv_count):
#     driver = gdal.GetDriver(idx)
#     print( "%10s: %s" % (driver.ShortName, driver.LongName))

import math

def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
  return (xtile, ytile)

def deg2url(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
  return 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7&ltype=0'.format(x=xtile, y=ytile, z=zoom)

def deg2numrange(lat_deg1, lon_deg1, lat_deg2, lon_deg2, zoom):
  tile1 = deg2num(lat_deg1, lon_deg1, zoom)
  tile2 = deg2num(lat_deg2, lon_deg2, zoom)
  tile1new = min(tile1[0], tile2[0]), min(tile1[1], tile2[1])
  tile2new = max(tile1[0], tile2[0]), max(tile1[1], tile2[1])
  return [tile1new[0], tile1new[1], tile2new[0] - tile1new[0], tile2new[1] - tile1new[1]]

# 输出瓦片坐标
print(deg2num(39.98836718933446, 116.31269474242018, 18))
# 输出瓦片网址
print(deg2url(39.90854390955025, 116.43579204294966, 18))
# 输出两个经纬度之间的瓦片坐标
print(deg2numrange(55.59490258792558, 73.125, -3.3087064670254187, 135.966796875, 5))
# print(deg2numrange(53.71287487574352, 69.24477328274534, -0.4121355821046667, 143.51235140774534, 7))
