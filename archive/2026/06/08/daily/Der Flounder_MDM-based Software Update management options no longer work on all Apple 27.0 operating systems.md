---
title: MDM-based Software Update management options no longer work on all Apple 27.0 operating systems
url: https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/
source: Der Flounder
date: 2026-06-08
fetch_date: 2026-06-09T06:02:12.261517
---

# MDM-based Software Update management options no longer work on all Apple 27.0 operating systems

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > MDM-based Software Update management options no longer work on all Apple 27.0 operating systems

## MDM-based Software Update management options no longer work on all Apple 27.0 operating systems

June 8, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of the release of macOS Tahoe, Apple [deprecated the MDM-based Software Update management options and said that they would be removed the following year](https://support.apple.com/124963).

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-08-at-1.33.png?w=595 "Screenshot 2026-06-08 at 1.33.png")

Apple has carried through on this and announced publicly that legacy software update management no longer functions in all Apple 27.0 operating systems. This announcement was posted as part of the following documentation:

* **WWDC26 device management updates**: <https://support.apple.com/guide/deployment/device-management-updates-depd638aa061/1/web/1.0> (see the [Software update command removal](https://support.apple.com/en-ca/guide/deployment/device-management-updates-depd638aa061/1/web/1.0#depd478f87b8) section.)

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-08-at-3.30.png?w=595 "Screenshot 2026-06-08 at 3.30.png")

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | Software update command removal |
|  |  |
|  | Announced last year, legacy software update management no longer functions in all 27.0 operating systems. This includes: |
|  |  |
|  | • Software update commands |
|  | • Software update queries |
|  | • Recommended cadence settings |
|  | • Software update restrictions, like deferrals and Background Security Improvements |
|  |  |
|  | IT teams should use declarative software update management to configure and enforce updates on devices with increased user transparency and more control. |

[view raw](https://gist.github.com/rtrouton/9ea2c55dab8d2f3d34e6015cd7f8bdb4/raw/11c63550346dac213bee6f8db9614e284a32d123/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9ea2c55dab8d2f3d34e6015cd7f8bdb4#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

What this means is that the only Software Update management settings which work on Apple 27.0 operating systems are those which are using declarative device management:

<https://developer.apple.com/documentation/devicemanagement/softwareupdatesettings>

For those who want to use [Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) to manage Software Update settings using declarative device management, I have a post on how to do this available via the link below:

<https://derflounder.wordpress.com/2025/06/24/deploying-software-update-management-using-blueprints-in-jamf-pro/>

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?share=tumblr)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/)

Comments (2)
[Leave a comment](#respond)

1. ![John's avatar](https://0.gravatar.com/avatar/3313d80a780d422e95a9801cc015a802e0e0b4c8737ff364b844b15fa3501b8c?s=32&d=identicon&r=G)

   John

   June 8, 2026 at 7:51 pm

   [Reply](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?replytocom=72896#respond)

   Did they ever work?
2. ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc5712a2f1a9d5eb78c66927fd488b3ced2e1cd4372?s=32&d=identicon&r=G)

   peteostro

   June 8, 2026 at 9:13 pm

   [Reply](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/?replytocom=72897#respond)

   does this mean defer major macOS update profile will not work on macOS 27?

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/#respond)

Δ

[Showing or hiding the Self Service+ menubar icon](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator"...