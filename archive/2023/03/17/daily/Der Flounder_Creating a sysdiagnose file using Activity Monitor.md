---
title: Creating a sysdiagnose file using Activity Monitor
url: https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/
source: Der Flounder
date: 2023-03-17
fetch_date: 2025-10-04T09:50:31.424297
---

# Creating a sysdiagnose file using Activity Monitor

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Creating a sysdiagnose file using Activity Monitor

## Creating a sysdiagnose file using Activity Monitor

March 16, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

The [sysdiagnose tool](https://www.manpagez.com/man/1/sysdiagnose) is used for gathering a large amount of diagnostic files and logging, and it’s often very useful when it comes to figuring out why a problem is happening. However, it can sometimes be challenging to get a sysdiagnose-generated file from someone who is not comfortable with using the Terminal as the usual method for generating a sysdiagnose file involves opening the Terminal and running commands there.

Fortunately, there’s also a way to generate a sysdiagnose file using Activity Monitor. This may be an alternate way to help get you the desired sysdiagnose file from someone who normally wouldn’t ever use the Terminal on macOS. For more details, please see below the jump.

Apple includes [how to generate a sysdiagnose file as part of the Activity Monitor User Guide](https://support.apple.com/guide/activity-monitor/run-system-diagnostics-actmntr2225/mac). For a step by step guide, please use the procedure below:

1. Launch Activity Monitor.

![Screenshot-2023-03-16-at-11.32.05-AM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-16-at-11.32.05-am.png?w=595)

2. Choose a method to generate the sysdiagnose file. There’s an option available in the **View** menu, where you can choose **Run System Diagnostics…**

![Screenshot-2023-03-16-at-11.34.16-AM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-16-at-11.34.16-am.png?w=595)

Another option is click the **System diagnostics options** pop-up menu (…) and select **System Diagnostics…**

![Screenshot-2023-03-16-at-11.33.04-AM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-16-at-11.33.04-am.png?w=595)

3. Click **OK** at the privacy agreement screen.

![Screenshot-2023-03-16-at-11.35.04-AM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-16-at-11.35.04-am.png?w=595)

After agreeing at the privacy agreement screen, a sysdiagnose file will be generated. This is a process that may take a few minutes to complete.

![Screenshot-2023-03-16-at-11.36.30-AM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-16-at-11.36.30-am.png?w=595)

Once the sysdiagnose file has been created, a Finder window will appear showing the location of the sysdiagnose file, which will be a compressed file named something similar to what’s shown below:

**sysdiagnose\_2023.03.16\_11-35-09-0400\_macOS\_iMacPro1-1\_22D68.tar.gz**

**![Screenshot-2023-03-16-at-11.38.04-AM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-16-at-11.38.04-am.png?w=595)**

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=linkedin)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=reddit)
* [Click to share on X (Opens in new window)
  X](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=twitter)
* [Click to share on Pinterest (Opens in new window)
  Pinterest](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=pinterest)
* [Click to share on Tumblr (Opens in new window)
  Tumblr](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=tumblr)
* [Click to share on Pocket (Opens in new window)
  Pocket](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?share=pocket)

Like Loading...

### *Related*

Categories: [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/)

Comments (1)
[Leave a comment](#respond)

1. ![isotopp's avatar](https://2.gravatar.com/avatar/280d95c4350c4a5e7c4f2b0524a049f13728799be8a96511fe31b684c6b00308?s=32&d=identicon&r=G)

   [isotopp](http://blog.koehntopp.info)

   March 18, 2023 at 8:05 am

   [Reply](https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/?replytocom=70444#respond)

   I am trying to subscribe to your blog’s RSS, but the feed comes up empty in Newsblur. A check of your blog’s RSS in the w3c validator fails with some kind of illegal characters in URL, referencing some revealButtonRef somewhere.

1. No trackbacks yet.

### Leave a comment [Cancel reply](/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/#respond)

Δ

[macOS Ventura 13.3 alters expected behavior for Finder’s Open With functionality for macOS installer packages](https://derflounder.wordpress.com/2023/04/01/macos-ventura-13-3-alters-expected-behavior-for-finders-open-as-functionality-for-macos-installer-packages/)
[Granting Volume Owner status on Apple Silicon Macs](https://derflounder.wordpress.com/2023/03/10/granting-volume-owner-status-on-apple-silicon-macs/)

[RSS feed](https://derflounder.wordpress.com/feed/ "Subscribe to this blog...")

* [Google](http://fusion.google.com/add?feedurl=https://derflounder.wordpress.com/feed/ "Subscribe with Google")
* [Youdao](http://reader.youdao.com/#url=https://derflounder.wordpress.com/feed/ "Subscribe with Youdao")
* [Xian Guo](http://www.xianguo.com/subscribe.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Xian Guo")
* [Zhua Xia](http://www.zhuaxia.com/add_channel.php?url=https://derflounder.wordpress.com/feed/ "Subscribe with Zhua Xia")
* [My Yahoo!](http://add.my.yahoo.com/rss?url=https://derflounder.wordpress.com/feed/ "Subscribe with My Yahoo!")
* [newsgator](http://www.newsgator.com/ngs/subscriber/subfext.aspx?url=https://derflounder.wordpress.com/feed/ "Subscribe with newsgator")
* [Bloglines](http://www.bloglines.com/sub/https%3A//derflounder.wordpress.com/feed/ "Subscribe with Bloglines")
* [iNezha](http://inezha.com/add?url=https://derflounder.wordpress.com/feed/ "Subscribe with iNezha")

March 2023

| M | T | W | T | F | S | S |
| --- | --- | --- | --- | --- | --- | --- |
|  | | 1 | 2 | [3](https://derflounder.wordpress.com/2023/03/03/) | [4](https://derflounder.wordpress.com/2023/03/04/) | 5 |
| 6 | 7 | 8 | 9 | [10](https://derflounder.wordpress.com/2023/03/10/) | 11 | 12 |
| 13 | 14 | 15 | [16](https://derflounder.wordpress.com/2023/03/16/) | 17 | 18 | 19 |
| 20 | 21 | 22 | 23 | 24 | 25 | 26 |
| 27 | 28 | 29 | 30 | 31 |  | |

[« Feb](https://derflounder.wordpress.com/2023/02/)

[Apr »](https://derflounder.wordpress.com/2023/04/)

### Recent Comments

|  |  |
| --- | --- |
| ![Chan's avatar](https://0.gravatar.com/avatar/00b00eb773de8fe8550f2e8e9783e9cff8a7896bc4af11cbc0d322a3b36d15ae?s=48&d=identicon&r=G) | Chan on...