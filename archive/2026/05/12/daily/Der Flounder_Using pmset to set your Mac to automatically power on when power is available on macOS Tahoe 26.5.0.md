---
title: Using pmset to set your Mac to automatically power on when power is available on macOS Tahoe 26.5.0
url: https://derflounder.wordpress.com/2026/05/12/using-pmset-to-set-your-mac-to-automatically-power-on-when-power-is-available-on-macos-tahoe-26-5-0/
source: Der Flounder
date: 2026-05-12
fetch_date: 2026-05-13T05:46:06.957706
---

# Using pmset to set your Mac to automatically power on when power is available on macOS Tahoe 26.5.0

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Using pmset to set your Mac to automatically power on when power is available on macOS Tahoe 26.5.0

## Using pmset to set your Mac to automatically power on when power is available on macOS Tahoe 26.5.0

May 12, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

One of the features included with macOS Tahoe 26.5.0 is a new option in the **Energy** preferences in System Settings for automatically starting a Mac when power is connected to it, either following a power failure or when the Mac is plugged in to power.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/05/screenshot-2026-05-11-at-8.54.png?w=595 "Screenshot 2026-05-11 at 8.54.png")

This setting does not appear to be manageable via MDM or DDM management as of this time, but it can be managed via the [pmset command line tool](https://gist.github.com/rtrouton/a1c35d0baa77ba7ab27f7346d51e2754). For more details, please see below the jump.

In the **pmset** man page , there is an **autorestartatconnect** setting which is listed as controlling this behavior. The **autorestartatconnect** setting can be set to an integer value of **0** or **1**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/05/screenshot-2026-05-11-at-8.29.png?w=595 "Screenshot 2026-05-11 at 8.29.png")

To turn on automatic restart on power connect, the following command should be run with root privileges:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/pmset autorestartatconnect 1 |

[view raw](https://gist.github.com/rtrouton/925e7b218d990d025070cc0271bd826c/raw/8e7bc7675ba9d119687415fcbe00592eb2dafa39/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/925e7b218d990d025070cc0271bd826c#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % sudo /usr/bin/pmset autorestartatconnect 1 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/067f069bd4a521c6694aab8fbab6c846/raw/35d81cff264fdc40dedb17799cec8ab3f05725c0/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/067f069bd4a521c6694aab8fbab6c846#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To verify that the setting has been set, run the following command and see if it returns a value of **1**.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | pmset -g | awk '/autorestartatconnect/ {print $2}' | sed '/^$/d' |

[view raw](https://gist.github.com/rtrouton/b81f0ededc9da6e136bd2a63aae16a9a/raw/f1baed05a1483865e261e4722474ef757012f464/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/b81f0ededc9da6e136bd2a63aae16a9a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % pmset -g | awk '/autorestartatconnect/ {print $2}' | sed '/^$/d' |
|  | 1 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/8390bc9b0f0b989cad67414b4fc07073/raw/085423ee037882bd8b48177bb3e171bdc0cb47b1/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/8390bc9b0f0b989cad67414b4fc07073#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

In the **Energy** preferences in System Settings, you should see the **Start up when power is connected** setting is set to **Always**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/05/screenshot-2026-05-11-at-8.18.12pm.png?w=595 "Screenshot 2026-05-11 at 8.18.12 PM.png")

To turn off automatic restart on power connect, the following command should be run with root privileges:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/pmset autorestartatconnect 0 |

[view raw](https://gist.github.com/rtrouton/834378f6e193d78152ee2d8214912592/raw/d4d85b26c0118d2fd7f8bc2ff3c525b0d9397913/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/834378f6e193d78152ee2d8214912592#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@computername ~ % sudo /usr/bin/pmset autorestartatconnect 0 |
|  | username@computername ~ % |

[view raw](https://gist.github.com/rtrouton/a98ff0dbc83223c1a32d80fb0ea33393/raw/0c60b0144271e8f21c010f390b54aedc2e9ada96/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/a98ff0dbc83223c1a32d80fb0ea33393#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To verify that the setting has been set, run the following command and see if it returns a value of **0.**

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | pmset -g | awk '/autorestartatconnect/ {print $2}' | sed '/^$/d' |

[view raw](https://gist.github.com/rtrouton/b81f0ededc9da6e136bd2a63aae16a9a/raw/f1baed05a1483865e261e4722474ef757012f464/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/b81f0ededc9da6e136bd2a63aae16a9a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirect...