---
title: Using Self Service+ as a privilege elevation tool
url: https://derflounder.wordpress.com/2026/02/18/using-self-service-as-a-privilege-elevation-tool/
source: Der Flounder
date: 2026-02-18
fetch_date: 2026-02-19T04:12:49.295611
---

# Using Self Service+ as a privilege elevation tool

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Self Service+](https://derflounder.wordpress.com/category/self-service/) > Using Self Service+ as a privilege elevation tool

## Using Self Service+ as a privilege elevation tool

February 18, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of developing [Self Service+](https://learn.jamf.com/en-US/bundle/self-service-plus-documentation/page/About_Self_Service_Plus.html), [Jamf](https://www.jamf.com/) built in functionality which originally came from their [Jamf Connect](https://www.jamf.com/products/jamf-connect/) tool. Among the functionality added to the **Self Service+** app is Jamf Connect’s ability to serve as a privilege elevation tool. This means that **Self Service+** can be used as a privilege elevation tool for those shops who are interested in providing and managing admin privileges to standard user accounts on macOS. For more details, please see below the jump.

One thing that’s important to know is that this privilege elevation functionality will not manage an account which already has admin privileges. It is designed to manage an account which has standard user privileges, by promoting that account to have admin privileges and then (if configured to do so) demote that account back to having standard user privileges. Jamf has documentation available which covers this topic, which is available via the link below:

<https://learn.jamf.com/en-US/bundle/jamf-connect-documentation-current/page/Privilege_Elevation_Local_Accounts.html>

The privilege elevation settings are documented here:

<https://learn.jamf.com/en-US/bundle/jamf-connect-documentation-current/page/Menu_Bar_App_Preferences.html#reference-7936>

Some of the privilege elevation functionality is dependent on Jamf Connect and an [identity provider](https://en.wikipedia.org/wiki/Identity_provider), but there are several settings which can be set independently for **Self Service+** and do not depend on Jamf Connect or an identity provider:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Management key | What it does | Value |
| --- | --- | --- | --- |
|  | TemporaryUserPromotion | Enables the feature for user promotion in Self Service+ | Boolean |
|  | UserPromotionTimer | Enables the feature for user promotion in Self Service+ | Boolean |
|  | UserPromotionDuration | Duration in minutes for user to be promoted | Integer |
|  | UserPromotionLimit | Enforces a maximum number of times that a user can request rights in one calendar month | Integer |
|  | UserPromotionReason | Requires the user to provide a reason for promotion which will be recorded in system logs | boolean |
|  | UserPromotionChoices | A list of default reasons for promotion. An 'other' field will be provided automatically with a 200 character maximum input limit. | Array |
|  | UserPromotionBiometrics | Require users to use Touch ID as a form of authentication prior to a temporary elevation session | Boolean |
|  | URLCommandLineElevation | Restricts users from using the privilege elevation feature through the command-line interface or URL schemes | Boolean |

[view raw](https://gist.github.com/rtrouton/b346909b118898bcf849e396f908cb65/raw/34d0b36dc59a5ca13e137eaf7ac303aa7ca6208d/SelfServicePlusPrivilegeElevation.csv)
 [SelfServicePlusPrivilegeElevation.csv](https://gist.github.com/rtrouton/b346909b118898bcf849e396f908cb65#file-selfserviceplusprivilegeelevation-csv)
hosted with ❤ by [GitHub](https://github.com)

For example, you can configure **Self Service+** to act as a privilege elevation tool for standard users with the following settings configured:

* Standard users can elevate to having admin privileges using the **Self Service+** menubar icon.
* Elevated users will be demoted back to standard user privileges after fifteen minutes.
* User will see a countdown clock appearing in the **Self Service+** menubar icon.
* Elevated users can choose to be demoted back to standard user privileges before the fifteen minute deadline using the **Self Service+** menubar icon.

The profile shown below will enforce these settings:

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
|  | <string>41B2AEAE-34D4-49A7-96EB-8E6D151911B6</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>41B2AEAE-34D4-49A7-96EB-8E6D151911B6</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Self Service+ Privilege Elevation Management</string> |
|  | <key>PayloadDescription</key> |
|  | <string>Configure Self Service+ to enable privilege elevation management</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadEnabled</key> |
|  | <true/> |
|  | <key>PayloadRemovalDisallowed</key> |
|  | <false/> |
|  | <key>PayloadScope</key> |
|  | <string>System</string> |
|  | <key>PayloadContent</key> |
|  | <array> |
|  | <dict> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Custom Settings</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>D7CA074E-C112-4B53-9E4C-9FBE8F429351</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.ManagedClient.preferences</string> |
|  | <key>PayloadUUID</key> |
|  | <string>D7CA074E-C112-4B53-9E4C-9FBE8F429351</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadContent</key> |
|  | <dict> |
|  | <key>com.jamf.connect</key> |
|  | <dict> |
|  | <key>Forced</key> |
|  | <array> |
|  | <dict> |
|  | <key>mcx\_preference\_settings</key> |
|  | <dict> |
|  | <key>TemporaryUserPermissions</key> |
|  | <dict> |
|  | <key>TemporaryUserPromotion</key> |
|  | <true/> |
|  | <key>UserPromotionTimer</key> |
|  | <true/> |
|  | <key>UserPromotionDuration</key> |
|  | <integer>15</integer> |
|  | </dict> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/fc01d000d8bd2e3e5468bcf044239c65/raw/627adf16016aa9c369764f42759c79decb9752a6/SelfService%2BPrivilegeElevationManagement.mobileconfig)
 [SelfService+PrivilegeElevationManagement.mobileconfig](https://gist.github.com/rtrouton/fc01d000d8bd2e3e5468bcf044239c65#file-selfservice-privilegeelevationmanagement-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

Here’s how this looks for a logged-in standard user on macOS Tahoe 26.3.0 with the **Self Service+**...