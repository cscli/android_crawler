import urllib.request
import re
import socket
header = {
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
};
now = open('url.txt','r')
now_list = now.readlines()
print(now_list)
logfile = open('log.txt','w+')
for url in now_list:
    #if url  in now_list and url:
        #pass
    try:

#url = 'https://www.wandoujia.com/apps/net.luoo.LuooFM'
        my_request = urllib.request.Request(url,headers = header)
        response = urllib.request.urlopen(my_request)
        #response = urllib.request.urlopen('https://www.wandoujia.com/apps/net.luoo.LuooFM',headers =header)
        readd = response.read()
        test=readd.decode('utf-8')

        #print(response.read().decode('utf-8'))

        m1 = re.search('data-name="(.*?)"',test)
        m2 = re.search('data-install="(.*?)"',test)
#<div.*?class="f18 mb20">(.*?)</div>      data-install="1220.8万
        name = m1.group(1) #apk文件名
        datainstall=m2.group(1)
        print(url.strip(),' ', name, ' ' , datainstall)
        #data = [url, nane, datainstall]
        logfile.writelines([url.strip(),',', name,',', datainstall, '\r\n'])
        logfile.flush()
        print(data)
    except Exception as e:
        print(url)
        logfile.writelines(url)
        pass
close(logfile)
close(now)
