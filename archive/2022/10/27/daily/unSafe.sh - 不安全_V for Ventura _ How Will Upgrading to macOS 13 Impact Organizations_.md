---
title: V for Ventura | How Will Upgrading to macOS 13 Impact Organizations?
url: https://buaq.net/go-132790.html
source: unSafe.sh - 不安全
date: 2022-10-27
fetch_date: 2025-10-03T20:58:21.286625
---

# V for Ventura | How Will Upgrading to macOS 13 Impact Organizations?

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

![](https://8aqnet.cdn.bcebos.com/25a9b86a8b5a9f391154a721d72fee82.jpg)

V for Ventura | How Will Upgrading to macOS 13 Impact Organizations?

This Monday saw Apple release its next OS upgrade, macOS 13 Ventura. Apple took the unusual step of
*2022-10-26 23:40:31
Author: [www.sentinelone.com(查看原文)](/jump-132790.htm)
阅读量:25
收藏*

---

This Monday saw Apple release its next OS upgrade, macOS 13 Ventura. Apple took the unusual step of pre-announcing the release date last week, perhaps in recognition of the  [calamities caused with Catalina](https://www.sentinelone.com/blog/macos-catalina-big-upgrad-dont-get-caught-out/) a couple of years ago. Then, as now, SentinelOne was ready with a supported agent (more details below) to ensure all enterprises can upgrade while remaining protected against the latest macOS malware threats.

For organizations, upgrading a major OS can be a fretful experience. In our [previous post on Ventura](https://www.sentinelone.com/blog/apples-macos-ventura-7-new-security-changes-to-be-aware-of/), we covered seven new security changes coming in macOS 13. In this post, we’ll discuss some of the wider impacts of upgrading to macOS 13 on users, admins and security teams.

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/V-for-Ventura-How-Will-Upgrading-to-macOS-13-Impact-Organizations-1.jpg?lossy=0&strip=1&webp=0)

## macOS 13 | Unlucky for Some?

Arguably the most significant change for existing macOS users is the number of models that macOS 13 doesn’t support, and for enterprises looking to upgrade to the latest and most secure version of macOS that could mean an upgrade of their Apple hardware.

Ventura requires a Mac that was manufactured no later than 2017. For MacBook Airs and Mac Minis the minimum is a 2018 model, and the 2019 model or later is required for the Mac Pro.

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ventura_release_6.jpg?lossy=0&strip=1&webp=0)

Users with hardware older than that are out of luck, although for personal devices projects like [OpenCore Legacy Patcher](https://dortania.github.io/OpenCore-Legacy-Patcher/) can revitalize aging hardware. [Security implications](https://assets.sentinelone.com/c/enterprise-mac-security?x=fvgtlj) (not to mention licensing) rule that out in organizational settings.

## Accessory Security | Not Quite Device Control

Like most recent Apple OS iterations, Ventura brings with it a new set of user ‘consent and control’ alerts. With macOS 13, this is primarily centered around USB and Thunderbolt peripherals that users plug into their Macs. These new controls, which ask users to approve or reject a new device via a dialog alert box, are intended to help protect users against malicious wired accessories, or what Apple calls “close-access attacks”.

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ventura_release_5.jpg?lossy=0&strip=1&webp=0)

Organizations using MDM solutions can choose to bypass user authorization via the `allowUSBRestrictedMode` restriction key, and other MDM options are available to control which devices a managed Mac can pair with.

There are, however, a number of caveats to bear in mind. The Accessory alert is triggered by the cable that is plugged in to the port, but after approval, users can change what device sits on the other end of a cable without causing a further prompt. In the case where the user has a USB hub or dock attached to the computer,  plugging a thumb drive into an approved hub will not trigger an alert. The other major caveat to bear in mind is the more general one with [TCC (*aka* UAC) alerts](https://www.sentinelone.com/labs/bypassing-macos-tcc-user-privacy-protections-by-accident-and-design/): if the user unknowingly plugs in a malicous flash drive, they are almost certainly going to approve the device if an alert pops up, since this was their intent when plugging it in.

Accessory security represents another barrier for threat actors to surmount, but it’s no replacement for proper and [fine-grained device control](https://www.sentinelone.com/blog/feature-spotlight-enhanced-usb-bluetooth-device-control/) managed by the security team.

## Eyes Front | Getting Organized with Stage Manager

Ventura’s headline UI feature is Stage Manager, a “new” way to control and switch application focus. We put “new” in quote marks as it turns out the concept was actually prototyped back in [2007](https://techreflect.net/2022/06/rising-from-the-ashes-stage-manager/).

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ventura_release_10.jpg?lossy=0&strip=1&webp=0)

That’s a lot of baking time! While at first glance Stage Manager might seem like a merely cosmetic addition (remember LaunchPad, anyone?), it does add some practical advantages to application management. Chief among these is the ability to organize windows into groups to create restorable ‘workspaces’, a feature that’s long been missing on macOS.

Stage Manager allows users to group windows together by dropping them onto an existing window in the strip to the left (or right, if you have your Dock on the left). Clicking on a Window group switches these to centre stage, in the orientation and size that you previously had them.

![Stage Manager on Ventura ](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ventura-Stage-Manager-v3-scaled.jpg?lossy=0&strip=1&webp=0)

What’s even nicer is that each Desktop ‘space’ has its own strip, creating lots of possibilities, particularly when combined with multiple displays.

There’s a couple of things missing with Stage Manager that would be nice to see for extra productivity: at present, adding a window to the strip is driven by drag and drop; some keyboard shortcuts would be nice. The ability to name groups would also help.

By default, Stage Manager is “off”, so turning it on requires a trip to the new System Settings.app (more on that below).

![How to turn on Stage Manager in macOS Ventura](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ventura_release_3.jpg?lossy=0&strip=1&webp=0)

## Ventura’s System Settings | Where Do You Start?

The short answer is: in the search bar! As we noted in our [preview of the Ventura beta](https://www.sentinelone.com/blog/apples-macos-ventura-7-new-security-changes-to-be-aware-of/), System Preferences has now become System Settings. Discovering where things are can be challenging compared to the System Peferences.app, and the search field is now all but mandatory.

![](https://899029.smushcdn.com/2131410/wp-content/uploads/2022/10/Ventura_release_4.jpg?lossy=0&strip=1&webp=0)

Perhaps the first and most obvious difference for security teams and admins is to update any scripts with the new name, as obviously they will fail on Ventura if they target “System Preferences”.

The settings themselves have some novelties and quirks. Persistence items are now visible and controllable to users via the **General > Login Items** menu item. Here, users can find a list of items that are set to run when the Mac is booted and when the user logs in to an account. Since the initial beta, this functionality has changed somewhat, and in the release version of Ventura only items that are labelled as ‘from an unidentified developer’ can be revealed in the Finder, via clicking the adjacent “i” button.

This is unfortunate, on two counts. First, since users cannot easily trace the parent application for items from identified developers, there is the risk that users will disable some essential services simply because they don’t recognize the name of the item displayed in System Settings. This is pa...