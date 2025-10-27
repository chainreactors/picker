---
title: Verifying installer package signing and notarization using pkgutil
url: https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/
source: Der Flounder
date: 2023-01-21
fetch_date: 2025-10-04T04:27:09.222872
---

# Verifying installer package signing and notarization using pkgutil

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Notarization](https://derflounder.wordpress.com/category/notarization/) > Verifying installer package signing and notarization using pkgutil

## Verifying installer package signing and notarization using pkgutil

January 20, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

Recently I needed a way to verify whether an installer package was signed and notarized. I’ve been using Apple’s [stapler](https://keith.github.io/xcode-man-pages/stapler.1.html) tool as my usual go-to for verifying notarization. However, the **stapler** tool needs for Xcode to to be installed and I needed a solution that worked regardless of Xcode or the Xcode Command Line Tools being installed on the Mac in question.

After some digging, I found that [pkgutil](https://www.manpagez.com/man/1/pkgutil/)‘s **check-signature** function on macOS Monterey and later works great for this and doesn’t have any dependencies on Xcode or the Xcode Command Line Tools. The **pkgutil** tool is installed as part of macOS and the **check-signature** function displays the following on Monterey and later:

**If a package is not signed:**

![Screenshot 2023 01 20 at 10 25 38 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/01/screenshot-2023-01-20-at-10.25.38-am.png?w=596&h=104 "Screenshot 2023-01-20 at 10.25.38 AM.png")

**If a package is signed with a certificate:**

![Screenshot 2023 01 20 at 10 24 52 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/01/screenshot-2023-01-20-at-10.24.52-am.png?w=599&h=419 "Screenshot 2023-01-20 at 10.24.52 AM.png")

**If a package is signed with a certificate and trusted by Apple’s notarization service:**

![Screenshot 2023 01 20 at 10 23 29 AM](https://derflounder.wordpress.com/wp-content/uploads/2023/01/screenshot-2023-01-20-at-10.23.29-am.png?w=600&h=436 "Screenshot 2023-01-20 at 10.23.29 AM.png")

To use the **check-signature** function, you should be able to use the command shown below (substituting */path/to/installer.pkg* with the actual directory path of the installer package you want to check.):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/pkgutil –check-signature /path/to/installer.pkg |

[view raw](https://gist.github.com/rtrouton/3fb75528116cb64411ccb09b82cac8b3/raw/f8df2b1066265d1cbf60b534ca7e396b999c6e89/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3fb75528116cb64411ccb09b82cac8b3#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Notarization](https://derflounder.wordpress.com/category/notarization/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2023/01/20/verifying-installer-package-signing-and-notarization-using-pkgutil/#respond)

Δ

[Using the Jamf Pro API to retrieve FileVault personal recovery keys](https://derflounder.wordpress.com/2023/01/25/using-the-jamf-pro-api-to-retrieve-filevault-personal-recovery-keys/)
[Finding the version number of the Xcode command line tools using the softwareupdate command](https://derflounder.wordpress.com/2023/01/18/finding-the-version-number-of-the-xcode-command-line-tools-using-the-softwareupdate-command/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

January 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | | [1](https://derflounder.wordpress.com/2023/01/01/) |
| 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| 16 | 17 | [18](https://derflounder.wordpress.com/2023/01/18/) | 19 | [20](https://derflounder.wordpress.com/2023/01/20/) | 21 | 22 |
| 23 | 24 | [25](https://derflounder.wordpress.com/2023/01/25/) | 26 | 27 | 28 | 29 |
| 30 | 31 |  | | | | |

[« Dec](https://derflounder.wordpress.com/2022/12/)

[Feb »](https://derflounder.wordpress.com/2023/02/)

### Recent Comments

|  |  |
| --- | --- |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/#comment-72798) |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on [rsync replaced with openrsync…](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-open...