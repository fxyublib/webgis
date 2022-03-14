# -*-coding:utf-8 -*-

import os, sys
import math
import urllib.request 
import PIL.Image as Image
from PIL import ImageDraw, ImageFont

import urllib
import time
import random
import datetime

def downloadImage(img_url, fname, mylog):
    try:
        urllib.request.urlretrieve(img_url,filename=fname)
    except IOError as e:
        print("--", fname, "->", e)
        print(img_url, file=mylog)
    except Exception as e:
        print("--", fname, "->", e)
        print(img_url, file=mylog)

def downloadImage2(img_url, fname, mylog):
    agents = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1']
    try:
        req = urllib.request.Request(img_url)
        req.add_header('User-Agent', random.choice(agents))
        response = urllib.request.urlopen(req)
        bytes = response.read()
    except Exception as e:
        print("--", fname, "->", e)
        print(img_url, file=mylog)
        sys.exit(1)
    
    if bytes.startswith(b"<html>"):
        print("-- forbidden", fname)
        print(img_url, file=mylog)
        sys.exit(1)
    
    print("-- saving", fname)
    
    f = open(fname,'wb')
    f.write(bytes)
    f.close()
    
    #time.sleep(1 + random.random())

# 切片行列号反算经纬度
def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)

# 经纬度反算切片行列号,3857坐标系
def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def getImageUrl(x, y, zoom):
    #Google影像瓦片
    img_url = 'http://mt2.google.cn/vt/lyrs=y&hl=zh-CN&gl=CN&src=app&x='+str(x)+'&y='+str(y)+'&z='+str(zoom)+'&s=G'
    # img_url = 'http://mt2.google.cn/vt/lyrs=y&hl=zh-CN&gl=CN&src=app&x='+str(x)+'&y='+str(y)+'&z='+str(zoom)+'&s=G'
    #谷歌卫星地图
    #http://mt3.google.cn/vt/lyrs=s&hl=zh-CN&gl=cn&x={x}&y={y}&z={z}
    #谷歌地形+矢量图
    #http://mt2.google.cn/vt/lyrs=p&hl=zh-CN&gl=cn&x={x}&y={y}&z={z}
    # https://mts0.googleapis.com/vt?lyrs=s&x=0&y=0&z=0

    # m：路线图
    # t：地形图
    # ​p：带标签的地形图
    # ​s：卫星图
    # y：带标签的卫星图
    # ​h：标签层（路名、地名等）

    # 地图图层说明：
    # h skeleton map light http://mt2.google.cn/vt/lyrs=h&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # m 全地图 http://mt2.google.cn/vt/lyrs=m&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # p terrain+map http://mt2.google.cn/vt/lyrs=p&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # r skeleton map dark http://mt2.google.cn/vt/lyrs=r&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # y hybrid satellite map http://mt1.google.cn/vt/lyrs=y&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # t 地形图 http://mt0.google.cn/vt/lyrs=t&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # s 卫星地图 http://mt3.google.cn/vt/lyrs=s&hl=zh-CN&gl=cn&x=420&y=193&z=9
    # 也可以进行组合，例如：s,r 或者 t,h http://mt3.google.cn/vt/lyrs=t,h&hl=zh-CN&gl=cn&x=420&y=193&z=9

    #高德瓦片，wprd03想必是和谷歌一样，有多个服务器提供服务。测试下来可以取到01 到 04。
    img_url = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&style=6'.format(x=x, y=y, z=zoom)
    #img_url = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7&ltype=0'.format(x=x, y=y, z=zoom)
    img_url = 'https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'.format(x=x, y=y, z=zoom)
    img_url = 'https://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile//{z}/{y}/{x}'.format(x=x, y=y, z=zoom)
               
    #天地图-地图
    #img_url = 'http://t4.tianditu.com/DataServer?T=vec_w&x='+str(x)+'&y='+str(y)+'&l='+str(zoom)+'&tk=45c78b2bc2ecfa2b35a3e4e454ada5ce'
    #天地图-标注
    #img_url = 'http://t3.tianditu.com/DataServer?T=cva_w&x='+str(x)+'&y='+str(y)+'&l='+str(zoom)+'&tk=45c78b2bc2ecfa2b35a3e4e454ada5ce'
    #天地图-影像
    #img_url = 'http://t2.tianditu.gov.cn/DataServer?T=img_w&x='+str(x)+'&y='+str(y)+'&l='+str(zoom)+'&tk=2ce94f67e58faa24beb7cb8a09780552'
    #天地图-影像标注
    #img_url = 'http://t2.tianditu.gov.cn/DataServer?T=cia_w&x='+str(x)+'&y='+str(y)+'&l='+str(zoom)+'&tk=2ce94f67e58faa24beb7cb8a09780552'

    return img_url

def getAndCheckImageFilePath(file_path, x, y, zoom):
    path = file_path + "/" +  str(zoom) + "/" + str(x)
    if not os.path.exists(path):
        os.makedirs(path)
    return getImageFilePath(file_path, x, y, zoom)

def getImageFilePath(file_path, x, y, zoom):
    return file_path + "/" +  str(zoom) + "/" + str(x) + '/'+ str(y)+'.png'

#################################################################
# 图片拼接
#################################################################

def mergeAllImageToOne(file_path, zoom, params):
    xmin = params[0]
    ymin = params[1]
    xmax = xmin + params[2]
    ymax = ymin + params[3]
    mw = 256 
    toImage = Image.new('RGB', (256*(xmax-xmin), 256*(ymax-ymin)) )

    for x in range(xmin, xmax):
        for y in range(ymin, ymax):
        
            fname = getImageFilePath(file_path, x, y, zoom)
            fromImage = Image.open(fname)
            fromImage = fromImage.convert('RGB')
            draw = ImageDraw.Draw(fromImage)
            
            # 添加每个瓦片的文字信息
            fontSize = 18
            setFont = ImageFont.truetype('C:/windows/fonts/arial.ttf', fontSize)
            fillColor = "#ff0000"
            pos = num2deg(x, y, zoom)
            text = 'Tile: ' + str(x)+ "," + str(y)+ "," + str(zoom)
            text2 = 'Lat: %.6f'%pos[0]
            text3 = 'Lon: %.6f'%pos[1]
            draw.text((1,1), text,font=setFont,fill=fillColor)
            draw.text((1,1+fontSize), text2,font=setFont,fill=fillColor)
            draw.text((1,1+2*fontSize), text3,font=setFont,fill=fillColor)
            
            # 添加每个瓦片的边框线条
            draw.rectangle([0, 0, mw-1, mw-1], fill=None, outline='red', width=1)
            
            # 将每个瓦片的小图绘制到大图里面。
            toImage.paste(fromImage, ((x-xmin) * mw, (y-ymin) * mw))

    toImage.save(file_path + '/' + str(zoom) +'/preview.png' )
    toImage.close()

#################################################################
# 图片拼接
#################################################################

def downloadMapAllImage(file_path, zoom, params):
    xmin = params[0]
    ymin = params[1]
    xmax = xmin + params[2]
    ymax = ymin + params[3]

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    mylog = open(file_path + '/err.log', mode = 'a',encoding='utf-8')

    for x in range(xmin, xmax):
        for y in range(ymin, ymax):

            img_url = getImageUrl(x, y, zoom)
            print(img_url)
            
            img_savepath = getAndCheckImageFilePath(file_path, x, y, zoom)
            print(img_savepath)

            if not os.path.exists(img_savepath):
                #downloadImage(img_url, img_savepath, mylog)     
                downloadImage2(img_url, img_savepath, mylog)

    mylog.close()

#################################################################

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    file_path='d:/maps11'

    # (1) 全球地图
    zoom = 4
    params = [0, 0, pow(2, zoom), pow(2, zoom)]

    # (2) 中国地图
    zoom = 5
    params = [22, 10, 6, 6]

    # (3) 局部地图
    # zoom = 18
    # params = [215768, 99253, 3, 3]

    downloadMapAllImage(file_path, zoom, params)
    mergeAllImageToOne(file_path, zoom, params)

    endtime = datetime.datetime.now()
    print("ok", (endtime - starttime).seconds)