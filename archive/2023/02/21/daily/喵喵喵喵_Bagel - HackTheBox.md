---
title: Bagel - HackTheBox
url: https://darkwing.moe/2023/02/20/Bagel-HackTheBox/
source: 喵喵喵喵
date: 2023-02-21
fetch_date: 2025-10-04T07:34:46.904505
---

# Bagel - HackTheBox

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

Bagel - HackTheBox

# Bagel - HackTheBox

##### 2023-02-20

#### TOC

1. [1. 基本信息](#基本信息)
   1. [1.1. 10.10.11.201](#10-10-11-201)
2. [2. 端口扫描](#端口扫描)
   1. [2.1. 8000](#8000)
3. [3. LFI](#LFI)
   1. [3.1. /proc/self/cmdline](#proc-self-cmdline)
   2. [3.2. /home/developer/app/app.py](#home-developer-app-app-py)
   3. [3.3. order app](#order-app)
4. [4. bagel.dll](#bagel-dll)
   1. [4.1. DB](#DB)
   2. [4.2. 反序列化](#反序列化)
   3. [4.3. Orders](#Orders)
5. [5. Json.Net反序列化](#Json-Net反序列化)
   1. [5.1. exp.py](#exp-py)
   2. [5.2. phil\_id\_rsa](#phil-id-rsa)
6. [6. user flag](#user-flag)
7. [7. 提权信息](#提权信息)
8. [8. 提权 & root flag](#提权-amp-root-flag)
   1. [8.1. shadow](#shadow)
9. [9. 参考资料](#参考资料)

# Bagel - HackTheBox

2023-02-20

# 基本信息

* <https://www.hackthebox.com/home/machines/profile/530>
* ## 10.10.11.201

![](https://raw.githubusercontent.com/zjicmDarkWing/images2023/master/2023022001.jpg)

# 端口扫描

22,5000,8000,5000直接HTTP访问是400:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 ``` | ``` $ nmap -sC -sV -Pn 10.10.11.201 Starting Nmap 7.93 ( https://nmap.org ) at 2023-02-20 18:56 CST Nmap scan report for 10.10.11.201 Host is up (0.093s latency). Not shown: 997 closed tcp ports (conn-refused) PORT     STATE SERVICE  VERSION 22/tcp   open  ssh      OpenSSH 8.8 (protocol 2.0) | ssh-hostkey: |   256 6e4e1341f2fed9e0f7275bededcc68c2 (ECDSA) |_  256 80a7cd10e72fdb958b869b1b20652a98 (ED25519) 5000/tcp open  upnp? | fingerprint-strings: |   GetRequest: |     HTTP/1.1 400 Bad Request |     Server: Microsoft-NetCore/2.0 |     Date: Mon, 20 Feb 2023 10:57:02 GMT |     Connection: close |   HTTPOptions: |     HTTP/1.1 400 Bad Request |     Server: Microsoft-NetCore/2.0 |     Date: Mon, 20 Feb 2023 10:57:17 GMT |     Connection: close |   Help, SSLSessionReq, TLSSessionReq, TerminalServerCookie: |     HTTP/1.1 400 Bad Request |     Content-Type: text/html |     Server: Microsoft-NetCore/2.0 |     Date: Mon, 20 Feb 2023 10:57:28 GMT |     Content-Length: 52 |     Connection: close |     Keep-Alive: true |     <h1>Bad Request (Invalid request line (parts).)</h1> |   RTSPRequest: |     HTTP/1.1 400 Bad Request |     Content-Type: text/html |     Server: Microsoft-NetCore/2.0 |     Date: Mon, 20 Feb 2023 10:57:02 GMT |     Content-Length: 54 |     Connection: close |     Keep-Alive: true |_    <h1>Bad Request (Invalid request line (version).)</h1> 8000/tcp open  http-alt Werkzeug/2.2.2 Python/3.10.9 | fingerprint-strings: |   FourOhFourRequest: |     HTTP/1.1 404 NOT FOUND |     Server: Werkzeug/2.2.2 Python/3.10.9 |     Date: Mon, 20 Feb 2023 10:57:02 GMT |     Content-Type: text/html; charset=utf-8 |     Content-Length: 207 |     Connection: close |     <!doctype html> |     <html lang=en> |     <title>404 Not Found</title> |     <h1>Not Found</h1> |     <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p> |   GetRequest: |     HTTP/1.1 302 FOUND |     Server: Werkzeug/2.2.2 Python/3.10.9 |     Date: Mon, 20 Feb 2023 10:56:57 GMT |     Content-Type: text/html; charset=utf-8 |     Content-Length: 263 |     Location: http://bagel.htb:8000/?page=index.html |     Connection: close |     <!doctype html> |     <html lang=en> |     <title>Redirecting...</title> |     <h1>Redirecting...</h1> |     <p>You should be redirected automatically to the target URL: <a href="http://bagel.htb:8000/?page=index.html">http://bagel.htb:8000/?page=index.html</a>. If not, click the link. |   Socks5: |     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" |     "http://www.w3.org/TR/html4/strict.dtd"> |     <html> |     <head> |     <meta http-equiv="Content-Type" content="text/html;charset=utf-8"> |     <title>Error response</title> |     </head> |     <body> |     <h1>Error response</h1> |     <p>Error code: 400</p> |     <p>Message: Bad request syntax (' |     ').</p> |     <p>Error code explanation: HTTPStatus.BAD_REQUEST - Bad request syntax or unsupported method.</p> |     </body> |_    </html> |_http-title: Did not follow redirect to http://bagel.htb:8000/?page=index.html |_http-server-header: Werkzeug/2.2.2 Python/3.10.9 2 services unrecognized despite returning data. If you know the service/version, please submit the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service : ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)============== SF-Port5000-TCP:V=7.93%I=7%D=2/20%Time=63F351FE%P=x86_64-apple-darwin21.5. SF:0%r(GetRequest,73,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nServer:\x20Mic SF:rosoft-NetCore/2\.0\r\nDate:\x20Mon,\x2020\x20Feb\x202023\x2010:57:02\x SF:20GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,E8,"HTTP/1\.1\x20 SF:400\x20Bad\x20Request\r\nContent-Type:\x20text/html\r\nServer:\x20Micro SF:soft-NetCore/2\.0\r\nDate:\x20Mon,\x2020\x20Feb\x202023\x2010:57:02\x20 SF:GMT\r\nContent-Length:\x2054\r\nConnection:\x20close\r\nKeep-Alive:\x20 SF:true\r\n\r\n<h1>Bad\x20Request\x20\(Invalid\x20request\x20line\x20\(ver SF:sion\)\.\)</h1>")%r(HTTPOptions,73,"HTTP/1\.1\x20400\x20Bad\x20Request\ SF:r\nServer:\x20Microsoft-NetCore/2\.0\r\nDate:\x20Mon,\x2020\x20Feb\x202 SF:023\x2010:57:17\x20GMT\r\nConnection:\x20close\r\n\r\n")%r(Help,E6,"HTT SF:P/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/html\r\nServer SF::\x20Microsoft-NetCore/2\.0\r\nDate:\x20Mon,\x2020\x20Feb\x202023\x2010 SF::57:28\x20GMT\r\nContent-Length:\x2052\r\nConnection:\x20close\r\nKeep- SF:Alive:\x20true\r\n\r\n<h1>Bad\x20Request\x20\(Invalid\x20request\x20lin SF:e\x20\(parts\)\.\)</h1>")%r(SSLSessionReq,E6,"HTTP/1\.1\x20400\x20Bad\x SF:20Request\r\nContent-Type:\x20text/html\r\nServer:\x20Microsoft-NetCore SF:/2\.0\r\nDate:\x20Mon,\x2020\x20Feb\x202023\x2010:57:28\x20GMT\r\nConte SF:nt-Length:\x2052\r\nConnection:\x20close\r\nKeep-Alive:\x20true\r\n\r\n SF:<h1>Bad\x20Request\x20\(Invalid\x20request\x20line\x20\(parts\)\.\)</h1 SF:>")%r(TerminalServerCookie,E6,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nCo SF:ntent-Type:\x20text/html\r\nServer:\x20Microsoft-NetCore/2\.0\r\nDate:\ SF:x20Mon,\x2020\x20Feb\x202023\x2010:57:28\x20GMT\r\nContent-Length:\x205 SF:2\r\nConnection:\x20close\r\nKeep-Alive:\x20true\r\n\r\n<h1>Bad\x20Requ SF:est\x20\(Invalid\x20request\x20line\x20\(parts\)\.\)</h1>")%r(TLSSessio SF:nReq,E6,"HTTP/1\.1\x20400\x20Bad\x20Request\r\nContent-Type:\x20text/ht SF:ml\r\nServer:\x20Microsoft-NetCore/2\.0\r\nDate:\x20Mon,\x2020\x20Feb\x SF:202023\x2010:57:28\x20GMT\r\nContent-Length:\x2052\r\nConnection:\x20cl SF:ose\r\nKeep-Alive:\x20true\r\n\r\n<h1>Bad\x20Request\x20\(Invalid\x20re SF:quest\x20line\x20\(parts\)\.\)</h1>"); ==============NEXT SERVICE FINGERPRINT (SUBMIT INDIVIDUALLY)============== SF-Port8000-TCP:V=7.93%I=7%D=2/20%Time=63F351F9%P=x86_64-apple-darwin21.5. SF:0%r(GetRequest,1EA,"HTTP/1\.1\x20302\x20FOUND\r\nServer:\x20Werkzeug/2\ SF:.2\.2\x20Python/3\.10\.9\r\nDate:\x20Mon,\x2020\x20Feb\x202023\x2010:56 SF::57\x20GMT\r\nContent-Type:\x20text/html;\x20charset=utf-8\r\nContent-L SF:ength:\x20263\r\nLocation:\x20http://bagel\.htb:8000/\?page=index\.html SF:\r\nConnection:\x20close\r\n\r\n<!doctype\x20html>\n<html\x20lang=en>\n SF:<title>Redirecting\.\.\.</title>\n<h1>Redi...