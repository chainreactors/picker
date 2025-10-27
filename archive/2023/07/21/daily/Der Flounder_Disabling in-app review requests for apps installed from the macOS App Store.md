---
title: Disabling in-app review requests for apps installed from the macOS App Store
url: https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/
source: Der Flounder
date: 2023-07-21
fetch_date: 2025-10-04T11:50:59.454463
---

# Disabling in-app review requests for apps installed from the macOS App Store

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Disabling in-app review requests for apps installed from the macOS App Store

## Disabling in-app review requests for apps installed from the macOS App Store

July 20, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

I was recently asked to look into how to disable in-app review requests for apps being deployed from the macOS App Store or VPP.

![Screenshot 2023 07 17 at 08 10 29](https://derflounder.wordpress.com/wp-content/uploads/2023/07/screenshot-2023-07-17-at-08.10.29.png?w=299&h=111 "Screenshot 2023-07-17 at 08.10.29.png")

After some digging, I was able to find what preference domain and key controlled this. In the macOS App Store app’s **Settings**, it is the **In-Apps Ratings & Reviews** setting.

![Screenshot 2023 07 20 at 4 04 52 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/07/screenshot-2023-07-20-at-4.04.52-pm.png?w=300&h=236 "Screenshot 2023-07-20 at 4.04.52 PM.png")

The relevant preference domain and key are below:

* Domain: **com.apple.appstore**
* Key: **InAppReviewEnabled**

This setting can be managed via the following **defaults** command run as the logged-in user:

* To enable the **In-Apps Ratings & Reviews** setting in the App Store app:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write com.apple.appstore InAppReviewEnabled -bool true |

[view raw](https://gist.github.com/rtrouton/0aa67520d17399a39bb473989faab6ab/raw/3f1d37f106589f96eb7acfc87a1212ba8209ef14/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0aa67520d17399a39bb473989faab6ab#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

* To disable the **In-Apps Ratings & Reviews** setting in the App Store app:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write com.apple.appstore InAppReviewEnabled -bool false |

[view raw](https://gist.github.com/rtrouton/8052b6162948bfd3900a7f7578a966dc/raw/69c3dbac3b4a24f8a3b1451cf11ffcf1003cffda/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8052b6162948bfd3900a7f7578a966dc#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

At this time, this setting does not appear to be manageable using a configuration profile. I’ve filed a bug report with Apple about this. For this who want to also report this and want a reference, it is Feedback ID FB12691822.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (3)
[Leave a comment](#respond)

1. ![tree_frog's avatar](https://0.gravatar.com/avatar/012185082d0175788fb317a89c620ccf63b61f6977170e01906b046f9dca0b76?s=32&d=identicon&r=G)

   tree\_frog

   August 22, 2023 at 6:27 pm

   [Reply](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?replytocom=71863#respond)

   The correct bundle id is com.apple.AppStore (note the capitalization).

   * ![rtrouton's avatar](https://0.gravatar.com/avatar/fb809ae714f8d9d5be5d4c0d7086f9bb3781e9ccdd25cf8b3aa24b140a641e0e?s=32&d=identicon&r=G)

     [rtrouton](http://www.taomechworks.net)

     August 22, 2023 at 7:21 pm

     [Reply](https://derflounder.wordpress.com/2023/07/20/disabling-in-app-review-requests-for-apps-installed-from-the-macos-app-store/?replytocom=71864#respond)

     I re-checked this and while the bundle ID for the App Store app is “com.apple.AppStore” the relevant preference domain appears to be “com.apple.appstore”. In my testing, if you try using “AppStore” in place of “appstore” in the defaults commands above, the setting in question does not change.

     + ![tree_frog's avatar](https://0.gravatar.com/avatar/012185082d0175788fb317a89c620ccf63b61f6977170e01906b046f9dca0b76?s=32&d=identicon&r=G)

       tree\_frog

       August 23, 2023 at 4:12 am

       That’s very interesting! Apologies that my first comment reads a little tersely, and that the second is so verbose.

       On my main installation of macOS Monterey, there is both a com.apple.AppStore AND a com.apple.appstore domain. UserDefaults is case-sensitive & treats these as distinct…. but, on a case-INsensitive filesystem, `defaults` can fall back to searching by file path under certain circumstances, causing it to find domains with differing capitalization & make things confusing.

       (Test: `defaults domains | tr ‘, ‘ ‘\n’ | grep -i com.apple.appstore`)

       On my machine, com.apple.appstore is mostly empty, whereas com.apple.AppStore has the expected defaults for the GUI App Store. In fact, it appears I erroneously created the lowercase domain myself in Jan 2020 with a mis-capitalized defaults command (aiming to remove the nag to upgrade from Mojave). There have been a slew of upgrades since then that have either migrated the preference or had capitalization bugs of their own.

       Interrogating cfprefsd shows that the plist for com.apple.AppStore is stored at:
       ~/Library/Preferences/com.apple.AppStore.plist

       …whereas the plist for com.apple.appstore is stored at:...