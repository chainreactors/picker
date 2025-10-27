---
title: Mac Admins | Why Apple’s Silent Approach to Endpoint Security Should be a Wake-Up Call
url: https://buaq.net/go-173527.html
source: unSafe.sh - 不安全
date: 2023-08-03
fetch_date: 2025-10-04T12:00:31.200982
---

# Mac Admins | Why Apple’s Silent Approach to Endpoint Security Should be a Wake-Up Call

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

![](https://8aqnet.cdn.bcebos.com/754a66e8a42913f7b13625d00e6431a3.jpg)

Mac Admins | Why Apple’s Silent Approach to Endpoint Security Should be a Wake-Up Call

If there’s one thing that everyone should be able to agree on about Apple, it is that the company r
*2023-8-2 23:23:53
Author: [www.sentinelone.com(查看原文)](/jump-173527.htm)
阅读量:23
收藏*

---

If there’s one thing that everyone should be able to agree on about Apple, it is that the company really does [think different](https://www.forbes.com/sites/onmarketing/2011/12/14/the-real-story-behind-apples-think-different-campaign/) when it comes to the design of its products, and this is nowhere more obvious than in the company’s approach to endpoint security. Users will find no Defender-like security center built into macOS, and admins and IT teams will search in vain for Apple web portals to log into or extra licenses to buy for ‘top tier’ telemetry.

Unlike rival OS vendors, Apple does endpoint security when – and where – admins and users aren’t looking. This approach has served Apple well from a marketing perspective – there’s a widespread if somewhat [misplaced belief](https://www.sentinelone.com/blog/which-is-more-secure-windows-linux-or-macos/) that macOS is more secure than Windows – but for small to medium-sized enterprises relying entirely on Apple to keep them safe, this lack of visibility is something to be addressed.

In this post, we’ll shed light on three areas of macOS security that are crucial to understand for businesses that do not currently deploy additional endpoint protection on their macOS devices.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/3-Hidden-Facts-About-macOS-Security-Every-Security-Team-Should-Know-6.jpg)

## Apple’s Approach to Platform Security

Last updated in May 2022, Apple’s most recent public [documentation](https://support.apple.com/en-gb/guide/security/sec469d47bd8/1/web/1) about protecting against malware on macOS states that its malware defenses are structured in three layers:

|  |  |
| --- | --- |
| **Service** | **Technologies** |
| Prevent launch or execution of malware | App Store, or Gatekeeper combined with Notarisation |
| Block malware from running on customer systems | Gatekeeper, Notarisation and XProtect |
| Remediate malware that has executed | XProtect |

None of the [technologies responsible](https://www.sentinelone.com/resources/the-complete-guide-to-understanding-apple-mac-security-for-enterprise/) in these layers has much in the way of user or admin-controlled granularity: it’s not possible, for example, to allow or exclude certain applications or code across users or devices. On a single device, a user *can* make extremely broad system policy decisions (such as allow or deny all apps sourced from outside the App Store), but even then – unless the system is administered by an MDM solution – that policy can be overridden by local users, even without administrator rights.

More concerning from an enterprise security perspective is that there is little visibility into what code has been blocked, when and why, nor is it obvious when these scans are being performed or how effective they have been.

This is a particular worry in terms of malware remediation, which happens silently in the background without warning to the user. In an enterprise setting, this is simply not sufficient: security teams need to understand when malware was introduced to the system, how long it was there and where malware came from if they are to adequately defend the enterprise.

## 1. XProtect Signatures | Missing Out On the Latest Malware

According to [Apple](https://support.apple.com/en-gb/guide/security/sec469d47bd8/1/web/1),

*macOS includes built-in antivirus technology called XProtect for the signature-based detection and removal of malware. The system uses YARA signatures, a tool used to conduct signature-based detection of malware, which Apple updates regularly.*

The last update to Apple’s `XProtect.bundle` which contains these YARA signatures was made on June 29th, though the update may have not been released till some days later depending on location of the user.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/apple_hidden_2.jpg)

Unfortunately, this update did not include any changes to the YARA signatures that Apple says power XProtect’s blocking abilities. The YARA file bears the same hash as version 2166, updated last February.

![](https://www.sentinelone.com/wp-content/uploads/2023/08/apple_hidden_1.jpg)

If one were to go by the version numbers, there should have been 7 updates to XProtect’s YARA rules in the last 12 months, but in fact only three have actually been observed in our test machines. In addition, the difference between v2165 released last November and the current version contains only three new rules, one for [Keysteal](https://www.sentinelone.com/wp-content/uploads/pdf-gen/1679501162/session-cookies-keychains-ssh-keys-and-more-7-kinds-of-data-malware-steals-from-macos-users.pdf) and two for a cryptominer known to Apple as [Honkbox](https://www.sentinelone.com/blog/hunting-for-honkbox-multistage-macos-cryptominer-may-still-be-hiding/).

Since both [SentinelOne](https://www.sentinelone.com/blog/apple-crimeware-massive-rust-infostealer-campaign-aiming-for-macos-sonoma-ahead-of-public-release/) and many other vendors have [reported on](https://www.sentinelone.com/blog/atomic-stealer-threat-actor-spawns-second-variant-of-macos-malware-sold-on-telegram/) multiple new [macOS malware](https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/) strains in the last few months alone, it should be concerning to users and admins relying entirely on XProtect’s rules that they are so far behind the rest of the industry.

## 2. XProtectRemediator | Hiding Infections After-the-Fact

Despite the lack of updates to Apple’s primary malware blocking tool, the company has been updating its [MRT-replacement tool](https://www.sentinelone.com/wp-content/uploads/2021/11/The-Complete-Guide-to-Understanding-Apple-Mac-Security-for-Enterprise.pdf) XProtectRemediator more regularly. XProtectRemediator runs at intervals of around 6 hours per day, looking for a small collection of known malware families.

While the increased attention there is an improvement on the [old MRT.app](https://www.sentinelone.com/blog/apples-malware-removal-mrt-tool-update/), the focus on remediation rather than blocking should be of concern to enterprise security teams. 6 hours is far too long for [infostealers](https://www.sentinelone.com/blog/atomic-stealer-threat-actor-spawns-second-variant-of-macos-malware-sold-on-telegram/) to be in the organization, particularly as they take only seconds to do their work. [Session cookies](https://www.sentinelone.com/blog/session-cookies-keychains-ssh-keys-and-more-7-kinds-of-data-malware-steals-from-macos-users/) are primary targets for threat actors to worm their way further into organizations and turn compromises from a single Mac into a serious breach, such as happened recently at [CircleCI](https://circleci.com/blog/jan-4-2023-incident-report/#c-consent-modal).

As noted above, there is no user interface on macOS for understanding what malware has been remediated, when or how it was introduced into the system. However, as of [macOS Ventura](https://www.sentinelone.com/blog/v-for-ventura-how-will-upgrading-to-macos-13-impact-organizations/), system administrators without 3rd party visibility tools can attempt to leverage the [eslogger](https://www.sentinelone.com/blog/apples-macos-ventura-7-new-security-changes-to-be-aware-o...