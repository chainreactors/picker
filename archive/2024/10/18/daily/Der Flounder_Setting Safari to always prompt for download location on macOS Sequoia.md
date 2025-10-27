---
title: Setting Safari to always prompt for download location on macOS Sequoia
url: https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/
source: Der Flounder
date: 2024-10-18
fetch_date: 2025-10-06T18:49:30.326566
---

# Setting Safari to always prompt for download location on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Safari](https://derflounder.wordpress.com/category/safari/) > Setting Safari to always prompt for download location on macOS Sequoia

## Setting Safari to always prompt for download location on macOS Sequoia

October 17, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the options in Safari is to set a location for file downloads to go to. By default, this is set to the **Downloads** directory in the logged-in user’s home folder.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-17-at-9.32.png?w=595 "Screenshot 2024-10-17 at 9.32.png")

An alternative option is to set Safari to always prompt for a download location.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-17-at-9.32-1.png?w=595 "Screenshot 2024-10-17 at 9.32.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-17-at-9.44.png?w=595 "Screenshot 2024-10-17 at 9.44.png")

For those who want to set the option for Safari to always prompt for a download location, it is possible to set this on macOS Sequoia using the **com.apple.Safari.SandboxBroker** preference domain. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.Safari.SandboxBroker**
* Key: **AlwaysPromptForDownloadFolder**
* Value: Boolean

This can be set for the logged-in user using the following [defaults](https://ss64.com/mac/defaults.html) command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | defaults write com.apple.Safari.SandboxBroker AlwaysPromptForDownloadFolder -bool true |

[view raw](https://gist.github.com/rtrouton/e5e6bdf365c2a56ee648a8103d117e86/raw/9979727128b6df3ec7a702eec7991ba3b568ba4f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e5e6bdf365c2a56ee648a8103d117e86#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This setting can also be managed by a configuration profile. Please see below for an example profile:

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
|  | <string>572C7A43-A6A4-4A68-817D-352C0FD0FC72</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>572C7A43-A6A4-4A68-817D-352C0FD0FC72</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Safari Always Prompt for Download Location</string> |
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
|  | <string>5C19AE28-76ED-4B00-ABD8-B9B76EA88287</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.ManagedClient.preferences</string> |
|  | <key>PayloadUUID</key> |
|  | <string>5C19AE28-76ED-4B00-ABD8-B9B76EA88287</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadContent</key> |
|  | <dict> |
|  | <key>com.apple.Safari.SandboxBroker</key> |
|  | <dict> |
|  | <key>Forced</key> |
|  | <array> |
|  | <dict> |
|  | <key>mcx\_preference\_settings</key> |
|  | <dict> |
|  | <key>AlwaysPromptForDownloadFolder</key> |
|  | <true /> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/3bc1d3f121031649fecdd74a84f8c545/raw/a31d7f6f729ea57c3ca89b0ea3a76e1aaf1a6272/Safari%20Always%20Prompt%20for%20Download%20Location.mobileconfig)
 [Safari Always Prompt for Download Location.mobileconfig](https://gist.github.com/rtrouton/3bc1d3f121031649fecdd74a84f8c545#file-safari-always-prompt-for-download-location-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Safari](https://derflounder.wordpress.com/category/safari/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2024/10/17/setting-safari-to-always-prompt-for-download-location-on-macos-sequoia/#respond)

Δ

[Successfully run sudo commands are no longer logged by default to unified logging on macOS Sequoia](https://derflounder.wordpress.com/2024/10/18/successfully-run-sudo-commands-are-no-longer-logged-by-default-to-unified-logging-on-ma...