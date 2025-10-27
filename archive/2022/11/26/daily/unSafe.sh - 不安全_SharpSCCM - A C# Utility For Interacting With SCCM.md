---
title: SharpSCCM - A C# Utility For Interacting With SCCM
url: https://buaq.net/go-137204.html
source: unSafe.sh - 不安全
date: 2022-11-26
fetch_date: 2025-10-03T23:47:24.037200
---

# SharpSCCM - A C# Utility For Interacting With SCCM

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

![](https://8aqnet.cdn.bcebos.com/8a5a66c793bcc9da3716a379a24146a1.jpg)

SharpSCCM - A C# Utility For Interacting With SCCM

SharpSCCM is a post-exploitation tool designed to leverage Microsoft Endpoint Configuration M
*2022-11-25 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-137204.htm)
阅读量:28
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ZAdfuaPhsN8-Kjti8hbHR8EUdvBLdswDeoEUlXN9lj2_ugapQxtx0ypnqqNIX5uPuXyOZbuY8eajHXuwp1E6bqHZmdml3QhPbVll-_Gu4APgiFi1utmsv8NtTfuF7Lr3mLsD1C9MmPh9HKIdgHFLu8_n27MfNDiQ-wbnXIpejMvm_K4HCdmpQkFeoQ/w640-h432/h121.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ZAdfuaPhsN8-Kjti8hbHR8EUdvBLdswDeoEUlXN9lj2_ugapQxtx0ypnqqNIX5uPuXyOZbuY8eajHXuwp1E6bqHZmdml3QhPbVll-_Gu4APgiFi1utmsv8NtTfuF7Lr3mLsD1C9MmPh9HKIdgHFLu8_n27MfNDiQ-wbnXIpejMvm_K4HCdmpQkFeoQ/s479/h121.png)

SharpSCCM is a [post-exploitation](https://www.kitploit.com/search/label/Post-Exploitation "post-exploitation") tool designed to leverage Microsoft Endpoint Configuration Manager (a.k.a. ConfigMgr, formerly SCCM) for [lateral movement](https://www.kitploit.com/search/label/Lateral%20Movement "lateral movement") and credential gathering without requiring access to the SCCM administration console GUI.

SharpSCCM was initially created to execute user hunting and lateral movement functions ported from PowerSCCM (by @harmj0y, @jaredcatkinson, @enigma0x3, and @mattifestation) and now contains additional functionality to gather credentials and abuse newly discovered attack primitives for coercing NTLM [authentication](https://www.kitploit.com/search/label/Authentication "authentication") in SCCM sites where automatic site-wide client push installation is enabled.

Please [visit the wiki](https://github.com/Mayyhem/SharpSCCM/wiki "visit the wiki") for documentation detailing how to build and use SharpSCCM.

### Author

Chris Thompson is the primary author of this project. Duane Michael (@subat0mik) and Evan McBroom (@mcbroom\_evan) are active contributors as well. Please feel free to reach out on Twitter (@\_Mayyhem) with questions, ideas for improvements, etc., and on GitHub with issues and pull requests.

### Warning

This tool was written as a [proof of concept](https://www.kitploit.com/search/label/Proof%20Of%20Concept "proof of concept") in a [lab environment](https://www.kitploit.com/search/label/Lab%20Environment "lab environment") and has not been thoroughly tested. There are lots of unfinished bits, terrible error handling, and functions I may never complete. Please be careful and use at your own risk.

SharpSCCM - A C# Utility For Interacting With SCCM
![SharpSCCM - A C# Utility For Interacting With SCCM](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh6ZAdfuaPhsN8-Kjti8hbHR8EUdvBLdswDeoEUlXN9lj2_ugapQxtx0ypnqqNIX5uPuXyOZbuY8eajHXuwp1E6bqHZmdml3QhPbVll-_Gu4APgiFi1utmsv8NtTfuF7Lr3mLsD1C9MmPh9HKIdgHFLu8_n27MfNDiQ-wbnXIpejMvm_K4HCdmpQkFeoQ/s72-w640-c-h432/h121.png)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2022/11/sharpsccm-c-utility-for-interacting.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)