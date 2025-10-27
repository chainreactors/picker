---
title: Creating a sysdiagnose file using Activity Monitor
url: https://buaq.net/go-153776.html
source: unSafe.sh - 不安全
date: 2023-03-17
fetch_date: 2025-10-04T09:49:23.069182
---

# Creating a sysdiagnose file using Activity Monitor

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/2c863116ddff2e8e3f6e29834ef1801e.jpg)

Creating a sysdiagnose file using Activity Monitor

Home > Mac administration, macOS > Creating a sysdiagnose file using Activity MonitorCre
*2023-3-16 23:55:54
Author: [derflounder.wordpress.com(查看原文)](/jump-153776.htm)
阅读量:28
收藏*

---

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Creating a sysdiagnose file using Activity Monitor

## Creating a sysdiagnose file using Activity Monitor

The [sysdiagnose tool](https://www.manpagez.com/man/1/sysdiagnose) is used for gathering a large amount of diagnostic files and logging, and it’s often very useful when it comes to figuring out why a problem is happening. However, it can sometimes be challenging to get a sysdiagnose-generated file from someone who is not comfortable with using the Terminal as the usual method for generating a sysdiagnose file involves opening the Terminal and running commands there.

Fortunately, there’s also a way to generate a sysdiagnose file using Activity Monitor. This may be an alternate way to help get you the desired sysdiagnose file from someone who normally wouldn’t ever use the Terminal on macOS. For more details, please see below the jump.

Apple includes [how to generate a sysdiagnose file as part of the Activity Monitor User Guide](https://support.apple.com/guide/activity-monitor/run-system-diagnostics-actmntr2225/mac). For a step by step guide, please use the procedure below:

1. Launch Activity Monitor.

![Screenshot-2023-03-16-at-11.32.05-AM.png](https://derflounder.files.wordpress.com/2023/03/screenshot-2023-03-16-at-11.32.05-am.png?w=595)

2. Choose a method to generate the sysdiagnose file. There’s an option available in the **View** menu, where you can choose **Run System Diagnostics…**

![Screenshot-2023-03-16-at-11.34.16-AM.png](https://derflounder.files.wordpress.com/2023/03/screenshot-2023-03-16-at-11.34.16-am.png?w=595)

Another option is click the **System diagnostics options** pop-up menu (…) and select **System Diagnostics…**

![Screenshot-2023-03-16-at-11.33.04-AM.png](https://derflounder.files.wordpress.com/2023/03/screenshot-2023-03-16-at-11.33.04-am.png?w=595)

3. Click **OK** at the privacy agreement screen.

![Screenshot-2023-03-16-at-11.35.04-AM.png](https://derflounder.files.wordpress.com/2023/03/screenshot-2023-03-16-at-11.35.04-am.png?w=595)

After agreeing at the privacy agreement screen, a sysdiagnose file will be generated. This is a process that may take a few minutes to complete.

![Screenshot-2023-03-16-at-11.36.30-AM.png](https://derflounder.files.wordpress.com/2023/03/screenshot-2023-03-16-at-11.36.30-am.png?w=595)

Once the sysdiagnose file has been created, a Finder window will appear showing the location of the sysdiagnose file, which will be a compressed file named something similar to what’s shown below:

**sysdiagnose\_2023.03.16\_11-35-09-0400\_macOS\_iMacPro1-1\_22D68.tar.gz**

**![Screenshot-2023-03-16-at-11.38.04-AM.png](https://derflounder.files.wordpress.com/2023/03/screenshot-2023-03-16-at-11.38.04-am.png?w=595)**

文章来源: https://derflounder.wordpress.com/2023/03/16/creating-a-sysdiagnose-file-using-activity-monitor/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)