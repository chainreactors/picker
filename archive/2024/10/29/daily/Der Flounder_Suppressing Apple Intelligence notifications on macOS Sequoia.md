---
title: Suppressing Apple Intelligence notifications on macOS Sequoia
url: https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/
source: Der Flounder
date: 2024-10-29
fetch_date: 2025-10-06T18:47:49.267966
---

# Suppressing Apple Intelligence notifications on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Suppressing Apple Intelligence notifications on macOS Sequoia

## Suppressing Apple Intelligence notifications on macOS Sequoia

October 28, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s rollout of Apple Intelligence, there’s a Notification Center notification which may appear on macOS 15.1 and later which prompts you to try using Apple Intelligence.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/suppressappleintelligencenotifications.png?w=595 "SuppressAppleIntelligenceNotifications.png")

Shops who want to block use of Apple Intelligence for security reasons may also want to stop these notifications from appearing. This is possible to do once you have the bundle identifier for the notification in question. Thanks to excellent detective work by colleagues in the Mac Admins Slack, the correct bundle identifier for this notification has been identified as the following:

**\_SYSTEM\_CENTER\_:com.apple.followup.alert**

Once you have the bundle identifier, you can put this into a configuration profile which [manages notification settings](https://developer.apple.com/documentation/devicemanagement/notifications) to block these notifications from appearing. For more details, please see below the jump.

Please see below for an example profile. This profile is also available via the following link:

<https://github.com/rtrouton/profiles/tree/main/SuppressAppleIntelligenceNotifications>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1"> |
|  | <dict> |
|  | <key>PayloadUUID</key> |
|  | <string>1B270908-4F78-4ADD-A97D-EEFD21AD3732</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>1B270908-4F78-4ADD-A97D-EEFD21AD3732</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Suppress Apple Intelligence notifications</string> |
|  | <key>PayloadDescription</key> |
|  | <string/> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadEnabled</key> |
|  | <true/> |
|  | <key>PayloadRemovalDisallowed</key> |
|  | <true/> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadContent</key> |
|  | <array> |
|  | <dict> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Notifications Payload</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>7B5578BC-11E6-45B1-A84F-61708AD47711</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.notificationsettings</string> |
|  | <key>PayloadUUID</key> |
|  | <string>7B5578BC-11E6-45B1-A84F-61708AD47711</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>NotificationSettings</key> |
|  | <array> |
|  | <dict> |
|  | <key>BundleIdentifier</key> |
|  | <string>\_SYSTEM\_CENTER\_:com.apple.followup.alert</string> |
|  | <key>CriticalAlertEnabled</key> |
|  | <false/> |
|  | <key>NotificationsEnabled</key> |
|  | <false/> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/694df663680394a0accbee90d813d223/raw/63f0c6dad93db200845cb5211769c46d033d642d/SuppressAppleIntelligenceNotifications.mobileconfig)
 [SuppressAppleIntelligenceNotifications.mobileconfig](https://gist.github.com/rtrouton/694df663680394a0accbee90d813d223#file-suppressappleintelligencenotifications-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (3)
[Leave a comment](#respond)

1. ![Luke.Mason's avatar](https://0.gravatar.com/avatar/9c8fee81e6c062a04dc6bc5f36b1f0096b3ae4b4966a964581623e304596b763?s=32&d=identicon&r=G)

   Luke.Mason

   October 29, 2024 at 4:33 pm

   [Reply](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?replytocom=72548#respond)

   This one too.

   [signature\_2346253767]

   Luke Mason (he/him/his)

   Systems Specialist

   Highways and Public Works | ICT | Data and Application Support

   C 867-335-1136 | Yukon.ca<https://yukon.ca/>

   I respectfully acknowledge that I live and work within the traditional territories of the Kwanlin DÃ¼n First Nation and the Taâan KwÃ¤châÃ¤n Council.
2. ![atombomb13's avatar](https://0.gravatar.com/avatar/0ca6aa21495ea12eb5571b5c94c008f2b42ed5a21e7ba50c305d041217069e9a?s=32&d=identicon&r=G)

   [atombomb13](http://adamdurancom.wordpress.com)

   October 31, 2024 at 2:39 pm

   [Reply](https://derflounder.wordpress.com/2024/10/28/suppressing-apple-intelligence-notifications-on-macos-sequoia/?replytocom=72555#respond)

   Thanks Rich!
3. ![Naren's avatar](https://1.gravatar.com/avatar/4c2a7133fc89d629e048ffa8daeb20d56d6da42cc57a5ef8eee85d8f8c2bebb5?s=32&d=identicon&r=G)

   Naren

   January 23, 2025 at 2:24 pm

   [Reply](https://derflounder.wordpress.com/2024/10/28/suppressing-app...