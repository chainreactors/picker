---
title: Blocking system extension disablement via System Settings on macOS Sequoia
url: https://derflounder.wordpress.com/2024/09/16/blocking-system-extension-disablement-via-system-settings-on-macos-sequoia/
source: Der Flounder
date: 2024-09-17
fetch_date: 2025-10-06T18:23:28.129286
---

# Blocking system extension disablement via System Settings on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Blocking system extension disablement via System Settings on macOS Sequoia

## Blocking system extension disablement via System Settings on macOS Sequoia

September 16, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Since the introduction of system extensions in macOS Catalina, Apple has been adding controls for both individual users and Mac admins to allow management of system extensions. For individual users who manage their own Macs without using MDM management, Apple asks the user to approve the system extensions functions. In turn, for managed environments, Apple has provided management profile options to allow Mac admins to pre-approve or block system extensions from running on the Macs in that environment.

As part of the release of macOS Sequoia, Apple has added new user functionality for managing system extensions, as well as management profile options for Mac admins. For more details, please see below the jump.

The new functionality is the ability to manage installed system extensions via System Settings, with the relevant controls being found in **System Settings**: **General**: **Login Items & Extensions**. As an example, let’s look at the [LuLu open-source firewall app](https://github.com/objective-see/LuLu). This app uses a [network extension](https://developer.apple.com/documentation/networkextension) and a content filter.

On macOS Sonoma, the following management profiles can be deployed to allow LuLu’s network extension to be deployed and removed without the user being prompted.

Profile to allow deployment and removal:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-14-at-10.13.43e280afam.png?w=595 "Screenshot 2024-09-14 at 10.13.43 AM.png")

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
|  | <string>634D0A81-903D-4639-8C72-39A773AF68A8</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>634D0A81-903D-4639-8C72-39A773AF68A8</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>LuLu System Extension Allowed and Removable Settings</string> |
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
|  | <key>PayloadUUID</key> |
|  | <string>FF5677D3-9A0A-4592-8FFE-638846B7F5DD</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.system-extension-policy</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>FF5677D3-9A0A-4592-8FFE-638846B7F5DD</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>System Extensions</string> |
|  | <key>PayloadDescription</key> |
|  | <string/> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadEnabled</key> |
|  | <true/> |
|  | <key>AllowUserOverrides</key> |
|  | <true/> |
|  | <key>AllowedSystemExtensions</key> |
|  | <dict> |
|  | <key>VBG97UB4TA</key> |
|  | <array> |
|  | <string>com.objective-see.lulu.extension</string> |
|  | </array> |
|  | </dict> |
|  | <key>RemovableSystemExtensions</key> |
|  | <dict> |
|  | <key>VBG97UB4TA</key> |
|  | <array> |
|  | <string>com.objective-see.lulu.extension</string> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/53ac1015a91dbbba09dd50fc489ca267/raw/a5a3b8e96bda29500f132fa6d76968c1bf5a0cc0/LuLu%20System%20Extension%20Allowed%20and%20Removable%20Settings.mobileconfig)
 [LuLu System Extension Allowed and Removable Settings.mobileconfig](https://gist.github.com/rtrouton/53ac1015a91dbbba09dd50fc489ca267#file-lulu-system-extension-allowed-and-removable-settings-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

Profile to configure the content filter:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-14-at-10.13.57e280afam.png?w=595 "Screenshot 2024-09-14 at 10.13.57 AM.png")

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
|  | <string>883C5AE4-FCBA-4A1D-83D5-51120C081063</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>883C5AE4-FCBA-4A1D-83D5-51120C081063</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>LuLu Content Filter Settings</string> |
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
|  | <key>FilterDataProviderBundleIdentifier</key> |
|  | <string>com.objective-see.lulu.extension</string> |
|  | <key>FilterDataProviderDesignatedRequirement</key> |
|  | <string>anchor apple generic and identifier "com.objective-see.lulu.extension" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /\* exists \*/ or certificate 1[field.1.2.840.113635.100.6.2.6] /\* exists \*/ and certificate leaf[field.1.2.840.113635.100.6.1.13] /\* exists \*/ and certificate leaf[subject.OU] = VBG97UB4TA)</string> |
|  | <key>FilterPacketProviderBundleIdentifier</key> |
|  | <string>com.objective-see.lulu.extension</string> |
|  | <key>FilterPacketProviderDesignatedRequirement</key> |
|  | <string>anchor apple generic and identifier "com.objective-see.lulu.extension" and (certificate leaf[field.1.2.840.113635.100.6.1.9] /\* exists \*/ or certificate 1[field.1.2.840.113635.100.6.2.6] /\* exists \*/ and certificate leaf[field.1.2.840.113635.100.6.1.13] /\* exists \*/ and certificate leaf[subject.OU] = VBG97UB4TA)</string> |
|  | <key>FilterPackets...