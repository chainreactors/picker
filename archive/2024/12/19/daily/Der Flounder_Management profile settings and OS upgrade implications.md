---
title: Management profile settings and OS upgrade implications
url: https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/
source: Der Flounder
date: 2024-12-19
fetch_date: 2025-10-06T19:34:15.913409
---

# Management profile settings and OS upgrade implications

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Management profile settings and OS upgrade implications

## Management profile settings and OS upgrade implications

December 18, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A question I’ve seen repeatedly in the Mac Admins Slack goes something like this:

***“I installed this profile for macOS NewVersion onto macOS OldVersion, then upgraded from macOS OldVersion to macOS NewVersion. The setting didn’t work. Why didn’t it work?”***

Why it didn’t work has to do with how management profile settings are handled. When a management profile is installed, the settings contained within that profile are applied.

This settings application occurs exclusively at the time of the profile installation. Those applied settings are never again re-read or re-applied as long as that profile is installed. The settings in a profile are applied only at the time of installation and that is the current state of things.

How is this relevant to settings you want to apply to macOS? Apple defines what OS version a setting was introduced for, which means it does not work for OS versions prior to that. For more information, please see below the jump.

An example of this is the management setting for iPhone mirroring:

<https://github.com/apple/device-management/blob/1fa842739c8f19db5b62f3ac6aed261cc378e5b8/mdm/profiles/com.apple.applicationaccess.yaml#L1834-L1860>

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/screenshot-2024-12-18-at-11.01.png?w=595 "Screenshot 2024-12-18 at 11.01.png")

This setting was introduced for macOS as of macOS 15 Sequoia. That means that the setting works on macOS Sequoia but what happens when you install a management profile like the one below which contains this setting onto a Mac running macOS 14 Sonoma?

Nothing.

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
|  | <string>com.apple.applicationaccess.DD8454BB-A1D6-4DD9-B1AC-C1B6ABA512E9</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.applicationaccess</string> |
|  | <key>PayloadUUID</key> |
|  | <string>DD8454BB-A1D6-4DD9-B1AC-C1B6ABA512E9</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>allowiPhoneMirroring</key> |
|  | <false/> |
|  | </dict> |
|  | </array> |
|  | <key>PayloadDescription</key> |
|  | <string>Blocks the use of iPhone mirroring</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Block iPhone Mirroring</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>D0B2E096-2C7F-4F2F-A1C0-FFE16919768B</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadUUID</key> |
|  | <string>D0B2E096-2C7F-4F2F-A1C0-FFE16919768B</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/2b6dd1feb9d429e7f9747540f161d429/raw/7819a25cff93fa22f3a917f98ced5bbae7da0e92/BlockiPhoneMirroring.mobileconfig)
 [BlockiPhoneMirroring.mobileconfig](https://gist.github.com/rtrouton/2b6dd1feb9d429e7f9747540f161d429#file-blockiphonemirroring-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

A profile’s settings get applied at the time of installation. If the setting isn’t understood by the OS the profile is installed onto at the time of installation, the setting is ignored.

In the context of the management setting for iPhone mirroring, macOS Sonoma doesn’t have the management option for managing iPhone mirroring so Sonoma will ignore the setting. It will remain ignored if the Mac gets upgraded to Sequoia because the setting only gets applied at the time of installation and the setting never gets re-evaluated to see if it applies to Sequoia. The outcome is that the setting does not get applied on Sequoia if the profile with the setting was installed on Sonoma.

How do you fix this? Remove the profile with the iPhone mirroring setting from the Sequoia Mac and re-install the profile. Once the profile is installed again, the setting will get applied as part of the install process. Sequoia has that setting as a management option, so Sequoia will then apply the setting from the profile and manage iPhone mirroring as defined by the profile’s settings.

So what does this mean for management settings you want to apply to macOS NewVersion? You’ll need to check what the introduction version is for the setting you want to apply. If it’s a brand new setting where the introduction is on macOS NewVersion, you’ll need to wait until the Mac is running macOS NewVersion before deploying a profile to manage that setting.

For Mac admins who want the capability to install a setting on macOS OldVersion and have it apply to macOS NewVersion, I recommend [filing feedback with Apple to request it](https://support.apple.com/en-mo/guide/feedback-assistant/fbad45b5bb25/mac) .

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/12/18/management-profile-settings-and-os-upgrade-implications/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://de...