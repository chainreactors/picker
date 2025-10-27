---
title: Managing Apple Intelligence features on macOS Sequoia 15.1
url: https://derflounder.wordpress.com/2024/10/28/managing-apple-intelligence-features-on-macos-sequoia-15-1/
source: Der Flounder
date: 2024-10-29
fetch_date: 2025-10-06T18:47:54.039795
---

# Managing Apple Intelligence features on macOS Sequoia 15.1

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Managing Apple Intelligence features on macOS Sequoia 15.1

## Managing Apple Intelligence features on macOS Sequoia 15.1

October 28, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of the release of macOS Sequoia, Apple has provided management options on macOS for [Apple Intelligence](https://www.apple.com/apple-intelligence) features. While not all of these Apple Intelligence features may be available as of macOS 15.1 in all areas of the world, use of these new features may not be acceptable for security reasons in all Mac environments. Having these management options available now allows Mac admins to get management of these features in place before Apple makes them available. For more details, please see below the jump.

As of macOS 15.1, management options are available for the following [Apple Intelligence functionality](https://developer.apple.com/apple-intelligence/):

* [Genmoji](https://bgr.com/tech/how-to-use-genmoji-ios-18/)
* [Image Playground](https://www.macrumors.com/guide/image-playground/)
* [Writing Tools](https://www.macrumors.com/guide/apple-intelligence-writing-tools/)
* [Summarizing emails](https://www.idownloadblog.com/2024/08/15/use-apple-intelligence-to-summarize-text/)

The relevant [preference domain and key values](https://developer.apple.com/documentation/devicemanagement/restrictions) are listed below:

**Genmoji**

* Preference domain: **com.apple.applicationaccess**
* Key: **allowGenmoji**
* Value: Boolean

**Image Playground**

* Preference domain: **com.apple.applicationaccess**
* Key: **allowImagePlayground**
* Value: Boolean

**Writing Tools**

* Preference domain: **com.apple.applicationaccess**
* Key: **allowWritingTools**
* Value: Boolean

**Summarize emails**

* Preference domain: **com.apple.applicationaccess**
* Key: **allowMailSummary**
* Value: Boolean

It’s important to note that while all of the settings listed above work on macOS Sequoia 15.1, not all the settings work on macOS Sequoia 15.0.0 and 15.0.1. Here’s the compatibility list:

**macOS 15.0 and later:**

* **allowGenmoji**
* **allowImagePlayground**
* **allowWritingTools**

**macOS 15.1 and later:**

* **allowMailSummary**

These settings can be managed by a configuration profile, where setting a boolean value of **false** will disable the Apple Intelligence feature in question. Please see below for example profiles. The example profiles are also available via the following links:

* Genmoji: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableGenmoji>
* Image Playground: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableImagePlayground>
* Writing Tools: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableWritingTools>
* Summarize emails: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableMailSummary>

**Genmoji**

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
|  | <string>com.apple.applicationaccess.1281701E-9695-4447-9028-4962C25162FF</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.applicationaccess</string> |
|  | <key>PayloadUUID</key> |
|  | <string>1281701E-9695-4447-9028-4962C25162FF</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>allowGenmoji</key> |
|  | <false/> |
|  | </dict> |
|  | </array> |
|  | <key>PayloadDescription</key> |
|  | <string>Disables creation of new Genmoji</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Apple Intelligence Disable Genmoji</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>B83678F5-B2CB-467C-A89F-73F2E2E1346C</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadUUID</key> |
|  | <string>B83678F5-B2CB-467C-A89F-73F2E2E1346C</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/ce7840339ba20f57cb28dfdb3eab45f0/raw/cf841842aacea54f3540e12417e558e23b192a2e/AppleIntelligenceDisableGenmoji.mobileconfig)
 [AppleIntelligenceDisableGenmoji.mobileconfig](https://gist.github.com/rtrouton/ce7840339ba20f57cb28dfdb3eab45f0#file-appleintelligencedisablegenmoji-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

**Image Playground**

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
|  | <string>com.apple.applicationaccess.4FDE23F1-2652-4653-813C-205C9B86C0F5</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.applicationaccess</string> |
|  | <key>PayloadUUID</key> |
|  | <string>4FDE23F1-2652-4653-813C-205C9B86C0F5</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>allowImagePlayground</key> |
|  | <false/> |
|  | </dict> |
|  | </array> |
|  | <key>PayloadDescription</key> |
|  | <string>Disables Image Playground and prohibits the use of image generation</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Apple Intelligence Disable Image Playground</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>5596EE02-5B47-4B4C-B3F0-AA531C1E9AEB</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadUUID</key> |
|  | <string>5596EE02-5B47-4B4C-B3F0-AA531C1E9AEB</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/9e6659df1e747e7a2cc0b48ad77cfd54/raw/21db7da001c8e88f4d238a995fd69c235c449de1/AppleIntelligenceDisableImagePlayground.mobileconfig)
 ...