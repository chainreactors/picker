---
title: Accessing subsystem logging configurations used by the macOS unified logging on macOS Sequoia
url: https://derflounder.wordpress.com/2025/05/05/accessing-subsystem-logging-configurations-used-by-the-macos-unified-logging-on-macos-sequoia/
source: Der Flounder
date: 2025-05-06
fetch_date: 2025-10-06T22:25:27.106959
---

# Accessing subsystem logging configurations used by the macOS unified logging on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Logging](https://derflounder.wordpress.com/category/logging/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Accessing subsystem logging configurations used by the macOS unified logging on macOS Sequoia

## Accessing subsystem logging configurations used by the macOS unified logging on macOS Sequoia

May 5, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

On macOS, the logging used by the OS leverages the [unified logging system](https://developer.apple.com/documentation/os/logging). First introduced as part of macOS 10.12 Sierra, this logging system replaced various individual system log files stored in the **/var/log** directory and replaced them with a central system log that various subsystems send their logging to. This central system log can then be read using a couple of tools included with macOS:

* [Console.app](https://support.apple.com/guide/console/welcome/mac)
* The [log command line tool](https://ss64.com/mac/log.html)

But what subsystems in macOS are currently configured to send logging to the unified system log and how are those subsystem configured? For more details, please see below the jump.

For the subsystems included with macOS, their logging configurations are stored in the following directory:

**/System/Library/Preferences/Logging/Subsystems**

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-05-at-10.40.43am.png?w=595 "Screenshot 2025-05-05 at 10.40.43 AM.png")

As of macOS 15.4.1, here’s the names of the subsystems, their identifiers, and where their configuration files are located:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Logging Subsystem Name | Logging Subsystem Identifier | Configuration File Location |
| --- | --- | --- | --- |
|  | aaafoundation | com.apple.aaafoundation | /System/Library/Preferences/Logging/Subsystems/com.apple.aaafoundation.plist |
|  | accelerate.bnns | com.apple.accelerate.bnns | /System/Library/Preferences/Logging/Subsystems/com.apple.accelerate.bnns.plist |
|  | Accessibility | com.apple.Accessibility | /System/Library/Preferences/Logging/Subsystems/com.apple.Accessibility.plist |
|  | AccessibilityPerformance | com.apple.AccessibilityPerformance | /System/Library/Preferences/Logging/Subsystems/com.apple.AccessibilityPerformance.plist |
|  | accessories.core.iap1 | com.apple.accessories.core.iap1 | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.core.iap1.plist |
|  | accessories.core.iap2 | com.apple.accessories.core.iap2 | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.core.iap2.plist |
|  | accessories.core | com.apple.accessories.core | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.core.plist |
|  | accessories.feature-plugins | com.apple.accessories.feature-plugins | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.feature-plugins.plist |
|  | accessories.frameworks | com.apple.accessories.frameworks | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.frameworks.plist |
|  | accessories.platform-plugins | com.apple.accessories.platform-plugins | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.platform-plugins.plist |
|  | accessories | com.apple.accessories | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.plist |
|  | accessories.transport-plugins | com.apple.accessories.transport-plugins | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.transport-plugins.plist |
|  | accessories.transport-plugins.t818 | com.apple.accessories.transport-plugins.t818 | /System/Library/Preferences/Logging/Subsystems/com.apple.accessories.transport-plugins.t818.plist |
|  | accessoryupdater.uarp | com.apple.accessoryupdater.uarp | /System/Library/Preferences/Logging/Subsystems/com.apple.accessoryupdater.uarp.plist |
|  | accounts | com.apple.accounts | /System/Library/Preferences/Logging/Subsystems/com.apple.accounts.plist |
|  | adplatforms.perf | com.apple.adplatforms.perf | /System/Library/Preferences/Logging/Subsystems/com.apple.adplatforms.perf.plist |
|  | amp.inappmessages | com.apple.amp.inappmessages | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.inappmessages.plist |
|  | amp.iTunesCloud | com.apple.amp.iTunesCloud | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.iTunesCloud.plist |
|  | amp.itunescloudd | com.apple.amp.itunescloudd | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.itunescloudd.plist |
|  | amp.medialibrary | com.apple.amp.medialibrary | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.medialibrary.plist |
|  | amp.mediaplaybackcore | com.apple.amp.mediaplaybackcore | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.mediaplaybackcore.plist |
|  | amp.mediaplayer | com.apple.amp.mediaplayer | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.mediaplayer.plist |
|  | amp.mediaremote | com.apple.amp.mediaremote | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.mediaremote.plist |
|  | amp.mediaremote.verbose | com.apple.amp.mediaremote.verbose | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.mediaremote.verbose.plist |
|  | amp.MediaServices | com.apple.amp.MediaServices | /System/Library/Preferences/Logging/Subsystems/com.apple.amp.MediaServices.plist |
|  | amsengagementd | com.apple.amsengagementd | /System/Library/Preferences/Logging/Subsystems/com.apple.amsengagementd.plist |
|  | amsondevicestoraged | com.apple.amsondevicestoraged | /System/Library/Preferences/Logging/Subsystems/com.apple.amsondevicestoraged.plist |
|  | ane | com.apple.ane | /System/Library/Preferences/Logging/Subsystems/com.apple.ane.plist |
|  | app\_launch\_measurement | com.apple.app\_launch\_measurement | /System/Library/Preferences/Logging/Subsystems/com.apple.app\_launch\_measurement.plist |
|  | appinstallation | com.apple.appinstallation | /System/Library/Preferences/Logging/Subsystems/com.apple.appinstallation.plist |
|  | appintents | com.apple.appintents | /System/Library/Preferences/Logging/Subsystems/com.apple.appintents.plist |
|  | appintentsservices | com.apple.appintentsservices | /System/Library/Preferences/Logging/Subsystems/com.apple.appintentsservices.plist |
|  | AppKit | com.apple.AppKit | /System/Library/Preferences/Logging/Subsystems/com.apple.AppKit.plist |
|  | appleaccount | com.apple.appleaccount | /System/Library/Preferences/Logging/Subsystems/com.apple.appleaccount.plist |
|  | AppleCV3D | com.apple.AppleCV3D | /System/Library/Preferences/Logging/Subsystems/com.apple.AppleCV3D.plist |
|  | appleevents | com.apple.appleevents | /System/Library/Preferences/Logging/Subsystems/com.apple.appleevents.plist |
|  | appleidauthentication | com.apple.appleidauthentication | /System/Library/Preferences/Logging/Subsystems/com.apple.appleidauthentication.plist |
|  | appleidsetup | com.apple.appleidsetup | /System/Library/Preferences/Logging/Subsystems/com.apple.appleidsetup.plist |
|  | AppleIR | com.apple.AppleIR | /System/Library/Preferences/Logging/Subsystems/com.apple.AppleIR.plist |
|  | AppleMediaServices | com.apple.AppleMediaServices | /System/Library/Preferen...