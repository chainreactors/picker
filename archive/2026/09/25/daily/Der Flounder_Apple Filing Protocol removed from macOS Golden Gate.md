---
title: Apple Filing Protocol removed from macOS Golden Gate
url: https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/
source: Der Flounder
date: 2026-09-25
fetch_date: 2026-09-26T06:50:24.188198
---

# Apple Filing Protocol removed from macOS Golden Gate

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Apple Filing Protocol removed from macOS Golden Gate

## Apple Filing Protocol removed from macOS Golden Gate

September 25, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

One of the less documented changes to macOS Golden Gate is the removal of [Apple Filing Protocol](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/AFP/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000854-CH1-SW1) (AFP) as a supported network protocol. AFP was first introduced as part of Apple’s [System 6 operating system](https://en.wikipedia.org/wiki/System_6) in 1988 and was Apple’s primary network protocol for connecting to file services up through [OS X 10.8 Mountain Lion](https://en.wikipedia.org/wiki/OS_X_Mountain_Lion).

Beginning with [OS X Mavericks 10.9](https://en.wikipedia.org/wiki/OS_X_Mavericks), Apple started transitioning file services to using [Server Message Block](https://en.wikipedia.org/wiki/Server_Message_Block) (SMB) in place of AFP for both hosting file services and connecting to them from a Mac, but connecting to AFP file services continued to work in Mavericks and later versions of OS X and macOS. However, Apple signaled that AFP was completely on its way out when they included a note for macOS Sequoia 15.5 in the [What’s new for enterprise in macOS Sequoia](https://support.apple.com/121011) release notes that AFP was deprecated and would be removed in a future version of macOS.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/09/screenshot-2026-09-25-at-11.51.png?w=599&h=230 "Screenshot 2026-09-25 at 11.51.png")

Apple did not make further mention of the removal status in their posted documentation, but in macOS 26 Tahoe (the macOS version preceding Golden Gate), there is a warning which appears when you try to set up a [Time Capsule](https://en.wikipedia.org/wiki/AirPort_Time_Capsule) for [Time Machine](https://en.wikipedia.org/wiki/Time_Machine_%28macOS%29) backups. That warning states that next major version of macOS will no longer support AirPort Disk or other Time Capsule disks for Time Machine backups.

![GtEqP14XUAA -bl 1.](https://derflounder.wordpress.com/wp-content/uploads/2026/09/gteqp14xuaa_-bl_1.png?w=600&h=302 "GtEqP14XUAA_-bl_1.png")

Time Capsules use AFP for their network file sharing, so this warning meant that AFP was likely gone in macOS 27 Golden Gate. This has proved to be the case for Golden Gate and support for AFP has been removed.

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/?share=tumblr)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/09/25/apple-filing-protocol-removed-from-macos-golden-gate/#respond)

Δ

[App Settings declarative management may block unsigned apps on macOS Golden Gate](https://derflounder.wordpress.com/2026/09/24/app-settings-declarative-management-may-block-unsigned-apps-on-macos-golden-gate/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

September 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | 1 | 2 | 3 | 4 | 5 | 6 |
| 7 | [8](https://derflounder.wordpress.com/2026/09/08/) | 9 | 10 | 11 | 12 | 13 |
| [14](https://derflounder.wordpress.com/2026/09/14/) | [15](https://derflounder.wordpress.com/2026/09/15/) | 16 | 17 | 18 | 19 | 20 |
| 21 | 22 | 23 | [24](https://derflounder.wordpress.com/2026/09/24/) | [25](https://derflounder.wordpress.com/2026/09/25/) | 26 | 27 |
| 28 | 29 | 30 |  | | | |

[« Aug](https://derflounder.wordpress.com/2026/08/)

### Recent Comments

|  |  |
| --- | --- |
| ![David Young's avatar](https://1.gravatar.com/avatar/de72034a6b35e29d0fbd1b4972f9cc964e689d9a92e913105b08ac2cca469711?s=48&d=identicon&r=G) | David Young on [Enrolling macOS Golden Gate 27…](https://derflounder.wordpress.com/2026/09/15/enrolling-macos-golden-gate-27-0-0-virtual-machines-with-mdm-servers-does-not-work-correctly/#comment-72967) |
| ![Mike Boylan's avatar](https://1.gravatar.com/avatar/73bec650dbec7e510d8357ad11fd4bc44b12782f6ba2d3a9ea9d030ee0830bb6?s=48&d=identicon&r=G) | Mike Boylan on [Enrolling macOS Golden Gate 27…](https://derflounder.wordpress.com/2026/09/15/enrolling-macos-golden-gate-27-0-0-virtual-machines-with-mdm-servers-does-not-work-correctly/#comment-72966) |
| ![David Young's avatar](https://1.gravatar.com/avatar/de72034a6b35e29d0fbd1b4972f9cc964e689d9a92e913105b08ac2cca469711?s=48&d=identicon&r=G) | David Young on [Enrolling macOS Golden Gate 27…](https://derflounder.wordpress.com/2026/09/15/enrolling-macos-golden-gate-27-0-0-virtual-machines-with-mdm-servers-does-not-work-correctly/#comment-72965) |
| [![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=48&d=identicon&r=G)](http://isotopp.wordpress.com/) | [isotopp](http://isotopp.wordpress.com/) on [Intel apps and macOS Golden…](https://derflounder.wordpress.com/2026/09/15/intel-apps-and-macos-golden-gate/#comment-72946) |
| [![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=48&d=identicon&r=G)](http://isotopp.wordpre...