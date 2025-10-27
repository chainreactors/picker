---
title: macOS Ventura 13.3 alters expected behavior for Finder’s Open With functionality for macOS installer packages
url: https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/
source: Der Flounder
date: 2023-04-02
fetch_date: 2025-10-04T11:26:42.978985
---

# macOS Ventura 13.3 alters expected behavior for Finder’s Open With functionality for macOS installer packages

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Installer](https://derflounder.wordpress.com/category/installer/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > macOS Ventura 13.3 alters expected behavior for Finder’s Open With functionality for macOS installer packages

## macOS Ventura 13.3 alters expected behavior for Finder’s Open With functionality for macOS installer packages

April 1, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

I’m a frequent user of macOS’s [Open With functionality](https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac), where I can control-click on a file and select what app I want to open the file with.

![Screenshot 2023 04 01 at 5 05 04 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-5.05.04-pm.png?w=595 "Screenshot 2023-04-01 at 5.05.04 PM.png")

Among the files I’m used to doing this with are installer package files. However, I noticed that as of macOS 13.3, this mostly stopped working as the only choice I now had for installer packages was the **Installer** app. Here’s how it looks on macOS 13.2.1, on a Mac with the [Suspicious Package application](https://www.mothersruin.com/software/SuspiciousPackage/) installed:

![Screenshot 2023 04 01 at 4 24 19 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-4.24.19-pm.png?w=595 "Screenshot 2023-04-01 at 4.24.19 PM.png")

Here’s how it looks on macOS 13.3, on a Mac with the [Suspicious Package application](https://www.mothersruin.com/software/SuspiciousPackage/) installed:

![Screenshot 2023 04 01 at 4 38 03 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-4.38.03-pm.png?w=595 "Screenshot 2023-04-01 at 4.38.03 PM.png")

When I looked in a **Get Info** window for an installer package on macOS 13.3, the **Open with:** functionality was both grayed out and set to **Installer**.

![Screenshot 2023 04 01 at 4 50 43 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-4.50.43-pm.png?w=595 "Screenshot 2023-04-01 at 4.50.43 PM.png")

Normally I would have suspected a bug in macOS 13.3, but according to Randy Saldinger of Mothers Ruin Software, [this appears to be an undocumented change by Apple in macOS 13.3](https://www.mothersruin.com/software/SuspiciousPackage/faq.html#finder-open-with).

![Screenshot 2023 04 01 at 5 12 50 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-5.12.50-pm.png?w=595 "Screenshot 2023-04-01 at 5.12.50 PM.png")

For more details, please see below the jump.

As of macOS 13.3, a new [LaunchServices](https://developer.apple.com/documentation/coreservices/launch_services) key in the **CFBundleDocumentTypes** dictionary, named **LSIsAppleDefaultNoOverrideForType**, appears to have been introduced. This new key so far only appears in the following file:

**/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/Exceptions.plist**

This key is applied to all three package document types used by the **Installer** app, which means it covers all known macOS installer package files (both flat packages and bundle-style packages.)

![Screenshot 2023 04 01 at 4 47 53 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-4.47.53-pm.png?w=595 "Screenshot 2023-04-01 at 4.47.53 PM.png")

The new key appears to affect how LaunchServices manages the **Open With** functionality specifically in the context of installer packages.

There are still ways outside of the **Open With** functionality to open an installer package in a desired application. One of the ways is to use the [open command](https://scriptingosx.com/2017/02/the-macos-open-command/) in Terminal. For example, if you had an installer package named **example.pkg** stored on your desktop and you wanted to open the installer package in the **Suspicious Package** application, you could run the command below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | open -a "/Applications/Suspicious Package.app" ~/Desktop/example.pkg |

[view raw](https://gist.github.com/rtrouton/7d8cad62e494c685695b074ace91fddb/raw/ce6031d7db3dee9bbee67f3fef2a9ebc5abe5724/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/7d8cad62e494c685695b074ace91fddb#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![Screenshot 2023 04 01 at 4 41 57 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-4.41.57-pm.png?w=595 "Screenshot 2023-04-01 at 4.41.57 PM.png")

The **Suspicious Package** application should subsequently open and display information about the installer package you had specified.

![Screenshot 2023 04 01 at 4 42 43 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/04/screenshot-2023-04-01-at-4.42.43-pm.png?w=595 "Screenshot 2023-04-01 at 4.42.43 PM.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/?share=pocket)

Like Loading...

### *Related*

Categories: [Installer](https://derflounder.wordpress.com/category/installer/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (7)
[Leave a comment](#respond)

1. ![prbsparx's avatar](https://1.gravatar.com/avatar/195f285e95059d0...