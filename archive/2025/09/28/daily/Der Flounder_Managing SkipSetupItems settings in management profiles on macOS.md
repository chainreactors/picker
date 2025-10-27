---
title: Managing SkipSetupItems settings in management profiles on macOS
url: https://derflounder.wordpress.com/2025/09/27/managing-skipsetupitems-settings-in-management-profiles-on-macos/
source: Der Flounder
date: 2025-09-28
fetch_date: 2025-10-02T20:49:05.905830
---

# Managing SkipSetupItems settings in management profiles on macOS

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Managing SkipSetupItems settings in management profiles on macOS

## Managing SkipSetupItems settings in management profiles on macOS

September 27, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Apple has provided settings for suppressing various screens which appear the first time you log into a Mac and sometimes also after an OS update. In recent OS releases, [Apple has been using the following preference domain and key for this](https://developer.apple.com/documentation/devicemanagement/skipkeys):

* Preference domain: **com.apple.SetupAssistant.managed**
* Key: **SkipSetupItems**

Apple has the **SkipSetupItems** key set to [store its settings in an array](https://github.com/apple/device-management/blob/release/mdm/profiles/com.apple.SetupAssistant.managed.yaml#L134-L144), as described below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | – key: SkipSetupItems |
|  | supportedOS: |
|  | iOS: |
|  | introduced: '14.0' |
|  | macOS: |
|  | introduced: '15.0' |
|  | type: <array> |
|  | presence: optional |
|  | content: An array of strings that describe the setup items to skip. `SkipKeys` provides |
|  | a list of valid strings and their meanings. Available in iOS 14 and later, and |
|  | macOS 15 and later. |

[view raw](https://gist.github.com/rtrouton/11be85078b2cf771da9aa8743a33da5e/raw/192b6c39565c534267bdbaabc9310b1c3fc9b75f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/11be85078b2cf771da9aa8743a33da5e#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Why this is important is that the array and its list of strings is what’s being interpreted as the setting for the **SkipSetupItems** key in a management profile. This detail is important in itself because it can lead to multiple management profiles managing what macOS sees as the same setting.

In a case where you have two or more management profiles managing the same setting differently, you get what Apple calls [indeterminate or undefined behavior](https://datajar.co.uk/system-information-app-to-troubleshoot-configuration-profile-conflicts). In a situation like this, macOS may randomly choose to apply one of the settings and ignore any others, or just ignore all of the settings. For more details, please see below the jump.

As an example, you may deploy a management profile to [stop the Your Mac is Ready for FileVault screen from appearing](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/).

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/skipfilevaultsetup-1.png?w=595 "SkipFileVaultSetup.png")

In that case, there’s now a profile which is deploying the following setting in the **SkipSetupItems** array:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <key>SkipSetupItems</key> |
|  | <array> |
|  | <string>FileVault</string> |
|  | </array> |

[view raw](https://gist.github.com/rtrouton/fd652628bd80b061b7620536a3bf9a0d/raw/5a1ee22e45426800fc015c2edffc9db07c5da2ef/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/fd652628bd80b061b7620536a3bf9a0d#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Later, you may choose to deploy a management profile to [stop the Software Update Complete screen from appearing](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-tahoe/).

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/skipsoftwareupdatecompletesetup-1.png?w=595 "SkipSoftwareUpdateCompleteSetup.png")

In that case, there’s now a management profile which is deploying the following setting in the **SkipSetupItems** array:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <key>SkipSetupItems</key> |
|  | <array> |
|  | <string>UpdateCompleted</string> |
|  | </array> |

[view raw](https://gist.github.com/rtrouton/7550b9a610d4bd00c4d2c3dee7dbceb8/raw/4819894d4077e4dfa6d306c3321f572bd5ac125b/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7550b9a610d4bd00c4d2c3dee7dbceb8#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Once the second management profile to suppress the **Software Update Complete** screen has been deployed, you may now see the following behavior occurring randomly on the Macs it was deployed to:

* The **Software Update Complete** screen appearing.
* The **Your Mac is Ready for FileVault** screen appearing.
* Both the **Software Update Complete** and **Your Mac is Ready for FileVault** screens appearing.

The fix for this situation is to not deploy separate management profiles containing settings for the **SkipSetupItems** key. Instead, combine the settings into one management profile with multiple entries in the array. For example, to suppress both the **Software Update Complete** and **Your Mac is Ready for FileVault** screens, you would deploy a single management profile with the following settings in the **SkipSetupItems** array:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <key>SkipSetupItems</key> |
|  | <array> |
|  | <string>FileVault</string> |
|  | <string>UpdateCompleted</string> |
|  | </array> |

[view raw](https://gist.github.com/rtrouton/fedd64d6300b92f5f6bad3c888b4e2aa/raw/c585e414d6d7bd9b866ee405dc035ae9ff7e0c51/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/fedd64d6300b92f5f6bad3c888b4e2aa#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For macOS Tahoe 26.0, the following management profile should stop the following screens from appearing:

* [Analytics](https://derflounder.wordpress.com/2025/08/12/suppressing-the-analytics-screen-with-a-configuration-profile-on-macos-sequoia/)
* [Apple Intelligence](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/)
* [Software Update Complete](https://derflounder.wordpress.com/2025/09/26/suppressing-the-software-update-complete-screen-with-a-configuration-profile-on-macos-t...