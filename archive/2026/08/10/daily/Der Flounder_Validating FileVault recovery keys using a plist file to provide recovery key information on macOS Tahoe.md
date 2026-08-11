---
title: Validating FileVault recovery keys using a plist file to provide recovery key information on macOS Tahoe
url: https://derflounder.wordpress.com/2026/08/10/validating-filevault-recovery-keys-using-a-plist-file-to-provide-recovery-key-information-on-macos-tahoe/
source: Der Flounder
date: 2026-08-10
fetch_date: 2026-08-11T03:30:05.824507
---

# Validating FileVault recovery keys using a plist file to provide recovery key information on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Validating FileVault recovery keys using a plist file to provide recovery key information on macOS Tahoe

## Validating FileVault recovery keys using a plist file to provide recovery key information on macOS Tahoe

August 10, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

As part of a recent discussion in the [Mac Admins Slack](https://macadmins.org/), it was asked if it was possible to validate a [FileVault personal recovery key](https://support.apple.com/en-is/guide/mac-help/mh35881/mac) (PRK) without having to interactively enter it. Normally, to validate a PRK using the [fdesetup command line tool](https://www.manpagez.com/man/8/fdesetup/), you would use the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | fdesetup validaterecovery |

[view raw](https://gist.github.com/rtrouton/a2dd3eee9ec449f271549f43e83fdae8/raw/5d89324132f5b9008a49f2bb77effd938017ffe8/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/a2dd3eee9ec449f271549f43e83fdae8#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

You’ll then be prompted to enter the PRK. This is an alphanumeric string separated by dashes, which should look similar to what’s shown below:

**XGRX-W8ZG-747N-KWQT-CQAV-FC49**

The output of running the command should look similar to what’s shown below. If the PRK is valid, the command should return a value of **true**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/08/screenshot-2026-08-10-at-11.45.32am.png?w=595 "Screenshot 2026-08-10 at 11.45.32 AM.png")

If not, the command will return a value of **false**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/08/screenshot-2026-08-10-at-11.46.05am.png?w=595 "Screenshot 2026-08-10 at 11.46.05 AM.png")

This method assumes you can interactively enter the PRK information. If an interactive entry of the PRK information is not an option for some reason, the **validaterecovery** function includes an **-inputplist** option. This allows the PRK information to be stored in a plist file and be read from that file. For more details, please see below the jump.

In this scenario, you would create a plist file formatted like the one shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>Password</key> |
|  | <string>recovery\_key\_value\_goes\_here</string> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/6a60f3caf9424129b5a976ea5656e515/raw/fc1f9d1fb506575a42a630427230131954de8fc1/filename.plist)
 [filename.plist](https://gist.github.com/rtrouton/6a60f3caf9424129b5a976ea5656e515#file-filename-plist)
hosted with ❤ by [GitHub](https://github.com)

Once you have the plist file created and stored in a location you can access, you can then run the following command to validate the recovery key using the information stored in the plist file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | fdesetup validaterecovery -inputplist < /path/to/filename.plist |

[view raw](https://gist.github.com/rtrouton/0acc95d3e2e6dba0c89ed7333ed7ea64/raw/bcbb01d984671ad504e2234c34bc81f9a6108050/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0acc95d3e2e6dba0c89ed7333ed7ea64#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Assuming that the PRK was **XGRX-W8ZG-747N-KWQT-CQAV-FC49** and stored in a file named **recoverykey.plist** located in the **/Users/Shared** directory, the **recoverykey.plist** file’s contents would look like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | <?xml version="1.0" encoding="UTF-8"?> |
|  | <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "[http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt](http://www.apple.com/DTDs/PropertyList-1.0.dtd%22%26gt); |
|  | <plist version="1.0"> |
|  | <dict> |
|  | <key>Password</key> |
|  | <string>XGRX-W8ZG-747N-KWQT-CQAV-FC49</string> |
|  | </dict> |
|  | </plist> |

[view raw](https://gist.github.com/rtrouton/005362101a8e93001a527cd961645af1/raw/c7b531dffb129190ae73b63690b189df05e8ceb4/recoverykey.plist)
 [recoverykey.plist](https://gist.github.com/rtrouton/005362101a8e93001a527cd961645af1#file-recoverykey-plist)
hosted with ❤ by [GitHub](https://github.com)

You could then run the following command to validate the PRK using the **recoverykey.plist** file stored in the **/Users/Shared** directory:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | fdesetup validaterecovery -inputplist < /Users/Shared/recovery.plist |

[view raw](https://gist.github.com/rtrouton/5a78025941dbf9c490fd81ca342d5305/raw/659b7744e34be3a097a68dfb2110a0927d027ce2/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5a78025941dbf9c490fd81ca342d5305#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If the PRK stored in the plist file is the current valid PRK, you should get a value of **true**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/08/screenshot-2026-08-10-at-11.47.48am.png?w=595 "Screenshot 2026-08-10 at 11.47.48 AM.png")

Otherwise, you will get a value of **false**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/08/screenshot-2026-08-10-at-12.03.28pm.png?w=595 "Screenshot 2026-08-10 at 12.03.28 PM.png")

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/08/10/validating-filevault-recovery-keys-using-a-plist-file-to-provide-recovery-key-information-on-macos-tahoe/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* Mor...