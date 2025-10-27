---
title: spctl command line tool no longer able to manage Gatekeeper on macOS Sequoia
url: https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/
source: Der Flounder
date: 2024-09-24
fetch_date: 2025-10-06T18:25:01.159600
---

# spctl command line tool no longer able to manage Gatekeeper on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Gatekeeper](https://derflounder.wordpress.com/category/gatekeeper/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > spctl command line tool no longer able to manage Gatekeeper on macOS Sequoia

## spctl command line tool no longer able to manage Gatekeeper on macOS Sequoia

September 23, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

On macOS Sonoma and earlier versions of macOS, the [spctl command line tool](https://www.manpagez.com/man/8/spctl/) could be used to turn Gatekeeper on and off. For example, on macOS Sonoma the following command can be run with root privileges to disable Gatekeeper:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/spctl –global-disable |

[view raw](https://gist.github.com/rtrouton/757c4f3931d54aa1c251b603bb27bc61/raw/0cfca8f216c14e7a7c3f9eef45e9adc2383063f3/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/757c4f3931d54aa1c251b603bb27bc61#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.38.28e280afam.png?w=595 "Screenshot 2024-09-23 at 8.38.28 AM.png")

After running this command, in **System Settings**: **Privacy and Security**, you should see Gatekeeper displaying that it is set to **Anywhere**:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.38.14e280afam.png?w=595 "Screenshot 2024-09-23 at 8.38.14 AM.png")

Also on macOS Sonoma, the following command can be run with root privileges to enable Gatekeeper:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/spctl –global-enable |

[view raw](https://gist.github.com/rtrouton/e17867526ec1d8796a41d99b34abb128/raw/ed9cd8b7a6c08e82156ba59bc082a111fd07bab2/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e17867526ec1d8796a41d99b34abb128#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.38.54e280afam.png?w=595 "Screenshot 2024-09-23 at 8.38.54 AM.png")

After running this command, in **System Settings**: **Privacy and Security**, you should see Gatekeeper displaying that it is set to **App Store and identified developers**:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.39.10e280afam.png?w=595 "Screenshot 2024-09-23 at 8.39.10 AM.png")

On macOS Sequoia, this Gatekeeper management approach no longer works. For more details, please see below the jump.

On macOS Sequoia, running the command to disable Gatekeeper produces the following output:

**Globally disabling the assessment system needs to be confirmed in System Settings.**

**![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.49.55e280afam.png?w=595 "Screenshot 2024-09-23 at 8.49.55 AM.png")**

On macOS Sequoia, running the command to enable Gatekeeper produces the following output:

**This operation is no longer supported. Please see the man page for more information.**

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.50.53e280afam.png?w=595 "Screenshot 2024-09-23 at 8.50.53 AM.png")

In both cases, the Gatekeeper settings in **System Settings**: **Privacy and Security** should remain unchanged.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/09/screenshot-2024-09-23-at-8.50.03e280afam.png?w=595 "Screenshot 2024-09-23 at 8.50.03 AM.png")

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/?share=pocket)

Like Loading...

### *Related*

Categories: [Gatekeeper](https://derflounder.wordpress.com/category/gatekeeper/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (0)
[Leave a comment](#respond)

1. No comments yet.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2024/09/23/spctl-command-line-tool-no-longer-able-to-manage-gatekeeper-on-macos-sequoia/#respond)

Δ

[Managing Gatekeeper with configuration profiles on macOS Sequoia](https://derflounder.wordpress.com/2024/09/24/managing-gatekeeper-with-configuration-profiles-on-macos-sequoia/)
[Keychain Access app in new location on macOS Sequoia](https://derflounder.wordpress.com/2024/09/16/keychain-access-app-in-new-location-on-macos-sequoia/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/ht...