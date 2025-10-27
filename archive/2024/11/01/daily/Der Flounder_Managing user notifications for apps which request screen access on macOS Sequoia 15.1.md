---
title: Managing user notifications for apps which request screen access on macOS Sequoia 15.1
url: https://derflounder.wordpress.com/2024/10/31/managing-user-notifications-for-apps-which-request-screen-access-on-macos-sequoia-15-1/
source: Der Flounder
date: 2024-11-01
fetch_date: 2025-10-06T19:14:50.063470
---

# Managing user notifications for apps which request screen access on macOS Sequoia 15.1

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Managing user notifications for apps which request screen access on macOS Sequoia 15.1

## Managing user notifications for apps which request screen access on macOS Sequoia 15.1

October 31, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

[As part of the macOS Sequoia 15.1 release notes](https://developer.apple.com/documentation/macos-release-notes/macos-15_1-release-notes#Mobile-Device-Management), this section is included:

***MDM profiles can use the new key ‘forceBypassScreenCaptureAlert’, which allows owners of managed devices to opt out of user notifications for content capture technologies. (131327961)***

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-31-at-8.36.png?w=595 "Screenshot 2024-10-31 at 8.36.png")

What’s this note discussing? It’s referring to a user notification that Apple introduced in macOS Sequoia for apps which request screen access but aren’t using Apple’s [SCContentSharingPickerMode](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpicker) API to do so. A good example is the user notification for the Zoom app, which uses screen access for video conferencing.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/disablescreenaccessrequestusernotifications.png?w=435&h=600 "DisableScreenAccessRequestUserNotifications.png")

These user notifications appear monthly and request the user to choose whether or not they want to allow this access for the app in question.

For Mac environments which want to manage these notifications and prevent them from being displayed to their users, Apple has provided management options as part of macOS Sequoia 15.1. For more details, please see below the jump.

The relevant [preference domain and key values](https://developer.apple.com/documentation/devicemanagement/restrictions) are listed below:

* Preference domain: **com.apple.applicationaccess**
* Key: **forceBypassScreenCaptureAlert**
* Value: Boolean

It’s important to note that while this management setting works on macOS Sequoia 15.1, it is not available to macOS Sequoia 15.0.1, 15.0.0 or earlier versions of macOS.

These settings can be managed by a configuration profile, where setting a boolean value of **true** will disable the user notifications. Please see below for an example profile. The example profile is also available via the following link:

<https://github.com/rtrouton/profiles/tree/main/DisableScreenAccessRequestUserNotifications>

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>PayloadContent</key> |
|  | <array> |
|  | <dict> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Restrictions</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>com.apple.applicationaccess.C70F311D-B330-4620-9097-F98FD7E39E33</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.applicationaccess</string> |
|  | <key>PayloadUUID</key> |
|  | <string>C70F311D-B330-4620-9097-F98FD7E39E33</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>forceBypassScreenCaptureAlert</key> |
|  | <true/> |
|  | </dict> |
|  | </array> |
|  | <key>PayloadDescription</key> |
|  | <string>Disables user notifications for apps which request screen access</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Disable Screen Access Request User Notifications</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>1A6E3566-0112-40F7-A49F-416D99C61566</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadUUID</key> |
|  | <string>1A6E3566-0112-40F7-A49F-416D99C61566</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/9d0662f328706ca6b60ac1999bfe3d9c/raw/6d9e53797b1322822ac411df16eb35d10d645137/DisableScreenAccessRequestUserNotifications.mobileconfig)
 [DisableScreenAccessRequestUserNotifications.mobileconfig](https://gist.github.com/rtrouton/9d0662f328706ca6b60ac1999bfe3d9c#file-disablescreenaccessrequestusernotifications-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

**Note:** If you’re planning to use the example profile with [Jamf Pro](https://www.jamf.com/jamf-pro), it will need to be signed before it can be uploaded to Jamf Pro. If you’re not familiar with how to sign profiles, the post linked below is a good guide to how that process works:

<https://macblog.org/sign-configuration-profiles/>

As an alternative, you can use the **Application & Custom Settings** profile payload in Jamf Pro with the plist shown below to create a profile with the same functionality as the example profile.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>forceBypassScreenCaptureAlert</key> |
|  | <true/> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/6e2637417f2ff694a4115c3eed50cc5d/raw/d479a57780113dbad3f50c87a13c928e5728af46/com.apple.applicationaccess.plist)
 [com.apple.applicationaccess.plist](https://gist.github.com/rtrouton/6e2637417f2ff694a4115c3eed50cc5d#file-com-apple-applicationaccess-plist)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-31-at-9.41.png?w=595 "Screenshot 2024-10-31 at 9.41.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/10/31/managing-user-notifications-for-apps-which-request-screen-access-on-macos-sequoia-15-1/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/10/31/managing-user-notifications-for-apps-which-request-screen-access-on-macos-sequoia-15-1/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/10/31/managing-user-notifications-for-apps-which-request-screen-access-on-macos-sequoia-15-1/?share=linkedin)
* [Click to share on Reddit (Opens in n...