---
title: Suppressing the Software Update Complete screen with a configuration profile on macOS Tahoe
url: https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/
source: Der Flounder
date: 2025-09-27
fetch_date: 2025-10-02T20:45:51.343140
---

# Suppressing the Software Update Complete screen with a configuration profile on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Suppressing the Software Update Complete screen with a configuration profile on macOS Tahoe

## Suppressing the Software Update Complete screen with a configuration profile on macOS Tahoe

September 26, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Over the years, Apple has introduced a number of screens which appear the first time you log into a Mac. Among those which appear following an upgrade to macOS Tahoe 26.0 is the **Software Update Complete** screen, which notifies you that the Mac has been upgraded to macOS Tahoe.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/skipsoftwareupdatecompletesetup.png?w=595 "SkipSoftwareUpdateCompleteSetup.png")

I have not found a way to suppress this screen using a [defaults](https://ss64.com/mac/defaults.html) command, but it is possible to suppress the **Software Update Complete** screen on macOS Tahoe using a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.SetupAssistant.managed**
* Key: **SkipSetupItems**
* Value: **UpdateCompleted**

The profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/blob/main/SkipSoftwareUpdateCompleteSetup>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/#respond)

Δ

[Managing SkipSetupItems settings in management profiles on macOS](https://derflounder.wordpress.com/2025/09/27/managing-skipsetupitems-settings-in-management-profiles-on-macos/)
[Managing Safari settings on macOS Tahoe using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/09/17/managing-safari-settings-on-macos-tahoe-using-blueprints-in-jamf-pro/)

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
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/#comment-72795) |
| ![aghali's avatar](https://2.gravatar.com/avatar/847cd0567de1ed9cb9843cb551446c2f304e65e8ccc3871b6bc90fe380cad198?s=48&d=identicon&r=G) | aghali on [Managing Safari bookmarks on m…](https://derflounder.wordpress.com/2025/09/16/managing-safari-bookmarks-on-macos-tahoe-using-blueprints-in-jamf-pro/#comment-72794) |
| ![Chris Johnson's avatar](https://0.gravatar.com/avatar/9c0a5bffb39d34cf5fe6e4b131701c411e499667be95bf4007dd7cb12ae2327f?s=48&d=identicon&r=G) | Chris Johnson on [Suppressing the FileVault scre…](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/#comment-72793) |
| ![Graham R.'s avatar](https://1.gravatar.com/avatar/41260c1adfd590e8a15fe12c5a2ac9ed802a2b44200fd07daa108b5e78803fc5?s=48&d=identicon&r=G) | Graham R. on [Deploying software update decl…](https://derflounder.wordpress.com/2025/08/03/deploying-software-update-declarations-using-blueprints-in-jamf-pro/#comment-72790) |
| ![adstretch's avatar](https://2.gravatar.com/avatar/2e81e85b61df3e7a1d24271ea537a306c16f4635672bd7f5474a987a2f89b1d3?s=48&d=identicon&r=G) | adstretch on [Suppressing the FileVault scre…](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/#comment-72789) |

### Categories

Categories
Select Category
Absolute Manage  (1)
Active Direc...