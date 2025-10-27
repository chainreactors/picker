---
title: Clearing MDM lock on Apple Silicon Macs when passcode has been lost
url: https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/
source: Der Flounder
date: 2024-08-31
fetch_date: 2025-10-06T17:59:17.693724
---

# Clearing MDM lock on Apple Silicon Macs when passcode has been lost

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Clearing MDM lock on Apple Silicon Macs when passcode has been lost

## Clearing MDM lock on Apple Silicon Macs when passcode has been lost

August 30, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the functions that Apple’s mobile device management (MDM) has had for years is the [ability to send a remote lock command](https://derflounder.wordpress.com/2012/04/06/using-casper-8-51-to-remotely-lock-or-wipe-10-7-macs/). In this case, an MDM command is sent to a device and a passcode is required in order to clear the lock.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/08/screenshot-2024-08-30-at-8.44.png?w=599&h=374 "Screenshot 2024-08-30 at 8.44.png")

However, sometimes this passcode can get mislaid or forgotten due to insufficient record keeping. In this case, how to clear the lock when you don’t have the passcode? On Apple Silicon Macs, it’s possible to clear the lock but it will require all data on the Mac to be destroyed and the operating system to be reloaded from scratch.

For more details, please see below the jump.

The solution is to put the Apple Silicon Mac into DFU mode and use Apple Configurator running on another Mac to restore the Mac using [an IPSW file for the desired operating system](https://mrmacintosh.com/apple-silicon-m1-full-macos-restore-ipsw-firmware-files-database/). Apple has a KBase article describing how to perform this restoration process available via the link below (follow the **Restore** procedures):

* **How to revive or restore Mac firmware**: <https://support.apple.com/108900>

Once the Mac has been restored, the lock should be cleared and a factory-fresh copy of macOS should be installed.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/08/screenshot-2024-08-30-at-8.53.png?w=599&h=374 "Screenshot 2024-08-30 at 8.53.png")

In the event that this process does not work, the other option available is a logic board hardware repair where the Mac’s existing logic board is exchanged for a new replacement one.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2024/08/30/clearing-mdm-lock-on-apple-silicon-macs-when-passcode-has-been-lost/#respond)

Δ

[Blocking system extension disablement via System Settings on macOS Sequoia](https://derflounder.wordpress.com/2024/09/16/blocking-system-extension-disablement-via-system-settings-on-macos-sequoia/)
[Setting custom variables in AutoPkg using the VariablePlaceholder processor](https://derflounder.wordpress.com/2024/08/16/setting-custom-variables-in-autopkg-using-the-variableplaceholder-processor/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

August 2024

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | [1](https://derflounder.wordpress.com/2024/08/01/) | 2 | 3 | 4 |
| 5 | 6 | [7](https://derflounder.wordpress.com/2024/08/07/) | [8](https://derflounder.wordpress.com/2024/08/08/) | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | [16](https://derflounder.wordpress.com/2024/08/16/) | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | [30](https://derflounder.wordpress.com/2024/08/30/) | 31 |  |

[« Jul](https://derflounder.wordpress.com/2024/07/)

[Sep »](https://derflounder.wordpress.com/2024/09/)

### Recent Comments

|  |  |
| --- | --- |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/#comment-72798) |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/#comment-72797) |
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/#comment-72795) |
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos...