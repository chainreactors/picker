---
title: Microsoft fixes driver blocklist placing users at risk from BYOVD attacks
url: https://buaq.net/go-131923.html
source: unSafe.sh - 不安全
date: 2022-10-21
fetch_date: 2025-10-03T20:27:05.083419
---

# Microsoft fixes driver blocklist placing users at risk from BYOVD attacks

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

Microsoft fixes driver blocklist placing users at risk from BYOVD attacks

There may be an all-new acronym for you to try and remember, as a resul
*2022-10-20 19:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-131923.htm)
阅读量:16
收藏*

---

There may be an all-new acronym for you to try and remember, as a result of [Microsoft fixing a lingering issue](https://arstechnica.com/information-technology/2022/10/how-a-microsoft-blunder-opened-millions-of-pcs-to-potent-malware-attacks). This issue is called Bring Your Own Vulnerable Driver (BYOVD), and BYOVD has been popping up in various forms for the last few months. These attacks may have been less impactful if a promoted solution from Microsoft to tackle them had been working. Unfortunately, it's come to light that this solution has *not* been behaving as it should have been.

## Bringing the party to you

Back in July, BYOVD was making waves [in the news](https://www.howtogeek.com/820374/bring-your-own-vulnerable-driver-attacks-are-breaking-windows/) . These attempts to compromise PCs work by having malware “bring along” signed drivers which are [vulnerable to exploitation](https://public.cnotools.studio/bring-your-own-vulnerable-kernel-driver-byovkd), and then placing them on the target PC. As the driver is genuine, it will theoretically bypass security checks and allow the attacker to then exploit it once on the system, using it as the launchpad to compromise the PC.

There are mitigations for this kind of activity, but it appears that one of them wasn’t doing everything it could be. In fact, Microsoft’s very own driver blocklist turns out to have been left gathering dust for roughly three years.

## A blocklist with blocking issues

The issue came to light when several people noticed this blocklist functionality didn’t appear to be working as expected.

> For years, Microsoft officials have claimed Windows can automatically block a list of malicious drivers that gets regularly updated through Windows Update. After stonewalling me and condescending to admins asking questions, MS has quietly admitted updates weren't ever pushed out. <https://t.co/Vj9oWoI893>
>
> — Dan Goodin (@dangoodin001) [October 14, 2022](https://twitter.com/dangoodin001/status/1580988509912936450?ref_src=twsrc%5Etfw)

Driver blocklisting would be a useful tool against this kind of attack if it worked as it was claimed to. If it *isn’t* operating at maximum efficiency, then attackers are able to potentially place any drivers released since whenever the last blocklist update took place. While there may well be other ways to stop these attacks from happening, the blocklist method promoted by Microsoft is [not going to be anywhere as effective as it could be](https://www.techradar.com/news/microsofts-own-mistake-may-have-left-users-at-risk-of-malware-attacks).

Despite initially dismissing the findings, Microsoft was forced to concede that there was indeed an issue, and set about getting its blocklist up to speed.

> Thanks for all the feedback. We have updated the online docs and added a download with instructions to apply the binary version directly. We're also fixing the issues with our servicing process which has prevented devices from receiving updates to the policy.
>
> — Jeffrey Sutherland (@j3ffr3y1974) [October 6, 2022](https://twitter.com/j3ffr3y1974/status/1578158506456145921?ref_src=twsrc%5Etfw)

This has been done, and the “gap in synchronisation across OS versions” has been closed. According to Tech Radar, issues related to blocklist updating will be tackled in “upcoming and future Windows updates”.

## Fuzzy answers and uncertain solutions

There is no word as to which Windows updates will do this, or how. For now, your best bet with regard to Microsoft products is use the [driver blocklist tool](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-driver-block-rules), but as Dan Goodin notes, this is a one-time update effort. You’ll still be reliant on Windows Updates down the line, because the tool doesn’t currently receive blocklist updates via Windows Updates itself.

For now, we’ll have to wait and see how this one plays out. At the very least, things are now somewhat more secure in relation to BYOVD attacks thanks to some dogged perseverance in the face of “this doesn’t work”.

文章来源: https://www.malwarebytes.com/blog/news/2022/10/microsoft-fixes-driver-blocklist-placing-users-at-risk-from-byovd-attacks
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)