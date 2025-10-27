---
title: Setting reduced transparency on macOS Sequoia
url: https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/
source: Der Flounder
date: 2025-06-19
fetch_date: 2025-10-06T22:49:26.377339
---

# Setting reduced transparency on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Setting reduced transparency on macOS Sequoia

## Setting reduced transparency on macOS Sequoia

June 18, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the user interface features in macOS is what Apple refers to as [Vibrancy](https://arstechnica.com/gadgets/2014/10/os-x-10-10/), where the color displayed for Finder windows, menus, the Dock, the menubar and other interfaces subtly change to reflect the colors behind them. This produces a translucent visual effect for those interfaces.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-17-at-9.26.png?w=402&h=54 "Screenshot 2025-06-17 at 9.26.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-17-at-9.27.png?w=597&h=42 "Screenshot 2025-06-17 at 9.27.png")

This feature, first introduced in OS X 10.10 Yosemite, can come at a cost in terms of processor and GPU resources because this visual effect is being recalculated and redrawn as needed. For those who want to reclaim those resources, it’s possible to turn Vibrancy off if needed. On macOS Sequoia, this is managed via the following setting in System Settings:

**System Settings: Accessibility: Display: Reduce Transparency**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-18-at-8.35.29am.png?w=599&h=524 "Screenshot 2025-06-18 at 8.35.29 AM.png")

With the **Reduce transparency** setting enabled, Vibrancy is turned off and the various interface components should change from their Vibrancy-managed translucent appearance to a non-translucent gray appearance.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-18-at-8.36.03am.png?w=599&h=524 "Screenshot 2025-06-18 at 8.36.03 AM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-17-at-9.29.png?w=432&h=43 "Screenshot 2025-06-17 at 9.29.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/06/screenshot-2025-06-17-at-9.29-1.png?w=586&h=40 "Screenshot 2025-06-17 at 9.29.png")

As of macOS Sequoia, it does not appear to be possible to manage the **Reduce transparency** setting using a [defaults](https://ss64.com/mac/defaults.html) command but it is possible to manage it via a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.universalaccess**
* Key: **reduceTransparency**
* Value: Boolean

Setting a boolean value of **true** will disable Vibrancy on macOS Sequoia. I’ve built a configuration profile with the boolean value of **true** set, where the profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/tree/main/ReduceTransparency>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (1)
[Leave a comment](#respond)

1. ![Isaac Halvorson's avatar](https://2.gravatar.com/avatar/b63615958167fa9aaa4c0ffffe1752ded33d16cfc18c783e55d5a307a2f57659?s=32&d=identicon&r=G)

   [Isaac Halvorson](http://hisaac.wordpress.com)

   June 18, 2025 at 1:32 pm

   [Reply](https://derflounder.wordpress.com/2025/06/18/setting-reduced-transparency-on-macos-sequoia/?replytocom=72753#respond)

   Hello! Small correction here. It is in fact possible to change this setting with a defaults command.

   `defaults write com.apple.universalaccess reduceTransparency -bool true`

   This changes the setting, but it only shows as changed after logging out/in, or restarting the computer.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/06/18/setting-reduced-transparency-on-macos-sequoia/#respond)

Δ

[Extracting fonts from configuration profiles on macOS Sequoia](https://derflounder.wordpress.com/2025/06/20/extracting-fonts-from-configuration-profiles-on-macos-sequoia/)
[Deploying disk management using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/06/11/deploying-disk-management-using-blueprints-in-jamf-pro/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

June 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | 1 |
| [2](https://derflounder.wordpress.com/2025/06/02/) | 3 | 4 | 5 | 6 | 7 | 8 |
| 9 | [10](https://derflounder.wordpress.com/2025/06/10/) | [11](https://derflounder.wordpress.com/2025/06/11/) | 12 | 13 | 14 | 15 |
| 16 | 17 | [18](https://derflounder.wordpress.com/2025/06/18/) | 19 | [20](https://derflounder.wordpress.com/2025/06/20/) | 21 | 22 |
| 23 | [24](https://derflounder.wordpress.com/2025/06/24/) | [25](https://derflounder.wordpress.com/2025/06/25/) | 26 | 27 | [28](https://derflounder.wordpress.com/2025/06/28/) | 29 |
| 30 |  | | | | | |

[« May](https://derflounder.wordpress.com/2025/05/)

[...