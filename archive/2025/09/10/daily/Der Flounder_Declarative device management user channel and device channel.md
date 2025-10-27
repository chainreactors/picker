---
title: Declarative device management user channel and device channel
url: https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/
source: Der Flounder
date: 2025-09-10
fetch_date: 2025-10-02T19:53:50.212080
---

# Declarative device management user channel and device channel

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Declarative device management user channel and device channel

## Declarative device management user channel and device channel

September 9, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

[Mobile device management](https://support.apple.com/en-au/guide/deployment/depc0aadd3fe/web) (MDM) has the concept of what’s referred to as channels, which defines how management settings can be delivered:

* Device channel: Allows MDM settings to be delivered to devices and apply device settings to the entire device.
* User channel: Allows MDM settings to be delivered to user accounts on devices and apply user settings just to the relevant users.

When enrolling a device into an MDM server using device enrollment, [a couple of things happen as part of the MDM enrollment process](https://developer.apple.com/documentation/devicemanagement/managing-mdm-devices-and-users-in-macos):

* The device becomes a managed device.
* The local user account which installs the MDM enrollment profile becomes a managed user.

There’s additional details on what it means to be a managed user, but one of the most important is that in this context, being a managed user means that the local user account can be managed with [settings delivered via the user channel](https://support.apple.com/guide/deployment/intro-to-mdm-profiles-depc0aadd3fe/web). Other local accounts on the Mac are not able to access the user channel and cannot be managed by user level settings.

[Declarative device management](https://support.apple.com/guide/deployment/intro-to-declarative-device-management-depb1bab77f8/web) (DDM) has these same concepts of device channel and user channel and as far as I can tell, it works exactly the same as it does for MDM:

* Device channel: Allows DDM declarations to be delivered to devices and apply device settings to the entire device.
* User channel: Allows DDM declarations to be delivered to MDM-managed user accounts on devices and apply user settings just to the relevant users.

What this means is that a MDM-managed user account is able to be managed via settings delivered by the DDM user channel and other accounts which are not MDM-managed are not part of the DDM user channel and cannot be managed by DDM user level settings.

An example of DDM management which uses the user channel are the [Safari extension management options](https://developer.apple.com/documentation/devicemanagement/safariextensionsettings). If you check the documentation, as of September 9th, 2025, Safari extension management has the following [configuration availability listing](https://developer.apple.com/documentation/devicemanagement/safariextensionsettings#Configuration-availability):

* Allowed in supervised enrollment: **iOS, macOS, Shared iPad, visionOS**
* Allowed in device enrollment: **NA**
* Allowed in user enrollment: **NA**
* Allowed in local enrollment: **NA**
* Allowed in system scope: **iOS, visionOS**
* Allowed in user scope: **macOS, Shared iPad**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/screenshot-2025-09-09-at-8.44.png?w=600&h=356 "Screenshot 2025-09-09 at 8.44.png")

This means that DDM Safari extension management is using the device channel on the following Apple platforms:

* iOS
* visionOS

DDM Safari extension management is using the user channel on the following Apple platforms:

* macOS
* Shared iPad

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/?share=pocket)

Like Loading...

### *Related*

Categories: [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/09/09/declarative-device-management-user-channel-and-device-channel/#respond)

Δ

[Suppressing the FileVault screen with a configuration profile on macOS Tahoe](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/)
[Managing Safari extensions on macOS Sequoia using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/09/06/managing-safari-extensions-on-macos-sequoia-using-blueprints-in-jamf-pro/)

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
| [15](https://derflounder.wordpress.com/2025...