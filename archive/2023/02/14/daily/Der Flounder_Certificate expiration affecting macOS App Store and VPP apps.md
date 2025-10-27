---
title: Certificate expiration affecting macOS App Store and VPP apps
url: https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/
source: Der Flounder
date: 2023-02-14
fetch_date: 2025-10-04T06:29:17.507757
---

# Certificate expiration affecting macOS App Store and VPP apps

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Volume Purchase Program](https://derflounder.wordpress.com/category/apple-volume-purchase-program/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Certificate expiration affecting macOS App Store and VPP apps

## Certificate expiration affecting macOS App Store and VPP apps

February 13, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Mac admins who have previously installed macOS apps from the Mac App Store (MAS) or the Volume Purchase Program (VPP) may be seeing some of those apps displaying warning messages on launch that the application is damaged.

![Screenshot 2023 02 07 at 5 37 40 PM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-07-at-5.37.40-pm.png?w=260&h=244 "Screenshot 2023-02-07 at 5.37.40 PM.png")

When observed, this behavior may be appearing because the certificates Apple has been using to digitally sign apps have recently expired, on February 6th 2023 or February 7th 2023. (Both expiration dates have appeared in signing certificates on the apps I’ve checked.)

![Screenshot 2023 02 13 at 11 39 25](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-13-at-11.39.25.png?w=600&h=401 "Screenshot 2023-02-13 at 11.39.25.png")

When the code signing is detected as being invalid, Apple’s security tools are blocking launch as a consequence. In most cases, it appears that the code signing is still appearing as valid despite being past the expiration date.

---

**Update: February 13, 2023** – I’ve received feedback from [@macmuleblog](https://twitter.com/macmuleblog) after posting that they have seen damaged apps from VPP where they had a valid code signing certificate, so the root cause for the damaged apps may be different than what I initially posted. My apologies for any confusion caused.

---

Both the **Apple Mac OS Application Signing** certificate used to sign the apps, and the **Apple Worldwide Developer Relations Certification Authority** intermediate certificate are showing expiration dates that are now in the past.

![Screenshot 2023 02 13 at 9 32 17 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-13-at-9.32.17-am.png?w=579&h=395 "Screenshot 2023-02-13 at 9.32.17 AM.png")

![Screenshot 2023 02 13 at 8 56 28 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-13-at-8.56.28-am.png?w=589&h=397 "Screenshot 2023-02-13 at 8.56.28 AM.png")

In the cases where I’ve experienced applications reporting as damaged, uninstalling the app and reinstalling it seems to have addressed the issue. Hopefully Apple is working on getting the issue handled by re-issuing apps which are signed with a certificate signed with a new expiration date in the future.

---

**Update: February 13, 2023** – It looks like Apple had previously begun the code signing effort I requested above. When I checked Microsoft’s **To Do** app, I saw that the **Apple Mac OS Application Signing** certificate used to sign the app and the **Apple Worldwide Developer Relations Certification Authority** intermediate certificate are showing expiration dates in the future.

![Screenshot 2023-02-13 at 10.54.24 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-13-at-10.54.24-am.png?w=595)

![Screenshot 2023-02-13 at 10.54.28 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/02/screenshot-2023-02-13-at-10.54.28-am.png?w=595)

---

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/?share=pocket)

Like Loading...

### *Related*

Categories: [Apple Volume Purchase Program](https://derflounder.wordpress.com/category/apple-volume-purchase-program/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2023/02/13/certificate-expiration-affecting-macos-app-store-and-vpp-apps/#respond)

Δ

[Providing Jamf Pro computer inventory information via macOS configuration profile](https://derflounder.wordpress.com/2023/02/25/providing-jamf-pro-computer-inventory-information-via-macos-configuration-profile/)
[Using the Jamf Pro API to retrieve FileVault personal recovery keys](https://derflounder.wordpress.com/2023/01/25/using-the-jamf-pro-api-to-retrieve-filevault-personal-recovery-keys/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

February 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | 1 | 2 | 3 | 4 | 5 |
| 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| [13](https://derflounder.wordpress.com/2023/02/13/) | 14 | 15 | 16 | 17 | 18 | 19 |
| 20 | 21 | 22 | 23 | 24 | [25](https://derflounder.wordpress.com/2023/02/25/) | 26 |
| [27](https://derflounder.wordpress.com/2023/02/27/) | 28 |  | | | | |

[« Jan](https://derflounder.wordpress.com/2023/01/)

[Mar »](https://derflounder.wordpress.com/2023/03/)

### Recent Comments

|  |  |
| --- | --- |
| ![Chan's avatar](https://0.grava...