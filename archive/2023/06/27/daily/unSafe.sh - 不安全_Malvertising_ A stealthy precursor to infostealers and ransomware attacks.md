---
title: Malvertising: A stealthy precursor to infostealers and ransomware attacks
url: https://buaq.net/go-170455.html
source: unSafe.sh - 不安全
date: 2023-06-27
fetch_date: 2025-10-04T11:44:55.853180
---

# Malvertising: A stealthy precursor to infostealers and ransomware attacks

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

![](https://8aqnet.cdn.bcebos.com/ebb7091a150efefd4e1d2811478f8284.jpg)

Malvertising: A stealthy precursor to infostealers and ransomware attacks

This article is based on research by Jérôme Segura, Senior Director of
*2023-6-26 18:45:0
Author: [www.malwarebytes.com(查看原文)](/jump-170455.htm)
阅读量:32
收藏*

---

*This article is based on research by [Jérôme Segura](https://www.malwarebytes.com/blog/authors/jeromesegura), Senior Director of Threat Intelligence at Malwarebytes, who oversees data collection from spam feeds and telemetry to identify the most relevant threats.*

[Malvertising](https://www.malwarebytes.com/malvertising), the practice of using online ads to spread malware, can have dire consequences—and the problem only seems to be growing.

[New research from the](https://try.malwarebytes.com/business-threat-intel-hub/) [Malwarebytes Threat Intelligence](https://www.malwarebytes.com/blog/category/threat-intelligence) team shows over 800 malvertising-related attacks in 2023 so far alone, an average of almost 5 attacks per day. But even these are only the ones reported by security researchers—in reality the number is much higher.

Our research indicates that malvertising ads often deliver [infostealer](https://www.malwarebytes.com/blog/threats/info-stealers) malware such as IcedID, Aurora Stealer, and BATLOADER among others. These programs steal credentials from users’ browsers or computers, sowing the seeds for a future ransomware attack. ![](https://www.malwarebytes.com/blog/business/2023/06/easset_upload_file7485_270834_e.png)

Malvertising attack count throughout 2023

[Ransomware gangs](https://www.malwarebytes.com/blog/business/2022/10/what-is-ransomware-as-a-service-and-how-is-it-evolving)often buy stolen credentials from other cyber criminals involved in the dirty work of initial access brokering. In the case of malvertising, the chain of events looks something like this:

1. **Malvertising campaigns infect users with infostealers.**
2. **Infostealers harvest user credentials.**
3. **Stolen credentials are sold in underground forums.**
4. **Ransomware actors buy these credentials to infiltrate networks.**

Alternatively, some ransomware gangs have been observed use malvertising themselves to launch an attack on a victim machine directly.

[The Royal ransomware group](https://www.malwarebytes.com/blog/business/2023/06/5-facts-to-know-about-the-royal-ransomware-gang), for example, used malvertising to disguise BATLOADER as legitimate installers for applications like TeamViewer. BATLOADER then drops a Cobalt Strike Beacon as a precursor to the ransomware execution.

For organizations looking to nip the malvertising-ransomware connection in the bud, however, perhaps the biggest challenge is how hard malvertising can be to spot. Threat actors often impersonate the official brand name and website in the ad snippet, making attacks extremely deceptive for the average user.

![](https://www.malwarebytes.com/blog/business/2023/06/easset_upload_file75932_270834_e.png)Can you spot the typo in this malvertising attempt?

Even experts at Google have struggled to identify malicious redirects from an ad, underscoring the fact that malvertising is a nuanced, technical problem that requires advanced tools to spot.

In other words, your defense strategy against malvertising shouldn't hinge entirely on your team recognizing brand impersonation. Instead, focus on equipping your team with advanced security tools to do the heavy lifting.

Some of the main tools you can use to prevent malvertising include:

* **[Vulnerability and patch management software](https://www.malwarebytes.com/blog/business/2022/09/vulnerability-response-for-smbs-the-malwarebytes-approach):** Malvertising often exploits known vulnerabilities in systems, applications, or browsers. These tools can help ensure that web browsers (including plug-ins) are up-to-date with the latest security patches.
* **[Web protection applications](https://www.malwarebytes.com/blog/business/2023/04/port-scan-attacks-protecting-your-business-from-rdp-attacks-and-mirai-botnetshttps%3A//www.malwarebytes.com/business/edr):** Since malvertising campaigns often rely on connecting to malicious servers to download additional malware or steal information, blocking these connections can stop the attack in its tracks.
* **Ad blockers:** These can filter out potential malvertising threats and prevent hazardous content from loading. [Malwarebytes Browser Guard](https://www.malwarebytes.com/browserguard) provides additional protection to standard ad-blocking features by covering a larger area of the attack chain all the way to domains controlled by attackers.

Download the Malwarebytes Threat Intelligence Threat Brief today for comprehensive insights on malvertising and its role in stealing credentials.

[Download Now](https://try.malwarebytes.com/business-threat-intel-hub/)

文章来源: https://www.malwarebytes.com/blog/business/2023/06/malvertising-a-stealthy-precursor-to-infostealers-and-ransomware-attacks
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)