---
title: Successfully run sudo commands are no longer logged by default to unified logging on macOS Sequoia
url: https://derflounder.wordpress.com/2024/10/18/successfully-run-sudo-commands-are-no-longer-logged-by-default-to-unified-logging-on-macos-sequoia/
source: Der Flounder
date: 2024-10-19
fetch_date: 2025-10-06T18:50:02.501477
---

# Successfully run sudo commands are no longer logged by default to unified logging on macOS Sequoia

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Successfully run sudo commands are no longer logged by default to unified logging on macOS Sequoia

## Successfully run sudo commands are no longer logged by default to unified logging on macOS Sequoia

October 18, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

On macOS, you can use macOS’s [unified logging](https://www.macminivault.com/faq/introduction-to-macos-unified-logs/) to display commands run using the [sudo command line tool](https://support.apple.com/guide/terminal/enter-administrator-commands-apd5b0b6259-a7d4-4435-947d-0dff528912ba/mac). On macOS Sonoma and earlier, both successful and unsuccessful commands were logged by default. For example, here’s what you would see on macOS Sonoma when the following command was run first unsuccessfully and then successfully:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | sudo date |

[view raw](https://gist.github.com/rtrouton/3f33d4101e5bc6b609e39c25a68ff969/raw/da5e2bf0ddb56880be828aac36850cf50dd316dd/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3f33d4101e5bc6b609e39c25a68ff969#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-1.41.17e280afpm.png?w=595 "Screenshot 2024-10-18 at 1.41.17 PM.png")

Assuming you ran this command within the past three hours, you could use the following command to see both the successful and unsuccessful attempts to run the command above in the unified logs:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | log show –style syslog –predicate 'process == "sudo" AND composedMessage CONTAINS "COMMAND"' –last 3h |

[view raw](https://gist.github.com/rtrouton/46fbd36e76e82ede2eb9f39b6440f641/raw/8ed6463afd9878f71d35d5be951acdf78e4d3b31/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/46fbd36e76e82ede2eb9f39b6440f641#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

On macOS Sonoma, you should see both the successful and unsuccessful attempts to run the **sudo date** command (along with any other successful and unsuccessful attempts to use the **sudo** command.)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-1.44.37e280afpm.png?w=595 "Screenshot 2024-10-18 at 1.44.37 PM.png")

However, on macOS Sequoia if you run the same set of successful and unsuccessful attempts and then run the **log** command shown above, you would only see the unsuccessful attempts in the unified logs:

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-3.36.51e280afpm.png?w=595 "Screenshot 2024-10-18 at 3.36.51 PM.png")

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-3.39.50e280afpm.png?w=595 "Screenshot 2024-10-18 at 3.39.50 PM.png")

Why is this? For more details, please see below the jump.

On macOS Sequoia and earlier, the **sudo** command’s behavior is defined by the **sudoers** configuration file stored in the **/etc** directory. For macOS Sequoia, the following section was added to the **/etc/sudoers** configuration file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # Remove this line to log successful sudo launches. May contain sensitive |
|  | # information passed as arguments to the command |
|  | Defaults !log\_allowed |

[view raw](https://gist.github.com/rtrouton/0c30ee99a40294a62943deda8bb67886/raw/cf4712361d68d6e5534ded78997de991761ce297/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0c30ee99a40294a62943deda8bb67886#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-3.41.03e280afpm.png?w=595 "Screenshot 2024-10-18 at 3.41.03 PM.png")

The **!log\_allowed** setting means that the **sudo** command should not log allowed, or successful, attempts to run the sudo command. That means only the not allowed, or unsuccessful, commands will get logged to the unified logging.

If you want to configure the logging to use the pre-Sequoia behavior, you can edit the **/etc/sudoers** configuration file in one of the following ways:

1. Comment out the new **!log\_allowed** line:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # Remove this line to log successful sudo launches. May contain sensitive |
|  | # information passed as arguments to the command |
|  | # Defaults !log\_allowed |

[view raw](https://gist.github.com/rtrouton/a879834a04d9b42ca0918fb6ab0ae32a/raw/51c7918bae60a6cd31de0bb8e43fd9f7540487d9/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/a879834a04d9b42ca0918fb6ab0ae32a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-3.42.22-pm.png?w=595 "Screenshot 2024-10-18 at 3.42.22 PM.png")

2. Remove the new **!log\_allowed** line:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # Remove this line to log successful sudo launches. May contain sensitive |
|  | # information passed as arguments to the command |
|  |  |

[view raw](https://gist.github.com/rtrouton/2926589e4324d74c5506b0d5ff0093e3/raw/c88db22b6c1cc144f4b008fb5e16b918a32bdc2a/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/2926589e4324d74c5506b0d5ff0093e3#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2024/10/screenshot-2024-10-18-at-3.42.23e280afpm.png?w=595 "Screenshot 2024-10-18 at 3.42.23 PM.png")

Once the **/etc/sudoers** configuration file has been edited to either comment out or remove the new **!log\_allowed** line, the **sudo** command on macOS Sequoia should log both successful and unsuccessful commands to the unified lo...