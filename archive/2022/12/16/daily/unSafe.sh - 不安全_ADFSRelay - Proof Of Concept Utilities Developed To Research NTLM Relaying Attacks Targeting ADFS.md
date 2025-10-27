---
title: ADFSRelay - Proof Of Concept Utilities Developed To Research NTLM Relaying Attacks Targeting ADFS
url: https://buaq.net/go-140168.html
source: unSafe.sh - 不安全
date: 2022-12-16
fetch_date: 2025-10-04T01:39:05.948505
---

# ADFSRelay - Proof Of Concept Utilities Developed To Research NTLM Relaying Attacks Targeting ADFS

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

![](https://8aqnet.cdn.bcebos.com/4c0b44315f6e14062339f6ab330675da.jpg)

ADFSRelay - Proof Of Concept Utilities Developed To Research NTLM Relaying Attacks Targeting ADFS

This repository includes two utilities NTLMParse and ADFSRelay. NTLMParse is a utility for d
*2022-12-15 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-140168.htm)
阅读量:26
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAJL9T6p-7s74HZMRbDuo3SVx6P1dmNAPIXOWfZNdAnSqc_xvCzJoAvUZFhTkm53pkK72GV1wL7lOVN3SuaUuve7lJr_XOoU-y103LkbSPWy1vjDwg08plQp_eXYaPCOdM97LkgLCIGNAT4b8p4BvdW10kr2IrvENd-EUmVVqdQ7CP8nryB9xe6agrGQ/s16000/ADFSRelay.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAJL9T6p-7s74HZMRbDuo3SVx6P1dmNAPIXOWfZNdAnSqc_xvCzJoAvUZFhTkm53pkK72GV1wL7lOVN3SuaUuve7lJr_XOoU-y103LkbSPWy1vjDwg08plQp_eXYaPCOdM97LkgLCIGNAT4b8p4BvdW10kr2IrvENd-EUmVVqdQ7CP8nryB9xe6agrGQ/s633/ADFSRelay.png)

This repository includes two utilities NTLMParse and ADFSRelay. NTLMParse is a utility for [decoding](https://www.kitploit.com/search/label/Decoding "decoding") base64-encoded NTLM messages and printing information about the underlying properties and fields within the message. Examining these NTLM messages is helpful when researching the behavior of a particular NTLM implementation. ADFSRelay is a [proof of concept](https://www.kitploit.com/search/label/Proof%20Of%20Concept "proof of concept") utility developed while researching the feasibility of NTLM [relaying](https://www.kitploit.com/search/label/Relaying "relaying") attacks targeting the ADFS service. This utility can be leveraged to perform NTLM relaying attacks targeting ADFS. We have also released a blog post discussing ADFS relaying attacks in more detail [1].

To use the NTLMParse utility you simply need to pass a Base64 encoded message to the application and it will decode the relevant fields and structures within the message. The snippet given below shows the expected output of NTLMParse when it is invoked:

```
➜  ~ pbpaste | NTLMParse
```

Below is a sample NTLM AUTHENTICATE\_MESSAGE message that can be used for testing:

`TlRMTVNTUAADAAAAGAAYAKAAAACAAYABuAAAABoAGgBYAAAAEAAQAHIAAAAeAB4AggAAABAAEAA4AgAAFYKI4goAYUoAAAAPqfU7N7/JSXVfIdKvlIvcQkMATwBOAFQATwBTAE8ALgBMAE8AQwBBAEwAQQBDAHIAbwBzAHMAZQByAEQARQBTAEsAVABPAFAALQBOAEkARAA0ADQANQBNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADDrMB+rTzdNeVkoczhRGTsBAQAAAAAAAIlfbVzIctgByXRlRbnd9zUAAAAAAgAOAEMATwBOAFQATwBTAE8AAQAeAFcASQBOAC0ARgBDAEcAVQA0AEcASABPADAAOAA0AAQAGgBDAE8ATgBUAE8AUwBPAC4ATABPAEMAQQBMAAMAOgBXAEkATgAtAEYAQwBHAFUANABHAEgATwAwADgANAAuAEMATwBOAFQATwBTAE8ALgBMAE8AQwBBAEwABQAaAEMATwBOAFQATwBTAE8ALgBMAE8AQwBBAEwABwAIAIlfbVzIctgBBgAEAAIAAAAIADAAMAAAAAAAAAABAAAAACAAABQaOHb4nG5F2JL1tA5kL+nKQXJSJLDWljeBv+/XlPXpCgAQAON+EDXYnla0bjpwA8gfVEgJAD4ASABUAFQAUAAvAHMAdABzAC4AYwBvAG4AdABvAHMAbwBjAG8AcgBwAG8AcgBhAHQAaQBvAG4ALgBjAG8AbQAAAAAAAAAAAKDXom0m65knt1NeZF1ZxxQ=`

The single required argument for ADFSRelay is the URL of the ADFS server to target for an NTLM relaying attack. Three optional arguments are -debug to enable [debugging](https://www.kitploit.com/search/label/Debugging "debugging") mode, -port to define the port the service should listen on, and -help to display the help menu. An example help menu is given below:

```
➜  ~ ADFSRelay -h
Usage of ADFSRelay:
  -debug
    	Enables debug output
  -help
    	Show the help menu
  -port int
    	The port the HTTP listener should listen on (default 8080)
  -targetSite string
    	The ADFS site to target for the relaying attack (e.g. https://sts.contoso.com)
➜  ~
```

[1] [https://www.praetorian.com/blog/relaying-to-adfs-attacks/](https://www.praetorian.com/blog/relaying-to-adfs-attacks/ "https://www.praetorian.com/blog/relaying-to-adfs-attacks/")

ADFSRelay - Proof Of Concept Utilities Developed To Research NTLM Relaying Attacks Targeting ADFS
![ADFSRelay - Proof Of Concept Utilities Developed To Research NTLM Relaying Attacks Targeting ADFS](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgAJL9T6p-7s74HZMRbDuo3SVx6P1dmNAPIXOWfZNdAnSqc_xvCzJoAvUZFhTkm53pkK72GV1wL7lOVN3SuaUuve7lJr_XOoU-y103LkbSPWy1vjDwg08plQp_eXYaPCOdM97LkgLCIGNAT4b8p4BvdW10kr2IrvENd-EUmVVqdQ7CP8nryB9xe6agrGQ/s72-c/ADFSRelay.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/12/adfsrelay-proof-of-concept-utilities.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)