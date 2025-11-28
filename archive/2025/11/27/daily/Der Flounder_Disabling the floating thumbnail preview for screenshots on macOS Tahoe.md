---
title: Disabling the floating thumbnail preview for screenshots on macOS Tahoe
url: https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/
source: Der Flounder
date: 2025-11-27
fetch_date: 2025-11-28T03:09:12.150452
---

# Disabling the floating thumbnail preview for screenshots on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Documentation](https://derflounder.wordpress.com/category/documentation/), [macOS](https://derflounder.wordpress.com/category/macos/) > Disabling the floating thumbnail preview for screenshots on macOS Tahoe

## Disabling the floating thumbnail preview for screenshots on macOS Tahoe

November 27, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the features available when taking screenshots is the option to see a floating thumbnail preview of the screenshot before it gets saved to the location you’ve chosen to save screenshots to. This option is enabled by default and looks like this on macOS Tahoe.

1. Screenshot is taken.
2. Floating thumbnail preview appears and slides off-screen.
3. Screenshot file icon appears (in this example, screenshots are being saved to the desktop.)

[![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/ezgif-1a5bf3cf593057da.gif?w=595)](https://derflounder.wordpress.com/wp-content/uploads/2025/11/ezgif-1a5bf3cf593057da.gif)

I prefer to have this option turned off, as I’d rather have the ability to select and work with the screenshot file right away in place of waiting for the floating thumbnail to appear and disappear.

Fortunately, this option can be turned off in a couple of ways. The first is through using  **Screenshot.app**, which is included with macOS.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-27-at-2.24.png?w=595 "Screenshot 2025-11-27 at 2.24.png")

When you use **Screenshot.app**, it will provide a toolbar for selecting screenshot image or screencapture movie options. As part of that toolbar, there is an **Options** button.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-27-at-2.25.png?w=595 "Screenshot 2025-11-27 at 2.25.png")

When you click the **Options** button, you get a menu where one of the selections is **Show Floating Thumbnail**. If you unselect that, the floating thumbnail preview no longer appears when taking screenshots or making screencapture movies.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-27-at-2.26.png?w=595 "Screenshot 2025-11-27 at 2.26.png")

You can also disable this from the command line, by running the two following commands in Terminal:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/defaults write com.apple.screencapture show-thumbnail -bool false |
|  | killall SystemUIServer |

[view raw](https://gist.github.com/rtrouton/62d4b82a7df094bc74244254b46ae234/raw/1ed164d1d8d9a89aab6928595eca3b603316793a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/62d4b82a7df094bc74244254b46ae234#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-27-at-2.52.48pm.png?w=595 "Screenshot 2025-11-27 at 2.52.48 PM.png")

In my case, I wanted to disable the floating thumbnail preview on my Macs so I’ve written a profile which can enforce this. It’s available via the link below:

<https://github.com/rtrouton/profiles/blob/main/DisableScreenshotFloatingThumbnail>

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?share=pocket)

Like Loading...

### *Related*

Categories: [Documentation](https://derflounder.wordpress.com/category/documentation/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (1)
[Leave a comment](#respond)

1. ![socalmacguy's avatar](https://1.gravatar.com/avatar/1fa20c0588d20dc1f8f18288d4731fb15eb34f0b533e2f716ba3d0864f40cac1?s=32&d=identicon&r=G)

   [socalmacguy](http://socalmacguy.wordpress.com)

   November 27, 2025 at 8:35 pm

   [Reply](https://derflounder.wordpress.com/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/?replytocom=72813#respond)

   This has always annoyed me, but not quite enough to search for a solution.

   Thanks Rich!!!

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2025/11/27/disabling-the-floating-thumbnail-preview-for-screenshots-on-macos-tahoe/#respond)

Δ

[Deploying custom DDM declarations using Blueprints in Jamf Pro](https://derflounder.wordpress.com/2025/11/26/deploying-custom-ddm-declarations-using-blueprints-in-jamf-pro/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

November 2025

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | | | | 1 | 2 |
| 3 | [4](https://derflounder.wordpress.com/2025/11/04/) | 5 | [6](https://derflounder.wordpress.com/2025/11/06/) | 7 | 8 | 9 |
| 10 | [11](https://derflounder.wordpress.com/2025/11/11/) | 12 | 13 | [14](https://derflounder.wordpress.com/2025/11/14/) | 15 | 16 |
| 17 | 18 | [19](https://derflounder.wordpress.com/2025/11/19/) | 20...