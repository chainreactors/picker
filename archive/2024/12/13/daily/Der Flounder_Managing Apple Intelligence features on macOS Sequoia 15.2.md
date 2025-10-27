---
title: Managing Apple Intelligence features on macOS Sequoia 15.2
url: https://derflounder.wordpress.com/2024/12/12/managing-apple-intelligence-features-on-macos-sequoia-15-2/
source: Der Flounder
date: 2024-12-13
fetch_date: 2025-10-06T19:36:10.764671
---

# Managing Apple Intelligence features on macOS Sequoia 15.2

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Managing Apple Intelligence features on macOS Sequoia 15.2

## Managing Apple Intelligence features on macOS Sequoia 15.2

December 12, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to [my earlier post on managing Apple Intelligence features on macOS Sequoia](https://derflounder.wordpress.com/2024/10/28/managing-apple-intelligence-features-on-macos-sequoia-15-1/), Apple has added a couple of new management options for Apple Intelligence now that Apple Intelligence is able to communicate with external services like ChatGPT. For more details, please see below the jump.

As of macOS 15.2, management options are available for the following [Apple Intelligence](https://developer.apple.com/apple-intelligence/) functionality:

* [Genmoji](https://bgr.com/tech/how-to-use-genmoji-ios-18/)
* [Image Playground](https://www.macrumors.com/guide/image-playground/)
* [Writing Tools](https://www.macrumors.com/guide/apple-intelligence-writing-tools/)
* [Summarizing emails](https://www.idownloadblog.com/2024/08/15/use-apple-intelligence-to-summarize-text/)
* [Enabling Siri to connect to third party cloud-based intelligence services](https://help.openai.com/en/articles/10269382-setting-up-chatgpt-with-apple-intelligence)
* [Managing non-anonymous login to third party cloud-based intelligence services](https://bgr.com/tech/apple-intelligence-offers-improved-chatgpt-privacy-but-theres-a-catch/)

The [relevant key values](https://developer.apple.com/documentation/devicemanagement/restrictions) are below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Restriction | Setting available in version | Description | Key | Key value | Default setting in macOS |
| --- | --- | --- | --- | --- | --- | --- |
|  | Allow Image Playground | macOS 15.0.0 | If key vaule is set to FALSE, prohibits the use of image generation. | allowImagePlayground | Boolean | TRUE |
|  | Allow Writing Tools | macOS 15.0.0 | If key vaule is set to FALSE, allows only anonymous access to external services | allowWritingTools | Boolean | TRUE |
|  | Allow Genmoji | macOS 15.0.0 | If key vaule is set to FALSE, disables Genmoji | allowGenmoji | Boolean | TRUE |
|  | Allow Mail Summary | macOS 15.1.0 | If key vaule is set to FALSE, prohibits the ability to create email summaries | allowMailSummary | Boolean | TRUE |
|  | Allow External Intelligence Integrations | macOS 15.2.0 | If key vaule is set to FALSE, prohibits integrations with external services including ChatGPT and Google Gemini | allowExternalIntelligenceIntegrations | Boolean | TRUE |
|  | Allow External Intelligence Sign-Ins | macOS 15.2.0 | If key vaule is set to FALSE, disables non-anonymous login to external services including ChatGPT and Google Gemini | allowExternalIntelligenceIntegrationsSignIn | Boolean | TRUE |

[view raw](https://gist.github.com/rtrouton/842f20e8c5266a46f1c00e8dc2449524/raw/2cdb661c615ad7b867699737f4eba6e7a07d8b35/Apple%20Intelligence%20profile%20information%2015%20dot%200%20through%2015%20dot%202.csv)
 [Apple Intelligence profile information 15 dot 0 through 15 dot 2.csv](https://gist.github.com/rtrouton/842f20e8c5266a46f1c00e8dc2449524#file-apple-intelligence-profile-information-15-dot-0-through-15-dot-2-csv)
hosted with ❤ by [GitHub](https://github.com)

It’s important to note that while all of the settings listed above work on macOS Sequoia 15.2, not all work on earlier versions of macOS Sequoia. Here’s the compatibility list:

**macOS 15.0 and later:**

* **allowGenmoji**
* **allowImagePlayground**
* **allowWritingTools**

**macOS 15.1 and later:**

* **allowMailSummary**

**macOS 15.2 and later:**

* **allowExternalIntelligenceIntegrations**
* **allowExternalIntelligenceIntegrationsSignIn**

These settings can be managed by a configuration profile, where setting a boolean value of **false** will disable the Apple Intelligence feature in question. Please see below for example profiles. The example profiles are also available via the following links:

* Genmoji: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableGenmoji>
* Image Playground: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableImagePlayground>
* Writing Tools: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableWritingTools>
* Summarize emails: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableMailSummary>
* Block Siri from connecting to third party cloud-based intelligence services: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableExternalIntelligenceIntegrations>
* Disable non-anonymous login to third party cloud-based intelligence services: <https://github.com/rtrouton/profiles/tree/main/AppleIntelligenceDisableExternalIntelligenceLogins>

**Note:** If you’re planning to use the example profiles with [Jamf Pro](https://www.jamf.com/jamf-pro), the profiles will need to be signed before they can be uploaded to Jamf Pro. If you’re not familiar with how to sign profiles, the post linked below is a good guide to how that process works:

<https://macblog.org/sign-configuration-profiles/>

**Genmoji**:

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
|  | <integer>1<...