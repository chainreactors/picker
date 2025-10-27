---
title: Displaying DDM-deployed settings on macOS Sequoia
url: https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/
source: Der Flounder
date: 2025-05-30
fetch_date: 2025-10-06T22:23:41.403580
---

# Displaying DDM-deployed settings on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Displaying DDM-deployed settings on macOS Sequoia

## Displaying DDM-deployed settings on macOS Sequoia

May 29, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Sometimes as part of troubleshooting mobile device management (MDM) problems, you need to look at the list of installed profiles to make sure the profile you need is actually installed. On macOS Sequoia, the list of installed profiles appears in **System Settings**: **General**: **Device Management**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-29-at-11.44.03am.png?w=599&h=524 "Screenshot 2025-05-29 at 11.44.03 AM.png")

But where do you go to look for declarative device management (DDM) settings that have been deployed to your Mac? Those can also be looked up via **System Settings**: **General**: **Device Management**, by locating the MDM enrollment profile in the list of profiles and double-clicking on it.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-29-at-11.44.18am.png?w=599&h=524 "Screenshot 2025-05-29 at 11.44.18 AM.png")

When you scroll to the bottom of the enrollment profile’s window, you should see a **Device Declarations** section. That’s where you’ll be able to see what DDM-deployed settings have been applied to your Mac. For example, if you’re [deploying configurations for the sudo command line tool](https://derflounder.wordpress.com/2025/05/27/deploying-sudo-configurations-using-blueprints-in-jamf-pro/), you should see a **Device Declarations** section, with a listing for **Configuration Files: com.apple.sudo**.

![MDM Enrollment Profile Device Declarations.](https://derflounder.wordpress.com/wp-content/uploads/2025/05/mdm_enrollment_profile_device_declarations.png?w=599&h=524 "MDM_Enrollment_Profile_Device_Declarations.png")

If you click on the **Configuration Files: com.apple.sudo** listing, it should provide the path to the tamper-resistant directory where it stored the DDM-deployed configuration file for the **sudo** command line tool. This should be the following location:

**/private/var/db/ManagedConfigurationFiles/com.apple.sudo**

![MDM Enrollment Profile Device Declarations Sudo Listing.png.](https://derflounder.wordpress.com/wp-content/uploads/2025/05/mdm_enrollment_profile_device_declarations_sudo_listing.png.png?w=599&h=524 "MDM_Enrollment_Profile_Device_Declarations_Sudo_Listing.png.png")

If you’re deploying a software update plan via DDM, you should see a listing for that software update plan in the **Device Declarations** section.

![MacOS 15 5 DDM Software Update Declaration.](https://derflounder.wordpress.com/wp-content/uploads/2025/05/macos_15_5_ddm_software_update_declaration.png?w=599&h=524 "macOS_15_5_DDM_Software_Update_Declaration.png")

If you click on that listing, you should see the details of the plan.

![MacOS 15 5 DDM Software Update Declaration Details.](https://derflounder.wordpress.com/wp-content/uploads/2025/05/macos_15_5_ddm_software_update_declaration_details.png?w=599&h=524 "macOS_15_5_DDM_Software_Update_Declaration_Details.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/#respond)

Δ

[Session videos available from MacAD.UK 2025](https://derflounder.wordpress.com/2025/05/30/session-videos-available-from-macad-uk-2025/)
[Deploying sudo configurations using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/05/27/deploying-sudo-configurations-using-blueprints-in-jamf-pro/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

May 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | 1 | 2 | 3 | 4 |
| [5](https://derflounder.wordpress.com/2025/05/05/) | 6 | 7 | [8](https://derflounder.wordpress.com/2025/05/08/) | 9 | 10 | 11 |
| 12 | 13 | [14](https://derflounder.wordpress.com/2025/05/14/) | 15 | [16](https://derflounder.wordpress.com/2025/05/16/) | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | [27](https://derflounder.wordpress.com/2025/05/27/) | 28 | [29](https://derflounder.wordpress.com/2025/05/29/) | [30](https://derflounder.wordpress.com/2025/05/30/) | 31 |  |

[« Apr](https://derflounder.wordpress.com/2025/04/)

[Jun »](https://derflounder.wordpress.com/2025/06/)

### Recent Comments

|  |  |
| --- | --- |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replac...