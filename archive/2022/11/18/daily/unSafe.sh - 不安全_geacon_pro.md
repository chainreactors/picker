---
title: geacon_pro
url: https://buaq.net/go-136113.html
source: unSafe.sh - 不安全
date: 2022-11-18
fetch_date: 2025-10-03T23:05:19.387273
---

# geacon_pro

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

![](https://8aqnet.cdn.bcebos.com/850387fefc1ece61a1bbb9e2238754a0.jpg)

geacon\_pro

中文说明在这里Introductiongeacon\_pro is an Anti-Virus bypassing CobaltStrike Beacon written
*2022-11-17 21:46:39
Author: [github.com(查看原文)](/jump-136113.htm)
阅读量:117
收藏*

---

## [中文说明在这里](https://github.com/H4de5-7/geacon_pro/blob/master/README_zh.md)

## Introduction

geacon\_pro is an Anti-Virus bypassing CobaltStrike Beacon written in Golang based on [geacon](https://github.com/darkr4y/geacon) project.

geacon\_pro supports CobaltStrike version 4.1+

geacon\_pro has implemented most functions of Beacon.

**We will continue to follow up the method of bypassing Anti-Virus and keep geacon\_pro from being detected by Anti-Virus. We will also integrate the pen test tools which can bypass Anti-Virus. We hope that geacon\_pro can be made into a cross-platform bypass Anti-Virus tool that is not limited to CobaltStrike native functions in the future. Discussions are welcome if you have relevant needs or ideas. your support and discussion is the driving force for us to move forward.**

**This project is only for learning CobaltStrike protocol. Please do not use it for any illegal purpose, and the consequences arising therefrom shall be borne by yourself.**

This project is developed by me and Z3ratu1. He has implemented a version of [geacon\_plus](https://github.com/Z3ratu1/geacon_plus) that supports CobaltStrike version 4.0. geacon\_pro supports version 4.1 and above. Functions of these two projects are almost same while encapsulation is slightly different.

**Loading the shellcode of Beacon through various loaders is the traditional method to bypass Anti-Virus. However, some Anti-Virus check the memory characteristics of Beacon strictly, especially Kaspersky, so it is better to rebuild one by yourself.**

The core of bypassing Anti-Virus can be reflected in three aspects:

* There is no CobaltStrike Beacon feature.
* Viruses written in Golang can bypass the detection of antivirus software to a certain extent.
* Some dangerous functions which can be easily detected by antivirus software has been changed to more stealthy implementations.

**The currently implemented functions can pass Defender, 360 core crystal (except powershell, you can use the tool I provide below), Kaspersky (except memory operations, such as injecting native CobaltStrike dll), and Huorong. Other antivirus software has not been tested yet, please contact me if you have relevant requirements.**

In order to avoid 360's monitoring of the fork&&run operation, geacon\_pro currently injects CobaltStrike native dll into itself rather than into the temporary process. However, we found that the CobaltStrike native powerpick function sometimes fails to get the echo when it is injected into geacon\_pro itself, while is works well in the fork&&run mode. Therefore, you can use `execute-assembly` to execute this [powershell-bypass tool](https://github.com/H4de5-7/powershell-bypass), which can bypass Defender, 360, etc.

If you want to make bypassUAC avoid the detection of antivirus software, please using `execute-assembly` to execute the Csharp version of [this project](https://github.com/0xlane/BypassUAC/). Although the Csharp program will be detected by 360 when it is on the disk, it can bypass Defender and 360 by executing in memory using `execute-assembly`. The dll version of this project can bypass Anti-Virus, but it needs to be uploaded and executed with rundll32.

**geacon\_pro is still in development, the current version may have some incomplete functions. Please contact me if you have any needs.**

**If you have a good solution for heap memory encryption, welcome to discuss, my implementation ideas are in the implementation details.**

## How to use geacon\_pro

geacon\_pro supports Windows, Linux and Mac.

For the basic usage, please refer to the original project geacon. Adding `-ldflags "-H windowsgui -s -w"` when compiling binary can reduce the program size and hide the cmd window. When compiling for linux and mac, adding `-ldflags "-s -w"` can reduce the size of the program, and then run it in the background.

The simplest way to use geacon\_pro is to modify the public key and C2 server address in config.go, and then replace the C2profile with the following example.

**At present, the project has some console output content, you can delete the related code to remove it.**

If your CobaltStrike's magic number changed from 48879 to other number before, it may cause the authentication to fail. In that case you can try to change the 0xBEEF in meta.go to the value you have changed.

## Functions

### Windows platform:

sleep, shell, upload, download, exit, cd, pwd, file\_browse, ps, kill, getuid, mkdir, rm, cp, mv, run, execute, drives, powershell-import, powershell, execute-assembly, Multiple thread injection methods (you can replace the source code yourself), shinject, dllinject, pipe, Various CobaltStrike native reflection dll injection (mimikatz, portscan, screenshot, keylogger, etc.), steal\_token, rev2self, make\_token, proxy, etc.

### Linux, Mac platform:

sleep, shell, upload, download, exit, cd, pwd, file\_browse, ps, kill, getuid, mkdir, rm, cp, mv, etc.

The process management and the file management support graphical interaction.

### C2profile:

geacon\_pro adapts the settings on the flow of C2profile and some settings on the host. The supported encoding algorithms are base64, base64url, mask, netbios, netbiosu. Details can be found in config.go. Here is an example C2profile.
**IMPORTANT!!! After modifying the C2profile, do not forget to sync the changes in config.go:**

```
# default sleep time is 60s
set sleeptime "3000";

https-certificate {
set C "KZ";
set CN "foren.zik";
set O "NN Fern Sub";
set OU "NN Fern";
set ST "KZ";
set validity "365";
}

# define indicators for an HTTP GET
http-get {

set uri "/www/handle/doc";

client {
#header "Host" "aliyun.com";
# base64 encode session metadata and store it in the Cookie header.
metadata {
			base64url;
prepend "SESSIONID=";
header "Cookie";
}
	}

	server {
		# server should send output with no changes
#header "Content-Type" "application/octet-stream";
header "Server" "nginx/1.10.3 (Ubuntu)";
header "Content-Type" "application/octet-stream";
header "Connection" "keep-alive";
header "Vary" "Accept";
header "Pragma" "public";
header "Expires" "0";
header "Cache-Control" "must-revalidate, post-check=0, pre-check=0";

output {
			mask;
netbios;
prepend "data=";
append "%%";
print;
}
	}
}

# define indicators for an HTTP
http-post {
	# Same as above, Beacon will randomly choose from this pool of URIs [if multiple URIs are provided]
set uri "/IMXo";
client {
#header "Content-Type" "application/octet-stream";

# transmit our session identifier as /submit.php?id=[identifier]

id {
			mask;
netbiosu;
prepend "user=";
append "%%";
header "User";
}

		# post our output with no real changes
		output {
			mask;
base64url;
prepend "data=";
append "%%";
print;
}
	}

	# The server's response to our HTTP POST
	server {
		header "Server" "nginx/1.10.3 (Ubuntu)";
header "Content-Type" "application/octet-stream";
header "Connection" "keep-alive";
header "Vary" "Accept";
header "Pragma" "public";
header "Expires" "0";
header "Cache-Control" "must-revalidate, post-check=0, pre-check=0";

		# this will just print an empty string, meh...
output {
			mask;
netbios;
prepend "data=";
append "%%";
print;
}
	}
}

post-ex {
set spawnto_x86 "c:\\windows\\syswow64\\rundll32.exe";
set spawnto_x64 "c:\\windows\\system32\\rundll32.exe";

set thread_hint "ntdll.dll!RtlUserThreadStart+0x1000";
set pipename "DserNamePipe##, PGMessagePipe##...