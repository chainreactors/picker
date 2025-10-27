---
title: Backing up Der Flounder Revisited Once Again
url: https://derflounder.wordpress.com/2023/03/03/backing-up-der-flounder-revisited-once-again/
source: Der Flounder
date: 2023-03-04
fetch_date: 2025-10-04T08:36:02.721968
---

# Backing up Der Flounder Revisited Once Again

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Backup](https://derflounder.wordpress.com/category/backup/), [Linux](https://derflounder.wordpress.com/category/linux/), [Raspberry Pi](https://derflounder.wordpress.com/category/raspberry-pi/) > Backing up Der Flounder Revisited Once Again

## Backing up Der Flounder Revisited Once Again

March 3, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

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

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | apt-get update |
|  | apt-get install wget |

[view raw](https://gist.github.com/rtrouton/50e056dbe18724b8b35b17784f92dac6/raw/f0702a1491482e624acf23b32318ccc3bfedc584/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/50e056dbe18724b8b35b17784f92dac6#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

2. Create a backup directory in the **pi** user’s home directory by running the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | mkdir -p /home/pi/derflounder\_backup |

[view raw](https://gist.github.com/rtrouton/e2c954862e8ceb255db091c2ac4b73c2/raw/260dde16afe89a6623e82e79005ea4a1784b8259/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e2c954862e8ceb255db091c2ac4b73c2#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

3. Set up the following script as **/usr/local/bin/der\_flounder\_backup.sh**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | backupDirectoryPath="/home/pi/derflounder\_backup" |
|  | website="<https://derflounder.wordpress.com&quot>; |
|  |  |
|  | /usr/bin/wget –show-progress –mirror –convert-links –adjust-extension –page-requisites –no-parent -P "$backupDirectoryPath" ${website} |

[view raw](https://gist.github.com/rtrouton/57d6b0811eefe1dedd40fa4348288312/raw/63db3690758a55f1256f2faa649e0aad15d5bc0e/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/57d6b0811eefe1dedd40fa4348288312#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

For the script itself, here’s what the various options are doing:

* **–show-progress**: When running the script manually, show what’s being currently downloaded.
* **–mirror**: Makes the download recursive, with recursive browsing and infinite recursion depth.
* **–convert-links**: Convert all the links to relative, so it will be suitable for offline viewing.
* **–adjust-extension**: Adds suitable filename extensions to filenames, (html, css, etc.) depending on their content-type.
* **–page-requisites**: Download support files like CSS style-sheets and images required to properly display the page offline.
* **–no-parent**: When recursing, do not go up to the parent directory.
* **-P**: Set directory where all files should be downloaded to.

4. Set up a cron job like the one shown below to run the backup script, with any messages from running the cron job sent to **/dev/null**. In my case, I set it up in the **pi** user’s crontab to run nightly at 2:00 AM:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 0 2 \* \* \* /usr/local/bin/der\_flounder\_backup.sh >/dev/null 2>&1 |

[view raw](https://gist.github.com/rtrouton/f03a94a6ffb44ae9e159421d87b3c70f/raw/3c6b41775268c375990f69ee1bb0b81a43abfcd1/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/f03a94a6ffb44ae9e159421d87b3c70f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Meanwhile, like the hosts which went before it, I’m also backing up the Raspberry Pi that the backup is stored on, so that I have two copies of the backed-up data available.

### Share this:

* [Click to print (Opens in new window)
  Print](https://derflounder.wordpress.com/2023/03/03/backing-up-der-flounder-revisited-once-again/#print?share=print)
* Click to email a link to a friend (Opens in new window)
  Email
* More

* [Click to share on Facebook (Opens in new window)
  Facebook](https://derflounder.wordpress.com/2023/03/03/backing-up-der-flounder-revisited-once-again/?share=facebook)
* [Click to share on LinkedIn (Opens in new window)
  LinkedIn](https://derflounder.wordpress.com/2023/03/03/backing-up-der-flounder-revisited-once-again/?share=linkedin)
* [Click to share on Re...