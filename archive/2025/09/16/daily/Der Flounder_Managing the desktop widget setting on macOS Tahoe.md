---
title: Managing the desktop widget setting on macOS Tahoe
url: https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/
source: Der Flounder
date: 2025-09-16
fetch_date: 2025-10-02T20:11:22.037820
---

# Managing the desktop widget setting on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Managing the desktop widget setting on macOS Tahoe

## Managing the desktop widget setting on macOS Tahoe

September 15, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Every so often, something gets added to macOS and enabled by default where I wish it was off by default. In macOS Tahoe, that’s the appearance of desktop widgets automatically on login.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-15-at-3.26.png?w=595 "Screenshot 2025-09-15 at 3.26.png")

This behavior is managed in **System Settings**: **Desktop & Dock** and is listed as the **Show Widgets** setting. This has two selectable settings:

* **On Desktop**
* **In Stage Manager**

The default behavior is for both the **On Desktop** and **In Stage Manager** options to be enabled.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-15-at-3.28.59pm.png?w=595 "Screenshot 2025-09-15 at 3.28.59 PM.png")

To prevent desktop widgets from appearing on your desktop, disable the **On Desktop** option.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-14-at-12.42.52pm.png?w=595 "Screenshot 2025-09-14 at 12.42.52 PM.png")

Fortunately for my preferences, the desktop widgets behavior can also be controlled via the following setting:

* Domain: **com.apple.WindowManager**
* Key: **StandardHideWidgets**
* Value: Boolean

To disable desktop widgets and prevent them from appearing, run the following command as the logged-in user:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write com.apple.WindowManager StandardHideWidgets -bool true |

[view raw](https://gist.github.com/rtrouton/3a8cf6933b31e1cf5bb92edcecec1f3b/raw/bcae50888717f8abb920de0783af4c23c79cadf6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3a8cf6933b31e1cf5bb92edcecec1f3b#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To enable desktop widgets to appear again, run the following command as the logged-in user:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write com.apple.WindowManager StandardHideWidgets -bool false |

[view raw](https://gist.github.com/rtrouton/3930ac8b98f290467774e78cd3c88591/raw/1d65b031c7c3d71ae5885666aad41b107ac06794/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3930ac8b98f290467774e78cd3c88591#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In my case, I wanted to disable desktop widgets and prevent them from appearing so I’ve also written a profile which can enforce this. It’s available via the link below:

<https://github.com/rtrouton/profiles/blob/main/DisableDesktopWidgets>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/09/15/managing-the-desktop-widget-setting-on-macos-tahoe/#respond)

Δ

[Managing Safari bookmarks on macOS Tahoe using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/)
[FireWire support removed from macOS Tahoe](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/)

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
| 22 | 23 | 24 | 25 | [26](https://derflounder.wordpress.com/2025/09/26/) | [27](https://derflounder.wordpress.com/2025/09/27/) | 28 |
| 29 | 30 |  | | | | |

[« Aug](https://derflounder.wordpress.com/2025/08/)

### Recent Comments

|  |  |
| --- | --- |
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress...