---
title: Providing GlobalProtect portal address via macOS configuration profile on macOS Sonoma
url: https://derflounder.wordpress.com/2024/07/28/providing-globalprotect-portal-address-via-macos-configuration-profile-on-macos-sonoma/
source: Der Flounder
date: 2024-07-29
fetch_date: 2025-10-06T17:38:44.817769
---

# Providing GlobalProtect portal address via macOS configuration profile on macOS Sonoma

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Providing GlobalProtect portal address via macOS configuration profile on macOS Sonoma

## Providing GlobalProtect portal address via macOS configuration profile on macOS Sonoma

July 28, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the limitations of [Palo Alto’s GlobalProtect VPN client](https://www.paloaltonetworks.com/sase/globalprotect) on macOS is that it’s not currently possible to natively provide the GlobalProtect VPN portal address using a macOS configuration profile. Instead, the GlobalProtect VPN client is looking for the portal address in a **com.paloaltonetworks.GlobalProtect.settings.plist** file, which is stored in the **/Library/Preferences** directory. However, with some work, it is possible to use a profile to provide the portal address information to the GlobalProtect VPN client. For more details, please see below the jump.

This method relies on the capability of a macOS configuration profile to create files in the following location:

**/Library/Managed Preferences**

With this capability, it’s possible to set up a profile which provides the GlobalProtect portal address to a plist file within the **/Library/Managed Preferences** directory. In turn, this allows a script to read from that plist file and provide the correct information for the GlobalProtect portal to the **/Library/Preferences/com.paloaltonetworks.GlobalProtect.settings.plist** file which GlobalProtect uses for its settings.

As an example, if the GlobalProtect portal address is **globalprotect.portal.address.goes.here**, you can set up and install a profile like the one shown below:

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
|  | <string>B0CBB3F2-D092-4B3D-A261-81F19050C56B</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>B0CBB3F2-D092-4B3D-A261-81F19050C56B</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Palo Alto GlobalProtect Portal Address</string> |
|  | <key>PayloadDescription</key> |
|  | <string /> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadEnabled</key> |
|  | <true /> |
|  | <key>PayloadRemovalDisallowed</key> |
|  | <true /> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadContent</key> |
|  | <array> |
|  | <dict> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Custom Settings</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>DA29D66E-134E-4A03-BAA0-1DD42B555C1E</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.ManagedClient.preferences</string> |
|  | <key>PayloadUUID</key> |
|  | <string>DA29D66E-134E-4A03-BAA0-1DD42B555C1E</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadContent</key> |
|  | <dict> |
|  | <key>com.paloalto.globalprotect.portal.address</key> |
|  | <dict> |
|  | <key>Forced</key> |
|  | <array> |
|  | <dict> |
|  | <key>mcx\_preference\_settings</key> |
|  | <dict> |
|  | <key>PortalAddress</key> |
|  | <string>globalprotect.portal.address.goes.here</string> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/20b7c3fee181e3492894dbb770d22e57/raw/ddf785f2b584cfc0cb03bee6f16f0fcbb13a4620/Palo%20Alto%20GlobalProtect%20Portal%20Address.mobileconfig)
 [Palo Alto GlobalProtect Portal Address.mobileconfig](https://gist.github.com/rtrouton/20b7c3fee181e3492894dbb770d22e57#file-palo-alto-globalprotect-portal-address-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/07/screenshot-2024-07-28-at-3.07.49e280afpm.png?w=595 "Screenshot 2024-07-28 at 3.07.49 PM.png")

Once the profile is installed, a **com.paloalto.globalprotect.portal.address.plist** file will be created in the **/Library/Managed Preferences** directory which looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>PortalAddress</key> |
|  | <string>globalprotect.portal.address.goes.here</string> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/73462e5235b0d7cdbe500f137d4b3f18/raw/beb89705bea280b92eff9584dc118f9d807f2689/com.paloalto.globalprotect.portal.address.plist)
 [com.paloalto.globalprotect.portal.address.plist](https://gist.github.com/rtrouton/73462e5235b0d7cdbe500f137d4b3f18#file-com-paloalto-globalprotect-portal-address-plist)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/07/screenshot-2024-07-28-at-3.09.08e280afpm.png?w=595 "Screenshot 2024-07-28 at 3.09.08 PM.png")

From there, a script like the one shown below can read the GlobalProtect portal address information stored in the **/Library/Managed Preferences/com.paloalto.globalprotect.portal.address.plist** file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # This script uses PlistBuddy to create a configuration plist for Palo Alto GlobalProtect |
|  | # using information provided by a macOS configuration profile, as GlobalProtect does not |
|  | # appear to be able to natively use a profile for management. |
|  |  |
|  | # Original script by Chad Brewer: |
|  | # <https://www.jamf.com/jamf-nation/discussions/10198/anyone-deployed-palo-alto-globalprotect#responseChild196652> |
|  |  |
|  | exitCode=0 |
|  | plistBuddy="/usr/libexec/PlistBuddy" |
|  | GPplistFile="/Library/Preferences/com.paloaltonetworks.GlobalProtect.settings.plist" |
|  | PortalAddressFile="/Library/Managed Preferences/com.paloalto.globalprotect.portal.address.plist" |
|  |  |
|  | if [[ -f "$P...