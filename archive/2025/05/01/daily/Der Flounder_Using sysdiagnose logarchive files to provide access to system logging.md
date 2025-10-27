---
title: Using sysdiagnose logarchive files to provide access to system logging
url: https://derflounder.wordpress.com/2025/04/30/using-sysdiagnose-logarchive-files-to-provide-access-to-system-logging/
source: Der Flounder
date: 2025-05-01
fetch_date: 2025-10-06T22:24:05.171295
---

# Using sysdiagnose logarchive files to provide access to system logging

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Logging](https://derflounder.wordpress.com/category/logging/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Using sysdiagnose logarchive files to provide access to system logging

## Using sysdiagnose logarchive files to provide access to system logging

April 30, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

When it comes to figuring out what is happening on an Apple device, [creating a sysdiagnose file is usually the way to go](https://support.kandji.io/kb/how-to-generate-a-sysdiagnose-in-macos). Sysdiagnose files are the final outcome of your Apple device running almost every performance and problem tracing tool available, then taking the resulting logs and bundling them all together into one compressed file. However, because these logs are intended for use and analysis by Apple’s engineers, they can almost overwhelm with information.

One way to manage this flood of data is to use the **system\_logs.logarchive** file [included with every sysdiagnose file](https://developer.apple.com/forums/thread/739560). The **system\_logs.logarchive** file is [a snapshot of the unified system log](https://developer.apple.com/forums/thread/705868) as of the time that the sysdiagnose was created, so it has a large amount of information about what was happening on that Apple device at the time.

Accessing the information in the **system\_logs.logarchive** file can be accomplished using the following process:

1. Get the desired sysdiagnose file
2. Uncompress it.
3. In the resulting directory, locate the **system\_logs.logarchive** file.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.30.26pm.png?w=599&h=214 "Screenshot 2025-04-30 at 5.30.26 PM.png")

You can work with the **system\_logs.logarchive** file using a couple of tools included with macOS:

* [Console.app](https://support.apple.com/guide/console/welcome/mac)
* The [log command line tool](https://ss64.com/mac/log.html)

For more information, please see below the jump.

**Using Console.app**

To access the **system\_logs.logarchive** file using **Console.app**, double-click on the **system\_logs.logarchive** file. It should then open the **Console** app if needed and display a window showing the logs from the **system\_logs.logarchive** file.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.36.55pm.png?w=595 "Screenshot 2025-04-30 at 5.36.55 PM.png")

From there, you can use the **Console** app’s [search functionality](https://support.apple.com/guide/console/find-log-messages-and-activities-cnslbf30b61a/mac) to find what you’re looking for.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.37.07pm.png?w=595 "Screenshot 2025-04-30 at 5.37.07 PM.png")

**Using the log command line tool**

If viewing logs using the **log** command line tool, you can use the **log** tool’s **show** function to specify that you want to reference from the **system\_logs.logarchive** file. For example, you can use a command like the one shown below to access the information in the **system\_logs.logarchive** file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –info –debug –archive /path/to/system\_logs.logarchive |

[view raw](https://gist.github.com/rtrouton/2c52d2cb507c6214ce7b1509b20974ef/raw/815bde1f706e2e2c6b85d042e1c5c88c8141f0f4/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/2c52d2cb507c6214ce7b1509b20974ef#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.38.26pm.png?w=595 "Screenshot 2025-04-30 at 5.38.26 PM.png")

This will likely result in a huge amount of data flying quickly through your Terminal window. It will likely make sense to provide additional filters to get back just the data you want.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.46.16pm.png?w=595 "Screenshot 2025-04-30 at 5.46.16 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.46.29pm.png?w=595 "Screenshot 2025-04-30 at 5.46.29 PM.png")

For example, if you want to get only information on mobile device management traffic which was captured by the system log, you can use a command like the one shown below to add [predicates](https://eclecticlight.co/2016/10/17/log-a-primer-on-predicates/) which can be used by the log command line tool:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –info –debug –archive /path/to/system\_logs.logarchive –predicate 'process=="mdmclient" OR subsystem=="com.apple.ManagedClient" and category == "HTTPUtil"' |

[view raw](https://gist.github.com/rtrouton/4ae07c97f34ceff2a30a3dec67b1fed1/raw/d985af1bdb5b7f0346ffa56f4f6f7672f7bbec26/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/4ae07c97f34ceff2a30a3dec67b1fed1#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.48.57pm.png?w=595 "Screenshot 2025-04-30 at 5.48.57 PM.png")

That should display only the information defined by the predicates, which are:

* Information logged from the **mdmclient** process
* Information logged from the **com.apple.ManagedClient** subsystem
* Information logged within the **HTTPUtil** logging category

This should produce a much smaller and more focused stream of information.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/04/screenshot-2025-04-30-at-5.48.58pm.png?w=595 "Screenshot 2025-04-30 at 5.48.58 PM.png")

Depending on how recently the sysdiagnose was created, you may be able to narrow down the returned data even further by specifying a timeframe. For example, if you wanted to check for only information logged from midnight of April 28th, 2025 to midnight of April 29th, 2025, you could use a command like the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log show –info –debug –archive /path/to/system\_logs.logarchive –predicate 'process=="mdmclient" OR subsystem=="com.apple.ManagedClient" and category == "HTTPUtil"' –start '2025-04-28 00:00:00' –end '2025-04-29 00:00:00' |

[view raw](https://gist.github.com/rtrouton/9c40d1b4af0ef5814fe5da275dc9c06b/raw/210e89870f1ca53decd07dee0e80a74e27ea0640/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9c40d1b4af0ef5814fe5da275dc9c06b#file-gistf...