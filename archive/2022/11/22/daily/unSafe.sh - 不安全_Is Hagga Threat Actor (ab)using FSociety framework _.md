---
title: Is Hagga Threat Actor (ab)using FSociety framework ?
url: https://buaq.net/go-136636.html
source: unSafe.sh - 不安全
date: 2022-11-22
fetch_date: 2025-10-03T23:22:48.947206
---

# Is Hagga Threat Actor (ab)using FSociety framework ?

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

![](https://8aqnet.cdn.bcebos.com/c9dc86a6007fae63c103762b69b24c2f.jpg)

Is Hagga Threat Actor (ab)using FSociety framework ?

IntroductionToday I’d like to share a quick analysis initiated during a threat hunting
*2022-11-21 23:36:56
Author: [marcoramilli.com(查看原文)](/jump-136636.htm)
阅读量:34
收藏*

---

#### Introduction

Today I’d like to share a quick analysis initiated during a threat hunting process. The first observable was found during hunting process over OSINT sources, the entire infrastructure was still up and running during the analyses as well as malicious payload were downloadable.

#### Analysis

My first observable was a zipped text file compressing a simple update.js script. The script was created to avoid automatic analisis tools since the dimension (>9MB) really makes hard to beautify or remove unwanted/funny or added trash code every which happens to be everywhere.

|  |  |
| --- | --- |
| name | update.js |
| sha256 | 9ea4eebd9cf2a5d4e6343cb559d8c996fae6bf0f3bd7ffada0567053c08acc31 |
| type | Drop and Execute |

Stage 1

The following images show how it looked like at first sight. As many of you are aware, analyzing scripts is just a matter of time or, if you have enough memory on your machine (or time to spend over that task) a computational matter during virtualization. If you are old style (I do like it a lot ) it is a matter of “keywords” , in other words adding some `console.println` or whatsoever you like to make debugging quick and easy. Few strings in this update.js reminded me to the use of obfuscator.io tool, but I did not investigate further on this direction, it was quite easy as well to reach the point.

Finally its execution was reached. I obtained this status by using some classic and romantic hand working balance to dynamic execution with the always great JSDetox. Finally the real behavior came out. It looks like to be a drop and execute artifact. It takes a file called Dll.ppam from an IP address (please take a look to IoC section to see details on found IoC), it decodes it from `base64`, and it invoked the method `VAI` (really interested Italian word to say “GO”, nice coincidence !?) in the `Fiber.Home` class. It then passes to such a function an interesting address: `<https://firebasestorage>. googleapis. com` with some parameters as the following image shows (please reverse the byte order on the right string).

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2022/11/3.png?resize=832%2C261&ssl=1)

Lets take a closer look to what Dll.ppam is. First it’s a .NET Portable Executable, so we might have an easy path ahead.

|  |  |
| --- | --- |
| name | Dll.ppam |
| sha256 | ab5b1989ddf6113fcb50d06234dbef65d871e41ce8d76d5fb5cc72055c1b28ba |
| type | Drop, evasion and Memory Invoke |

The .NET is not packed and the code reading is quite “straight forward”. An interesting technique that I’d like to highlight (and to track) is in the way the malware developer used to step forward the malware control flow, which reminds me a known threat actor. Many different techniques could be used at this point if you want to make something happening after specific conditions or if you simply want to give an execution order. The most easy and (maybe) quick way to follow could be the adoption of `nested functions` or, if you are a more sophisticated malware developer, you might decide to use `exception handlers` or, again, you might decide to switch from function to function in different libraries, or for the shake of example, a simple single flow as a simple unique function. But this malware developer decided to use a quite characteristic way developing an interesting combination of `switch`/`case`. In other words it starts by assigning `0` to `num` variable which it makes `case 0` to switch. In each `case` it updates the `num` variable to control the `switch(num)` selector making the flow running in the desired way. The following image shows the `VAI` function, in where you might appreciate the control flow and additional IoC (such as IP address, dropped url and artifact name, etc..).

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2022/11/4.png?resize=1024%2C680&ssl=1)

Principal routine on Dll.ppam

The VAI routing starts by downloading a file called `Rump.xls` from a remote server. It places the file content into a variable and it reverse its bytes order, later it replaces special characters to the letter `A`. The resulting decoded file (bytes Inverted, Special Character replaced and base64 decoded) is another PE file written in .NET technology and encoded in base64.

Finally once the Rump.xls file is decoded in memory, `Dll.ppam` runs it by calling the method `Adre` inside the `Fsociety.Tools` library, passing as argument `RegAsm.exe`.

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2022/11/Call_Ande_FromMail.png?resize=1024%2C306&ssl=1)

Memory invoke of Rump.xls (later fsociety tools)

The following table sums up the original and dropped file by Dll.ppam named Rump.xls, while the next table shows details about the .NET PE file resulting from the decoding process.

|  |  |
| --- | --- |
| name | Rump.xls (Original) |
| sha256 | 20a53f17071f377d50ad9de30fdddd320d54d00b597bf96565a2b41c15649f76 |
| type | post exploitation tool, C2 communication |

|  |  |
| --- | --- |
| name | Rump.xls.inverted.charsReplaced.decoded (given name) |
| sha256 | 5d910ee5697116faa3f4efe230a9d06f6e3f80a7ad2cf8e122546b10e34a0088 |
| type | post exploitation tool, C2 communication decoded |

Rump.xls looks like to be an implementation of Fsociety tools, a complete post exploitation framework. This library is able to get system information `RtlGetVersion`, `RtlGetNtProductType`, `GetSystemTimeAsFileTime` and to get the used software policies: `"regsvr32.exe" (Path: "HKLM\SOFTWARE\POLICIES\MICROSOFT\WINDOWS\SAFER\CODEIDENTIFIERS"; Key: "TRANSPARENTENABLED")`. It also contains the ability to get persistence by  and it might get remote access by using the `WmiPrvSE` module.

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2022/11/FunctionAndeInLibraryFsociety.png?resize=1024%2C753&ssl=1)

The image above shows an interested detail about the called function `Ande`, where you might appreciate a similar coding style if compared to the Dll.ppam even if the control flow, this time, is managed by simple nested if. The infinitive loop and the variable names are matching the previous code. However those similarities are way too weak to say anything about the authorship (IMHO), but still indicators to keep tracking.

#### Threat Intelligence

According to Microsoft Threat intelligence the drop server ( `4.204.233.44`) has been seen with two certificates (please refer to IoC sections for sha1). The first certificate (SN: `136234453590953102797263558291395548452`) has been issued on 2022-11-14 with common name `servidor` (server as in Spanish). On 2022-11-14 the attacker changed the webserver certificate by adding the certificate having as SN: `13098529066745705731` issued on 2009-11-11 and having with common name `localhost`. This Certificate has been recorded in almost 50k related IPs over the past 13 years. The following image shows what I meant.

![](https://i0.wp.com/marcoramilli.com/wp-content/uploads/2022/11/7.png?resize=1024%2C459&ssl=1)

From Microsoft Threat Intel

One of the 50k IPs in where the same certificate was found, was the same that [TeamCymru](https://team-cymru.com/blog/2022/07/12/an-analysis-of-infrastructure-linked-to-the-hagga-threat-actor/) was able to track, thanks to previously posted IoC from [Yoroi Threat Intelligence](https://yoroi.company/research/server...