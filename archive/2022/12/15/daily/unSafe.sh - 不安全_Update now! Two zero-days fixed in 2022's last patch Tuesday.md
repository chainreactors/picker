---
title: Update now! Two zero-days fixed in 2022's last patch Tuesday
url: https://buaq.net/go-140061.html
source: unSafe.sh - 不安全
date: 2022-12-15
fetch_date: 2025-10-04T01:29:34.484072
---

# Update now! Two zero-days fixed in 2022's last patch Tuesday

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

Update now! Two zero-days fixed in 2022's last patch Tuesday

In numbers, the patch Tuesday of December 2022 is a relatively light on
*2022-12-14 23:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-140061.htm)
阅读量:17
收藏*

---

In numbers, the patch Tuesday of December 2022 is a relatively light one for Windows users. Microsoft patched 48 vulnerabilities with only six considered critical. But numbers are only half the story. Two of the updates are zero-days with one of them known to be actively exploited.

## Windows SmartScreen

Publicly disclosed computer security flaws are listed in the Common Vulnerabilities and Exposures (CVE) database. Its goal is to make it easier to share data across separate vulnerability capabilities (tools, databases, and services).

The vulnerability that is [exploited in the wild](https://www.malwarebytes.com/blog/news/2022/11/qbot-uses-zero-day-motw-bypass-in-phishing-campaign) is listed under [CVE-2022-44698](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44698) and described as a Windows SmartScreen Security Feature bypass vulnerability. To understand how this works, you need to understand that files can be cryptographically signed in order to confirm who created them, and to confirm that they have not been changed since they were signed. [Mark-of-the-Web (MOTW)](https://www.malwarebytes.com/blog/news/2022/10/malware-authors-use-malformed-signature-trick-to-bypass-mark-of-the-web) is the name for the Windows technology that warns users of potential harm when downloading and opening a file from the internet or an email attachment. In other words, it's a safety precaution in the form of a reminder that the user is about to use a risky file that might harm their computer. The problem is that a malformed signature bypasses all the warnings you should get, so you are bound to assume everything is dandy while it’s not.

## DirectX Graphics Kernel

The other zero-day is labeled as “Exploitation Less Likely” but information about the vulnerability has been made public. The vulnerability is listed as [CVE-2022-44710](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44710) and described as a DirectX Graphics Kernel Elevation of Privilege (EoP) vulnerability. To successfully exploit it the attacker would need to win a race condition. But if they succeed they could gain SYSTEM privileges.

A race condition, or race hazard, is the behavior of a system where the output depends on the sequence or timing of other uncontrollable events. It becomes a bug when events do not happen in the order the programmer intended. Sometimes these bugs can be exploited when the outcome is predictable and works to the attackers’ advantage.

## Windows Secure Socket Tunneling Protocol

Two critical vulnerabilities we want to highlight were found in the Windows Secure Socket Tunneling Protocol (SSTP). [CVE-2022-44670](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44670)and [CVE-2022-44676](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-44676)are remote code execution (RCE) vulnerabilities. Successful exploitation of these vulnerabilities requires an attacker to win a race condition but when successful could enable an attacker to remotely execute code on a remote access server (RAS).

A RAS is a type of server that provides a suite of services to remotely connected users over a network or the Internet. It operates as a remote gateway or central server that connects remote users with an organization's internal local area network (LAN).

## PowerShell

One more vulnerability we want to highlight because exploitation is more likely is listed as [CVE-2022-41076](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-41076) and described as a PowerShell RCE vulnerability. Successful exploitation of this vulnerability requires an attacker to take additional actions prior to exploitation to prepare the target environment and to be authenticated. If these conditions are met, the attacker could escape the PowerShell Remoting Session Configuration and run unapproved commands on the target system. This seems a very likely candidate to be chained or exploited in combination with leaked or stolen login credentials.

## Other vendors

As per usual, other vendors also released important updates:

Adobe released updates for [Adobe Campaign Classic](https://helpx.adobe.com/security/products/campaign/apsb22-58.html), [Adobe Experience Manager](https://helpx.adobe.com/security/products/experience-manager/apsb22-59.html), and [Adobe Illustrator](https://helpx.adobe.com/security/products/illustrator/apsb22-60.html).

Apple released several updates. More on that later.

Cisco released updates for [Cisco IP Phone 7800 and 8800 phones](https://www.cisco.com/c/dam/global/en_hk/solutions/collaboration/files/white-paper-c11-739097.pdf).

Citrix released updates for [Citrix ADC and Citrix Gateway](https://www.citrix.com/blogs/2022/12/13/critical-security-update-now-available-for-citrix-adc-citrix-gateway/).

Fortinet released an update to patch for an actively exploited [FortiOS SSL-VPN vulnerability](https://www.fortiguard.com/psirt/FG-IR-22-398).

Google released an Android security bulletin [we discussed last week](https://www.malwarebytes.com/blog/news/2022/12/update-now-google-patches-android-vulnerability-that-allows-remote-code-execution-over-bluetooth).

Mozilla released updates for for [Thunderbird 102.6](https://www.mozilla.org/en-US/security/advisories/mfsa2022-53/), [Firefox ESR 102.6](https://www.mozilla.org/en-US/security/advisories/mfsa2022-52/), and [Firefox 108](https://www.mozilla.org/en-US/security/advisories/mfsa2022-51/).

SAP has released its round of [December 2022 updates](https://dam.sap.com/mac/app/e/pdf/preview/embed/ucQrx6G?ltr=a&rc=10).

VMWare has released security updates for multiple products. Users should review the VMware Security Advisories [VMSA-2022-0031](https://www.vmware.com/security/advisories/VMSA-2022-0031.html), [VMSA-2022-0033](https://www.vmware.com/security/advisories/VMSA-2022-0033.html), and apply the necessary updates.

---

文章来源: https://www.malwarebytes.com/blog/news/2022/12/update-now-the-last-patch-tuesday-of-2022-fixes-two-zero-days
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)