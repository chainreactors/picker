---
title: Disabling iPhone mirroring on macOS Sequoia
url: https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/
source: Der Flounder
date: 2024-10-29
fetch_date: 2025-10-06T18:47:59.203401
---

# Disabling iPhone mirroring on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [iPhone](https://derflounder.wordpress.com/category/iphone/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Disabling iPhone mirroring on macOS Sequoia

## Disabling iPhone mirroring on macOS Sequoia

October 28, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

[iPhone mirroring](https://support.apple.com/120421) is a new feature as of macOS Sequoia, which acts as a screen sharing method for an iPhone from a Mac. It allows the use of an iPhone from a nearby Mac by displaying the iPhone’s screen within an **iPhone Mirroring.app** window and allowing the Mac user to interact with the iPhone’s screen, including being able to access its apps and notifications.

This new screen sharing capability may not be acceptable for security reasons in all Mac environments, so Apple has provided management options for disabling the use of iPhone mirroring. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.applicationaccess**
* Key: **allowiPhoneMirroring**
* Value: Boolean

This setting can be managed by a configuration profile, where setting a boolean value of **false** will disable iPhone mirroring and prevent it from working. Please see below for an example profile. This profile is also available via the following link:

<https://github.com/rtrouton/profiles/tree/main/BlockiPhoneMirroring>

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

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [iPhone](https://derflounder.wordpress.com/category/iphone/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (2)
[Leave a comment](#respond)

1. ![Timothy's avatar](https://2.gravatar.com/avatar/e13496c1524b27ab9e58074e98d700390eda4484f90010fec848389770621527?s=32&d=identicon&r=G)

   Timothy Hellum

   October 28, 2024 at 3:00 pm

   [Reply](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?replytocom=72533#respond)

   When uploaded to JAMF the ConfigProfile example here appears empty, no payloads. Which Option should be chosen in JAMF to populate ‘allowiPhoneMirroring’ with false?
2. ![Anthony Reimer's avatar](https://0.gravatar.com/avatar/3cdc4d3349b9df1a3f22d49d4b7d9ceeaa9208ea4ce15a5d37467c8c03a8aa5e?s=32&d=identicon&r=G)

   [Anthony Reimer](http://maclabs.jazzace.ca)

   October 28, 2024 at 8:56 pm

   [Reply](https://derflounder.wordpress.com/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/?replytocom=72543#respond)

   If you upload a profile to Jamf Pro and Jamf has not yet implemented a GUI interface for those settings, it will appear that there are no payloads. If you sign the profile before uploading, it will tell Jamf Pro to not try to interpret the profile and simply push it out. Again, you may not see a payload reflected, but as long as you have correctly constructed the profile, it will apply the settings in the profile. You need to test, of course, in case there is an error in the profile, but the above profile is almost certainly OK.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2024/10/28/disabling-iphone-mirroring-on-macos-sequoia/#respond)

Δ

[Managing Apple Intelligence features on macOS Sequoia 15.1](https://derflounder.wordpress.com/2024/10/28/managing-apple-intelligence-features-on-macos-sequoia-15-1/)
[Managed Apple Accounts which were out of scope for ABM or ASM federation may be changed to be in scope by the federation process](https://derflounder.wordpress.com/2024/10/21/managed-apple-accounts-which-were-out-of-scope-for-abm-or-asm-federation-may-be-changed-to-be-in-scope-by-the-federation-process/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Su...