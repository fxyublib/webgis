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

# pip install fake-useragent
# from fake_useragent import UserAgent
# ua = UserAgent()
# ua.chrome
# ua.ie
# ua.random

USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]
	
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
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20', 
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1']

    bytes = bytearray()
    try:
        req = urllib.request.Request(img_url)
        req.add_header('User-Agent', random.choice(agents))
        response = urllib.request.urlopen(req)
        bytes = response.read()

    except Exception as e:
        print("-- error", fname, "->", e)
        print(img_url, file=mylog)
        # sys.exit(1)
        return

    if bytes == None or len(bytes) == 0 or bytes.startswith(b"<html>"):
        print("-- forbidden", fname)
        print(img_url, file=mylog)
        # sys.exit(1)
        return
            
    f = open(fname,'wb')
    f.write(bytes)
    f.close()
    print("-- saving", fname)
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
    img_url = 'http://mt'+str(random.randint(0,3))+'.google.cn/vt/lyrs=y&hl=zh-CN&gl=CN&src=app&x='+str(x)+'&y='+str(y)+'&z='+str(zoom)+'&s=G'
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
    # img_url = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&style=6'.format(x=x, y=y, z=zoom)
    #img_url = 'https://wprd01.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7&ltype=0'.format(x=x, y=y, z=zoom)
    # img_url = 'https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'.format(x=x, y=y, z=zoom)
    # img_url = 'https://map.geoq.cn/ArcGIS/rest/services/ChinaOnlineCommunity/MapServer/tile//{z}/{y}/{x}'.format(x=x, y=y, z=zoom)
               
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
            img_savepath = getAndCheckImageFilePath(file_path, x, y, zoom)
            
            if not os.path.exists(img_savepath):
                print(img_url)
                print(img_savepath)
                #downloadImage(img_url, img_savepath, mylog)     
                downloadImage2(img_url, img_savepath, mylog)

    mylog.close()

#################################################################

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    file_path='d:/test/maps_google_y'

    # (1) 全球地图
    zoom = 7
    params = [0, 0, pow(2, zoom), pow(2, zoom)]

    # (2) 中国地图
    # zoom = 6
    # params = [22, 10, 6, 6]

    # (3) 局部地图
    # zoom = 18
    # params = [215768, 99253, 3, 3]

    downloadMapAllImage(file_path, zoom, params)
    mergeAllImageToOne(file_path, zoom, params)

    endtime = datetime.datetime.now()
    print("ok", (endtime - starttime).seconds)