---
title: Opening macOS Ventura’s System Settings to desired locations via the command line
url: https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/
source: Der Flounder
date: 2022-10-26
fetch_date: 2025-10-03T20:52:27.595276
---

# Opening macOS Ventura’s System Settings to desired locations via the command line

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Opening macOS Ventura’s System Settings to desired locations via the command line

## Opening macOS Ventura’s System Settings to desired locations via the command line

October 25, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

With the release of macOS Ventura, the **System Preferences** application has been replaced with the **System Settings** application.

macOS Monterey System Preferences:

![Screen Shot 2022 10 25 at 3 08 11 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screen-shot-2022-10-25-at-3.08.11-pm.png?w=600&h=510 "Screen Shot 2022-10-25 at 3.08.11 PM.png")

macOS Ventura System Settings:

![Screenshot 2022 10 25 at 3 10 04 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/10/screenshot-2022-10-25-at-3.10.04-pm.png?w=599&h=524 "Screenshot 2022-10-25 at 3.10.04 PM.png")

Along with this change, a number of previously-known commands for [opening individual System Preferences preference panes from the command line](https://apple.stackexchange.com/questions/227002/open-preference-pane-from-command-line-on-el-capitan-mac-os-x-10-11) no longer work with System Settings.

However, it looks like the underlying command line functionality wasn’t changed by Apple. You just need to know what the new options are to enter. For more details, please see below the jump.

I’ve put together a list of the ones I’ve found to work, which is available below. Find any more? Please let me know in the comments:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | Open Storage, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.settings.Storage |
|  |  |
|  |  |
|  | Open Software Update, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Software-Update-Settings.extension |
|  |  |
|  |  |
|  | Open General, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.systempreferences.GeneralSettings |
|  |  |
|  |  |
|  | Open Privacy & Security, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.preference.security |
|  |  |
|  |  |
|  | Open Privacy & Security, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.settings.PrivacySecurity.extension |
|  |  |
|  |  |
|  | Open Startup Disk, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.preference.startupdisk |
|  |  |
|  |  |
|  | Open Startup Disk, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Startup-Disk-Settings.extension |
|  |  |
|  |  |
|  | Open Displays, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.preference.displays |
|  |  |
|  |  |
|  | Open Wallpaper, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Wallpaper-Settings.extension |
|  |  |
|  |  |
|  | Open Network, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.preference.network |
|  |  |
|  |  |
|  | Open Network, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Network-Settings.extension |
|  |  |
|  |  |
|  | Open Profiles, in System Settings: Privacy & Security: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Profiles-Settings.extension |
|  |  |
|  |  |
|  | Open Transfer or Reset, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Transfer-Reset-Settings.extension |
|  |  |
|  |  |
|  | Open Date & Time, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Date-Time-Settings.extension |
|  |  |
|  |  |
|  | Open About, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.SystemProfiler.AboutExtension |
|  |  |
|  |  |
|  | Open Language & Region, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Localization-Settings.extension |
|  |  |
|  |  |
|  | Open Login Items, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.LoginItems-Settings.extension |
|  |  |
|  |  |
|  | Open Sharing, in System Settings: General: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Sharing-Settings.extension |
|  |  |
|  |  |
|  | Open AirDrop & Handoff, in System Settings: General |
|  |  |
|  | open x-apple.systempreferences:com.apple.AirDrop-Handoff-Settings.extension |
|  |  |
|  |  |
|  | Open Time Machine, in System Settings: General |
|  |  |
|  | open x-apple.systempreferences:com.apple.Time-Machine-Settings.extension |
|  |  |
|  |  |
|  | Open Appearance, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.Appearance-Settings.extension |
|  |  |
|  |  |
|  | Open Apple ID, in System Settings: |
|  |  |
|  | open x-apple.systempreferences:com.apple.preferences.AppleIDPrefPane |

[view raw](https://gist.github.com/rtrouton/87806d7ccdd8db1be2836fd7613b2e63/raw/5f8b19b36186a90205fa1ec7cb657984fa7b09c2/Open%20Ventura%20System%20Settings%20to%20desired%20locations.txt)
 [Open Ventura System Settings to desired locations.txt](https://gist.github.com/rtrouton/87806d7ccdd8db1be2836fd7613b2e63#file-open-ventura-system-settings-to-desired-locations-txt)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2022/10/25/opening-macos-venturas-system-settings-to-desired-locations-via-the-command-line/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress...