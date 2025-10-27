---
title: Details about the iOS Inactivity Reboot Feature
url: https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html
source: Instapaper: Unread
date: 2024-12-05
fetch_date: 2025-10-06T19:41:52.493037
---

# Details about the iOS Inactivity Reboot Feature

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Details about the iOS Inactivity Reboot Feature

I recently [wrote about](https://www.schneier.com/blog/archives/2024/11/new-ios-security-feature-makes-it-harder-for-police-to-unlock-seized-phones.html) the new iOS feature that forces an iPhone to reboot after it’s been inactive for a longish period of time.

Here are the [technical details](https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html), discovered through reverse engineering. The feature triggers after seventy-two hours of inactivity, even it is remains connected to Wi-Fi.

Tags: [Apple](https://www.schneier.com/tag/apple/), [iOS](https://www.schneier.com/tag/ios/), [iPhone](https://www.schneier.com/tag/iphone/), [law enforcement](https://www.schneier.com/tag/law-enforcement/), [reverse engineering](https://www.schneier.com/tag/reverse-engineering/)

[Posted on December 2, 2024 at 7:08 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html) •
[12 Comments](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html#comments)

### Comments

Paul Sagi •
[December 2, 2024 8:21 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441936)

Interesting that the Apple code is so transparent that it’s easy to reverse engineer.

John White •
[December 2, 2024 6:03 PM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441941)

I’m not convinced that this has been fully answered. It’s great that this feature exists, and it would be even better if Apple made it possible to adjust the time down so that it occurs more rapidly, but is it conclusively proven that button activity, interaction with the touch screen etc does not reset the timer as actually unlocking the phone would? Because the risk is that pigs and other bad actors could simply automate button clicks- or manually ‘touch’ all the phones- to extend the unlock time.

ResearcherZero •
[December 2, 2024 11:53 PM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441945)

@John White

The countdown timer is likely started each time the device is locked. Therefore the device would have to be in an unlocked to state to stop the inactivity timer from counting down.

*“The Secure Enclave Processor (SEP) keeps track on when your phone was last unlocked.”*

‘https://naehrdine.blogspot.com/2024/11/reverse-engineering-ios-18-inactivity.html

ResearcherZero •
[December 3, 2024 12:39 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441946)

Not that it is guaranteed to keep attackers from targeting your phone with some kind of spyware, or discovering your authentication details via other surveillance methods.

If a device contains sensitive information then remotely wiping it as soon as possible may prevent data from being accessed, as long as the device has not been shielded/turned off.

There are alternative solutions with a 10 minute inactivity timer and a scrambled 128 character password, with charging only allowed from a locked state to reduce attacks. Yet all the same caveats apply with such secure mobile operating system implementations. If an attacker has physical access to a device, they can hold onto it until such time an exploit is released that the device has not yet been patched to the prevent that exploit method.

Apple does not implement the remote wipe/anti-theft features in the device BIOS, yet bootkits that exploited recovery mode were developed and zero-click spyware with support for later updates or new modules that could support yet undiscovered exploits exist. So even without physical access, a well resourced adversary can defeat any security measures.

However, if you practice good OPSEC, then none of that will matter.

ResearcherZero •
[December 3, 2024 12:53 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441947)

Keep in mind your family, friends and colleagues likely will **not** practice good OPSEC.

ResearcherZero •
[December 3, 2024 6:23 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441952)

One should also assume those administering the law understand little about IT.

‘https://www.postofficescandal.uk/post/proposed-amendment-to-legal-assumption-about-the-reliability-of-computers/

MDK •
[December 3, 2024 3:15 PM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441972)

@All

Feature should have been implemented a long time ago.

@Bruce

I’m sure you are aware but a confirmed nation state cyber campaign running against US Telco etc. It’s not good from the sounds of it. Dangerous times indeed.

MDK

anon •
[December 3, 2024 6:00 PM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441974)

re: JW
Wouldn’t that simply increase the delay before the phone could be unlocked? Even if you pressed ‘1’ ‘backspace’ repeatedly?

ResearcherZero •
[December 4, 2024 12:49 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441977)

@anon

The way countdown timers are generally implemented ensures that simply pressing keys or touching the screen will cause no effect to the countdown once the device is locked. If anyone attempts to interfere with the countdown timer through an exploit, that should cause kernel panic which will then cause the phone to reboot, hopefully neutering the attack.

‘https://en.wikipedia.org/wiki/Init

Clive Robinson •
[December 4, 2024 4:02 AM](https://www.schneier.com/blog/archives/2024/12/details-about-the-ios-inactivity-reboot-feature.html/#comment-441984)

@ ResearcherZero, ALL,

With regards your comment,

> “Keep in mind your family, friends and colleagues likely will not practice good OPSEC.”

In my experience in life a couple of aspects to this occur,

1, Even when a persons very life depends on OpSec / Situational Awareness, they stop doing it effectively or at all very quickly.

2, No matter how you try to make others aware of the importance of OpSec / Situational Awareness, they will discount you, tell you you are paranoid, and tell others you are weird / mad.

Yet when their number comes up for “unpleasantness” from those with “ill interest” etc against them, they blame you for not pushing / explaining / etc to them hard / well enough…

Yes I understand OpSec / Situational Awareness has a cognitive load, as well as a required mind set, but why do they not want to take responsibility for their own actions?

I know, you don’t have to answer that, after all the expression “low hanging f...