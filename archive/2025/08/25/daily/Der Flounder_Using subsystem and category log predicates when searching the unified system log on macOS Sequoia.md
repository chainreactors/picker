---
title: Using subsystem and category log predicates when searching the unified system log on macOS Sequoia
url: https://derflounder.wordpress.com/2025/08/24/using-subsystem-and-category-log-predicates-when-searching-the-unified-system-log-on-macos-sequoia/
source: Der Flounder
date: 2025-08-25
fetch_date: 2025-10-07T00:16:42.689980
---

# Using subsystem and category log predicates when searching the unified system log on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Logging](https://derflounder.wordpress.com/category/logging/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Using subsystem and category log predicates when searching the unified system log on macOS Sequoia

## Using subsystem and category log predicates when searching the unified system log on macOS Sequoia

August 24, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

When searching the the unified system log on macOS using [predicates](https://eclecticlight.co/2016/10/17/log-a-primer-on-predicates/), it’s often useful to use logging [subsystems](https://derflounder.wordpress.com/2025/05/05/accessing-subsystem-logging-configurations-used-by-the-macos-unified-logging-on-macos-sequoia/) when searching for information. For example, as part of a previous post on finding [DDM status information in the logs](https://derflounder.wordpress.com/2025/08/19/reading-ddm-logging-on-macos-sequoia/), I used the following command to find data logged within the last ten minutes:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –predicate 'subsystem=="com.apple.remotemanagementd"' –info –last 10m |

[view raw](https://gist.github.com/rtrouton/368e65f05860854fdbc1b2e2159ab496/raw/ad6c5aa6009aaafe0cb90413b21f5d88b36858d8/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/368e65f05860854fdbc1b2e2159ab496#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This search uses the **com.apple.remotemanagementd** subsystem as a predicate when searching the logs. However, you can get even more granular by searching for a specific category of information within the **com.apple.remotemanagementd** subsystem. For example, let’s look at the data returned from running the command above:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@ZHW4T3TFTH ~ % sudo /usr/bin/log show –predicate 'subsystem=="com.apple.remotemanagementd"' –info –last 10m |
|  | Password: |
|  | Filtering the log data using "subsystem == "com.apple.remotemanagementd"" |
|  | Skipping debug messages, pass –debug to include. |
|  | Timestamp Thread Type Activity PID TTL |
|  | 2025-08-24 13:50:20.341060-0400 0x2a02 Default 0x0 423 0 remotemanagementd: [com.apple.remotemanagementd:XPCListenerDelegate] Evaluating new connection <NSXPCConnection: 0x97011c0a0> connection from pid 1177 on mach service named com.apple.remotemanagementd |
|  | 2025-08-24 13:50:20.341093-0400 0x2a02 Default 0x0 423 0 remotemanagementd: [com.apple.remotemanagementd:XPCListenerDelegate] Accepted new connection <NSXPCConnection: 0x97011c0a0> connection from pid 1177 on mach service named com.apple.remotemanagementd |
|  | 2025-08-24 13:50:20.341969-0400 0x2cd9 Default 0x86bf 423 0 remotemanagementd: [com.apple.remotemanagementd:XPCListenerDelegate] Finding management channel |
|  | 2025-08-24 13:50:20.345364-0400 0x2cd9 Default 0x86bf 423 0 remotemanagementd: [com.apple.remotemanagementd:XPCListenerDelegate] Found management channel |
|  | 2025-08-24 13:50:20.345616-0400 0x2cd9 Default 0x3d1c0 423 0 remotemanagementd: [com.apple.remotemanagementd:XPCListenerDelegate] Updating 50721780-919B-4DC3-992C-0645A2E38B01 with sync tokens response.. |
|  | 2025-08-24 13:50:20.345738-0400 0x2cd9 Info 0x3d1c2 423 0 remotemanagementd: [com.apple.remotemanagementd:client] Updating via sync tokens… |
|  | 2025-08-24 13:50:20.348540-0400 0x2cd9 Info 0x3d1c2 423 0 remotemanagementd: [com.apple.remotemanagementd:client] Updating finished |
|  | 2025-08-24 13:50:20.348554-0400 0x2cd9 Default 0x3d1c2 423 0 remotemanagementd: [com.apple.remotemanagementd:XPCListenerDelegate] Updated with 50721780-919B-4DC3-992C-0645A2E38B01 with sync tokens |
|  | 2025-08-24 13:50:20.348567-0400 0x2a02 Info 0x3d1c2 423 0 remotemanagementd: [com.apple.remotemanagementd:client] Syncing only if needed… |
|  | 2025-08-24 13:50:20.476354-0400 0x2a02 Info 0x3d1c2 423 0 remotemanagementd: [com.apple.remotemanagementd:client] There was no status report to send. |
|  | 2025-08-24 13:50:21.106677-0400 0x2cd9 Info 0x3d1c4 423 0 remotemanagementd: [com.apple.remotemanagementd:mdmConduit] Got back from MDM: 200 |
|  | 2025-08-24 13:50:21.172921-0400 0x2cd9 Info 0x3d1c4 423 0 remotemanagementd: [com.apple.remotemanagementd:mdmConduit] Successfully saved server tokens |
|  | 2025-08-24 13:50:21.180791-0400 0x302d Info 0x3d1c3 423 0 remotemanagementd: [com.apple.remotemanagementd:client] Sync only if needed finished |
|  | ——————————————————————————————————————– |
|  | Log – Default: 6, Info: 7, Debug: 0, Error: 0, Fault: 0 |
|  | Activity – Create: 0, Transition: 0, Actions: 0 |
|  | username@ZHW4T3TFTH ~ % |

[view raw](https://gist.github.com/rtrouton/489864e07db9a37a90ba476d37cdb94d/raw/78e6f56ca2c9a88044ae287ed07cea3272a7ef1d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/489864e07db9a37a90ba476d37cdb94d#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Within the data returned by searching for the **com.apple.remotemanagementd** subsystem, there’s several categories included as part of the subsystem log entries:

* **XPCListenerDelegate**
* **client**
* **mdmConduit**

Those categories show up following the listing for the **com.apple.remotemanagementd** subsystem in the returned log entries like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | com.apple.remotemanagementd:XPCListenerDelegate |
|  | com.apple.remotemanagementd:client |
|  | com.apple.remotemanagementd:mdmConduit |

[view raw](https://gist.github.com/rtrouton/c4ed69937847a6fb00f6833528f6af27/raw/a6c0a1d323828d195bf63d6d7c89b64d0510c464/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/c4ed69937847a6fb00f6833528f6af27#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If we wanted to get more granular and search the unified system log for only the logs associated with a particular category for a logging subsystem from the last ten minutes, the following command could be used to search using the following predicates:

* Subsystem: **com.apple.remotemanagementd**
* Category: **mdmConduit**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –predicate 'subsystem=="com.apple....