---
title: Volume ownership and Erase All Contents and Settings on macOS Sonoma
url: https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/
source: Der Flounder
date: 2024-06-01
fetch_date: 2025-10-06T16:55:34.339944
---

# Volume ownership and Erase All Contents and Settings on macOS Sonoma

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Volume ownership and Erase All Contents and Settings on macOS Sonoma

## Volume ownership and Erase All Contents and Settings on macOS Sonoma

May 31, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A colleague ran into a problem recently where they tried to run the [Erase All Content and Settings (EACAS) function](https://support.apple.com/guide/personal-safety/how-to-erase-all-content-and-settings-ips4603248a8/web) on an Apple Silicon Mac. Instead of erasing the Mac, instead the following error message was displayed.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/05/screenshot-2024-05-31-at-16.05.41.png?w=328&h=264 "Screenshot 2024-05-31 at 16.05.41.png")

***Erase Assistant is not supported on this Mac***

The error message was misleading however, because the Mac actually supported EACAS without a problem. The root problem was the user account which was logged in had the following characteristics:

* Had administrator rights
* Did not have volume ownership

macOS on Apple Silicon Macs includes a concept known as [volume ownership](https://derflounder.wordpress.com/2023/03/10/granting-volume-owner-status-on-apple-silicon-macs/). You must be a volume owner to perform the following tasks on an Apple Silicon Mac:

* Make changes to startup security policy for a specific install of macOS.\*
* Be able to authorize the installation of macOS software updates or macOS upgrades.
* Authorize running Erase All Contents and Settings.

\* There may be multiple installations of macOS on one Apple Silicon Mac; each macOS install would have their own startup security policy.

For more information on volume ownership, please see Apple’s Platform Deployment article linked below:

<https://support.apple.com/guide/deployment/use-secure-and-bootstrap-tokens-dep24dbdcf9e/web> (see the **Volume ownership** section.)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/05/screenshot-2024-05-31-at-11.25.22-am.png?w=600&h=184 "Screenshot 2024-05-31 at 11.25.22 AM.png")

In this case, since the account in question did not have volume ownership, it couldn’t run EACAS. Fortunately for my colleague, there was another account on the Mac which did have the following characteristics:

* Had administrator rights
* Had volume ownership

Once they logged into that account and ran the EACAS function, this time EACAS worked fine and the Mac was successfully wiped.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (5)
[Leave a comment](#respond)

1. ![Franck Sartori's avatar](https://1.gravatar.com/avatar/1c37f376162ab80e0f02b3962a55b426a0fa774ad65ee941e159450292b33c95?s=32&d=identicon&r=G)

   agnosys

   May 31, 2024 at 3:59 pm

   [Reply](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?replytocom=72374#respond)

   Hi from France. Did you find out why in this context the admin account in question did not have volume ownership, and not the other admin account ?

   * ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc5712a2f1a9d5eb78c66927fd488b3ced2e1cd4372?s=32&d=identicon&r=G)

     peteostro

     June 3, 2024 at 9:06 pm

     [Reply](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?replytocom=72377#respond)

     I’m not sure about this particular case but there is a scenario when a password is changed for the account that might make an account not a volume owner. Like when using Jamf laps

     + ![Franck Sartori's avatar](https://1.gravatar.com/avatar/1c37f376162ab80e0f02b3962a55b426a0fa774ad65ee941e159450292b33c95?s=32&d=identicon&r=G)

       Franck Sartori

       June 4, 2024 at 6:46 am

       This is precisely the most likely scenario that I wanted to confirm by posting my comment.
2. ![peteostro's avatar](https://1.gravatar.com/avatar/dc2ad6b1fcdefcade7b53cc5712a2f1a9d5eb78c66927fd488b3ced2e1cd4372?s=32&d=identicon&r=G)

   peteostro

   June 3, 2024 at 9:05 pm

   [Reply](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?replytocom=72376#respond)

   I’m not sure about this particular case but there is a scenario when a password is changed for the account that might make an account not a volume owner. Like when using Jamf laps
3. ![Carlos's avatar](https://0.gravatar.com/avatar/3bdee9e45da7c1558205dd5da5685459ffbea481b0838718fd5a567ef7e20b83?s=32&d=identicon&r=G)

   Carlos

   July 24, 2024 at 4:06 pm

   [Reply](https://derflounder.wordpress.com/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/?replytocom=72449#respond)

   We’ve came across this in our org when attempting to run OS Updates, some users are volume owners, some aren’t. Would you happen to know if there is a way to make a non-volume owner and a volume owner?

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2024/05/31/volume-ownership-and-erase-all-contents-and-settings-on-macos-sonoma/#respond)

Δ

[Using Wi-Fi hardware network interface information with Jamf Pro to identify macOS virtual machines](https://derflounder.wordpress.com/2024/06/07/using-wi-fi-hardware-network-interface-information-with-jamf-pro-to-identify-macos-virtual-machines/)
[Basic Authentication authentication now disabled for the Jamf Pro Classic API as of Jamf Pro 11.5.0](https://derflounder.wordpress.com/2024/05/21/basic-authentication-authentication-now-disabled-for-the-jamf-pro-classic-api-as-of-jamf-pro-11-5-0/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.word...