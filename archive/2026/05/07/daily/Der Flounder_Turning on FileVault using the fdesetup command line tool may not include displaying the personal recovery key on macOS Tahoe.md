---
title: Turning on FileVault using the fdesetup command line tool may not include displaying the personal recovery key on macOS Tahoe
url: https://derflounder.wordpress.com/2026/05/07/turning-on-filevault-using-the-fdesetup-command-line-tool-may-not-include-displaying-the-personal-recovery-key-on-macos-tahoe/
source: Der Flounder
date: 2026-05-07
fetch_date: 2026-05-08T04:55:32.312845
---

# Turning on FileVault using the fdesetup command line tool may not include displaying the personal recovery key on macOS Tahoe

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [fdesetup](https://derflounder.wordpress.com/category/fdesetup/), [FileVault 2](https://derflounder.wordpress.com/category/filevault-2/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Turning on FileVault using the fdesetup command line tool may not include displaying the personal recovery key on macOS Tahoe

## Turning on FileVault using the fdesetup command line tool may not include displaying the personal recovery key on macOS Tahoe

May 7, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

I recently did some FileVault testing using the [fdesetup command line tool](https://www.manpagez.com/man/8/fdesetup/) on macOS Tahoe and noticed something was missing when I did so. On prior versions of macOS, when you ran the **fdesetup enable** command, it would prompt you for the username and password of the user account you wanted to enable for FileVault and then it would show you the [personal recovery key](https://support.apple.com/guide/mac-help/mh35881/mac) which was created as part of turning on FileVault. Here’s how this process appears on macOS Sequoia:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@Z7M1XGLX3L ~ % sudo fdesetup enable |
|  | Password: |
|  | Enter the user name:username |
|  | Enter the password for user 'username': |
|  | Recovery key = 'YBC9-AQEF-WPME-WWRW-VHXO-WB3Y' |
|  | username@Z7M1XGLX3L ~ % |

[view raw](https://gist.github.com/rtrouton/5341bb51000c57f0edf541fd2fb336db/raw/70299446983478f464ac9d9b9c0df0f636a24574/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5341bb51000c57f0edf541fd2fb336db#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

One thing that’s very important to know is that the personal recovery key information is not saved anywhere. You will need to make a record of it when it’s displayed or you will not have it later.

On macOS Tahoe, this recovery key information is not displayed when the same command is run:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@Z44QF45X37 ~ % sudo fdesetup enable |
|  | Password: |
|  | Enter the user name:username |
|  | Enter the password for user 'username': |
|  | username@Z44QF45X37 ~ % |

[view raw](https://gist.github.com/rtrouton/0932118e5140e002c6147844aa7f42af/raw/7c2ec22122be01b44b20dede8a9972d8a12f9a49/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0932118e5140e002c6147844aa7f42af#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, the recovery key is created. This can be verified by running the following command and verifying that there is an entry for **Personal Recovery User**:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | diskutil apfs listcryptoUsers / |

[view raw](https://gist.github.com/rtrouton/218c0dacdf59057cce7b6de52b9a60c5/raw/0a1cdfbf7e71a98ab2d791cfce98ddd23bf75048/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/218c0dacdf59057cce7b6de52b9a60c5#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Here’s what the Terminal output looks like when you turn on FileVault using the **fdesetup** command line tool and then use the [diskutil command line tool](https://www.manpagez.com/man/8/diskutil/) to check and see if there is a **Personal Recovery User** entry:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@Z44QF45X37 ~ % sudo fdesetup enable |
|  | Password: |
|  | Enter the user name:username |
|  | Enter the password for user 'username': |
|  | username@Z44QF45X37 ~ % diskutil apfs listcryptoUsers / |
|  | Cryptographic users for disk3s1s1 (3 found) |
|  | | |
|  | +– DA145BD0-81C7-41AA-9676-794E0A14B63D |
|  | | Type: Local Open Directory User |
|  | | Volume Owner: Yes |
|  | | |
|  | +– 2457711A-523C-4604-B75A-F48A571D5036 |
|  | | Type: MDM Bootstrap Token External Key |
|  | | Volume Owner: Yes |
|  | | |
|  | +– EBC6C064-0000-11AA-AA11-00306543ECAC |
|  | Type: Personal Recovery User |
|  | Volume Owner: Yes |
|  |  |
|  | username@Z44QF45X37 ~ % |

[view raw](https://gist.github.com/rtrouton/93d29b8984627c0696bbe1836b7281bd/raw/aae4e35cf2d4347f0d622c52d2b7035d9e4ba621/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/93d29b8984627c0696bbe1836b7281bd#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

How to fix this? Fortunately, the **fdesetup** command line tool includes an option to output relevant information to plist format as part of turning on FileVault using the **fdesetup** command line tool’s **enable** option. This information includes the personal recovery key. For more details, please see below the jump.

For example, running the following command will turn on FileVault using the **fdesetup** command line tool and write a plist file which includes the recovery key to [standard output](https://en.wikipedia.org/wiki/Standard_streams):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | fdesetup enable -outputplist |

[view raw](https://gist.github.com/rtrouton/fe18830c743c85898a7aca1988a3bb0a/raw/1be27d5ba22d6c3f51e482a03bc6baa0c6d77448/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/fe18830c743c85898a7aca1988a3bb0a#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Here’s what the Terminal output looks like when you turn on FileVault using the **fdesetup** command line tool and include the option of exporting to plist format:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | username@Z44QF45X37 ~ % sudo fdesetup enable -outputplist |
|  | Password: |
|  | Enter the user name:username |
|  | Enter ...