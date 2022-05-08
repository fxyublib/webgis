# -*- coding: utf-8 -*-
import http, time, random
import urllib.request

def getHeader():
	"""
		随机请求头
	"""
    USER_AGENTS = [
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    ]

    user_agent = random.choice(USER_AGENTS)
    headers = {
        'User-Agent':user_agent
    }

    return headers
   
 
def requestImg(url, file_name, num_retries=3):
	"""
		下载并保存图片
		url：图片URI
		file_name：保存文件名
		num_retries：失败重连次数
	"""
    try:
        headers = getHeader()
        request = urllib.request.Request(url, headers=headers)
        res = urllib.request.urlopen(request)
        with open(file_name, "wb") as f:
            content = res.read()
            f.write(content)
            res.close()
    except urllib.error.HTTPError or urllib.error.URLError as e:
        print(e)
    except http.client.IncompleteRead or http.client.RemoteDisconnected as e:
        if num_retries == 0:
            return
        else:
            requestImg(url, file_name, num_retries - 1)



if __name__ == "__main__":
	
	# 基础瓦片URI
    base_url = 'http://t0.tianditu.gov.cn/img_w/wmts?SERVICE=WMTS&REQUEST=GetTile&VERSION=1.0.0&LAYER=img&STYLE=default&TILEMATRIXSET=w&FORMAT=tiles&TILEMATRIX=11&TILEROW=%s&TILECOL=%s&tk=xxxxx'
	
	# 给定瓦片行列范围，构造完整瓦片URI并下载
    for r in range(893, 896):
        for c in range(1668, 1671):
            print(r, c)
            url = base_url%(r, c)
            print(url)
            file_name = "./images/" + str(r) + "-" + str(c) + '.jpg'
            requestImg(url, file_name)
            time.sleep(random.random())

    print("------ok------")