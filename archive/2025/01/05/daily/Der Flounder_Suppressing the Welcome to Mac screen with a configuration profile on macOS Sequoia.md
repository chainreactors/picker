---
title: Suppressing the Welcome to Mac screen with a configuration profile on macOS Sequoia
url: https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/
source: Der Flounder
date: 2025-01-05
fetch_date: 2025-10-06T20:04:38.467528
---

# Suppressing the Welcome to Mac screen with a configuration profile on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Suppressing the Welcome to Mac screen with a configuration profile on macOS Sequoia

## Suppressing the Welcome to Mac screen with a configuration profile on macOS Sequoia

January 4, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Over the years, Apple has introduced a number of screens which appear the first time you log into a Mac and sometimes also after an OS update. Apple added a new **Welcome to Mac** screen as part of macOS Sequoia. This screen appears before you are given access to the Desktop.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/01/setupassistantwelcometomacscreen.png?w=599&h=374 "SetupAssistantWelcomeToMacScreen.png")

I have not found a way to suppress this screen using a [defaults](https://ss64.com/mac/defaults.html) command, but it is possible to suppress the **Welcome to Mac** screen on macOS Sequoia using a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.SetupAssistant.managed**
* Key: **SkipSetupItems**
* Value: **Welcome**

The profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/blob/main/SkipWelcomeToMacSetup>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (3)
[Leave a comment](#respond)

1. ![cade's avatar](https://0.gravatar.com/avatar/f40e0a7f0a66081b5bed71339cea05f10b34e717bfe05efd4d56b56de163126c?s=32&d=identicon&r=G)

   cade

   January 4, 2025 at 7:04 pm

   [Reply](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?replytocom=72641#respond)

   yes thanks. will save for whenever I eventually update to sequoia.

   I HATE the splash screens apple forces on users on startup for last several iterations.

   don’t recall how I did it but in sonoma now my splash screen startup is under ~MYHOME> macos-big-sur-wallpaper-8.jpg

   probably used the terminal to point it there but can’t remember how/where I found it. I seem to recall something about a cache file/folder…

   thanks for this.
2. ![cade's avatar](https://0.gravatar.com/avatar/f40e0a7f0a66081b5bed71339cea05f10b34e717bfe05efd4d56b56de163126c?s=32&d=identicon&r=G)

   cade

   January 4, 2025 at 7:04 pm

   [Reply](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?replytocom=72642#respond)

   yes thanks. will save for whenever I eventually update to sequoia.

   I HATE the splash screens apple forces on users on startup for last several iterations.

   don’t recall how I did it but in sonoma now my splash screen startup is under ~MYHOME> macos-big-sur-wallpaper-8.jpg

   probably used the terminal to point it there but can’t remember how/where I found it. I seem to recall something about a cache file/folder…

   thanks for this.
3. ![MikeHunt's avatar](https://1.gravatar.com/avatar/d0f7b240d588429b53d8dcc6a256b2d74f5d8a2dc610a17a023f9ea7e36baec2?s=32&d=identicon&r=G)

   MikeHunt

   April 9, 2025 at 5:37 pm

   [Reply](https://derflounder.wordpress.com/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/?replytocom=72708#respond)

   This does not appear to work since macOS 15.4

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/01/04/suppressing-the-welcome-to-mac-screen-with-a-configuration-profile-on-macos-sequoia/#respond)

Δ

[Disabling Apple Mail website link previews compose option on macOS Sequoia](https://derflounder.wordpress.com/2025/01/05/disabling-apple-mail-website-link-previews-compose-option-on-macos-sequoia/)
[Detecting successful MDM command execution on macOS Sequoia](https://derflounder.wordpress.com/2024/12/21/detecting-successful-mdm-command-execution-on-macos-sequoia/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

January 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | 1 | 2 | 3 | [4](https://derflounder.wordpress.com/2025/01/04/) | [5](https://derflounder.wordpress.com/2025/01/05/) |
| 6 | 7 | 8 | 9 | 10 | 11 | [12](https://derflounder.wordpress.com/2025/01/12/) |
| 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 21 | 22 | 23 | 24 | 25 | 26 |
| 27 | 28 | [29](https://derflounder.wordpress.com/2025/01/29/) | 30 | 31 |  | |

[« Dec](https://derflounder.wordpress.com/2024/12/)

[Feb »](https://derflounder.wo...