---
title: Disabling Rosetta awareness messages on macOS Tahoe
url: https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/
source: Der Flounder
date: 2026-03-25
fetch_date: 2026-03-26T04:30:00.407035
---

# Disabling Rosetta awareness messages on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Rosetta 2](https://derflounder.wordpress.com/category/rosetta-2/) > Disabling Rosetta awareness messages on macOS Tahoe

## Disabling Rosetta awareness messages on macOS Tahoe

March 25, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s move from using Intel processors to Apple Silicon processors for all Mac models, [Apple has announced a transition timeline for macOS’s Rosetta 2 translation environment](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment). Rosetta 2 will continue in its current form on both macOS 26 and macOS 27, but there will be as-yet unspecified changes occurring beyond macOS 27.

As part of this transition process, as of macOS Tahoe 26.4 there is a new window that will be periodically displayed when [apps which are Intel-based](https://support.apple.com/102527) get launched on Apple Silicon Macs. For example, an earlier version of an Automator app I wrote named [Show or Hide Desktop Icons.app](https://github.com/rtrouton/Show-or-Hide-Desktop-Icons) is an Intel-based app.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/03/screenshot-2026-03-24-at-5.33.28pm.png?w=265&h=507 "Screenshot 2026-03-24 at 5.33.28 PM.png")

On macOS 26.4 and later, launching this earlier version of the **Show or Hide Desktop Icons** app will periodically result in the following message being displayed by the OS.

![Rosetta awareness window.](https://derflounder.wordpress.com/wp-content/uploads/2026/03/rosetta_awareness_window.png?w=364&h=118 "rosetta_awareness_window.png")

This new message may not be desirable to display in all Mac environments, so Apple has provided management options to prevent this message from being shown. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.applicationaccess**
* Key: **allowRosettaUsageAwareness**
* Value: Boolean

This setting can be managed by a configuration profile, where setting a boolean value of **false** will prevent the message from being displayed. Please see below for an example profile. This profile is also available via the following link:

<https://github.com/rtrouton/profiles/tree/main/DisableRosettaUsageAwareness>

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
|  | <string>A3A6F8B9-3A59-4D39-8569-FF38DA9A8C1F</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>A3A6F8B9-3A59-4D39-8569-FF38DA9A8C1F</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Disable Rosetta Usage Awareness</string> |
|  | <key>PayloadDescription</key> |
|  | <string>Disables Rosetta Usage Awareness Dialog Window</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadEnabled</key> |
|  | <true /> |
|  | <key>PayloadRemovalDisallowed</key> |
|  | <false /> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadContent</key> |
|  | <array> |
|  | <dict> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Custom Settings</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>E36A3269-B3A0-42F1-B045-1DB4D27CE7A2</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.ManagedClient.preferences</string> |
|  | <key>PayloadUUID</key> |
|  | <string>E36A3269-B3A0-42F1-B045-1DB4D27CE7A2</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadContent</key> |
|  | <dict> |
|  | <key>com.apple.applicationaccess</key> |
|  | <dict> |
|  | <key>Forced</key> |
|  | <array> |
|  | <dict> |
|  | <key>mcx\_preference\_settings</key> |
|  | <dict> |
|  | <key>allowRosettaUsageAwareness</key> |
|  | <false /> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/9ee5d5e8a71e5cf2c8f17df1cc532841/raw/922bac095ec42bfea909d98ed2afabc6d1166687/DisableRosettaUsageAwareness.mobileconfig)
 [DisableRosettaUsageAwareness.mobileconfig](https://gist.github.com/rtrouton/9ee5d5e8a71e5cf2c8f17df1cc532841#file-disablerosettausageawareness-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/?share=tumblr)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Rosetta 2](https://derflounder.wordpress.com/category/rosetta-2/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/03/25/disabling-rosetta-awareness-messages-on-macos-tahoe/#respond)

Δ

[Managing automatic installation of Background Security Improvements for macOS using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2026/03/20/managing-automatic-installation-of-background-security-improvements-for-macos-using-blueprints-in-jamf-pro/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://ww...