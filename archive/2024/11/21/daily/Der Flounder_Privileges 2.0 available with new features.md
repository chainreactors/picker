---
title: Privileges 2.0 available with new features
url: https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/
source: Der Flounder
date: 2024-11-21
fetch_date: 2025-10-06T19:14:10.953933
---

# Privileges 2.0 available with new features

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Privileges.app](https://derflounder.wordpress.com/category/privileges-app/) > Privileges 2.0 available with new features

## Privileges 2.0 available with new features

November 20, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

[SAP](https://sap.com) has released a new major version of their open source [Privileges app](https://github.com/SAP/macOS-enterprise-privileges). This tool provides [macOS standard user accounts](https://support.apple.com/guide/mac-help/add-a-user-or-group-mchl3e281fc9/mac) with a way to request administrator rights. Privileges 2.x includes a number of new features not available in Privileges 1.x and in particular fulfills two particular long-standing requests from its user community:

1. It provides a unified mechanism for time-limited admin rights.
2. SAP now provides a signed and notarized installer package for deployment.

For more details, please see below the jump.

**Time-limited admin**

Privileges 1.x featured a mechanism for setting a time limit, but it was tied specifically to [using the Toggle Privileges function](https://derflounder.wordpress.com/2022/07/22/privileges-app-and-time-limited-admin/). This was discussed in the previous version of the Privileges FAQ:

*By default, is there a time limit on the admin rights granted by Privileges?*

**No. Admin rights are granted until some process (like running Privileges again) takes them away.**

*Can I set Privileges to give me administrator rights for a defined amount of time?*

**Yes. You can use the Toggle Privileges option on the dock icon to get admin rights for a set amount of time (the default amount is 20 minutes.)**

![Screen Shot 2022-07-22 at 10.05.50 AM.](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screen-shot-2022-07-22-at-10.05.50-am.png?w=595 "Screen Shot 2022-07-22 at 10.05.50 AM.png")

With Privileges 2.x, time-limited admin is no longer tied exclusively to the **Toggle Privileges** function. For those who want to set a time limit for granting admin rights, you can now set this and Privileges 2.x will remove admin rights after the set time regardless of if you used the Privileges application, the dock tile or the command line tool to request admin rights.

By default, [Privileges 2.x will grant administrator privileges for 20 minutes if not configured otherwise](https://github.com/SAP/macOS-enterprise-privileges/wiki/Frequently-Asked-Questions#by-default-is-there-a-time-limit-on-the-admin-rights-granted-by-privileges).

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-20-at-3.37.21e280afpm.png?w=491&h=600 "Screenshot 2024-11-20 at 3.37.21 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-20-at-3.40.01e280afpm.png?w=595 "Screenshot 2024-11-20 at 3.40.01 PM.png")

This is discussed in the updated Privileges FAQ:

*By default, is there a time limit on the admin rights granted by Privileges?*

**Yes. By default, administrator privileges are granted for 20 minutes (if not configured otherwise). However, if necessary, you can configure Privileges not to remove administrator privileges by setting the expiration interval to “Never” in the app’s settings.**

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-20-at-3.46.png?w=595 "Screenshot 2024-11-20 at 3.46.png")

**Installer package deployment**

Privileges 1.x had an odd issue, where some folks who tried packaging it into an installer package consistently ran into problems. This was partially addressed by [using AutoPkg to build the installer package](https://derflounder.wordpress.com/2022/04/20/building-a-privileges-installer-package-using-autopkg/), as AutoPkg-driven workflows consistently produced working installers. SAP has addressed this issue by providing a signed and notarized installer package for Privileges 2.x, which solves the problem by making it unnecessary for Mac admins to create their own installer packages for deployment.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/11/screenshot-2024-11-20-at-2.58.png?w=599&h=429 "Screenshot 2024-11-20 at 2.58.png")

For those using Privileges in your own shops, I recommend taking a look at Privileges 2.x as it includes more features and fixes in addition to what I’ve discussed above. It is available via the following link:

<https://github.com/SAP/macOS-enterprise-privileges>

For those who want to manage Privileges, please see here for the **Managing Privileges** documentation:

<https://github.com/SAP/macOS-enterprise-privileges/wiki/Managing-Privileges>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/11/20/privileges-2-0-available-with-new-features/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Privileges.app](https://derflounder.wordpress.com/category/privileges-app/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2024/11/20/privileges-2-0-available-with-new-features/#respond)

Δ

[Managing time limited admin rights with Privileges 2.x](https://derflounder.wordpress.com/2024/11/21/managing-time-limited-admin-rights-with-privileges-2-x/)
[Accessing the recovery key password reset option at the login window on macOS Sequoia](https://derflounder.wordpress.com/2024/11/18/accessing-the-recovery-key-password-reset-option-at-the-login-window-on-macos-sequoia/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounde...