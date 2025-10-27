---
title: Authority - HackTheBox
url: https://darkwing.moe/2023/07/17/Authority-HackTheBox/
source: 喵喵喵喵
date: 2023-07-18
fetch_date: 2025-10-04T11:50:58.591626
---

# Authority - HackTheBox

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

Authority - HackTheBox

# Authority - HackTheBox

##### 2023-07-17

#### TOC

1. [1. 基本信息](#基本信息)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 80](#80)
   2. [2.2. 8443](#8443)
3. [3. SMB](#SMB)
   1. [3.1. Development](#Development)
   2. [3.2. main.yml](#main-yml)
   3. [3.3. mail.yml content](#mail-yml-content)
4. [4. Ansbile](#Ansbile)
5. [5. PWM](#PWM)
   1. [5.1. Configuration Manager](#Configuration-Manager)
   2. [5.2. Responder + ldap](#Responder-ldap)
6. [6. user flag](#user-flag)
7. [7. 提权信息](#提权信息)
8. [8. ADCS ESC1](#ADCS-ESC1)
9. [9. PassTheCert & root flag](#PassTheCert-amp-root-flag)
   1. [9.1. root flag](#root-flag)
   2. [9.2. hashdump](#hashdump)
10. [10. 参考资料](#参考资料)

# Authority - HackTheBox

2023-07-17

# 基本信息

* <https://app.hackthebox.com/machines/Authority>
* 10.10.11.222

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023071701.jpg)

# 端口扫描

80,445,8443,以及一些常见域端口：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.222 Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-17 13:40 CST Nmap scan report for 10.10.11.222 Host is up (0.12s latency). Not shown: 987 closed tcp ports (conn-refused) PORT     STATE SERVICE       VERSION 53/tcp   open  domain        Simple DNS Plus 80/tcp   open  http          Microsoft IIS httpd 10.0 |_http-title: IIS Windows Server | http-methods: |_  Potentially risky methods: TRACE |_http-server-header: Microsoft-IIS/10.0 88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-07-17 09:41:16Z) 135/tcp  open  msrpc         Microsoft Windows RPC 139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn 389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: authority.htb, Site: Default-First-Site-Name) | ssl-cert: Subject: | Subject Alternative Name: othername:<unsupported>, DNS:authority.htb.corp, DNS:htb.corp, DNS:HTB | Not valid before: 2022-08-09T23:03:21 |_Not valid after:  2024-08-09T23:13:21 |_ssl-date: 2023-07-17T09:42:08+00:00; +4h00m00s from scanner time. 445/tcp  open  microsoft-ds? 464/tcp  open  kpasswd5? 593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0 636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: authority.htb, Site: Default-First-Site-Name) | ssl-cert: Subject: | Subject Alternative Name: othername:<unsupported>, DNS:authority.htb.corp, DNS:htb.corp, DNS:HTB | Not valid before: 2022-08-09T23:03:21 |_Not valid after:  2024-08-09T23:13:21 |_ssl-date: 2023-07-17T09:42:06+00:00; +4h00m00s from scanner time. 3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: authority.htb, Site: Default-First-Site-Name) |_ssl-date: 2023-07-17T09:42:08+00:00; +4h00m00s from scanner time. | ssl-cert: Subject: | Subject Alternative Name: othername:<unsupported>, DNS:authority.htb.corp, DNS:htb.corp, DNS:HTB | Not valid before: 2022-08-09T23:03:21 |_Not valid after:  2024-08-09T23:13:21 3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: authority.htb, Site: Default-First-Site-Name) |_ssl-date: 2023-07-17T09:42:06+00:00; +4h00m00s from scanner time. | ssl-cert: Subject: | Subject Alternative Name: othername:<unsupported>, DNS:authority.htb.corp, DNS:htb.corp, DNS:HTB | Not valid before: 2022-08-09T23:03:21 |_Not valid after:  2024-08-09T23:13:21 8443/tcp open  ssl/https-alt |_http-title: Site doesn't have a title (text/html;charset=ISO-8859-1). |_ssl-date: TLS randomness does not represent time | fingerprint-strings: |   FourOhFourRequest, GetRequest: |     HTTP/1.1 200 |     Content-Type: text/html;charset=ISO-8859-1 |     Content-Length: 82 |     Date: Mon, 17 Jul 2023 09:41:22 GMT |     Connection: close |     <html><head><meta http-equiv="refresh" content="0;URL='/pwm'"/></head></html> |   HTTPOptions: |     HTTP/1.1 200 |     Allow: GET, HEAD, POST, OPTIONS |     Content-Length: 0 |     Date: Mon, 17 Jul 2023 09:41:22 GMT |     Connection: close |   RTSPRequest: |     HTTP/1.1 400 |     Content-Type: text/html;charset=utf-8 |     Content-Language: en |     Content-Length: 1936 |     Date: Mon, 17 Jul 2023 09:41:28 GMT |     Connection: close |     <!doctype html><html lang="en"><head><title>HTTP Status 400 |     Request</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 400 |_    Request</h1><hr class="line" /><p><b>Type</b> Exception Report</p><p><b>Message</b> Invalid character found in the HTTP protocol [RTSP&#47;1.00x0d0x0a0x0d0x0a...]</p><p><b>Description</b> The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid | ssl-cert: Subject: commonName=172.16.2.118 | Not valid before: 2023-07-15T06:48:09 |_Not valid after:  2025-07-16T18:26:33 1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service : SF-Port8443-TCP:V=7.94%T=SSL%I=7%D=7/17%Time=64B4D482%P=x86_64-apple-darwi SF:n22.4.0%r(GetRequest,DB,"HTTP/1\.1\x20200\x20\r\nContent-Type:\x20text/ SF:html;charset=ISO-8859-1\r\nContent-Length:\x2082\r\nDate:\x20Mon,\x2017 SF:\x20Jul\x202023\x2009:41:22\x20GMT\r\nConnection:\x20close\r\n\r\n\n\n\ SF:n\n\n<html><head><meta\x20http-equiv=\"refresh\"\x20content=\"0;URL='/p SF:wm'\"/></head></html>")%r(HTTPOptions,7D,"HTTP/1\.1\x20200\x20\r\nAllow SF::\x20GET,\x20HEAD,\x20POST,\x20OPTIONS\r\nContent-Length:\x200\r\nDate: SF:\x20Mon,\x2017\x20Jul\x202023\x2009:41:22\x20GMT\r\nConnection:\x20clos SF:e\r\n\r\n")%r(FourOhFourRequest,DB,"HTTP/1\.1\x20200\x20\r\nContent-Typ SF:e:\x20text/html;charset=ISO-8859-1\r\nContent-Length:\x2082\r\nDate:\x2 SF:0Mon,\x2017\x20Jul\x202023\x2009:41:22\x20GMT\r\nConnection:\x20close\r SF:\n\r\n\n\n\n\n\n<html><head><meta\x20http-equiv=\"refresh\"\x20content= SF:\"0;URL='/pwm'\"/></head></html>")%r(RTSPRequest,82C,"HTTP/1\.1\x20400\ SF:x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Language:\x2 SF:0en\r\nContent-Length:\x201936\r\nDate:\x20Mon,\x2017\x20Jul\x202023\x2 SF:009:41:28\x20GMT\r\nConnection:\x20close\r\n\r\n<!doctype\x20html><html SF:\x20lang=\"en\"><head><title>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20B SF:ad\x20Request</title><style\x20type=\"text/css\">body\x20{font-family:T SF:ahoma,Arial,sans-serif;}\x20h1,\x20h2,\x20h3,\x20b\x20{color:white;back SF:ground-color:#525D76;}\x20h1\x20{font-size:22px;}\x20h2\x20{font-size:1 SF:6px;}\x20h3\x20{font-size:14px;}\x20p\x20{font-size:12px;}\x20a\x20{col SF:or:black;}\x20\.line\x20{height:1px;background-color:#525D76;border:non SF:e;}</style></head><body><h1>HTTP\x20Status\x20400\x20\xe2\x80\x93\x20Ba SF:d\x20Request</h1><hr\x20class=\"line\"\x20/><p><b>Type</b>\x20Exception SF:\x20Report</p><p><b>Message</b>\x20Invalid\x20character\x20found\x20in\ SF:x20the\x20HTTP\x20protocol\x20\[RTSP&#47;1\.00x0d0x0a0x0d0x0a\.\.\.\]</ SF:p><p><b>Description</b>\x20The\x20server\x20cannot\x20or\x20will\x20not SF:\x20process\x20the\x20request\x20due\x20to\x20something\x20that\x20is\x SF:20perceived\x20to\x20be\x20...