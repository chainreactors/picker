---
title: Detecting successful MDM command execution on macOS Sequoia
url: https://derflounder.wordpress.com/2024/12/21/detecting-successful-mdm-command-execution-on-macos-sequoia/
source: Der Flounder
date: 2024-12-22
fetch_date: 2025-10-06T19:33:08.042664
---

# Detecting successful MDM command execution on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Mobile Device Management](https://derflounder.wordpress.com/category/mobile-device-management/) > Detecting successful MDM command execution on macOS Sequoia

## Detecting successful MDM command execution on macOS Sequoia

December 21, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the challenges in figuring out why a Mac isn’t responding to MDM commands is sometimes just figuring out if the Mac is receiving MDM commands at all. Fortunately, this is possible to figure out via the unified system logging using the right [predicates](https://eclecticlight.co/2016/10/17/log-a-primer-on-predicates/) when searching. For more details, please see below the jump.

To start, send an MDM command to the device in question. If your MDM server says it sent successfully, see what shows up on the Mac’s end using the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –predicate 'process=="mdmclient" OR subsystem=="com.apple.ManagedClient"' –info –last 10m |

[view raw](https://gist.github.com/rtrouton/88f910cc3745f346c2cdc32614818c8e/raw/5c52a96677bb02a52f1ef2357c5d5541b6493b7f/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/88f910cc3745f346c2cdc32614818c8e#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This will likely give you a large number of log entries, but it’s possible to filter for what you’re looking for. For example, a [blank push remote command](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Remote_Commands_for_Computers.html) sent from a Jamf Pro MDM server will include a log entry that looks similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | 2024-12-21 13:04:21.263154-0500 0x4d0d Default 0x0 1738 7 mdmclient: [com.apple.ManagedClient:MDMDaemon] [\*] [0:MDMDaemon:<0x4d0d>] Processing server request: DeclarativeManagement for: <Device> (3fb48527-9aaa-492d-94fc-efd999d812a3) PowerNap: no |

[view raw](https://gist.github.com/rtrouton/3afbec18a5aeac6ac80aba516e684089/raw/9d7148989bac677241613ccb3b441de386542549/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3afbec18a5aeac6ac80aba516e684089#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Since we can see from the log entry that the relevant process is **mdmclient** and the string to search for includes “**Processing server request: DeclarativeManagement for**“, then if you know you sent a blank push within the last ten minutes you can use the following command to see if the entry appears in the returned logs:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –info –predicate 'process=="mdmclient" AND eventMessage contains "Processing server request: DeclarativeManagement for"' –last 10m |

[view raw](https://gist.github.com/rtrouton/df2e910b15004beea84235991048d00b/raw/f373ada75b109a90d891cd6b968887a604d314e5/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/df2e910b15004beea84235991048d00b#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

That should pull up the relevant log entry:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % /usr/bin/log show –info –predicate 'process=="mdmclient" AND eventMessage contains "Processing server request: DeclarativeManagement for"' –last 10m |
|  | Filtering the log data using "process == "mdmclient" AND composedMessage CONTAINS "Processing server request: DeclarativeManagement for"" |
|  | Skipping debug messages, pass –debug to include. |
|  | Timestamp Thread Type Activity PID TTL |
|  | 2024-12-21 14:18:44.084210-0500 0xb9d7 Default 0x0 2867 7 mdmclient: [com.apple.ManagedClient:MDMDaemon] [\*] [0:MDMDaemon:<0xb9d7>] Processing server request: DeclarativeManagement for: <Device> (a3a16dd4-ba49-4d3e-bd67-39c48dc2fc32) PowerNap: no |
|  | ——————————————————————————————————————– |
|  | Log – Default: 1, Info: 0, Debug: 0, Error: 0, Fault: 0 |
|  | Activity – Create: 0, Transition: 0, Actions: 0 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/f7219b4220e3a8415866348b0a68ee75/raw/df67e44baa3aff12a6cf8ba2553fb795be0d36ab/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/f7219b4220e3a8415866348b0a68ee75#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

From there, we can see the UUID identifier of the MDM command. In this example, the UUID is the following:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | a3a16dd4-ba49-4d3e-bd67-39c48dc2fc32 |

[view raw](https://gist.github.com/rtrouton/d1a924e6a30b1ad14983563bd0b2d3a9/raw/840000fe79ce7893538b497a6d4370d0715ea534/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/d1a924e6a30b1ad14983563bd0b2d3a9#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

We can then use that to figure out from the Mac’s side if the MDM command was successful by running the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –predicate 'process=="mdmclient" AND eventMessage contains "a3a16dd4-ba49-4d3e-bd67-39c48dc2fc32"' –info –last 10m |

[view raw](https://gist.github.com/rtrouton/fa82328509b263923e7126f652d13976/raw/6c55438ad3dd3cd54e54d47dc5d76897964c96e1/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/fa82328509b263923e7126f652d13976#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

From there, we should see output that looks similar to what’s shown ...