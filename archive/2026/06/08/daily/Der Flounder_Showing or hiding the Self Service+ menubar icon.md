---
title: Showing or hiding the Self Service+ menubar icon
url: https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/
source: Der Flounder
date: 2026-06-08
fetch_date: 2026-06-09T06:02:12.569390
---

# Showing or hiding the Self Service+ menubar icon

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Self Service+](https://derflounder.wordpress.com/category/self-service/) > Showing or hiding the Self Service+ menubar icon

## Showing or hiding the Self Service+ menubar icon

June 8, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

[Self Service+ 2.23.0](https://learn.jamf.com/r/en-US/self-service-plus-documentation/2.23.0) (released on June 8 2026) includes new options for customizing how **Self Service+** appears to users. The documentation for these options is available via the following links:

* **Configuring Self Service+ Administrator Controls**: <https://learn.jamf.com/r/en-US/self-service-plus-documentation/Configuring_Self_Service_Administrator_Controls>
* **Administrator Controls Configuration Profile Example**: <https://learn.jamf.com/r/en-US/self-service-plus-documentation/Administrator_Controls_Configuration_Profile_Example>

One of the customization options called out in the [release notes for Self Service+ 2.23.0](https://learn.jamf.com/r/en-US/self-service-plus-documentation/2.23.0) is whether or not the Self Service+ menubar icon is visible in the menubar.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-08-at-1.44.png?w=595 "Screenshot 2026-06-08 at 1.44.png")

For more details, please see below the jump.

You can use the new **Self Service+** administrator controls to configure the **Self Service+** menubar icon to be hidden using a configuration profile. The example profile shown below includes the necessary settings to enforce hiding the **Self Service+** menubar icon:

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
|  | <string>D084BA94-E07D-4C1E-B531-6AF823E48F18</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>D084BA94-E07D-4C1E-B531-6AF823E48F18</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Self Service+ Hide Menubar Icon</string> |
|  | <key>PayloadDescription</key> |
|  | <string>Configure Self Service+ to hide the menubar icon</string> |
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
|  | <string>9B98E43D-82D2-49E6-99BD-3A9D9B485370</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.ManagedClient.preferences</string> |
|  | <key>PayloadUUID</key> |
|  | <string>9B98E43D-82D2-49E6-99BD-3A9D9B485370</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadContent</key> |
|  | <dict> |
|  | <key>group.com.jamf.selfserviceplus</key> |
|  | <dict> |
|  | <key>Forced</key> |
|  | <array> |
|  | <dict> |
|  | <key>mcx\_preference\_settings</key> |
|  | <dict> |
|  | <key>blueprint</key> |
|  | <dict> |
|  | <key>configs</key> |
|  | <dict> |
|  | <key>connect</key> |
|  | <dict> |
|  | <key>HideMenubarIcon</key> |
|  | <true/> |
|  | </dict> |
|  | </dict> |
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

[view raw](https://gist.github.com/rtrouton/62c2543a2a1b375588caec78918717a3/raw/0e1d322e8440e8cd048f0754e841346837227d8b/SelfService%2BHideMenubarIcon.mobileconfig)
 [SelfService+HideMenubarIcon.mobileconfig](https://gist.github.com/rtrouton/62c2543a2a1b375588caec78918717a3#file-selfservice-hidemenubaricon-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

Before the profile’s installation, the **Self Service+** icon appears in the menubar.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-08-at-1.45.png?w=595 "Screenshot 2026-06-08 at 1.45.png")

Once the profile is installed, the the **Self Service+** icon no longer appears in the menubar.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-08-at-1.56.png?w=595 "Screenshot 2026-06-08 at 1.56.png")

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/?share=reddit)
* [Share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/?share=twitter)
* [Share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/?share=pinterest)
* [Share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/?share=tumblr)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Self Service+](https://derflounder.wordpress.com/category/self-service/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2026/06/08/showing-or-hiding-the-self-service-menubar-icon/#respond)

Δ

[MDM-based Software Update management options no longer work on all Apple 27.0 operating systems](https://derflounder.wordpress.com/2026/06/08/mdm-based-software-update-management-options-no-longer-work-on-all-apple-27-0-operating-systems/)
[Managing menubar spacing using a configuration profile on macOS Tahoe](https://derflounder.wordpress.com/2026/06/03/managing-menubar-spacing-using-a-configuration-profile-on-macos-tahoe/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpres...