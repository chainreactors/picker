---
title: macOS 26.1.0 virtual machines do not generate valid system serial numbers
url: https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/
source: Der Flounder
date: 2025-11-04
fetch_date: 2025-11-05T03:09:24.499393
---

# macOS 26.1.0 virtual machines do not generate valid system serial numbers

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Virtualization](https://derflounder.wordpress.com/category/virtualization/) > macOS 26.1.0 virtual machines do not generate valid system serial numbers

## macOS 26.1.0 virtual machines do not generate valid system serial numbers

November 4, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

After updating to macOS Tahoe 26.1.0 yesterday, I then did what I normally do and began building new virtual machines to test with. I built a VM for macOS 26.1.0 and then noticed something odd. The virtual machine did not have an assigned system serial number. Instead, where you would expect to see the serial number displayed, there is a blank entry.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-04-at-10.07.png?w=276&h=453 "Screenshot 2025-11-04 at 10.07.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-04-at-10.07-1.png?w=599&h=523 "Screenshot 2025-11-04 at 10.07.png")

I built a macOS 26.0.1 VM and saw the serial number appear.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-04-at-11.47.png?w=273&h=451 "Screenshot 2025-11-04 at 11.47.png")

I then upgraded the VM from macOS 26.0.1 to macOS 26.1.0. Poof, no more serial number.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-04-at-11.47-1.png?w=276&h=453 "Screenshot 2025-11-04 at 11.47.png")

After talking with colleagues in the Mac Admins Slack, I was pointed to a **Known Issues** entry for **Virtualization** in the [macOS 26.1.0 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-26_1-release-notes#Virtualization):

***The serial number published for the virtual machine is 0, which prevents iCloud and related applications from functioning correctly. (163294564)***

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-04-at-12.53.png?w=600&h=204 "Screenshot 2025-11-04 at 12.53.png")

You can’t set a system serial number manually for macOS VMs running on Apple Silicon Macs, so it looks like this state of affairs is with us until Apple fixes it. Hopefully that is soon.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Virtualization](https://derflounder.wordpress.com/category/virtualization/)

Comments (2)
[Leave a comment](#respond)

1. ![staze's avatar](https://1.gravatar.com/avatar/dff8e942e5e58ae5de0868fc4fc2d6f437ac8113bb8e2956a5b990e06d52b422?s=32&d=identicon&r=G)

   staze

   November 4, 2025 at 6:39 pm

   [Reply](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?replytocom=72802#respond)

   Funny that’s the bug description. The one time I’ve had an iCloud account get disabled (I had to jump through hoops to get it re-enabled) is when I signed up for it on a VM. I would almost assume this was intentional…
2. ![staze's avatar](https://1.gravatar.com/avatar/dff8e942e5e58ae5de0868fc4fc2d6f437ac8113bb8e2956a5b990e06d52b422?s=32&d=identicon&r=G)

   staze

   November 4, 2025 at 6:39 pm

   [Reply](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/?replytocom=72803#respond)

   Funny that’s the bug description. The one time I’ve had an iCloud account get disabled (I had to jump through hoops to get it re-enabled) is when I signed up for it on a VM. I would almost assume this was intentional…

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/#respond)

Δ

[Identifying MDM-managed user accounts using System Information on macOS Tahoe](https://derflounder.wordpress.com/2025/10/18/identifying-mdm-managed-user-accounts-using-system-information-on-macos-tahoe/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

November 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | [4](https://derflounder.wordpress.com/2025/11/04/) | 5 | 6 | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | 26 | 27 | 28 | 29 | 30 |

[« Oct](https://derflounder.wordpress.com/2025/10/)

### Recent Comments

|  |  |
| --- | --- |
| ![staze's avatar](https://1.gravatar.com/avatar/dff8e942e5e58ae5de0868fc4fc2d6f437ac8113bb8e2956a5b990e06d52b422?s=48&d=identicon&r=G) | staze on [macOS 26.1.0 virtual machines…](https://derflounder.wordpress.com/2025/11/04/macos-26-1-0-virtual-machines-do-not-generate-valid-system-serial-numbers/#comment-72803) |
| ![staze's avatar](https://1.gravatar.com/avatar/dff8e942e5e58ae5de0868fc4fc2d6f437ac8113bb8e2956a5b990e06d...