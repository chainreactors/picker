---
title: Suppressing the Analytics screen with a configuration profile on macOS Sequoia
url: https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/
source: Der Flounder
date: 2025-08-13
fetch_date: 2025-10-07T00:13:13.893133
---

# Suppressing the Analytics screen with a configuration profile on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Suppressing the Analytics screen with a configuration profile on macOS Sequoia

## Suppressing the Analytics screen with a configuration profile on macOS Sequoia

August 12, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Over the years, Apple has introduced a number of screens which appear the first time you log into a Mac. Among those which appear as of macOS Sequoia 15.6.0 is the **Analytics** screen, which asks if you want to opt-in to sending app crash and usage data to developers.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/08/skipappanalyticssetup.png?w=595 "SkipAppAnalyticsSetup.png")

I have not found a way to suppress this screen using a [defaults](https://ss64.com/mac/defaults.html) command, but it is possible to suppress the **Analytics** screen on macOS Sequoia using a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.SetupAssistant.managed**
* Key: **SkipSetupItems**
* Value: **Diagnostics**

The profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/blob/main/SkipAppAnalyticsSetup>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (2)
[Leave a comment](#respond)

1. ![nr577s2bxg's avatar](https://0.gravatar.com/avatar/0b3b067011ffc61176152e52aff45207abb50aa943289c7ad56f06f0fe714fc7?s=32&d=identicon&r=G)

   nr577s2bxg

   August 12, 2025 at 3:42 pm

   [Reply](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?replytocom=72778#respond)

   This is great! Testing now. Thanks, Rich 🙂
2. ![BMan's avatar](https://1.gravatar.com/avatar/1b7addf1e646ac216a84a008e3c60a4d1d9f932957668c3fb3689dadf1135b21?s=32&d=identicon&r=G)

   BMan

   August 27, 2025 at 2:39 pm

   [Reply](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/?replytocom=72783#respond)

   Also suppressing FileVault auto activation after updating to Tahoe may be useful. Thanks, Rich!

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/#respond)

Δ

[Reading DDM logging on macOS Sequoia](https://derflounder.wordpress.com/2025/08/19/reading-ddm-logging-on-macos-sequoia/)
[Session videos now available from Penn State MacAdmins Conference 2025](https://derflounder.wordpress.com/2025/08/11/session-videos-now-available-from-penn-state-macadmins-conference-2025/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

August 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | 1 | 2 | [3](https://derflounder.wordpress.com/2025/08/03/) |
| 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| [11](https://derflounder.wordpress.com/2025/08/11/) | [12](https://derflounder.wordpress.com/2025/08/12/) | 13 | 14 | 15 | 16 | 17 |
| 18 | [19](https://derflounder.wordpress.com/2025/08/19/) | 20 | 21 | 22 | 23 | [24](https://derflounder.wordpress.com/2025/08/24/) |
| 25 | 26 | 27 | 28 | 29 | 30 | 31 |

[« Jul](https://derflounder.wordpress.com/2025/07/)

[Sep »](https://derflounder.wordpress.com/2025/09/)

### Recent Comments

|  |  |
| --- | --- |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/#comment-72798) |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/#comment-72797) |
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/#comment-72795) |
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-...