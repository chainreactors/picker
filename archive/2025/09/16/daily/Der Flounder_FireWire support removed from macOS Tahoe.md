---
title: FireWire support removed from macOS Tahoe
url: https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/
source: Der Flounder
date: 2025-09-16
fetch_date: 2025-10-02T20:11:22.453338
---

# FireWire support removed from macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > FireWire support removed from macOS Tahoe

## FireWire support removed from macOS Tahoe

September 15, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of the release of macOS Tahoe 26.0, [Apple has removed built-in support for FireWire devices from macOS](https://512pixels.net/2025/07/tahoe-no-firewire/). This removal of support can be verified by looking in System Profiler.

For more details, please see below the jump.

On macOS Sequoia 15.7.0, System Profiler shows an entry for FireWire.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-08-30-at-12.57.24pm.png?w=595 "Screenshot 2025-08-30 at 12.57.24 PM.png")

On macOS Tahoe 26.0, System Profiler no longer shows an entry for FireWire.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-08-30-at-1.01.51pm.png?w=595 "Screenshot 2025-08-30 at 1.01.51 PM.png")

Running the following command on both macOS Sequoia and macOS Tahoe also shows that **SPFireWireDataType** has been removed from macOS, which means that [System Profiler is not longer gathering data from that area](https://www.robertopasini.com/index.php?id=548):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/system\_profiler -listDataTypes |

[view raw](https://gist.github.com/rtrouton/6cb93b1f52f236157324384cfc5ea61d/raw/fcd428887ad2d2aae2fcda84af162652b46cc91a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/6cb93b1f52f236157324384cfc5ea61d#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-08-30-at-1.12.png?w=595 "Screenshot 2025-08-30 at 1.12.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/09/15/firewire-support-removed-from-macos-tahoe/#respond)

Δ

[Managing the desktop widget setting on macOS Tahoe](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/)
[Suppressing the FileVault screen with a configuration profile on macOS Tahoe](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

September 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | 3 | 4 | 5 | [6](https://derflounder.wordpress.com/2025/09/06/) | 7 |
| 8 | [9](https://derflounder.wordpress.com/2025/09/09/) | 10 | 11 | 12 | 13 | 14 |
| [15](https://derflounder.wordpress.com/2025/09/15/) | [16](https://derflounder.wordpress.com/2025/09/16/) | [17](https://derflounder.wordpress.com/2025/09/17/) | 18 | 19 | 20 | 21 |
| 22 | 23 | 24 | 25 | 26 | 27 | 28 |
| 29 | 30 |  | | | | |

[« Aug](https://derflounder.wordpress.com/2025/08/)

### Recent Comments

|  |  |
| --- | --- |
| ![Graham R.'s avatar](https://1.gravatar.com/avatar/41260c1adfd590e8a15fe12c5a2ac9ed802a2b44200fd07daa108b5e78803fc5?s=48&d=identicon&r=G) | Graham R. on [Deploying software update decl…](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/#comment-72790) |
| ![adstretch's avatar](https://2.gravatar.com/avatar/2e81e85b61df3e7a1d24271ea537a306c16f4635672bd7f5474a987a2f89b1d3?s=48&d=identicon&r=G) | adstretch on [Suppressing the FileVault scre…](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/#comment-72789) |
| ![Akeem's avatar](https://1.gravatar.com/avatar/15f667c0b2f3781fbb0b388b5d9402a4a23d4c9b6fdce328ad344ce82e38dc1c?s=48&d=identicon&r=G) | Akeem on [Using the Jamf Pro API to retr…](https://derflounder.wordpress.com/2023/01/25/using-the-jamf-pro-api-to-retrieve-filevault-personal-recovery-keys/#comment-72788) |
| ![BMan's avatar](https://1.gravatar.com/avatar/1b7addf1e646ac216a84a008e3c60a4d1d9f932957668c3fb3689dadf1135b21?s=48&d=identicon&r=G) | BMan on [Suppressing the FileVault scre…](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/#comment-72786) |
| ![StandAdminUser's avatar](https://0.gravatar.com/avatar/fa6aabf4d722bf3d5bfcb8118709e52a5b99ea1b02264ff158357c1a8a4b1085?s=48&d=identicon&r=G) | StandAdminUser on [Deploying software update decl…](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/#comment-72785) |

### Categories

Categories
Select Category
Absolute Manage  (1)
Active Di...