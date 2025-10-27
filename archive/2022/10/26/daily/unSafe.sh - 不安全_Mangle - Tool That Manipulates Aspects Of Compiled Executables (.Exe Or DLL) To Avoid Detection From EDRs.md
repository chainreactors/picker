---
title: Mangle - Tool That Manipulates Aspects Of Compiled Executables (.Exe Or DLL) To Avoid Detection From EDRs
url: https://buaq.net/go-132571.html
source: unSafe.sh - 不安全
date: 2022-10-26
fetch_date: 2025-10-03T20:52:39.161410
---

# Mangle - Tool That Manipulates Aspects Of Compiled Executables (.Exe Or DLL) To Avoid Detection From EDRs

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

![](https://8aqnet.cdn.bcebos.com/2c9fb60641c716dfaa39ae1b1f018a8b.jpg)

Mangle - Tool That Manipulates Aspects Of Compiled Executables (.Exe Or DLL) To Avoid Detection From EDRs

Authored By Tyl0us Featured at Source Zero Con 2022 Mangle is a tool that manipulates aspec
*2022-10-25 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-132571.htm)
阅读量:33
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5c46_nTyHbdBAxoWUtPRPC1IT69t42mlHIB-tnP3FT4cpHi7AgoKcl00n89_vMQLXC75z1RLT5D9LL2GIUTonGxIfhFJF5lY2wPZ2Y_GC-yeqxM_xpSPSjhWPdNJ_9r7yAQT9z7tilpTi6-oI0eGkJm4e4cl8rn96ISpGlItgipttYDkBozoCaiwvyw/w494-h640/Mangle_1_logo.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5c46_nTyHbdBAxoWUtPRPC1IT69t42mlHIB-tnP3FT4cpHi7AgoKcl00n89_vMQLXC75z1RLT5D9LL2GIUTonGxIfhFJF5lY2wPZ2Y_GC-yeqxM_xpSPSjhWPdNJ_9r7yAQT9z7tilpTi6-oI0eGkJm4e4cl8rn96ISpGlItgipttYDkBozoCaiwvyw/s452/Mangle_1_logo.png)

**Authored By Tyl0us**

**Featured at Source Zero Con 2022**

Mangle is a tool that manipulates aspects of compiled executables (.exe or DLL). Mangle can remove known [Indicators of Compromise](https://www.kitploit.com/search/label/Indicators%20of%20Compromise "Indicators of Compromise") (IoC) based strings and replace them with random characters, change the file by inflating the size to avoid EDRs, and can clone code-signing certs from legitimate files. In doing so, Mangle helps loaders evade on-disk and in-memory scanners.

## Contributing

Mangle was developed in Golang.

## Install

The first step, as always, is to clone the repo. Before you compile Mangle, you'll need to install the dependencies. To install them, run the following commands:

```
go get github.com/Binject/debug/pe
```

Then build it

## Important

While Mangle is written in Golang, a lot of the features are designed to work on executable files from other languages. At the time of release, the only feature that is Golang specific is the string [manipulation](https://www.kitploit.com/search/label/Manipulation "manipulation") part.

## Usage

```
./mangle -h

_____                        .__
	  /     \ _____    ____    ____ |  |   ____
	 /  \ /  \\__  \  /    \  / ___\|  | _/ __ \
	/    Y    \/ __ \|   |  \/ /_/  >  |_\  ___/
	\____|__  (____  /___|  /\___  /|____/\___  >
		\/     \/     \//_____/   	  \/
					(@Tyl0us)
Usage of ./Mangle:
  -C string
        Path to the file containing the certificate you want to clone
  -I string
        Path to the orginal file
  -M    Edit the PE file to strip out Go indicators
  -O string
        The new file name
  -S int
        How many MBs to increase the file by
```

## Strings

Mangle takes the input executable and looks for known strings that security products look for or alert on. These strings alone are not the sole point of detection. Often, these strings are in conjunction with other data points and pieces of [telemetry](https://www.kitploit.com/search/label/Telemetry "telemetry") for detection and prevention. Mangle finds these known strings and replaces the hex values with random ones to remove them. IMPORTANT: Mangle replaces the exact size of the strings it’s manipulating. It doesn’t add any more or any less, as this would create misalignments and instabilities in the file. Mangle does this using the `-M` command-line option.

Currently, Mangle only does Golang files but as time goes on other languages will be added. If you know of any for other languages, please open an issue ticket and submit them.

**Before**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnttttUBg4eFz8NqeI10YjWJZmTGB2i_E9zBDd17CdrNo7gXoNCT-w7yD7-tvsw1nltX8CEal56oTj_dNvfAMh5Lji5TR6Rm8_ztxRavGcjEbtnoRF0XBaZ1qyB1ekg3XtzbRAe6KGyA3VD5GhnM9FlY7Z2-2UUF-tIpE_2m34W-fsJ7mIYmqpOFywkQ/w640-h142/Mangle_2_Strings_Before.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhnttttUBg4eFz8NqeI10YjWJZmTGB2i_E9zBDd17CdrNo7gXoNCT-w7yD7-tvsw1nltX8CEal56oTj_dNvfAMh5Lji5TR6Rm8_ztxRavGcjEbtnoRF0XBaZ1qyB1ekg3XtzbRAe6KGyA3VD5GhnM9FlY7Z2-2UUF-tIpE_2m34W-fsJ7mIYmqpOFywkQ/s630/Mangle_2_Strings_Before.png)

**After**

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTcD29a1Cy_1eSqo5LrOTc1hBi5jroiNVIHW-8QI6SmyzdBvrzXHAdOGO3uE88AfItr0SlUgxXoKEY_zaLBrY9acBkS5opTh_qBU8bKHuDGYz135AzmN-Cu3FRZT8nI5tivonS-CSzzPIcXJSXVO752CQ-RravgrPS4IQAzRcJ3bo2lpCJvOkL_CqAgw/w640-h100/Mangle_3_Strings_After.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgTcD29a1Cy_1eSqo5LrOTc1hBi5jroiNVIHW-8QI6SmyzdBvrzXHAdOGO3uE88AfItr0SlUgxXoKEY_zaLBrY9acBkS5opTh_qBU8bKHuDGYz135AzmN-Cu3FRZT8nI5tivonS-CSzzPIcXJSXVO752CQ-RravgrPS4IQAzRcJ3bo2lpCJvOkL_CqAgw/s633/Mangle_3_Strings_After.png)

## Inflate

Pretty much all EDRs can’t scan both on disk or in memory files beyond a certain size. This simply stems from the fact that large files take longer to review, scan, or monitor. EDRs do not want to impact [performance](https://www.kitploit.com/search/label/Performance "performance") by slowing down the user's productivity. Mangle inflates files by creating a padding of Null bytes (Zeros) at the end of the file. This ensures that nothing inside the file is impacted. To inflate an executable, use the `-S` command-line option along with the number of bytes you want to add to the file. Large payloads are really not an issue anymore with how fast Internet speeds are, that being said, it's not recommended to make a 2 gig file.

Based on test cases across numerous userland and kernel EDRs, it is recommended to increase the size by either 95-100 megabytes. Because vendors do not check large files, the activity goes unnoticed, resulting in the successful execution of shellcode.

### Example:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsmMexlN01H-wwtSaHLrAUgECYruYthXiyM4O4Sy_DsihusplovCkK1fVSNfXOAG14jhBnQG_fbj0D6EeX89SVvCdTXCXflOiPeFjepf4PnjvPT5KsAaAOJGxtuhMRQOKgOFs5k-wXiHSdLggK6vdERlWRtGMPsTs_9Nmd6TWJVH_3XgejbigrLJbr2Q/w640-h268/Mangle_4_Demo.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhsmMexlN01H-wwtSaHLrAUgECYruYthXiyM4O4Sy_DsihusplovCkK1fVSNfXOAG14jhBnQG_fbj0D6EeX89SVvCdTXCXflOiPeFjepf4PnjvPT5KsAaAOJGxtuhMRQOKgOFs5k-wXiHSdLggK6vdERlWRtGMPsTs_9Nmd6TWJVH_3XgejbigrLJbr2Q/s3440/Mangle_4_Demo.gif)

## Certificate

Mangle also contains the ability to take the full chain and all attributes from a legitimate code-signing certificate from a file and copy it onto another file. This includes the signing date, counter signatures, and other measurable attributes.

While this feature may sound similar to another tool I developed, [Limelighter](https://github.com/Tylous/Limelighter "Limelighter"), the major difference between the two is that [Limelighter](https://www.kitploit.com/search/label/Limelighter "Limelighter") makes a fake certificate based off a domain and signs it with the current date and time, versus using valid attributes where the timestamp is taken from when the original file. This option can use DLL or .exe files to copy using the `-C` command-line option, along with the path to the file you want to copy the certificate from.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYTfA6m3i7I3Fvq4SL2prtwRzPSCeHB5_5apT3e2lnP72p0vFMvsivo_vbRES2gFlhvmvFpDpxURTL051smEu1s9NBTfmuPjpBYyz2q4UPG5xp0-ygFQUWNEXzYCjJ3zxfUb2TD7xtUVvC5BSmzznaVHFKgIorbhl3xdpy-2ZmhkAHHeC0fRnWZn4RJQ/w640-h474/Mangle_5_Cert_Copy.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYTfA6m3i7I3Fvq4SL2prtwRzPSCeHB5_5apT3e2lnP72p0vFMvsivo_vbRES2gFlhvmvFpDpxURTL051smEu1s9NBTfmuPjpBYyz2q4UPG5xp0-ygFQUWNEXzYCjJ3zxfUb2TD7xtUVvC5BSmzznaVHFKgIorbhl3xdpy-2ZmhkAHHeC0fRnWZn4RJQ/s724/Mangle_5_Cert_Copy.png)

## Cred...