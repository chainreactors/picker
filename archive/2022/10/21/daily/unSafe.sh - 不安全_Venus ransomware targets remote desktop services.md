---
title: Venus ransomware targets remote desktop services
url: https://buaq.net/go-131922.html
source: unSafe.sh - 不安全
date: 2022-10-21
fetch_date: 2025-10-03T20:27:04.516474
---

# Venus ransomware targets remote desktop services

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

Venus ransomware targets remote desktop services

It’s time for another tale of remote desktop disaster, as a newish form
*2022-10-20 19:15:0
Author: [www.malwarebytes.com(查看原文)](/jump-131922.htm)
阅读量:19
收藏*

---

It’s time for another tale of remote desktop disaster, as a newish form of ransomware carves out a name for itself. Bleeping Computer reports that individuals behind [Venus ransomware](https://www.bleepingcomputer.com/news/security/venus-ransomware-targets-publicly-exposed-remote-desktop-services/) are breaking into “publicly exposed Remote Desktop services”, with the intention of encrypting any and all Windows devices. Since at least August 2022, Venus has been causing chaos and has become rather visible lately.

> This "Venus" is some skidware ransomware. For example samples:
>
> — MalwareHunterTeam (@malwrhunterteam) [October 6, 2022](https://twitter.com/malwrhunterteam/status/1577930703098068992?ref_src=twsrc%5Etfw)

## Venus brings bad remote tidings

It seems these attacks very much follow the typical Remote Services/Remote Desktop Protocol (RDP) gameplan. Break into the network via insecure access, stop processes and services according to the whims of the ransomware authors, and then encrypt the desired files. Confused people on the network will now find their filenames end with the .venus extension, and additional file markers with no currently obvious purpose placed inside the encrypted files.

The incredibly overt ransom note, which is somewhat difficult to read given it sports white text on a bright orange background, reads as follows:

*"We downloaded and encrypted your data. Only we can decrypt your data. IMPORTANT! If you, your programmers or your friends would try to help you to decrypt the files it can cause data loss even after you pay. In this case we will not be able to help you. Do not play with files. Do not rename encrypted files. Do not try to decrypt your data using third party software, it may cause permanent data loss. Decryption of your files with the help of third parties may cause increased price or you can become a victim of a scam."*

You know, as opposed to being the victim of this scam instead.

## A risk whether at home or in the office

Bleeping Computer notes [one victim on their forum](https://www.bleepingcomputer.com/forums/t/777945/venus-ransomware-support-help-topic-venus-readmehtml/?p=5418300) made several posts about being struck by this particular slice of ransomware. This individual found their home network under attack, external drives compromised, and a PC elsewhere in the house being used as a server receiving similar treatment.

In this case, the issue was RDP left running as a way to access a computer remotely. The victim notes that RDP was password protected, but it seems the password may not have been enough. This—and the timeless classic of having backup devices available but not getting round to doing the actual backing up—proved to be a dreadful combination blow.

## Tips for avoiding the RDP to ransomware pipeline

RDP specifically continues to be a sore point for networks whether at home or in the office. Even with password protection, it may not be enough, as we've just seen to devastating effect for one unlucky individual.

If you’re running Windows 11, you’ll be pleased to know that Microsoft is taking action to help shore up the ways attackers can use RDP to break in. This has been achieved by limiting the number of times you can attempt to login, as per our [article from back in July](https://www.malwarebytes.com/blog/news/2022/07/microsoft-clamps-down-on-rdp-brute-force-attacks-in-windows-11). If you’re interested in locking down your RDP in other ways, we have a long list of tactics for you to try out. The full list of tricks and tips from March can be seen [here](https://www.malwarebytes.com/blog/news/2022/07/microsoft-clamps-down-on-rdp-brute-force-attacks-in-windows-11). Some of the key actions you should consider taking right now include:

* Use multifactor authentication for your RDP access. Attackers may crack your password, but without that second form of authentication to hand they’re going to find it a lot harder to get in.
* Rate limiting may now be somewhat redundant if you’re using Windows 11 [considering recent security changes](https://www.zdnet.com/article/this-windows-11-security-feature-makes-your-pc-very-unattractive-to-password-hackers/), but if not, this will slow down the speed that attackers can keep trying to guess your login.
* Place your RDP behind a VPN, but make sure you focus on keeping the VPN login secure as this is now your new point of access. This can be done by using multifactor authentication for login, and ensuring any email address tied to your account is similarly protected. If you're able to use rate limiting alongside your VPN login too, then so much the better.

Stay safe out there!

文章来源: https://www.malwarebytes.com/blog/news/2022/10/venus-ransomware-targets-remote-desktop-services
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)