---
title: Suppressing the FileVault screen with a configuration profile on macOS Tahoe
url: https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/
source: Der Flounder
date: 2025-09-16
fetch_date: 2025-10-02T20:11:23.436064
---

# Suppressing the FileVault screen with a configuration profile on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/) > Suppressing the FileVault screen with a configuration profile on macOS Tahoe

## Suppressing the FileVault screen with a configuration profile on macOS Tahoe

September 15, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Over the years, Apple has introduced a number of screens which appear the first time you log into a Mac. Among those which appear as of macOS Tahoe 26.0 is the **Your Mac is Ready for FileVault** screen, which asks if you want to enable FileVault if it is not already enabled.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/09/skipfilevaultsetup.png?w=599&h=374 "SkipFileVaultSetup.png")

I have not found a way to suppress this screen using a [defaults](https://ss64.com/mac/defaults.html) command, but it is possible to suppress this screen on macOS Tahoe using a configuration profile. For more details, please see below the jump.

The relevant preference domain and key values are below:

* Preference domain: **com.apple.SetupAssistant.managed**
* Key: **SkipSetupItems**
* Value: **FileVault**

The profile is available on GitHub via the link below:

<https://github.com/rtrouton/profiles/blob/main/SkipFileVaultSetup>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?share=pocket)

Like Loading...

### *Related*

Categories: [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Management Profiles](https://derflounder.wordpress.com/category/management-profiles/)

Comments (4)
[Leave a comment](#respond)

1. ![BMan's avatar](https://1.gravatar.com/avatar/1b7addf1e646ac216a84a008e3c60a4d1d9f932957668c3fb3689dadf1135b21?s=32&d=identicon&r=G)

   BMan

   September 16, 2025 at 1:07 pm

   [Reply](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?replytocom=72786#respond)

   Thank you!
2. ![Douglas Pred,pre's avatar](https://1.gravatar.com/avatar/467648cced07bf1c15b115c9ca4814831827dfe6271b4da310dc3a4bb8bd41f3?s=32&d=identicon&r=G)

   Douglas Pred,pre

   September 16, 2025 at 5:35 pm

   [Reply](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?replytocom=72787#respond)

   THank you, but this is not working for me when doing an over the top update. It works fine for a new install.
3. ![adstretch's avatar](https://2.gravatar.com/avatar/2e81e85b61df3e7a1d24271ea537a306c16f4635672bd7f5474a987a2f89b1d3?s=32&d=identicon&r=G)

   adstretch

   September 17, 2025 at 7:03 pm

   [Reply](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?replytocom=72789#respond)

   I’m using this for shared machines using Jamf Connect for login. If I apply this profile to the prestage it works properly for the first user.

   If I scope it to the machine in addition to the prestage, subsequent users are prompted to enable filevault even with the profile applied.

   Am I missing something or is this the expected behavior? Is there a way to block the dialog for ALL potential users of the system?

   * ![Chris Johnson's avatar](https://0.gravatar.com/avatar/9c0a5bffb39d34cf5fe6e4b131701c411e499667be95bf4007dd7cb12ae2327f?s=32&d=identicon&r=G)

     Chris Johnson

     September 23, 2025 at 9:34 pm

     [Reply](https://derflounder.wordpress.com/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/?replytocom=72793#respond)

     I had the same issue @adstretch. For me the fix was to use the solution posted in the MacAdmins Slack channel, namely rtrouton’s config profile to suppress all Tahoe setup assistant screens: <https://gist.github.com/rtrouton/351afcc75263ab3b8c713f9224489da1>

     If you use this profile, make sure there are no other profiles that are in-scope that use keys that live under the payload identifier: com.apple.SetupAssistant.managed. (In my case I had to de-scope the “Skips the Software Update Setup Assistant Screen” profile as it shares a “SoftwareUpdate” key.)

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/09/15/suppressing-the-filevault-screen-with-a-configuration-profile-on-macos-tahoe/#respond)

Δ

[FireWire support removed from macOS Tahoe](https://derflounder.wordpress.com/2025/09/15/firewire-support-removed-from-macos-tahoe/)
[Declarative device management user channel and device channel](https://derflounder.wordpress.com/2025/09/09/declarative-device-management-user-channel-and-device-channel/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

September 2025...