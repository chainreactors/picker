---
title: Backing up Der Flounder Revisited Once Again
url: https://buaq.net/go-151912.html
source: unSafe.sh - 不安全
date: 2023-03-05
fetch_date: 2025-10-04T08:43:20.233855
---

# Backing up Der Flounder Revisited Once Again

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

![]()

Backing up Der Flounder Revisited Once Again

Home > Backup, Linux, Raspberry Pi > Backing up Der Flounder Revisited Once AgainBacking
*2023-3-4 05:20:16
Author: [derflounder.wordpress.com(查看原文)](/jump-151912.htm)
阅读量:34
收藏*

---

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Backup](https://derflounder.wordpress.com/category/backup/), [Linux](https://derflounder.wordpress.com/category/linux/), [Raspberry Pi](https://derflounder.wordpress.com/category/raspberry-pi/) > Backing up Der Flounder Revisited Once Again

## Backing up Der Flounder Revisited Once Again

[Eleven years ago](https://derflounder.wordpress.com/2012/03/19/backing-up-der-flounder/), I wrote a post on how I back up this blog. Overall, the reasons I’m backing up haven’t changed:

* I like this blog and don’t want to see it or its data disappear because of data loss
* WordPress.com’s free hosting doesn’t provide me with an automated backup method.

[Two years ago, I wrote another post](https://derflounder.wordpress.com/2021/02/12/backing-up-der-flounder-revisited/) on how I needed to switch from hosting on a Mac to now hosting on a Raspberry Pi. The overall methodology hadn’t changed, [I was creating a nightly mirror using HTTrack](http://btmash.com/article/2011-05-25/mirroring-website-using-httrack). This worked fine until the latest move to a new host in February 2023, where [HTTrack](https://debian.httrack.com) was failing for me because the Raspberry Pi was running headless without a connected display and **HTTrack** was having problems with trying to launch a headless browser. After an hour of futzing with it, I moved to using [wget](https://linux.die.net/man/1/wget). The **wget** tool has a number of handy options for mirroring websites, including the following:

* **–mirror**: Makes the download recursive, with recursive browsing and infinite recursion depth.
* **–convert-links**: Convert all the links to relative, so it will be suitable for offline viewing.
* **–adjust-extension**: Adds suitable filename extensions to filenames, (html, css, etc.) depending on their content-type.

Based on my research, using **wget** would be a decent replacement for what I had been doing with **HTTrack** and wouldn’t have the problems I was seeing with **HTTrack** not being able to launch a headless browser session. For those wanting to know more, please see below the jump.

The current backup host is a [Raspberry Pi 4](https://www.raspberrypi.org) running [Raspberry Pi OS Bullseye](https://en.wikipedia.org/wiki/Raspberry_Pi_OS). To set up an automated backup using **wget**, I used the following procedure:

1. Install [wget for Debian Bullseye](https://packages.debian.org/bullseye/wget) by running the commands below with root privileges:

2. Create a backup directory in the **pi** user’s home directory by running the following command:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

3. Set up the following script as **/usr/local/bin/der\_flounder\_backup.sh**

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | backupDirectoryPath="/home/pi/derflounder\_backup" |
|  | website="<https://derflounder.wordpress.com>" |
|  |  |
|  | /usr/bin/wget –show-progress –mirror –convert-links –adjust-extension –page-requisites –no-parent -P "$backupDirectoryPath" ${website} |

For the script itself, here’s what the various options are doing:

* **–show-progress**: When running the script manually, show what’s being currently downloaded.
* **–mirror**: Makes the download recursive, with recursive browsing and infinite recursion depth.
* **–convert-links**: Convert all the links to relative, so it will be suitable for offline viewing.
* **–adjust-extension**: Adds suitable filename extensions to filenames, (html, css, etc.) depending on their content-type.
* **–page-requisites**: Download support files like CSS style-sheets and images required to properly display the page offline.
* **–no-parent**: When recursing, do not go up to the parent directory.
* **-P**: Set directory where all files should be downloaded to.

4. Set up a cron job like the one shown below to run the backup script, with any messages from running the cron job sent to **/dev/null**. In my case, I set it up in the **pi** user’s crontab to run nightly at 2:00 AM:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Meanwhile, like the hosts which went before it, I’m also backing up the Raspberry Pi that the backup is stored on, so that I have two copies of the backed-up data available.

文章来源: https://derflounder.wordpress.com/2023/03/03/backing-up-der-flounder-revisited-once-again/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)