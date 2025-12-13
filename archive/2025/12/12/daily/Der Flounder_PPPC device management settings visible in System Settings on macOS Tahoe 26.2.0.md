---
title: PPPC device management settings visible in System Settings on macOS Tahoe 26.2.0
url: https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/
source: Der Flounder
date: 2025-12-12
fetch_date: 2025-12-13T03:14:21.078930
---

# PPPC device management settings visible in System Settings on macOS Tahoe 26.2.0

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > PPPC device management settings visible in System Settings on macOS Tahoe 26.2.0

## PPPC device management settings visible in System Settings on macOS Tahoe 26.2.0

December 12, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of the [What’s new for enterprise in macOS Tahoe 26](https://support.apple.com/124963) release notes for macOS Tahoe 26.2.0, there’s this note:

***App privacy permissions configured by device management are now shown in System Settings > Privacy & Security.***

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-1.07.png?w=595 "Screenshot 2025-12-12 at 1.07.png")

What this indicates is that a long-standing feature request by Mac admins has been fulfilled by Apple. For more details, please see below the jump.

As part of macOS 10.14 Mojave, [Apple introduced a number of privacy controls for user data](https://learn.jamf.com/en-US/bundle/technical-articles/page/Preparing_Your_Organization_for_User_Data_Protections_on_macOS_10-14.html). At the same time, Apple also introduced device management options to allow [authorized applications to access data protected by those privacy controls](https://support.apple.com/guide/deployment/privacy-preferences-policy-control-payload-dep38df53c2a/web). These permissions are referred to collectively as Privacy Preferences Policy Control (PPPC) and are deployed via management profiles from an MDM server. However, up until macOS Tahoe 26.2, there was no way to see in the **Privacy & Security** section of System Settings which applications had which permissions granted via PPPC management profiles.

As an example, by default, Macs managed by Jamf Pro will get a management profile which allows the Jamf agent permission to access data stored in the user home folder via the PPPC permission known as [full disk access](https://support.jamf.com/en/articles/11004245-grant-full-disk-access-for-application-or-process-name). Here’s how this looks on macOS Tahoe 26.1.0:

Privacy Preferences Policy Control profile installed which enables full disk access to the Jamf agent.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-2.11.01pm.png?w=595 "Screenshot 2025-12-12 at 2.11.01 PM.png")

No mention of the full disk access permissions granted to the Jamf agent in the **Privacy & Security** section of System Settings.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-2.57.19pm.png?w=595 "Screenshot 2025-12-12 at 2.57.19 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-3.55.17pm.png?w=595 "Screenshot 2025-12-12 at 3.55.17 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-3.56.08pm.png?w=595 "Screenshot 2025-12-12 at 3.56.08 PM.png")

How this looks on macOS Tahoe 26.2.0:

Privacy Preferences Policy Control profile installed which enables full disk access for the Jamf agent.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-2.11.01pm.png?w=595 "Screenshot 2025-12-12 at 2.11.01 PM.png")

Full disk access permissions granted to the Jamf agent is disclosed in the **Privacy & Security** section of System Settings. It is also disclosed that the permissions setting is configured by a profile.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-4.02.49pm.png?w=595 "Screenshot 2025-12-12 at 4.02.49 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-4.03.43pm.png?w=595 "Screenshot 2025-12-12 at 4.03.43 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-12-at-4.03.51pm.png?w=595 "Screenshot 2025-12-12 at 4.03.51 PM.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?share=pocket)

Like Loading...

### *Related*

Categories: [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/)

Comments (2)
[Leave a comment](#respond)

1. ![TheAppleUser's avatar](https://1.gravatar.com/avatar/700464cb5ab99986d55c4a635276f44f5c4a8085d054dff760c2e34e05c084f6?s=32&d=identicon&r=G)

   TheAppleUser

   December 12, 2025 at 9:54 pm

   [Reply](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?replytocom=72819#respond)

   Woohoo!! Thank you for finding this!!
2. ![Robert Hammen's avatar](https://2.gravatar.com/avatar/2512b7be9b07c1dbeabf3d0e82e8d9b4ad7f13410681ecf2946594d2427a98f2?s=32&d=identicon&r=G)

   Robert Hammen

   December 12, 2025 at 10:23 pm

   [Reply](https://derflounder.wordpress.com/2025/12/12/pppc-device-management-settings-visible-in-system-settings-on-macos-tahoe-26-2-0/?replytocom=72820#respond)

   Please note, if you deploy a profile to allow standard users on macOS to approve screen recording permissions for specific apps (i.e. <https://github.com/poundbangbash/community-screenrecording-pppc-profile>), in macOS 26.2, the On/Off Status for these apps will not be correctly displayed. Apple is aware of this, but please file Feedback and/or open an AppleCare ticket.

1. No trackbacks yet.

### Leave a com...