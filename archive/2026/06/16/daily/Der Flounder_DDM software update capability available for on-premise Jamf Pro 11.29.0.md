---
title: DDM software update capability available for on-premise Jamf Pro 11.29.0
url: https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/
source: Der Flounder
date: 2026-06-16
fetch_date: 2026-06-17T07:02:18.855543
---

# DDM software update capability available for on-premise Jamf Pro 11.29.0

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > DDM software update capability available for on-premise Jamf Pro 11.29.0

## DDM software update capability available for on-premise Jamf Pro 11.29.0

June 16, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of the release of Jamf Pro 11.29.0, the ability to run software updates using DDM is available for folks using on-premise installations of Jamf Pro. Information about this is available via the link below:

* **Support for Managed Software Updates via Declarative Device Management for Self-Hosted Instances**: <https://learn.jamf.com/r/en-US/jamf-pro-release-notes-current/Support_for_Managed_Software_Updates_via_Declarative_Device_Management_for_On-Premise_Instances>

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-16-at-12.10.png?w=600&h=225 "Screenshot 2026-06-16 at 12.10.png")

This change is in response to Apple’s announcement last year that [MDM-based Software Update management options were deprecated on macOS Tahoe](https://support.apple.com/124963). Apple’s recent followup announcement that [MDM-based Software Update management options no longer work on all Apple 27.0 operating systems](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/) underscores the need for DDM-based software update options to be available.

DDM software updates in 11.29.0 are part of the [Software Updates section of Jamf Pro](https://derflounder.wordpress.com/2025/06/02/using-jamf-pros-managed-software-updates-for-macos/). For on-premise Jamf Pro users, it is the **Download and schedule to install** option.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-16-at-12.06.png?w=599&h=357 "Screenshot 2026-06-16 at 12.06.png")

All other software update options listed in the **Software Updates** section are using the MDM commands which no longer work on any of Apple’s 27.0 operating systems.

For more information about how to use the **Download and schedule to install** option, please see the following link:

* **Updating macOS Using Managed Software Updates**: <https://learn.jamf.com/r/en-US/jamf-pro-documentation-current/Updating_macOS_Using_Managed_Software_Updates>

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?share=tumblr)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (2)
[Leave a comment](#respond)

1. ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc5712a2f1a9d5eb78c66927fd488b3ced2e1cd4372?s=32&d=identicon&r=G)

   peteostro

   June 16, 2026 at 8:45 pm

   [Reply](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?replytocom=72902#respond)

   You do not know how happy this makes me! Thank you Jamf!
2. ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc5712a2f1a9d5eb78c66927fd488b3ced2e1cd4372?s=32&d=identicon&r=G)

   peteostro

   June 16, 2026 at 9:09 pm

   [Reply](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/?replytocom=72903#respond)

   Wait, t only works on **Download and schedule to install** option? arg.

   Does the defer major OS software updates for 90 days still work?

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/#respond)

Δ

[MDM-based Software Update management options no longer work on all Apple 27.0 operating systems](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

June 2026

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| [1](https://derflounder.wordpress.com/2026/06/01/) | 2 | [3](https://derflounder.wordpress.com/2026/06/03/) | 4 | 5 | 6 | 7 |
| [8](https://derflounder.wordpress.com/2026/06/08/) | 9 | 10 | 11 | 12 | 13 | 14 |
| 15 | [16](https://derflounder.wordpress.com/2026/06/16/) | 17 | 18 | 19 | 20 | 21 |
| 22 | 23 | 24 | 25 | 26 | 27 | 28 |
| 29 | 30 |  | | | | |

[« May](https://derflounder.wordpress.com/2026/05/)

### Recent Comments

|  |  |
| --- | --- |
| ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc5712a2f1a9d5eb78c66927fd488b3ced2e1cd4372?s=48&d=identicon&r=G) | peteostro on [DDM software update capability…](https://derflounder.wordpress.com/2026/06/16/ddm-software-update-capability-available-for-on-premise-jamf-pro-11-29-0/#comment-72903) |
| ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc...