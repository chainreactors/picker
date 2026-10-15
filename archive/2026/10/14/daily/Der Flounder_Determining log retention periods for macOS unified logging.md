---
title: Determining log retention periods for macOS unified logging
url: https://derflounder.wordpress.com/2026/10/14/determining-log-retention-periods-for-macos-unified-logging/
source: Der Flounder
date: 2026-10-14
fetch_date: 2026-10-15T06:41:55.565282
---

# Determining log retention periods for macOS unified logging

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Logging](https://derflounder.wordpress.com/category/logging/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Determining log retention periods for macOS unified logging

## Determining log retention periods for macOS unified logging

October 14, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

Every so often when working with the unified logging system, you need to know how far back the current logging goes. After all, if you’re looking for logs for something that happened last week, it’s a good idea to check if your Mac’s logs actually go back that far.

You can accomplish this using the [log command line tool](https://www.manpagez.com/man/1/log/), using the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log stats –overview |

[view raw](https://gist.github.com/rtrouton/e99ef21a124d60d0afc227e77ff693ec/raw/25d747000aff8d0b5c3b5dc56de4d3d2e530187a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/e99ef21a124d60d0afc227e77ff693ec#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

**Note:** This command may take a few minutes to run while it builds the requested logging overview, so patience is recommended.

The overview includes a large amount of data about the logging currently stored on your Mac and among the items displayed will be the times and dates of both the oldest log entry and the newest log entry using the **start** and **end** values. The **start** value is the oldest and the **end** value is the newest.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/10/screenshot-2026-10-14-at-1.51.57pm.png?w=595 "Screenshot 2026-10-14 at 1.51.57 PM.png")

If you have a unified system log archive file, you can check for the archive’s oldest and newest log entries the same way:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log stats –overview –archive /path/to/archive\_file\_goes\_here |

[view raw](https://gist.github.com/rtrouton/9e3e7691d2e5b12cfc47e6d24b3adfe7/raw/61dacccfea66aef6b25e36e4e5ab2ccb8290df12/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/9e3e7691d2e5b12cfc47e6d24b3adfe7#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2026/10/screenshot-2026-10-14-at-1.59.11pm.png?w=595 "Screenshot 2026-10-14 at 1.59.11 PM.png")

By default, this information is displayed in a human-readable format but it can also be exported in JSON format.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log stats –overview –style json |

[view raw](https://gist.github.com/rtrouton/a0c7240ef6bd4739131d91c27bfc3581/raw/798539d6f780ff70e56b5c8724e43631cbeb9a8a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/a0c7240ef6bd4739131d91c27bfc3581#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2026/10/screenshot-2026-10-14-at-2.02.02-pm.png?w=595 "Screenshot 2026-10-14 at 2.02.02 PM.png")

This is convenient because now we can use command line tools like [jq](https://jqlang.org) to [parse the JSON output](https://jqlang.org/manual) and return just the **start** and **end** values we want. For example, the following command should get the **start** and **end** values and convert them to being displayed in UTC time:

**Note:** By default, the **log** command will use your computer’s local time zone for displaying the times. I’m using UTC here as a personal preference.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log stats –overview –style json | /usr/bin/jq -r '.start, .end | sub("\\.[0-9]+"; "")' | { read -r s; read -r e; echo "Oldest log entry: $(/bin/date -u -jf "%Y-%m-%d %H:%M:%S%z" "$s" "+%Y-%m-%d %H:%M:%S UTC")"; echo "Newest log entry: $(/bin/date -u -jf "%Y-%m-%d %H:%M:%S%z" "$e" "+%Y-%m-%d %H:%M:%S UTC")"; } |

[view raw](https://gist.github.com/rtrouton/5e70a35a66304cb3b3210ef3c0293239/raw/a49114a592fbe0d4a19bd066de042402be9ed55a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5e70a35a66304cb3b3210ef3c0293239#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The output from this command should look similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@ZCDP1X75FT ~ % /usr/bin/log stats –overview –style json | /usr/bin/jq -r '.start, .end | sub("\\.[0-9]+"; "")' | { read -r s; read -r e; echo "Oldest log entry: $(/bin/date -u -jf "%Y-%m-%d %H:%M:%S%z" "$s" "+%Y-%m-%d %H:%M:%S UTC")"; echo "Newest log entry: $(/bin/date -u -jf "%Y-%m-%d %H:%M:%S%z" "$e" "+%Y-%m-%d %H:%M:%S UTC")"; } |
|  | Oldest log entry: 2026-09-28 17:45:16 UTC |
|  | Newest log entry: 2026-10-14 21:08:58 UTC |
|  | username@ZCDP1X75FT ~ % |

[view raw](https://gist.github.com/rtrouton/371c6293452c34d2547c048b98ff6612/raw/3373e039e7b7befc2b229406d971a8aa4d045fb3/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/371c6293452c34d2547c048b98ff6612#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You can do the same with a unified system log archive file using a command like the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/log stats –overview –style json –archive /path/to/archive\_file\_goes\_here | /usr/bin/jq -r '.start, .end | sub("\\.[0-9]+"; "")' | { read -r s; read -r e; echo "Oldest log entry: $(/bin/date -u -jf "%Y-%m-%d %H:%M:%S%z" "$s" "+%Y-%m-%d %H:%M:%S UTC")"; echo "Newest log entry: $(/bin/date -u -jf "%Y-%m-%d %H:%M:%S%z" "$e" "+%Y...