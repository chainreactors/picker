---
title: Managing menubar spacing using a configuration profile on macOS Tahoe
url: https://derflounder.wordpress.com/2026/06/03/managing-menubar-spacing-using-a-configuration-profile-on-macos-tahoe/
source: Der Flounder
date: 2026-06-03
fetch_date: 2026-06-04T06:30:12.596724
---

# Managing menubar spacing using a configuration profile on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Managing menubar spacing using a configuration profile on macOS Tahoe

## Managing menubar spacing using a configuration profile on macOS Tahoe

June 3, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

I noticed the following [9to5Mac](https://9to5mac.com) article by [Ben Lovejoy](https://9to5mac.com/author/benlovejoy/) and was interested to see that there was a solution for menubar spacing which could be applied using the [defaults command line tool](https://ss64.com/mac/defaults.html).:

<https://9to5mac.com/2026/05/22/how-to-stop-menu-bar-items-being-hidden-behind-the-macbook-pro-notch/>

From the article, the following commands can be used to set menubar spacing to an integer value of 8 (half the default spacing of 16):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults -currentHost write -globalDomain NSStatusItemSpacing -int 8 |
|  | /usr/bin/defaults -currentHost write -globalDomain NSStatusItemSelectionPadding -int 8 |

[view raw](https://gist.github.com/rtrouton/ef25fe16e8971ea1da6704e8a9fc9159/raw/90afe93379c28f2aec861364768fdb080d7f6c79/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/ef25fe16e8971ea1da6704e8a9fc9159#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To revert back to the default spacing of 16:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults -currentHost delete -globalDomain NSStatusItemSpacing |
|  | /usr/bin/defaults -currentHost delete -globalDomain NSStatusItemSelectionPadding |

[view raw](https://gist.github.com/rtrouton/890ef351eeba3f884663c5e2d6f9ce94/raw/92ee77bf6f917407e710d43a8d45d4d6d01dd9c0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/890ef351eeba3f884663c5e2d6f9ce94#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

**Note**: I needed to log out and log back in to see the menubar spacing changes.

These **defaults** commands are setting [user-level global preferences](https://developer.apple.com/documentation/foundation/nsglobaldomain), which are [manageable via a configuration profile](https://derflounder.wordpress.com/2023/05/12/setting-user-level-global-preferences-in-a-macos-configuration-profile/). Since this is the case, I decided to see if that meant menubar spacing is manageable via a profile. It is. For more details, please see below the jump.

The following profile matches the behavior of the **defaults** commands referenced earlier, where menubar spacing is set to an integer value of 8 (half the default spacing of 16):

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
|  | <string>9D97A4A8-932D-4317-9EF0-2322870D0C4E</string> |
|  | <key>PayloadType</key> |
|  | <string>Configuration</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>9D97A4A8-932D-4317-9EF0-2322870D0C4E</string> |
|  | <key>PayloadDisplayName</key> |
|  | <string>Set Menubar Spacing</string> |
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
|  | <key>PayloadDisplayName</key> |
|  | <string>Custom Settings</string> |
|  | <key>PayloadIdentifier</key> |
|  | <string>7D899888-256F-4E81-B890-2A7D25DA32D2</string> |
|  | <key>PayloadOrganization</key> |
|  | <string>Company Name</string> |
|  | <key>PayloadType</key> |
|  | <string>com.apple.ManagedClient.preferences</string> |
|  | <key>PayloadUUID</key> |
|  | <string>7D899888-256F-4E81-B890-2A7D25DA32D2</string> |
|  | <key>PayloadVersion</key> |
|  | <integer>1</integer> |
|  | <key>PayloadContent</key> |
|  | <dict> |
|  | <key>.GlobalPreferences</key> |
|  | <dict> |
|  | <key>Forced</key> |
|  | <array> |
|  | <dict> |
|  | <key>mcx\_preference\_settings</key> |
|  | <dict> |
|  | <key>NSStatusItemSelectionPadding</key> |
|  | <integer>8</integer> |
|  | <key>NSStatusItemSpacing</key> |
|  | <integer>8</integer> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | </dict> |
|  | </array> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/dae421cc3639f3df26505fa5741b8a28/raw/b8f99336eaf31fc343d9f4a9f060b62ff8917e8d/Set%20Menubar%20Spacing.mobileconfig)
 [Set Menubar Spacing.mobileconfig](https://gist.github.com/rtrouton/dae421cc3639f3df26505fa5741b8a28#file-set-menubar-spacing-mobileconfig)
hosted with ❤ by [GitHub](https://github.com)

Before profile installation (macOS is using default menubar spacing of 16):

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-03-at-10.34.png?w=595 "Screenshot 2026-06-03 at 10.34.png")

After profile installation (menubar spacing is set to an integer value of 8, half the default spacing):

![](https://derflounder.wordpress.com/wp-content/uploads/2026/06/screenshot-2026-06-03-at-10.35.png?w=595 "Screenshot 2026-06-03 at 10.35.png")

As with the **defaults** commands discussed earlier, I needed to log out and log back in to see the menubar spacing changes applied by the profile.

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/06/03/managing-menubar-spacing-using-a-configuration-profile-on-macos-tahoe/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2026/06/03/managing-menubar-spacing-using-a-configuration-profile-on-macos-tahoe/?share=facebook)
* [Share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2026/06/03/managing-menubar-spacing-using-a-configuration-profile-on-macos-tahoe/?share=linkedin)
* [Share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2026/06/03/managing-menubar-spacing-using-a-configuration-profile-on-macos-tahoe/?share=reddit)
* [Share on X (Opens in new window...