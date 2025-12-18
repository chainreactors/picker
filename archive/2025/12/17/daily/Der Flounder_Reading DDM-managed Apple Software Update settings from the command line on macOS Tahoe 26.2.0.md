---
title: Reading DDM-managed Apple Software Update settings from the command line on macOS Tahoe 26.2.0
url: https://derflounder.wordpress.com/2025/12/17/reading-ddm-managed-apple-software-update-settings-from-the-command-line-on-macos-tahoe-26-2-0/
source: Der Flounder
date: 2025-12-17
fetch_date: 2025-12-18T03:19:27.980833
---

# Reading DDM-managed Apple Software Update settings from the command line on macOS Tahoe 26.2.0

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Reading DDM-managed Apple Software Update settings from the command line on macOS Tahoe 26.2.0

## Reading DDM-managed Apple Software Update settings from the command line on macOS Tahoe 26.2.0

December 17, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the challenges with reporting on DDM settings is that as of macOS Tahoe 26.2.0 there aren’t currently command line tools available which can report back on settings which are managed via DDM declarations. [You can see the settings which have been applied on the managed Mac via System Settings](https://derflounder.wordpress.com/2025/05/29/displaying-ddm-deployed-settings-on-macos-sequoia/), but so far that’s about it. However, in some cases, Apple is writing information for some DDM declarations to files which are readable by command line tools. I recently discovered that one of those declarations was the [com.apple.configuration.softwareupdate.settings](https://github.com/apple/device-management/blob/release/declarative/declarations/configurations/softwareupdate.settings.yaml) Software Update Settings declaration. For more details, please see below the jump.

I have [an earlier post on the Software Update Settings declaration and how it is used by Jamf Pro’s Blueprints](https://derflounder.wordpress.com/2025/06/24/deploying-software-update-management-using-blueprints-in-jamf-pro/). Using that information, I built and deployed a Software Update Settings declaration which has the following settings:

* Standard users can’t install Apple software updates
* Logged-in users will see all software update notifications
* OS updates will be automatically downloaded
* OS updates will be automatically installed
* Security updates will be automatically installed
* Rapid Security Response updates will be installed
* Rapid Security Response updates can be removed

Once deployed to managed Macs, you should be able to verify these settings by looking at the **Software Update Settings** declaration’s listing in System Settings.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-17-at-9.50.13am.png?w=595 "Screenshot 2025-12-17 at 9.50.13 AM.png")

You can also verify them by checking the following file:

**/var/db/softwareupdate/SoftwareUpdateDDMStatePersistence.plist**

On a managed Mac with those DDM settings running macOS Tahoe 26.2.0, the **SoftwareUpdateDDMStatePersistence.plist** file should show information similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>SUCorePersistedStateContentsType</key> |
|  | <string>SoftwareUpdateCorePersistedStateFile</string> |
|  | <key>SUCorePersistedStateCoreFields</key> |
|  | <dict/> |
|  | <key>SUCorePersistedStateCoreSecureCodedObjectsFields</key> |
|  | <dict/> |
|  | <key>SUCorePersistedStateCoreVersion</key> |
|  | <string>2.1.0</string> |
|  | <key>SUCorePersistedStatePolicyFields</key> |
|  | <dict> |
|  | <key>SUCoreDDMDeclarationGlobalSettings</key> |
|  | <dict> |
|  | <key>adminInstallRequired</key> |
|  | <integer>1</integer> |
|  | <key>automaticallyDownload</key> |
|  | <integer>1</integer> |
|  | <key>automaticallyInstallOSUpdates</key> |
|  | <integer>1</integer> |
|  | <key>automaticallyInstallSystemAndSecurityUpdates</key> |
|  | <integer>1</integer> |
|  | <key>enableGlobalNotifications</key> |
|  | <true/> |
|  | <key>enableRapidSecurityResponse</key> |
|  | <true/> |
|  | <key>enableRapidSecurityResponseRollback</key> |
|  | <true/> |
|  | <key>serializedKeys</key> |
|  | <array> |
|  | <string>com.apple.RemoteManagement.SoftwareUpdateExtension.GlobalSettings/811362F1-10F1-4D2F-BFB7-F97393F3F44C:Qmx1ZXByaW50XzM3MTllZWRlLTI0MjUtNGE2ZC04YjljLTIyMGViMzMwYWQ2NF9zMV9jMV9zeXNfY2ZnMQ==.NDg5NTdiNjZkYmUwMWM3YzM2MzcwMTJjNTkxZTg4MWM1ZDk3YTNkMWUxZTI1MjI0NTYwMmJlNjQ0MTFmYjdkOA==</string> |
|  | </array> |
|  | </dict> |
|  | </dict> |
|  | <key>SUCorePersistedStatePolicySecureCodedObjectsFields</key> |
|  | <dict/> |
|  | <key>SUCorePersistedStatePolicyVersion</key> |
|  | <string>1.0</string> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/21b0d5e08d7731d4e23758c0403fee74/raw/c0890a7c103bf880be8352d3482ae15357fb2afb/SoftwareUpdateDDMStatePersistence.plist)
 [SoftwareUpdateDDMStatePersistence.plist](https://gist.github.com/rtrouton/21b0d5e08d7731d4e23758c0403fee74#file-softwareupdateddmstatepersistence-plist)
hosted with ❤ by [GitHub](https://github.com)

From there, you can use tools like [PlistBuddy](https://www.manpagez.com/man/8/PlistBuddy/) to read the values stored in the **/var/db/softwareupdate/SoftwareUpdateDDMStatePersistence.plist** file. For example, the following command should read the value for the **enableRapidSecurityResponse** key from the **SoftwareUpdateDDMStatePersistence.plist** file.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/libexec/PlistBuddy -c "Print :SUCorePersistedStatePolicyFields:SUCoreDDMDeclarationGlobalSettings:enableRapidSecurityResponse" /var/db/softwareupdate/SoftwareUpdateDDMStatePersistence.plist |

[view raw](https://gist.github.com/rtrouton/9f834460692ecd6a782f9b11d37e83cd/raw/2bfa2275f143e6dd0a1f1ef504855bc2fcb01453/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9f834460692ecd6a782f9b11d37e83cd#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If Rapid Security Response updates are set to be installed, that should give you a value of **true**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@Z6WCW076MR ~ % /usr/libexec/PlistBuddy -c "Print :SUCorePersistedStatePolicyFields:SUCoreDDMDeclarationGlobalSettings:enableRapidSecurityResponse" /var/db/softwareupdate/SoftwareUpdateDDMStatePersistence.plist |
|  | true |
|  | username@Z6WCW076MR ~ % |

[view raw](https://gist.github.com/rtrouton/3d25cfdd0e7c172db41db9c945f3efa3/raw/147c75c26c936321a2feade6752580f01cbb22a0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3d25cfdd0e7c172db41db9c945f3efa3#file-gistfile1-txt)
hosted with ...