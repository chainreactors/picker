---
title: Granting Volume Owner status on Apple Silicon Macs
url: https://derflounder.wordpress.com/2023/03/10/granting-volume-owner-status-on-apple-silicon-macs/
source: Der Flounder
date: 2023-03-11
fetch_date: 2025-10-04T09:12:06.287232
---

# Granting Volume Owner status on Apple Silicon Macs

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Secure Token](https://derflounder.wordpress.com/category/secure-token/) > Granting Volume Owner status on Apple Silicon Macs

## Granting Volume Owner status on Apple Silicon Macs

March 10, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

macOS on Apple Silicon Macs includes a concept known as volume ownership. You must be a volume owner to perform the following tasks on an Apple Silicon Mac:

* [Make changes to startup security policy](https://support.apple.com/guide/deployment/startup-security-dep5810e849c/web) for a specific install of macOS.\*
* Be able to authorize the installation of [macOS software updates](https://support.apple.com/HT201541) or [macOS upgrades](https://support.apple.com/macos/upgrade).
* Authorize running [Erase All Contents and Settings](https://support.apple.com/HT212749).

\* There may be multiple installations of macOS on one Apple Silicon Mac; each macOS install would have their own startup security policy.

For more information on volume ownership, please see Apple’s Platform Deployment article linked below:

<https://support.apple.com/guide/deployment/use-secure-and-bootstrap-tokens-dep24dbdcf9e/web> (see the **Volume ownership** section.)

How do you get volume ownership though? It turns out that Apple has this currently set up on macOS as a two-fer deal: If an account account has [Secure Token](https://derflounder.wordpress.com/2018/01/20/secure-token-and-filevault-on-apple-file-system/), it is also granted volume ownership. For more details, please see below the jump.

To see which users on the Mac have Secure Token, run the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/diskutil apfs listCryptoUsers / |

[view raw](https://gist.github.com/rtrouton/97d489551f0e9670078ae925b90aa81f/raw/e2007f70aa4aca825e793f560fac4529e2703c33/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/97d489551f0e9670078ae925b90aa81f#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

The user accounts with Secure Token assigned should appear listed with the following information:

* Type: **Local Open Directory User**
* Volume Owner: **Yes**

![Screenshot-2023-03-10-at-4.42.10-PM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-10-at-4.42.10-pm.png?w=595)

In place of the account’s username, the account’s assigned UUID identifier (also referred to as a GeneratedUID) is listed. To get the account username, run the following command with the UUID identifier in the appropriate place:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/bin/dscl . -search /Users GeneratedUID UUID\_goes\_here | awk '{print $1}' | head -n 1 |

[view raw](https://gist.github.com/rtrouton/3fd99c8c9fc2a500c7c55df09d677138/raw/5e0825098154f97917216d0aef98d40cf500cf4b/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3fd99c8c9fc2a500c7c55df09d677138#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![Screenshot-2023-03-10-at-4.42.11-PM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-10-at-4.42.11-pm.png?w=595)

If the account you want to be a Volume Owner isn’t listed, you can check the account’s Secure Token status by running the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/sysadminctl -secureTokenStatus username\_goes\_here |

[view raw](https://gist.github.com/rtrouton/d9b19ebae708f5d778b246ded26a2316/raw/8174c5dcaaa0637066eb0b559e79cd923003b49e/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/d9b19ebae708f5d778b246ded26a2316#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

If the account does not have Secure Token assigned, the output of the command should tell you this.

![Screenshot-2023-03-10-at-4.52.54-PM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-10-at-4.52.54-pm.png?w=595)

To assign Secure Token (and Volume Owner) to the desired account, run the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/sysadminctl -secureTokenOn username\_goes\_here -password password\_goes\_here -adminUser user\_with\_secure\_token\_goes\_here -adminPassword admin\_password\_goes\_here |

[view raw](https://gist.github.com/rtrouton/ea554c06037ec8ab529240628e15fd94/raw/a244e543884fa8e682809ec8c22f08eaa93c648d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/ea554c06037ec8ab529240628e15fd94#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![Screenshot-2023-03-10-at-4.54.53-PM.png](https://derflounder.wordpress.com/wp-content/uploads/2023/03/screenshot-2023-03-10-at-4.54.53-pm.png?w=595)

If you want to be prompted for passwords in place of including them as part of the command in plaintext, enter a dash ( **–** ) where you would otherwise enter the relevant account’s password when running the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | /usr/sbin/sysadminctl -secureTokenOn username\_goes\_here -password – -adminUser user\_with\_secure\_token\_goes\_here -adminPassword – |

[view raw](https://gist.github.com/rtrouton/398f2d96113b7ba0d2ccb9191be2b655/raw/4e03da1c49d0718dce11f7ed8b58d42e7b6a1322/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/398f2d96113b7ba0d2ccb9191be2b655#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Once this has been done, you can verify that Secure Token has been assigned to the desired account by running the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https:/...