---
title: macOS 14 Sonoma | Toughening up macOS for the Enterprise?
url: https://buaq.net/go-167900.html
source: unSafe.sh - 不安全
date: 2023-06-09
fetch_date: 2025-10-04T11:46:00.863891
---

# macOS 14 Sonoma | Toughening up macOS for the Enterprise?

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

![](https://8aqnet.cdn.bcebos.com/ffd9cfc44f8649d658f20d717c2a8a43.jpg)

macOS 14 Sonoma | Toughening up macOS for the Enterprise?

At WWDC23 this week, Apple made some big announcements across its product lines and maintained its
*2023-6-8 21:56:47
Author: [www.sentinelone.com(查看原文)](/jump-167900.htm)
阅读量:25
收藏*

---

At [WWDC23](https://developer.apple.com/wwdc23/) this week, Apple made some big announcements across its product lines and maintained its annual ritual of upgrading macOS, now to version 14 and tagged as [macOS Sonoma](https://www.apple.com/uk/newsroom/2023/06/macos-sonoma-brings-new-capabilities-for-elevating-productivity-and-creativity/). At SentinelOne, we’re already busy testing the new operating system and preparing for macOS 14 support.

With Apple’s mixed AR/VR kit [Vision Pro](https://www.apple.com/apple-vision-pro/) predictably grabbing most of the headlines, the latest developments in macOS might have seemed a little underwhelming. However, our early look at the Sonoma beta suggests Apple has given the operating system and supporting services some much needed attention that should be welcome news to enterprise users.

Here’s a quick round-up of what’s new in the early preview released this week.

![](https://www.sentinelone.com/wp-content/uploads/2023/06/macOS-14-Sonoma-Toughening-up-macOS-for-the-Enterprise.jpg)

## Sonoma Specs | macOS 14 Hardware Requirements

Apple continues its migration away from Intel architecture with macOS Sonoma dropping support for another year’s worth of hardware. Last year, Ventura dropped support for models earlier than 2017. This year, with the exception of the iMac 2017, Sonoma requires a Mac manufactured in or after 2018.

![Sonoma supported Mac](https://www.sentinelone.com/wp-content/uploads/2023/06/Sonoma_beta_3.jpg)

Notably, Sonoma drops support for the 2017 line of Intel MacBook Pros and iMacs. The [ill-fated](https://www.macrumors.com/2019/07/09/apple-discontinues-12-inch-macbook/) MacBook, first introduced in 2015 and not updated since 2017, is now entirely cut off from further macOS upgrades.

As for the rest of the Intel line, last updated in 2019, it’s not unimaginable that Sonoma could be the end of the line. Certainly, support for Intel Macs is unlikely to extend beyond next year’s macOS 15 as the company completes its [ARM64 transition](https://www.sentinelone.com/blog/feature-spotlight-announcing-native-support-for-apple-m1/).

## Safari Profiles | Apple Taking Work Seriously

In Safari 17, users can now take advantage of Profiles to help maintain that work-life separation, something that is increasingly important as more organizations move towards allowing hybrid use of “mobile” devices – think laptops not just smartphones – in the workplace.

![Profiles macOS 14 Sonoma Safari 17](https://www.sentinelone.com/wp-content/uploads/2023/06/Screenshot-2023-06-08-at-14.20.13.jpg)

Users can make as many Profiles as they wish – work, education, social, hobbies – and each gets its own bookmarks, favorites, history, cookies, and extensions. Identification of which profile you’re in is accomplished by a simple dropdown menu in the toolbar.

## Video Conferencing | Zoom In on the Details

The pandemic unarguably changed the nature of work with video conferencing software suddenly becoming a necessity for pretty much everybody in the enterprise. Recognizing the centrality of video conferencing software to people’s workday, Sonoma introduces some enhancements that will work across third party apps. These include “Presenter Overlay” that allows the speaker to move independently of a display of their screen, allowing them to highlight different details.

![Sonoma video conferencing](https://www.sentinelone.com/wp-content/uploads/2023/06/Sonoma_beta_1.jpg)

Source: Apple

The newly-introduced screen sharing picker will also ease fears about sharing unwanted details inadvertently. Instead of having to pick an entire display to share to the audience, Sonoma will allow the user to pick just the view from a particular app, multiple apps or an entire screen.

## Passwords and Passkeys | Making Theft Harder, Sharing Simpler

Apple had previously announced [Passkeys](https://www.sentinelone.com/blog/apples-macos-ventura-7-new-security-changes-to-be-aware-of/) in Ventura as a long-term solution and replacement for passwords, but in Sonoma there’s a new emphasis on using passkeys in the workplace to help protect against cyber attacks from vectors such as [phishing](https://www.sentinelone.com/cybersecurity-101/phishing-scams/), [credential theft](https://www.sentinelone.com/resources/7-ways-cyber-criminals-steal-your-passwords/) and [2FA bypasses](https://www.sentinelone.com/blog/has-mfa-failed-us-how-authentication-is-only-one-part-of-the-solution/).

With Sonoma, passkeys are now supported across Managed Apple IDs. Moreover, admins can now control which devices users can sign in with and ensure that passkeys stay on work devices only.

Users can also create groups for passwords and passkeys such that they can be shared securely with others in the group. While this is touted primarily as a “family and friends” feature, it also has obvious benefits for small teams that need to share credentials for some common resources.

## Safari 17 | Create a Web App from Any Webpage

![Sonoma web apps](https://www.sentinelone.com/wp-content/uploads/2023/06/Sonoma_beta_2.jpg)

In Sonoma, Safari adds the ability for users to create a web app from any web page simply by browsing to the site and choosing ‘Add to Dock’ from Safari’s File menu.

The web app isn’t just a short link to open the site in the browser – it’s a completely browser-independent application. Internal links will open within the web app, though this and some other ways the web app behaves can be customized by web site devs. By default, users should remain logged in to any accounts associated with the site, but there are some gotchas for devs to look out for. More information can be found [here](https://developer.apple.com/videos/play/wwdc2023/10120/), but web apps could be a great feature for enterprises that want to provide a unique experience for either employees or customers.

## For Mac Admins | Declarative Device Management

Away from the user interface, Apple is making improvements to the way IT admins manage their fleet of Macs with further development of “DDM” – Declarative Device Management. DDM works with the existing MDM (Mobile Device Management) but is ultimately intended to replace it.  DDM brings greater support for enforcing software updates, managing applications and securing devices through task monitoring and lockdown of system services. More information about DDM can be found in the WWDC session [here](https://developer.apple.com/videos/play/wwdc2023/10041/).

## Security and Privacy | Application Data Protection

macOS Sonoma brings some under the hood changes to data security which we will be keenly testing over the beta period. Among these are new restrictions designed to protect application data such as [session cookies](https://www.sentinelone.com/blog/session-cookies-keychains-ssh-keys-and-more-7-kinds-of-data-malware-steals-from-macos-users/) and other sensitive files like databases from messaging apps (e.g., Telegram, Signal, WhatsApp and others) that can be stolen by [malware](https://www.sentinelone.com/blog/macos-payloads-7-prevalent-and-emerging-obfuscation-techniques/).

Up to now, sandboxing has been a one-way affair – sandboxed apps are prevented from reaching out to access data elsewhere, but there’s nothing to stop unsandboxed apps from *reaching in* to grab data held...