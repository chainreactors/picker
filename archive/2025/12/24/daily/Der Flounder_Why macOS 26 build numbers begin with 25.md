---
title: Why macOS 26 build numbers begin with 25
url: https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/
source: Der Flounder
date: 2025-12-24
fetch_date: 2025-12-25T03:24:11.822037
---

# Why macOS 26 build numbers begin with 25

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Why macOS 26 build numbers begin with 25

## Why macOS 26 build numbers begin with 25

December 24, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A question I’ve seen pop up in the Mac Admins Slack since the release of macOS Tahoe 26.x goes something like this:

***Why does macOS 26 have a build number that starts with 25?***

![](https://derflounder.wordpress.com/wp-content/uploads/2025/12/screenshot-2025-12-23-at-8.30.58pm.png?w=595 "Screenshot 2025-12-23 at 8.30.58 PM.png")

The answer has to do with [Darwin](https://en.wikipedia.org/wiki/Darwin_%28operating_system%29), the core operating system that is the foundation for all of the following Apple operating systems:

* [audioOS](https://en.wikipedia.org/wiki/AudioOS)
* [bridgeOS](https://en.wikipedia.org/wiki/BridgeOS)
* [iOS](https://en.wikipedia.org/wiki/IOS)
* [iPadOS](https://en.wikipedia.org/wiki/IPadOS)
* [macOS](https://en.wikipedia.org/wiki/MacOS)
* [tvOS](https://en.wikipedia.org/wiki/TvOS)
* [visionOS](https://en.wikipedia.org/wiki/VisionOS)
* [watchOS](https://en.wikipedia.org/wiki/WatchOS)

For more details, please see below the jump.

The Darwin operating system has its own version number which is separate from the version number of the other Apple operating systems. In the case of macOS, Apple includes Darwin’s version number in the macOS build number. For example, the build number for macOS Tahoe 26.2.0 is the following:

**25C56**

The **25** part refers to the [major version number](https://semver.org) for the current Darwin release. Beginning in 2011, the major version numbers of the Darwin operating system have coincided with the last two digits of the year it was released:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | Darwin Version | Release Date |
| --- | --- | --- |
|  | 11.0.0 | July 20 2011 |
|  | 12.0.0 | February 16 2012 |
|  | 13.0.0 | June 11 2013 |
|  | 14.0.0 | September 18 2014 |
|  | 15.0.0 | September 16 2015 |
|  | 16.0.0 | September 13 2016 |
|  | 17.0.0 | September 19 2017 |
|  | 18.0.0 | September 24 2018 |
|  | 19.0.0 | September 19 2019 |
|  | 20.0.0 | June 22 2020 |
|  | 21.0.0 | June 7 2021 |
|  | 22.0.0 | June 6 2022 |
|  | 23.0.0 | September 18 2023 |
|  | 24.0.0 | September 16 2024 |
|  | 25.0.0 | September 15 2025 |

[view raw](https://gist.github.com/rtrouton/2232529e6aa6e2eec44180bc73181a0d/raw/564895d9c762591d9cdd0cd557ac5d5133e3c8f1/darwin_versions_release_date.csv)
 [darwin\_versions\_release\_date.csv](https://gist.github.com/rtrouton/2232529e6aa6e2eec44180bc73181a0d#file-darwin_versions_release_date-csv)
hosted with ❤ by [GitHub](https://github.com)

The current Darwin operating system release is 25.0.0 as of macOS Tahoe 26.2.0, so macOS Tahoe build numbers start with 25. Unless Apple decides to change Darwin’s version numbering system, this will mean that future macOS releases will continue to have build numbers that will start with a two digit number that is one number less than the macOS major version number.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/12/24/why-macos-26-build-numbers-begin-with-25/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/12/24/why-macos-26-build-numbers-begin-with-25/#respond)

Δ

[Using printf to write variable values to JSON strings in Bash scripts](https://derflounder.wordpress.com/2025/12/22/using-printf-to-write-variable-values-to-json-strings-in-bash-scripts/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

December 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [2](https://derflounder.wordpress.com/2025/12/02/) | 3 | 4 | 5 | 6 | 7 |
| 8 | 9 | 10 | 11 | [12](https://derflounder.wordpress.com/2025/12/12/) | 13 | 14 |
| 15 | 16 | [17](https://derflounder.wordpress.com/2025/12/17/) | 18 | 19 | 20 | 21 |
| [22](https://derflounder.wordpress.com/2025/12/22/) | 23 | [24](https://derflounder.wordpress.com/2025/12/24/) | 25 | 26 | 27 | 28 |
| 29 | 30 | 31 |  | | | |

[« Nov](https://derflounder.wordpress.com/2025/11/)

### Recent Comments

|  |  |
| --- | --- |
| ![jeffvandehey's avatar](https://1.gravatar.com/avatar/725d83085406242cc21273dfc090fe23c12aa99f9bbba831105e55f9b6995bc4?s=48&d=identicon&r=G) | jeffvandehey on [Providing Jamf Pro computer in…](https://derflounder.wordpress.com/2023/02/25/providing-jamf-pro-computer-inventory-information-via-macos-configuration-profile/#comment-72823) |
| ![yassermkh's avatar](https://2.gravatar.com/avatar/eeb5b73a52315b9d425fa05e45fa1f5085a92074729f96ec3873a2d05c7e8ca4?s=48&d=identicon&r=G) | yassermkh on [Updating management status in…](https://derflounder.wordpress.com/2025/12/12/13154/#co...