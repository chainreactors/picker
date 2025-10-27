---
title: OpenSSL 3 Critical Vulnerabililty | What Do Organizations Need To Do Now?
url: https://buaq.net/go-133548.html
source: unSafe.sh - 不安全
date: 2022-11-01
fetch_date: 2025-10-03T21:23:27.739835
---

# OpenSSL 3 Critical Vulnerabililty | What Do Organizations Need To Do Now?

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

![](https://8aqnet.cdn.bcebos.com/894153fe9c712d1f9f98892d979d8e59.jpg)

OpenSSL 3 Critical Vulnerabililty | What Do Organizations Need To Do Now?

Last week, the OpenSSL project team announced the release of OpenSSL version 3.0.7, which will be m
*2022-10-31 22:33:19
Author: [www.sentinelone.com(查看原文)](/jump-133548.htm)
阅读量:26
收藏*

---

Last week, the OpenSSL project team [announced](https://mta.openssl.org/pipermail/openssl-announce/2022-October/000238.html) the release of OpenSSL version 3.0.7, which will be made available on Tuesday, November 1st. The update is a security fix for a critical vulnerability in OpenSSL 3.0.x, and developers and organizations are being urged to ensure that they patch any instances of OpenSSL 3 in their software stack as a matter of urgency. The vulnerability is reported to affect version 3.0.x and does not impact OpenSSL 1.1.1 or LibreSSL.

SentinelOne customers have instant visibility of OpenSSL versions within their organizations.  As such, Singularity XDR becomes a useful visibility solution in ensuring your organization is ready for the Tuesday, Nov 1st OpenSSL updates.

![](https://www.sentinelone.com/wp-content/uploads/2022/10/OpenSSL-3-Critical-Vulnerability-What-Do-Organizations-Need-To-Do-Now.jpg)

## What is OpenSSL?

OpenSSL is an open-source cryptography library widely used by applications, operating systems and websites to secure communications over the internet using SSL (Secure Sockets Layer) and TLS (Transport Layer Security). OpenSSL has been around since 2012, with version 3 released in September 2021, and is one of the most widely used open-source libraries worldwide.

## Which Versions Of OpenSSL Are Vulnerable?

OpenSSL version 3.0.0 and higher are vulnerable to the critical security flaw, which is patched in version 3.0.7. The majority of OpenSSL implementations in use today use version 1.1.1 or 1.0.2; however, OpenSSL 3 is bundled with many flavors of Linux, including RedHat, Fedora, CentOS, Linux Mint and others.

Docker containers typically include some version of OpenSSL but which version and whether it is vulnerable will depend on the original configuration. The library can also be optionally installed on macOS and Windows devices, although by default Macs run the unaffected LibreSSL library. Vulnerable versions of OpenSSL are also used in popular development software like Gradle, privacy tools such as TOR and security platforms like Kali Linux.

**Vulnerable**

* OpenSSL 3.0.x

**Not Vulnerable**

* OpenSSL 1.1.1
* OpenSSL 1.1.0
* OpenSSL 1.0.2
* OpenSSL 1.0.1
* LibreSSL

## What Is the Risk with OpenSSL 3 Critical Vulnerability?

Although there are few details of the vulnerability at present and a CVE is yet to be assigned, the OpenSSL project [says](https://www.openssl.org/policies/general/security-policy.html) that a critical vulnerability affects common configurations which are likely to be exploitable. In addition, flaws with a ‘critical’ severity rating include those which can be easily exploited remotely or where remote code execution is considered likely.

This isn’t the first time OpenSSL has suffered from a critical vulnerability. In 2014,  CVE-2014-0160, dubbed Heartbleed, was discovered in OpenSSL v1.0.1. Heartbleed was due to a buffer over-read in the TLS Heartbeat Extension, which allowed more data to be read than should be allowed. In practice, the bug could be exploited to acquire passwords or encryption keys.

Despite the patch being available the same day the flaw was disclosed, many were slow to patch. The bug was used to compromise a number of websites and steal sensitive data, including Social Insurance Numbers belonging to Canadian taxpayers. Even 5 years after initial disclosure, it was estimated that over 90,000 servers remained vulnerable to Heartbleed.

## How To Prepare and Patch the OpenSSL 3 Critical Vulnerability

As with Heartbleed, which was rapidly exploited, organizations need to ensure that they prioritize discovering and patching the OpenSSL critical vulnerability as soon as the update to 3.0.7 is made available, estimated to be between 1300-1700 UTC on Tuesday 1st November.

SentinelOne customers can run queries to determine which endpoints are running vulnerable versions of OpenSSL in the management console. Customers should consult the KB documentation [here](https://support.sentinelone.com/hc/en-us/articles/9901837777687).

![openssl hunting in SentinelOne](https://www.sentinelone.com/wp-content/uploads/2022/10/openssl-hunting-in-SentinelOne.jpg)

End users can run simple queries locally to see if their operating system contains the vulnerable version.

`openssl version`

![An Ubuntu distro vulnerable to the OpenSSL vulnerability.](https://www.sentinelone.com/wp-content/uploads/2022/10/Vulnerable-Ubuntu-Distro.jpg)

An Ubuntu distro vulnerable to the OpenSSL vulnerability.

## Conclusion

Organizations and IT teams can become weary of patch warnings. [Vulnerability discovery](https://www.sentinelone.com/labs/our-cves/) is at an all time high, and despite the evidence that attackers [routinely exploit](https://www.sentinelone.com/blog/enterprise-security-essentials-top-15-most-routinely-exploited-vulnerabilities-2022/) flaws in popular software and operating systems, patch management doesn’t always get the time and resources it should.

Even so, a critical vulnerability in a software library like OpenSSL, which is so widely in use and so fundamental to the security of data on the internet, is one that no organization can afford to overlook or delay, as many learned in the wake of the Heartbleed bug.

As further details emerge over the coming days, SentinelOne will update this post. What organizations can do now is determine how much exposure they have to OpenSSL 3 and allocate the necessary resources to update to 3.0.7 as soon as possible.

文章来源: https://www.sentinelone.com/blog/openssl-3-critical-vulnerabililty-what-do-organizations-need-to-do-now/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)