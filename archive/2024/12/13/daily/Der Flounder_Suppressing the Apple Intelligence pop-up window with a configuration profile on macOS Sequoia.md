---
title: Suppressing the Apple Intelligence pop-up window with a configuration profile on macOS Sequoia
url: https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/
source: Der Flounder
date: 2024-12-13
fetch_date: 2025-10-06T19:36:05.004486
---

# Suppressing the Apple Intelligence pop-up window with a configuration profile on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Suppressing the Apple Intelligence pop-up window with a configuration profile on macOS Sequoia

## Suppressing the Apple Intelligence pop-up window with a configuration profile on macOS Sequoia

December 12, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Apple has introduced a number of pop-up windows over the years, which appear the first time you log into a Mac and sometimes also after an OS update. Apple added a new one for macOS Sequoia as part of introducing [Apple Intelligence](https://www.apple.com/apple-intelligence).

![](https://derflounder.wordpress.com/wp-content/uploads/2024/12/screenshot-2024-12-11-at-5.55.png?w=600&h=450 "Screenshot 2024-12-11 at 5.55.png")

The Apple Intelligence pop-up window can be suppressed for the logged-in user by running the command shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write com.apple.SetupAssistant DidSeeIntelligence -bool true |

[view raw](https://gist.github.com/rtrouton/5e97db2a061a13888a9f0720718304c3/raw/664d53c749624f57308020aa6fedbb2b198afe96/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5e97db2a061a13888a9f0720718304c3#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

It is also possible to suppress the Apple Intelligence pop up window on macOS Sequoia using a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.SetupAssistant.managed**
* Key: **SkipSetupItems**
* Value: **Intelligence**

The profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/blob/main/SkipAppleIntelligenceSetup>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Apple Intelligence](https://derflounder.wordpress.com/category/apple-intelligence/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (11)
[Leave a comment](#respond)

1. ![atombomb13's avatar](https://0.gravatar.com/avatar/0ca6aa21495ea12eb5571b5c94c008f2b42ed5a21e7ba50c305d041217069e9a?s=32&d=identicon&r=G)

   [atombomb13](http://adamdurancom.wordpress.com)

   December 12, 2024 at 9:20 pm

   [Reply](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?replytocom=72596#respond)

   Thanks as always, Rich.
2. ![Daniel's avatar](https://2.gravatar.com/avatar/e72f28af5bf5e79b5b0d950f341ee3218eefdcae35614bf2e92e001a5c3d605f?s=32&d=identicon&r=G)

   Daniel\_Ross

   December 12, 2024 at 10:41 pm

   [Reply](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?replytocom=72597#respond)

   Can this be applied to non 15.X.X machines ahead of time and during pre-stage for any net new machines?
3. ![Dave's avatar](https://2.gravatar.com/avatar/5818e7856ebc0a71049566604c852e705204299398c59b7748f3286e1ecc8158?s=32&d=identicon&r=G)

   Dave

   December 17, 2024 at 11:51 pm

   [Reply](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?replytocom=72606#respond)

   I have applied the profile from your GitHub page and still seeing the Apple Intelligence’s window appearing during setup assistant…

   Any ideas as to why? I have modified it at all and simply deployed the profile prior to updating from Sonoma to Sequoia.

   * ![rtrouton's avatar](https://0.gravatar.com/avatar/fb809ae714f8d9d5be5d4c0d7086f9bb3781e9ccdd25cf8b3aa24b140a641e0e?s=32&d=identicon&r=G)

     [rtrouton](http://www.taomechworks.net)

     December 18, 2024 at 12:47 am

     [Reply](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?replytocom=72607#respond)

     A profile’s settings get applied at the time of installation. If the setting isn’t understood by the OS, it’s ignored. macOS Sonoma doesn’t have the setting for skipping the Apple Intelligence screen, so Sonoma will ignore it. It will remain ignored when upgrading to Sequoia because the setting never gets re-evaluated and thus isn’t applied on Sequoia.

     TL;DR: in order for the profile to work, it needs to be installed when the Mac is running Sequoia.
4. ![pioneeringd33a693588's avatar](https://2.gravatar.com/avatar/5818e7856ebc0a71049566604c852e705204299398c59b7748f3286e1ecc8158?s=32&d=identicon&r=G)

   pioneeringd33a693588

   December 18, 2024 at 9:30 pm

   [Reply](https://derflounder.wordpress.com/2024/12/12/suppressing-the-apple-intelligence-pop-up-window-with-a-configuration-profile-on-macos-sequoia/?replytocom=72615#respond)

   Thank you, Rich for that feedback!

   The reason why I asked is because since we are now past the 90 days max deferral (I have a Jamf config. profile with key>enforcedSoftwareUpdateMajorOSDeferredInstallDelay</key> set to Tr...