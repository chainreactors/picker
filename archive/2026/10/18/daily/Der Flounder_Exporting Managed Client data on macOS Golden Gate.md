---
title: Exporting Managed Client data on macOS Golden Gate
url: https://derflounder.wordpress.com/2026/10/18/exporting-managed-client-data-on-macos-golden-gate/
source: Der Flounder
date: 2026-10-18
fetch_date: 2026-10-19T07:07:12.081173
---

# Exporting Managed Client data on macOS Golden Gate

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Exporting Managed Client data on macOS Golden Gate

## Exporting Managed Client data on macOS Golden Gate

October 18, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

On macOS, you can access and read which managed preference settings are currently being applied to a particular Mac. This information is available in the following ways:

1. Viewing the contents of the **Managed Client** section of **System Information.app**
2. Using the [system\_profiler command line tool](https://www.manpagez.com/man/8/system_profiler/) to view the **SPManagedClientDataType** data type’s data.

These managed preference settings are reported in the following way:

* The [preference domain](https://developer.apple.com/documentation/devicemanagement/managedpreferences)
* The setting’s key
* The setting key’s value (as text)
* Whether it applies to the computer or to a user
* How often it is enforced.

Here’s an example of how the **Managed Client** section appears in the **System Information** app:

![](https://derflounder.wordpress.com/wp-content/uploads/2026/10/screenshot-2026-10-18-at-2.52.21pm.png?w=595 "Screenshot 2026-10-18 at 2.52.21 PM.png")

Here’s an example of the output from the **system\_profiler** command line tool when displaying the **SPManagedClientDataType** data:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@ZCDP1X75FT ~ % /usr/sbin/system\_profiler SPManagedClientDataType |
|  | Managed Client: |
|  |  |
|  | com.apple.gamed: |
|  |  |
|  | GKFeatureGameCenterMultiplayerOtherPlayerTypesAllowed: |
|  |  |
|  | Value: 2 |
|  | State: always |
|  | Source: com.apple.gamed (User) |
|  |  |
|  | PayloadUUID: |
|  |  |
|  | Value: 7BE22222-B233-4C44-9D55-000000000010 |
|  | State: always |
|  | Source: com.apple.gamed (User) |
|  |  |
|  | com.apple.appstore: |
|  |  |
|  | RestrictPurchaseLimit: |
|  |  |
|  | Value: 1000 |
|  | State: always |
|  | Source: com.apple.appstore (User) |
|  |  |
|  | PayloadUUID: |
|  |  |
|  | Value: 7BE22222-B233-4C44-9D55-000000000060 |
|  | State: always |
|  | Source: com.apple.appstore (User) |
|  |  |
|  | com.apple.familycontrols.contentfilter: |
|  |  |
|  | PayloadUUID: |
|  |  |
|  | Value: 7BE22222-B233-4C44-9D55-000000000070 |
|  | State: always |
|  | Source: com.apple.familycontrols.contentfilter (User) |
|  |  |
|  | limitWebProxies: |
|  |  |
|  | Value: 0 |
|  | State: always |
|  | Source: com.apple.familycontrols.contentfilter (User) |
|  |  |
|  | com.apple.iTunes: |
|  |  |
|  | moviesLimit: |
|  |  |
|  | Value: 1000 |
|  | State: always |
|  | Source: com.apple.iTunes (User) |
|  |  |
|  | restrictTVShows: |
|  |  |
|  | Value: 1 |
|  | State: always |
|  | Source: com.apple.iTunes (User) |
|  |  |
|  | tvShowsLimit: |
|  |  |
|  | Value: 1000 |
|  | State: always |
|  | Source: com.apple.iTunes (User) |
|  |  |
|  | restrictMovies: |
|  |  |
|  | Value: 1 |
|  | State: always |
|  | Source: com.apple.iTunes (User) |
|  |  |
|  | PayloadUUID: |
|  |  |
|  | Value: 7BE22222-B233-4C44-9D55-000000000020 |
|  | State: always |
|  | Source: com.apple.iTunes (User) |
|  |  |
|  | username@ZCDP1X75FT ~ % |

[view raw](https://gist.github.com/rtrouton/fe1467974badeec6baa1c51c7d248d83/raw/fd6a95ee4d0f61b4b42c3ff461628d4f33b7f9d8/Terminal%20Saved%20Output3.txt)
 [Terminal Saved Output3.txt](https://gist.github.com/rtrouton/fe1467974badeec6baa1c51c7d248d83#file-terminal-saved-output3-txt)
hosted with ❤ by [GitHub](https://github.com)

It is possible to export this information using the **system\_profiler** command line tool and work with the exported information. For more details, please see below the jump.

It is possible to use the **system\_profiler** command line tool to export the **SPManagedClientDataType** data type’s data in either XML or JSON format. To display the data in XML format, you would use the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/system\_profiler SPManagedClientDataType -xml |

[view raw](https://gist.github.com/rtrouton/13465e903be1ea295228bf1619569807/raw/4cc4c7f0e65c9f2f2919ba932bb3b9f032d8260a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/13465e903be1ea295228bf1619569807#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The output should look similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@ZCDP1X75FT ~ % /usr/sbin/system\_profiler SPManagedClientDataType -xml |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <array> |
|  | <dict> |
|  | <key>\_SPCommandLineArguments</key> |
|  | <array> |
|  | <string>/usr/sbin/system\_profiler</string> |
|  | <string>-nospawn</string> |
|  | <string>-xml</string> |
|  | <string>SPManagedClientDataType</string> |
|  | <string>-detailLevel</string> |
|  | <string>full</string> |
|  | </array> |
|  | <key>\_SPCompletionInterval</key> |
|  | <real>0.025364995002746582</real> |
|  | <key>\_SPResponseTime</key> |
|  | <real>0.041681051254272461</real> |
|  | <key>\_dataType</key> |
|  | <string>SPManagedClientDataType</string> |
|  | <key>\_detailLevel</key> |
|  | <integer>1</integer> |
|  | <key>\_items</key> |
|  | <array> |
|  | <dict> |
|  | <key>\_items</key> |
|  | <array> |
|  | <dict> |
|  | <key>\_name</key> |
|  | <string>GKFeatureGameCenterMultiplayerOtherPlayerTypesAllowed</string> |
|  | <key>data\_keyValue</key> |
|  | <string>2</string> |
|  | <key>data\_source</key> |
|  | <string>com.apple.gamed (User)</string> |
|  | <key>data\_state</key> |
|  | <string>always</string> |
|  | </dict> |
|  | <dict> |
|  | <key>\_name</key> |
|  | <string>PayloadUUID</string> |
|  | <key>data\_keyValue</key> |
|  | <string>7BE22222-B233-4C44-9D55-000000000010</string> |
|  | <key>data\_source</key> |
|  | <string>com.apple.gamed (User)</string> |
|  | <key>data\_state</key> |
|  | <string>always</string> |
|  | </dict> |
|  | </array> |
|  | <key>\_name</key> |
|  | <string>com.apple.gamed</string> |
|  | </dict> |
|  | <dict> |
|  | <key>\_items</key> |
|  | <array> |
|  | <dict> |
|  | <key>\_name</key> |
|  | <string>RestrictPurchaseLimit</string> |
|  | <key>data\_keyValue</key> ...