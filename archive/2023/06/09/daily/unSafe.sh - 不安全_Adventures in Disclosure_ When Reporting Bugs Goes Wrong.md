---
title: Adventures in Disclosure: When Reporting Bugs Goes Wrong
url: https://buaq.net/go-167926.html
source: unSafe.sh - 不安全
date: 2023-06-09
fetch_date: 2025-10-04T11:45:53.845285
---

# Adventures in Disclosure: When Reporting Bugs Goes Wrong

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

Adventures in Disclosure: When Reporting Bugs Goes Wrong

The Zero Day Initiative (ZDI) is the world’s largest vendor-agnostic bug bounty program. That mea
*2023-6-8 23:46:1
Author: [www.thezdi.com(查看原文)](/jump-167926.htm)
阅读量:21
收藏*

---

The Zero Day Initiative (ZDI) is the world’s largest vendor-agnostic bug bounty program. That means we purchase bug reports from independent security researchers around the world in Microsoft applications, Adobe, Cisco, Apple, IBM, Dell, Trend Micro, SCADA systems, etc. We don’t buy every bug report submitted, but we buy a lot of bugs. Of course, this means we disclose a lot of bugs. And not every disclosure goes according to plan.

**Why Disclose at All?**

This is a fine place to start. Why would anyone disclose a bug to a vendor – or anywhere for that matter? In our opinion – ***disclosure drives action***. We hope that the action will be a vendor producing a patch. We hold vendors accountable for producing patches and will release public details if they fail to take action within a reasonable timeline. Wait – what action does this drive? To start, it provides defenders with information they can use to protect their unpatched systems. It also produces additional pressure on the vendor to produce a patch. Just look at [this example](https://www.zerodayinitiative.com/blog/2017/8/17/busting-myths-in-foxit-reader). And behind the scenes, there are numerous examples of us telling a vendor we’ll 0day the case on Friday only for a patch to “appear” on Wednesday. Of course, not every patch released – scheduled or other otherwise – is of perfect quality. That’s one reason we announced special [disclosure timelines](https://www.zerodayinitiative.com/blog/2022/8/11/new-disclosure-timelines-for-bugs-from-faulty-patches) for bugs resulting from faulty or incomplete patches. We want to drive the action of vendors producing real, effective defenses for the bug reports we send them.

**Who Pays for All of This?**

This is another area where there’s a lot of public confusion. Many people think the vendors pay us for the bug reports. I wish that were true. The simple fact is that the Trend Micro Zero Day Initiative pays 100% of the cost of the vulnerabilities we acquire. And we pay before we disclose a bug to the vendor, too. Some programs only pay out when a patch is made available. When people realize the ZDI pays for the bugs we purchase, their first question usually is, “Then how do you make money?” That’s the neat part – we don’t! We take the threat intelligence we gain through bug acquisition and add it to our internal research to develop virtual patches and better filters for Trend Micro products. We take no money from other vendors through our standard program. We do have some co-sponsors for Pwn2Own events. For example, Tesla has worked with us for several years, and they are the ones providing the actual Model 3 under test. However, most of other vendors have products under test that provide no funding at all. In fact, some even refuse to participate in receiving the bug reports even though we don’t ask for any funding or compensation. That was the case in Pwn2Own Toronto for one router vendor, and this is not a unique occurrence. We’ve had other vendors decline participation. We’ve even had a few that acted surprised when we e-mailed them bugs after the contest – even though they had participated in previous events. By the way, you don’t have to be in person to participate. We disclose over Teams/Zoom all the time, even if you’re less than a two hour drive from being in the room where it happens. It’s free ~~real estate~~ bug reports, so it’s always confusing to us as to why vendors don’t want free bugs, but here we are.

**What’s the Problem with Disclosure?**

Sometimes, there isn’t a problem. We reach out to a vendor’s PSIRT and report the bug. They acknowledge receipt and produce a patch within 120 days. They publish their advisory and let us know we can publish ours. Easy peasy lemon squeezy. Unfortunately, that’s not always the case. Sometimes it’s hardy tardy lemon party. Not every vendor has a “[[email protected]](https://www.thezdi.com/cdn-cgi/l/email-protection#7f0c1a1c0a0d1a3f091a111b100d511c1012)” or “[[email protected]](https://www.thezdi.com/cdn-cgi/l/email-protection#f282819b8086b284979c969d80dc919d9f)” e-mail address. It can take some time to find the right place to notify. Not everyone is familiar with ZDI or what we do, so we get some interesting responses. We had one vendor CC their local FBI field office when replying to a bug report. I still don’t know what they expected the FBI to do. We’ve received ~~threats~~ responses from lawyers threatening all sorts of legal actions. We’ve been at this since 2005, so we’re aware of all the relevant laws (and have had some input on more than one of them). One odd problem we run in to is vendors not telling us when a patch is available. We buy lots of bugs and can’t track every step of every report. This means vendors will release a patch we don’t know about, or the advisories are paywalled, or they just choose to not involve us in the public disclosure at all. It isn’t until we inform them that we’re releasing a report as 0day that they tell us the bug was patched last month. The sad fact is that plenty of vendors do not have a robust and efficient sustained engineering program to handle bug reports, patch releases, and customer notification. In fact, it’s becoming increasingly rare to find a well-run PSIRT, and it’s something as an industry we should all be worried about.

**Why Does It Have to Be So Hard?**

Sustained engineering and running a PSIRT are not trivial. We know this. Many people on the ZDI team come from that world, so we intimately know the problems that can arise. But we have seen a disturbing trend over the last few years of companies disinvesting in these areas. We’ve already seen companies outsource support to third parties. Now, they are outsourcing PSIRT responsibilities as well. Even though many in our industry have seen this decline in quality occur, there have been no negative consequences to vendors who do not patch well. No one is losing market share due to bad patches. The insurance companies that are paying out ransomware fees aren’t chasing vendors for higher-quality fixes. There’s no legislation enacted to hold vendors accountable for poor disclosure practices. Quite frankly, this decline will likely continue until there are negative consequences.

**If I Report a Bug, Do I Have to Do All of This?**

If you report a bug to the ZDI, we handle the disclosure process entirely. We’ll keep you informed of course, but we handle all the interactions with the vendor. That’s one of the primary benefits of working with the ZDI (aside from us paying you cash). We find the e-mail address. We handle the questions from the vendor. We respond to requests for more info, or stack traces, or proof of concept, or (in rare cases) demonstration videos. Yes – we really had a vendor ask for a video. When necessary, we assign a CVE. We monitor releases as much as we can, and when the vendor informs us it’s fixed, we publish our advisory. You say want to publish a blog about the bug after the patch is available? No problem – just let us know ahead of time. We may even offer to host it for you. In other words, you’ve already done the hard part of finding the bug. Let us do the next hard part of disclosing the bug to the vendor.

**Today I Learned…**

Hopefully, this blog has educated you on something about our program. Maybe it reinforced something you already knew. Maybe you learned something new to...