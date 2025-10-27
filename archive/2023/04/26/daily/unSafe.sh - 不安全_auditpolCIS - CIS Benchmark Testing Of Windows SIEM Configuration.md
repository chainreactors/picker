---
title: auditpolCIS - CIS Benchmark Testing Of Windows SIEM Configuration
url: https://buaq.net/go-160485.html
source: unSafe.sh - 不安全
date: 2023-04-26
fetch_date: 2025-10-04T11:31:35.130744
---

# auditpolCIS - CIS Benchmark Testing Of Windows SIEM Configuration

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

![](https://8aqnet.cdn.bcebos.com/040545051a8859b2fea9ff10c98accf4.jpg)

auditpolCIS - CIS Benchmark Testing Of Windows SIEM Configuration

CIS Benchmark testing of Windows SIEM configuration This is an application for testing the
*2023-4-25 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-160485.htm)
阅读量:24
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj2qz653asYqPYxfEizQzUEkzl7b8m8U_GEabqb3jqXpvNFPxh7IcIF7nFpsjJRojvQbda16aAElWLhbcNIAsXSjuw6r1Ai0_UfYXByOr-vfnRpYdjZHdfQS_hjSXwy5uOls6yyNIfTSyrHbyCspA3Td49RdDhtDnhkRrSb6XRNWdYpyd5sVfMsY1QFRg=w640-h470)](https://blogger.googleusercontent.com/img/a/AVvXsEj2qz653asYqPYxfEizQzUEkzl7b8m8U_GEabqb3jqXpvNFPxh7IcIF7nFpsjJRojvQbda16aAElWLhbcNIAsXSjuw6r1Ai0_UfYXByOr-vfnRpYdjZHdfQS_hjSXwy5uOls6yyNIfTSyrHbyCspA3Td49RdDhtDnhkRrSb6XRNWdYpyd5sVfMsY1QFRg)

CIS Benchmark [testing](https://www.kitploit.com/search/label/Testing "testing") of [Windows](https://www.kitploit.com/search/label/Windows "Windows") SIEM configuration

This is an application for testing the configuration of Windows Audit Policy settings against the [CIS Benchmark](https://www.kitploit.com/search/label/CIS%20Benchmark "CIS Benchmark") recommended settings. A few points:

* The tested system was Windows Server 2019, and the benchmark used was also Windows Server 2019.
* The script connects with SSH. SSH is included with Windows Server 2019, it just has to be enabled. If you would like to see WinRM (or other) connection types, let me know or send a PR.
* Some tests are included here which were not included in the CIS guide. The recommended settings for these Subcategories are based on the [logging](https://www.kitploit.com/search/label/Logging "logging") volume for these events, versus the security value. In nearly all cases, the recommendation is to turn off [auditing](https://www.kitploit.com/search/label/Auditing "auditing") for these settings.
* The YAML file cis-benchmarks.yaml is the YAML representation of the CIS Benchmark guideline for each Subcategory.
* The command run under SSH is auditpol /get /category:\*

Further details on usage and other background info is at [https://www.seven-stones.biz/blog/auditpolcis-automating-windows-siem-cis-benchmarks-testing/](https://www.seven-stones.biz/blog/auditpolcis-automating-windows-siem-cis-benchmarks-testing/ "https://www.seven-stones.biz/blog/auditpolcis-automating-windows-siem-cis-benchmarks-testing/")

auditpolCIS - CIS Benchmark Testing Of Windows SIEM Configuration
![auditpolCIS - CIS Benchmark Testing Of Windows SIEM Configuration](https://blogger.googleusercontent.com/img/a/AVvXsEj2qz653asYqPYxfEizQzUEkzl7b8m8U_GEabqb3jqXpvNFPxh7IcIF7nFpsjJRojvQbda16aAElWLhbcNIAsXSjuw6r1Ai0_UfYXByOr-vfnRpYdjZHdfQS_hjSXwy5uOls6yyNIfTSyrHbyCspA3Td49RdDhtDnhkRrSb6XRNWdYpyd5sVfMsY1QFRg=s72-w640-c-h470)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/04/auditpolcis-cis-benchmark-testing-of.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)