---
title: When does the upgrade to macOS Ventura need admin rights?
url: https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/
source: Der Flounder
date: 2022-12-20
fetch_date: 2025-10-04T01:57:08.112983
---

# When does the upgrade to macOS Ventura need admin rights?

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > When does the upgrade to macOS Ventura need admin rights?

## When does the upgrade to macOS Ventura need admin rights?

December 19, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Upgrading to macOS Ventura from macOS Monterey or earlier seems like it should be a straightforward process.

1. Open System Preferences

2. Click on **Software Update**.

![Screen Shot 2022 12 19 at 12 40 55 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-12.40.55-pm.png?w=300&h=255 "Screen Shot 2022-12-19 at 12.40.55 PM.png")

3. If the macOS Ventura upgrade is listed there, click on the **Upgrade Now** button.

![Screen Shot 2022 12 19 at 11 19 59 AM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-11.19.59-am.png?w=299&h=146 "Screen Shot 2022-12-19 at 11.19.59 AM.png")

However, you may get different upgrade experiences depending on whether you are running macOS 12.3 or later, or if you’re running macOS 12.21 or earlier.

**macOS 12.3 or later:**

1. You see a macOS Ventura installer which is around 6 GBs or less.

![Screen Shot 2022 12 19 at 11 23 04 AM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-11.23.04-am.png?w=299&h=146 "Screen Shot 2022-12-19 at 11.23.04 AM.png")

2. When you click **Upgrade Now**, you are asked to authenticate as a user. Not as a user with administrator privileges, just as a user.

![Screen Shot 2022 12 19 at 11 24 31 AM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-11.24.31-am.png?w=129&h=144 "Screen Shot 2022-12-19 at 11.24.31 AM.png")

**macOS 12.2.1 or earlier**

1. You see a macOS Ventura installer which is around 12 GBs or more.

![Screen Shot 2022 12 19 at 11 18 59 AM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-11.18.59-am.png?w=299&h=146 "Screen Shot 2022-12-19 at 11.18.59 AM.png")

2. It downloads an **Install macOS Ventura** app to your Mac and installs it in **/Applications**.

![Screen Shot 2022 12 19 at 12 31 54 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-12.31.54-pm.png?w=299&h=151 "Screen Shot 2022-12-19 at 12.31.54 PM.png")

3. The **Install macOS Ventura** app automatically launches once download and installation of the application completes.

![Screen Shot 2022 12 19 at 12 31 57 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-12.31.57-pm.png?w=299&h=235 "Screen Shot 2022-12-19 at 12.31.57 PM.png")

4. Running the **Install macOS Ventura** app will prompt for a user with administrator privileges to authenticate before the upgrade proceeds.

![Screen Shot 2022 12 19 at 12 32 17 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screen-shot-2022-12-19-at-12.32.17-pm.png?w=299&h=235 "Screen Shot 2022-12-19 at 12.32.17 PM.png")

Why the difference? The reason is that Apple has developed a new software upgrade path to macOS Ventura for Macs running macOS 12.3 or later which doesn’t require the following:

1. The need to run the macOS Ventura full installer
2. The requirement to authenticate as an administrator before upgrading from macOS Monterey to macOS Ventura.

Apple did include additional logic for macOS Ventura upgrades for upgrading to Ventura 13.0.0 and 13.0.1, where if a Mac running macOS Monterey 12.3 or later was enrolled with an MDM management solution and was thus in [supervised mode](https://support.apple.com/guide/deployment/about-device-supervision-dep1d89f0bff/web), the new software upgrade path was disabled for those Macs.

As of the release of macOS 13.1, this logic no longer applies and supervised Macs may be offered the new upgrade path (which doesn’t require admin rights to upgrade.)

For more details about this, and information on how to block the macOS Ventura upgrade from appearing in Software Update if your organization needs more time, please see the Apple KBase article linked below:

* Manage upgrading to macOS Ventura in your organization: <https://support.apple.com/HT213471>

My colleague [Robert Hammen](https://hammen.medium.com) has also written on the topic of delaying upgrades, so if you’re interested in that topic, please see his Medium post linked below:

* Holding Back the OS Upgrades: <https://hammen.medium.com/holding-back-the-os-upgrades-6c2d97f99ac3>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2022/12/19/when-does-the-upgrade-to-macos-ventura-need-admin-rights/#respond)

Δ

[Identifying Mac laptops and desktops from the command line by checking for a built-in battery](https://derflounder.wordpress.com/2022/12/26/identifying-mac-laptops-and-desktops-from-the-command-line-by-checking-for-a-built-in-battery/)
[Using AutoPkg to build installers for Palo Alto’s GlobalProtect VPN software](https://derflounder.wordpress.com/2022/12/11/using-autopkg-to-build-installers-for-palo-altos-globalprotect-vpn-software/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.new...