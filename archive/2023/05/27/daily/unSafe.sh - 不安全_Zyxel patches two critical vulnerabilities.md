---
title: Zyxel patches two critical vulnerabilities
url: https://buaq.net/go-165977.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:07.813145
---

# Zyxel patches two critical vulnerabilities

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

Zyxel patches two critical vulnerabilities

Zyxell has released a security advisory for multiple buffer overflow vu
*2023-5-26 23:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-165977.htm)
阅读量:31
收藏*

---

Zyxell has released a [security advisory](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-multiple-buffer-overflow-vulnerabilities-of-firewalls) for multiple buffer overflow vulnerabilities. Exploitation of these vulnerabilities could allow an unauthenticated attacker to cause denial-of-service (DoS) conditions and even a remote code execution on the affected Zyxell firewalls.

Affected users should patch as a matter of urgency, and we urge you not to expose the management interfaces of network edge devices to the Internet, in order to reduce their attack surface.

The Common Vulnerabilities and Exposures (CVE) database lists publicly disclosed computer security flaws. The CVEs patched in these updates are:

[CVE-2023-33009](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33009): A buffer overflow vulnerability in the notification function in Zyxel ATP series firmware versions 4.32 through 5.36 Patch 1, USG FLEX series firmware versions 4.50 through 5.36 Patch 1, USG FLEX 50(W) firmware versions 4.25 through 5.36 Patch 1, USG20(W)-VPN firmware versions 4.25 through 5.36 Patch 1, VPN series firmware versions 4.30 through 5.36 Patch 1, ZyWALL/USG series firmware versions 4.25 through 4.73 Patch 1.

[CVE-2023-33010](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-33010): Another buffer overflow vulnerability in the ID processing function in the same Zyxel firmware versions.

A buffer overflow is a type of software vulnerability that exists when an area of memory within a software application reaches its address boundary and writes into an adjacent memory region.

Both vulnerabilities received a [CVSS score](https://www.malwarebytes.com/blog/news/2020/05/how-cvss-works-characterizing-and-scoring-vulnerabilities) of 9.8 out of 10. In case that isn't enough reason for you to act urgently, it is worth remembering that it only took four days for the first active exploitation to take place after Zyxel patched [CVE-2022-30525](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-30525) last year.

The security advisory lists the vulnerable firewall series that are within their vulnerability support period:

* ATP versions ZLD V4.32 to V5.36 Patch 1 are covered by ZLD V5.36 Patch 2.
* USG FLEX versions ZLD V4.50 to V5.36 Patch 1 are covered by ZLD V5.36 Patch 2.
* USG FLEX50(W) / USG20(W)-VPN versions ZLD V4.25 to V5.36 Patch 1 are covered by ZLD V5.36 Patch 2.
* VPN versions ZLD V4.30 to V5.36 Patch 1 are covered by ZLD V5.36 Patch 2.
* ZyWALL/USG versions ZLD V4.25 to V4.73 Patch 1 are covered by  ZLD V4.73 Patch 2.

## How to install updates

Login to your ZLD appliance and go to **Configuration → Licensing → Registration → Service** and click the **Service License Refresh** button.  This must be done before you can access your myZyxel account to download new firmware patches. This will sync necessary info with the myZyxel server (info like running firmware version, MAC Address, S/N, etc.).

Open an internet browser and go to URL: <https://portal.myzyxel.com/> and login to your account.

Once in your account dashboard, find the ZLD router you wish to download firmware for and click on the Download button under the "Firmware Update" column.

Once downloaded, there may be up to four ways you can update the firmware, you can update the firmware manually via the Web GUI, you can FTP into the router and upload the firmware, you can utilize the Automatic Cloud Firmware update feature introduced on firmware version 4.25, or upgrade via USB flash drive.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/05/zyxel-patches-two-critical-vulnerabilities-which-could-lead-to-remote-take-over
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)