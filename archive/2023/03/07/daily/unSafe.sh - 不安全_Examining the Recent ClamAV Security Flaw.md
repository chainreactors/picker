---
title: Examining the Recent ClamAV Security Flaw
url: https://buaq.net/go-152237.html
source: unSafe.sh - 不安全
date: 2023-03-07
fetch_date: 2025-10-04T08:47:27.842189
---

# Examining the Recent ClamAV Security Flaw

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

![]()

Examining the Recent ClamAV Security Flaw

But if the malware is inside some container file, such as a Zip archive, its distinct signature
*2023-3-6 20:22:31
Author: [www.forcepoint.com(查看原文)](/jump-152237.htm)
阅读量:24
收藏*

---

But if the malware is inside some container file, such as a Zip archive, its distinct signature might get encoded in some way, like being compressed, that hides it from the AV engine. So the AV engines get a bit smarter. They recognise the container file, open it, and check the files inside against the signatures.

But this means they have to understand the container file format and handle its structures—it’s no longer treating all the data as a simple pile of bytes.

This is ok, as long as no mistakes are made.

However, In this case (tracked as [CVE-2023-20032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-20032)), the container file was an Apple HFS+ file system partition file. The ClamAV engine understands this format and opens it up to find and scan the files inside. But if the file was slightly corrupt in a particular way, the AV code went wrong and accidentally executed some of the data in the file.

This is bad, particularly on Windows machines, as it happens that ClamAV is running with high levels of privilege.

This is not just a ClamAV issue. The problem is that while AV vendors are making their AV engines more effective, they are making them more complicated. And complicated things have a habit of going wrong. Security has to do complex things, but in order to be sure it works we have to [keep them simple](https://www.forcepoint.com/blog/x-labs/simplifying-complexity-in-security). This is a serious dilemma, but when it comes to defeating malware, there is a way out of it.

**Forcepoint Zero Trust CDR goes beyond basic CDR**

With Forcepoint’s [Zero Trust Content Disarm and Reconstruction](https://www.forcepoint.com/product/zero-trust-cdr) (CDR), none of the data received from a potential attacker gets delivered. Instead, the information carried by the data is pulled out, missing out any executable code, then new data is created to carry that same information to its destination. The effect of this is that any corrupt structures in the input data don't get through.

But this alone is not enough, because the Zero Trust CDR code that extracts the information has to handle the complex, potentially corrupt, structures. So if it goes wrong, the attacker might take control of it—like what happened in the ClamAV situation.

This is where Zero Trust CDR wins over basic CDR, because the two parts—extract and build—can be deployed separately with a simple interface between them. Then, if the extraction part fails to handle the input data correctly and runs the attacker’s code, the attack faces the simple interface that carries information over to the build code.

This is much simpler so there’s a lot less to go wrong. And where the threat is seriously high, it’s even possible to deploy hardware logic to verify that the information is passed correctly. So with this we can make security effective but also keep it simple.

文章来源: https://www.forcepoint.com/blog/x-labs/examining-clamav-security-flaw
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)