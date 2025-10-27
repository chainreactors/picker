---
title: Deploying sudo configurations using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/05/27/deploying-sudo-configurations-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-05-28
fetch_date: 2025-10-06T22:25:30.676347
---

# Deploying sudo configurations using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Deploying sudo configurations using Blueprints in Jamf Pro

## Deploying sudo configurations using Blueprints in Jamf Pro

May 27, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As part of Apple’s unveiling of Declarative Device Management (DDM) at WWDC 2023, Apple announced that DDM management included the ability to manage sets of tamper-resistant system configuration files for different system services. As of this date, the following services built into macOS can be managed this way:

* **sshd**
* **sudo**
* **PAM**
* **CUPS**
* **Apache httpd**
* **bash**
* **zsh**

[Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) supports managing these services via the [Service configuration files component](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Blueprints_Components_Pro.html). Let’s see how this looks, using management of the [sudo command line tool](https://www.sudo.ws)‘s configuration as an example. For more details, please see below the jump.

By default, macOS 15.5.0 ships with a sudo configuration file that looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # |
|  | # Sample /etc/sudoers file. |
|  | # |
|  | # This file MUST be edited with the 'visudo' command as root. |
|  | # |
|  | # See the sudoers man page for the details on how to write a sudoers file. |
|  |  |
|  | ## |
|  | # Override built-in defaults |
|  | ## |
|  | Defaults env\_reset |
|  | Defaults env\_keep += "BLOCKSIZE" |
|  | Defaults env\_keep += "COLORFGBG COLORTERM" |
|  | Defaults env\_keep += "\_\_CF\_USER\_TEXT\_ENCODING" |
|  | Defaults env\_keep += "CHARSET LANG LANGUAGE LC\_ALL LC\_COLLATE LC\_CTYPE" |
|  | Defaults env\_keep += "LC\_MESSAGES LC\_MONETARY LC\_NUMERIC LC\_TIME" |
|  | Defaults env\_keep += "LINES COLUMNS" |
|  | Defaults env\_keep += "LSCOLORS" |
|  | Defaults env\_keep += "SSH\_AUTH\_SOCK" |
|  | Defaults env\_keep += "TZ" |
|  | Defaults env\_keep += "DISPLAY XAUTHORIZATION XAUTHORITY" |
|  | Defaults env\_keep += "EDITOR VISUAL" |
|  | Defaults env\_keep += "HOME MAIL" |
|  |  |
|  | Defaults lecture\_file = "/etc/sudo\_lecture" |
|  |  |
|  | # Remove this line to log successful sudo launches. May contain sensitive |
|  | # information passed as arguments to the command |
|  | Defaults !log\_allowed |
|  |  |
|  | ## |
|  | # User alias specification |
|  | ## |
|  | # User\_Alias FULLTIMERS = millert, mikef, dowdy |
|  |  |
|  | ## |
|  | # Runas alias specification |
|  | ## |
|  | # Runas\_Alias OP = root, operator |
|  |  |
|  | ## |
|  | # Host alias specification |
|  | ## |
|  | # Host\_Alias CUNETS = 128.138.0.0/255.255.0.0 |
|  | # Host\_Alias CSNETS = 128.138.243.0, 128.138.204.0/24, 128.138.242.0 |
|  | # Host\_Alias SERVERS = master, mail, www, ns |
|  | # Host\_Alias CDROM = orion, perseus, hercules |
|  |  |
|  | ## |
|  | # Cmnd alias specification |
|  | ## |
|  | # Cmnd\_Alias PAGERS = /usr/bin/more, /usr/bin/pg, /usr/bin/less |
|  |  |
|  | ## |
|  | # User specification |
|  | ## |
|  |  |
|  | # root and users in group wheel can run anything on any machine as any user |
|  | root ALL = (ALL) ALL |
|  | %admin ALL = (ALL) ALL |
|  |  |
|  | ## Read drop-in files from /private/etc/sudoers.d |
|  | ## (the '#' here does not indicate a comment) |
|  | #includedir /private/etc/sudoers.d |

[view raw](https://gist.github.com/rtrouton/5e0d3c4bdfeda160e856e609e0834570/raw/f55d359a2f6447fd1b7ad82926e57bdea6697ead/sudoers)
 [sudoers](https://gist.github.com/rtrouton/5e0d3c4bdfeda160e856e609e0834570#file-sudoers)
hosted with ❤ by [GitHub](https://github.com)

We’re going to change the following line:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | %admin ALL = (ALL) ALL |

[view raw](https://gist.github.com/rtrouton/27d5864bf6bc9804323c370555b52b2c/raw/7f6ad4828e83cc0d6a50fcdc8cc9993402e32e79/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/27d5864bf6bc9804323c370555b52b2c#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-23-at-10.13.png?w=595 "Screenshot 2025-05-23 at 10.13.png")

To now read as follows:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | otheruser ALL = (ALL) ALL |

[view raw](https://gist.github.com/rtrouton/81bfadb96384956ae3dc1cb6cd489dce/raw/37b8a94cc1de3d58e37b1bc475c26c3ba2eccd15/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/81bfadb96384956ae3dc1cb6cd489dce#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/05/screenshot-2025-05-23-at-10.14.png?w=595 "Screenshot 2025-05-23 at 10.14.png")

What this change does is remove the ability for all users of the **admin** group to use all available privileges for the **sudo** tool. In its place, now only a user account with the account shortname of **otheruser** has all available privileges for the sudo tool.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # |
|  | # Sample /etc/sudoers file. |
|  | # |
|  | # This file MUST be edited with the 'visudo' command as root. |
|  | # |
|  | # See the sudoers man page for the details on how to write a sudoers file. |
|  |  |
|  | ## |
|  | # Override built-in defaults |
|  | ## |
|  | Defaults env\_reset |
|  | Defaults env\_keep += "BLOCKSIZE" |
|  | Defaults env\_keep += "COLORFGBG COLORTERM" |
|  | Defaults env\_keep += "\_\_CF\_USER\_TEXT\_ENCODING" |
|  | Defaults env\_keep += "CHARSET LANG LANGUAGE LC\_ALL LC\_COLLATE LC\_CTYPE" |
|  | Defaults env\_keep += "LC\_MESSAGES LC\_MONETARY LC\_NUMERIC LC\_TIME" |
|  | Defaults env\_keep += "LINES COLUMNS" |
|  | Defaults env\_keep += "LSCOLORS" |
|  | Defaults env\_keep += "SSH\_AUTH\_SOCK" |
|  | Defaults env\_keep += "TZ" |
|  | Defaults env\_keep += "DISPLAY XAUTHORIZATION XAUTHORITY" |
|  | Defaults env\_keep +...