---
title: Managing Apple Intelligence features on macOS Sequoia 15.3
url: https://derflounder.wordpress.com/2025/01/29/managing-apple-intelligence-features-on-macos-sequoia-15-3/
source: Der Flounder
date: 2025-01-30
fetch_date: 2025-10-06T20:08:46.148580
---

# Managing Apple Intelligence features on macOS Sequoia 15.3

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Managing Apple Intelligence features on macOS Sequoia 15.3

## Managing Apple Intelligence features on macOS Sequoia 15.3

January 29, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to my earlier posts on managing Apple Intelligence features on macOS Sequoia [15.1](https://derflounder.wordpress.com/2024/10/28/managing-apple-intelligence-features-on-macos-sequoia-15-1/) and [15.2](https://derflounder.wordpress.com/2024/12/12/managing-apple-intelligence-features-on-macos-sequoia-15-2/) , Apple has added a couple of new management options for Apple Intelligence as part of the release of macOS Sequoia 15.3. For more details, please see below the jump.

As of macOS 15.3, management options are available for the following [Apple Intelligence](https://developer.apple.com/apple-intelligence/) functionality:

* Genmoji
* Image Playground
* Writing Tools
* Summarizing emails
* Enabling Siri to connect to third party cloud-based intelligence services
* Managing non-anonymous login to third party cloud-based intelligence services
* Allowing third party cloud-based intelligence service workspace IDs
* Notes transcription summaries

The [relevant key values](https://developer.apple.com/documentation/devicemanagement/restrictions) are below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Restriction | Setting available in version | Description | Key | Key value | Default setting in macOS |
| --- | --- | --- | --- | --- | --- | --- |
|  | Allow Image Playground | macOS 15.0.0 | If key value is set to FALSE, prohibits the use of image generation. | allowImagePlayground | Boolean | TRUE |
|  | Allow Writing Tools | macOS 15.0.0 | If key value is set to FALSE, allows only anonymous access to external services | allowWritingTools | Boolean | TRUE |
|  | Allow Genmoji | macOS 15.0.0 | If key value is set to FALSE, disables Genmoji | allowGenmoji | Boolean | TRUE |
|  | Allow Mail Summary | macOS 15.1.0 | If key value is set to FALSE, prohibits the ability to create email summaries | allowMailSummary | Boolean | TRUE |
|  | Allow External Intelligence Integrations | macOS 15.2.0 | If key value is set to FALSE, prohibits integrations with external services including ChatGPT and Google Gemini | allowExternalIntelligenceIntegrations | Boolean | TRUE |
|  | Allow External Intelligence Sign-Ins | macOS 15.2.0 | If key value is set to FALSE, prohibits the ability to create email summaries | allowExternalIntelligenceIntegrationsSignIn | Boolean | TRUE |
|  | Allow External Intelligence Workspace IDs | macOS 15.3.0 | If key value is set to the correct workspace ID string, Apple Intelligence will only allow the given external integration workspace ID to be used and will require a sign-in in order to make requests | allowedExternalIntelligenceWorkspaceIDs | String | None |
|  | Allow Notes Transcription Summary | macOS 15.3.0 | If key value is set to FALSE, disables transcription summarization in Notes. | allowNotesTranscriptionSummary | Boolean | TRUE |

[view raw](https://gist.github.com/rtrouton/0ed191e47bd954422f81682c6c03b8f2/raw/4de54db9371b58b451da554c9b85bd4452e358d4/Apple%20Intelligence%20profile%20information%2015%20dot%200%20through%2015%20dot%203.csv)
 [Apple Intelligence profile information 15 dot 0 through 15 dot 3.csv](https://gist.github.com/rtrouton/0ed191e47bd954422f81682c6c03b8f2#file-apple-intelligence-profile-information-15-dot-0-through-15-dot-3-csv)
hosted with ❤ by [GitHub](https://github.com)

It’s important to note that while all of the settings listed above work on macOS Sequoia 15.3, not all work on earlier versions of macOS Sequoia. Here’s the compatibility list:

**macOS 15.0 and later**:

* **allowGenmoji**
* **allowImagePlayground**
* **allowWritingTools**

**macOS 15.1 and later:**

* **allowMailSummary**

**macOS 15.2 and later:**

* **allowExternalIntelligenceIntegrations**
* **allowExternalIntelligenceIntegrationsSignIn**

**macOS 15.3 and later:**

* **allowedExternalIntelligenceWorkspaceIDs**
* **allowNotesTranscriptionSummary**

Most of these settings can be managed by a configuration profile, where setting a boolean value of **false** will disable the Apple Intelligence feature in question. The one exception at this point is the one for managing workspace IDs for allowed external intelligence integrations, which uses a string value. An example profile which allows one workspace ID is available below:

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
|  | <string>com.apple.applicationaccess.CF921560-2717-4986-8885-4FC8002C6BF7</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.applicationaccess</string> |
|  | <key>PayloadUUID</key> |
|  | <string>CF921560-2717-4986-8885-4FC8002C6BF7</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>allowedExternalIntelligenceWorkspaceIDs</key> |
|  | <array> |
|  | <string>workspace\_id\_goes\_here</string> |
|  | </array> |
|  | </dict> |
|  | </array> |
|  | <key>PayloadDescription</key> |
|  | <string>Alows External Intelligence Integrations using specific Workspace ID</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Apple Intelligence Allow External Intelligence Workspace ID</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>14A04D12-F054-4E11-8943-D55DA53A61E9</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadUUID</key> |
|  | <string>14A04D12-F054-4E11-8943-D55DA53A61E9</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/b9764eee13574843783015c0b33c1173/raw/b30a1e6ffe9fa56567627e55a140680aff8ac683/AppleIntelligenceAllowExternalIntelligenceWorkspaceID.mobileconfig)
 [AppleIntelligenceAllowExternalIntelligenceWorkspaceID.mobileconfig](https://gist.github.com/rtrouton/b9764eee13574843783015c0b33c1173#file-appleintelligenceallowexternalintelligenceworkspaceid-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

If you need to allow the use of multiple workspace IDs, an ...