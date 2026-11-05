---
title: Managing Local Network access settings on macOS Golden Gate using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2026/11/04/13554/
source: Der Flounder
date: 2026-11-04
fetch_date: 2026-11-05T08:43:23.434489
---

# Managing Local Network access settings on macOS Golden Gate using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Managing Local Network access settings on macOS Golden Gate using Blueprints in Jamf Pro

## Managing Local Network access settings on macOS Golden Gate using Blueprints in Jamf Pro

November 4, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

One of the management options Jamf Pro provides with Blueprints for macOS Golden Gate is using DDM declarations to manage Local Network access settings. On earlier versions of macOS, these settings had not been manageable and users needed to click **Allow** or **Don’t Allow** when prompted.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/11/screenshot-2026-11-02-at-3.50.05pm.png?w=595 "Screenshot 2026-11-02 at 3.50.05 PM.png")

On macOS Golden Gate, these settings can be managed for specified apps using the privacy permissions available via the [App Settings DDM declaration](https://developer.apple.com/documentation/devicemanagement/appsettings). The user will still be prompted to allow the requested privacy permissions, but now you can provide more information to the user as to why they should approve the privacy permission change. For more details, please see below the jump.

The **App Settings** declaration is managed on macOS at the user level, which like with user-level MDM profiles, means that [they can be applied only to MDM-managed users](https://derflounder.wordpress.com/2025/04/04/identifying-mdm-managed-user-accounts-on-macos-sequoia/). When dealing with local accounts, this means that only the local user account which installs the MDM enrollment profile becomes the MDM-managed user. For our purposes here, this means that the management declarations used for Local Network access settings can only be applied to the MDM-managed user and any other local accounts on the Mac cannot have their Local Network access settings managed.

In this example, I’m choosing to manage the Local Network access settings for [Cyberduck](https://cyberduck.io), which is a free, open-source file transfer client and cloud storage browser available for macOS.

As of Jamf Pro 11.33.3, there is not a Blueprints template available for creating blueprints which manage Local Network access settings so the blueprint will need to be configured manually. To do this, use the following procedure:

1. Log into Jamf Pro.

2. Select Blueprints

3. Click the **Create blueprint** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/11/screenshot-2026-11-03-at-3.30.png?w=595 "Screenshot 2026-11-03 at 3.30.png")

4. You should see an unconfigured Blueprint. Click where it says **Untitled blueprint** and provide a name.

For this example, I’m using **Local Network Access Management Settings**.

5. Scroll down in the list on the left-hand side of the browser window to locate the **App Settings** component.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/11/screenshot-2026-11-03-at-3.31.png?w=595 "Screenshot 2026-11-03 at 3.31.png")

6. Click on the **App Settings** component and drag the **App Settings** component to the **Components in this blueprint** section.

![App Settings Drag and Drop.](https://derflounder.wordpress.com/wp-content/uploads/2026/11/app-settings-drag-and-drop.gif?w=595 "App Settings Drag and Drop.gif")

7. Once added to the **Components in this blueprint** section, click anywhere on the **App Settings** component to open it for editing.

8. At this point, you will see the **App Settings** settings. From there, scroll down to the **App privacy** section and click the **Configure** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/11/screenshot-2026-11-03-at-3.39.png?w=595 "Screenshot 2026-11-03 at 3.39.png")

9. Click the **Add key** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/11/screenshot-2026-11-03-at-3.39-1.png?w=595 "Screenshot 2026-11-03 at 3.39.png")

For the **Key name** section, you will need to get the following information:

* The bundle identifier for the app in question
* The code signing information for the app in question

**Note:** The app in question must be code signed. The **App Privacy** settings use the [Designated Requirement code signature information](https://developer.apple.com/library/archive/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919-CH1-TNTAG6) to identify the app.

To get the relevant code signature information, you would run a command similar to the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | codesign -d -r - /path/to/app\_goes\_here |

[view raw](https://gist.github.com/rtrouton/9be8ca0f9a8f499bd26614c4bd0428de/raw/57ae5063f2fa051f03abc238c764eede2c1bb0ff/gistfile1.txt)
[gistfile1.txt](https://gist.github.com/rtrouton/9be8ca0f9a8f499bd26614c4bd0428de#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For our example, the **Cyberduck** app is installed in the **Applications** directory. In that case, you would run the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | codesign -d -r - "/Applications/Cyberduck.app" |

[view raw](https://gist.github.com/rtrouton/42d854bd521129ee5f8a4cdadff97262/raw/ae7a65d4da043a953c181df3523b6356de84d4b8/gistfile1.txt)
[gistfile1.txt](https://gist.github.com/rtrouton/42d854bd521129ee5f8a4cdadff97262#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

That should provide output similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@ZYKWPPFHQ ~ % codesign -d -r - "/Applications/Cyberduck.app" |
|  | Executable=/Applications/Cyberduck.app/Contents/MacOS/Cyberduck |
|  | designated => (anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.9] /\* exists \*/ or anchor apple generic and certificate 1[field.1.2.840.113635.100.6.2.6] /\* exists \*/ and certificate leaf[field.1.2.840.113635.100.6.1.13] /\* exists \*/ and certificate leaf[subject.OU] = G69SCX94XU) and identifier "ch.sudo.cyberduck" |
|  | username@ZYKWPPFHQ ~ % |

[view raw](https://gist.github.com/rtrouton/2869b086dd2e975d74e8869fee319eda/raw/9388f9c47016657f6b9c3b3bdce634a350b3473a/gistfile1.txt)
[gistfile1.txt](https://gist.github.com/rtrouton/2869b086dd2e975d74e8869fee319eda#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

From this, we need the bundle...