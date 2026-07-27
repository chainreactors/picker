---
title: Fixing automatic login issues on Ubuntu 26.04 LTS
url: https://derflounder.wordpress.com/2026/07/26/fixing-automatic-login-issues-on-ubuntu-26-04-lts/
source: Der Flounder
date: 2026-07-26
fetch_date: 2026-07-27T05:39:03.380548
---

# Fixing automatic login issues on Ubuntu 26.04 LTS

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Linux](https://derflounder.wordpress.com/category/linux/) > Fixing automatic login issues on Ubuntu 26.04 LTS

## Fixing automatic login issues on Ubuntu 26.04 LTS

July 26, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/) [Leave a comment](#respond)
[Go to comments](#comments)

[As part of an earlier project](https://derflounder.wordpress.com/2022/01/02/2021-holiday-vacation-project/), I had set up a status board using [MagicMirror](https://magicmirror.builders/) on Ubuntu LTS. As part of this, I had set Ubuntu to do the following:

* Reboot on a daily basis, in case any of the MagicMirror modules got hung or there was some other problem.
* Automatically log in as the user account used to run MagicMirror.
* Set MagicMirror to automatically launch when the user account in question logged in.

This setup has worked reliably for a few years now, until the automatic login process quit working out of the blue this week. When I did some research, I saw that I was not the only person who had problems with this:

<https://www.reddit.com/r/Ubuntu/comments/1v627xc/autologin/>
<https://askubuntu.com/questions/1501453/automatic-login-not-working/1568632#1568632>

I [verified via the documentation](https://help.ubuntu.com/stable/ubuntu-help/user-autologin.html.en) that I had everything configured like it is supposed to be for automatic login to work, but it looks like something in the latest software updates for Ubuntu 26.04 LTS is preventing automatic login from working. What to do? After some additional research, I found an answer. For more details, please see below the jump.

I’m using [GNOME](https://help.ubuntu.com/stable/ubuntu-help/gnome-on-ubuntu.html.en) for my desktop environment on Ubuntu 26.04 LTS, which means that the automatic login settings are stored in the following file:

**/etc/gdm3/custom.conf**

My **custom.conf** file looked like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # GDM configuration storage |
|  | # |
|  | # See /usr/share/gdm/gdm.schemas for a list of available options. |
|  |  |
|  | [daemon] |
|  | AutomaticLoginEnable=True |
|  | AutomaticLogin=username\_goes\_here |
|  |  |
|  | # Enabling automatic login |
|  | # AutomaticLoginEnable = true |
|  | # AutomaticLogin = user1 |
|  |  |
|  | # Enabling timed login |
|  | # TimedLoginEnable = true |
|  | # TimedLogin = user1 |
|  | # TimedLoginDelay = 30 |
|  |  |
|  | [security] |
|  |  |
|  | [debug] |
|  | # Uncomment the line below to turn on debugging |
|  | # More verbose logs |
|  | # Additionally lets the X server dump core if it crashes |
|  | #Enable=true |

[view raw](https://gist.github.com/rtrouton/8da81d7b01ff204b803ea03cb8f41f1a/raw/36ed3fc6d1e0402f2629d01447e9f4ba72419fe9/custom_conf1.txt)
 [custom\_conf1.txt](https://gist.github.com/rtrouton/8da81d7b01ff204b803ea03cb8f41f1a#file-custom_conf1-txt)
hosted with ❤ by [GitHub](https://github.com)

The relevant section which controls the automatic login is this, in the **[daemon]** section of the **custom.conf** file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | AutomaticLoginEnable=True |
|  | AutomaticLogin=username\_goes\_here |

[view raw](https://gist.github.com/rtrouton/3280e61d5a68daaa05905b8161648cb7/raw/0265a2b5482c3b8d7dca747d62e6867574dacb80/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/3280e61d5a68daaa05905b8161648cb7#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

However, there is another option for automatically logging in. This is [GNOME’s time delay automatic login option](https://fostips.com/enable-automatic-login-ubuntu/#rb-Option-b-Automatic-Login-with-a-few-seconds-delay). This allows the login screen to appear and wait for a specified time in seconds. If no action occurs at the login screen, the computer logs in as the user account configured in the timed login settings. This option is commented out by default and should also be in the **[daemon]** section of the **custom.conf** file:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # Enabling timed login |
|  | # TimedLoginEnable = true |
|  | # TimedLogin = user1 |
|  | # TimedLoginDelay = 30 |

[view raw](https://gist.github.com/rtrouton/0204d6c93de42a14bad44cb216d09211/raw/83bbc60a85faed3249d76b6816582571a283b2e6/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/0204d6c93de42a14bad44cb216d09211#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

I updated my configuration file to comment out the automatic login section, then enabled the timed login settings to log in as the desired user account with a delay of one second. Once my edits were completed, my **custom.conf** file looked like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # GDM configuration storage |
|  | # |
|  | # See /usr/share/gdm/gdm.schemas for a list of available options. |
|  |  |
|  | [daemon] |
|  | # AutomaticLoginEnable=True |
|  | # AutomaticLogin=username\_goes\_here |
|  |  |
|  | # Enabling automatic login |
|  | # AutomaticLoginEnable = true |
|  | # AutomaticLogin = user1 |
|  |  |
|  | # Enabling timed login |
|  | TimedLoginEnable = true |
|  | TimedLogin = username\_goes\_here |
|  | TimedLoginDelay = 1 |
|  |  |
|  | [security] |
|  |  |
|  | [debug] |
|  | # Uncomment the line below to turn on debugging |
|  | # More verbose logs |
|  | # Additionally lets the X server dump core if it crashes |
|  | #Enable=true |

[view raw](https://gist.github.com/rtrouton/7b5f6d63088ad357f5dcec09f11d5d14/raw/89325063ee425599a0246bc5781752c751f05c22/custom_conf2.txt)
 [custom\_conf2.txt](https://gist.github.com/rtrouton/7b5f6d63088ad357f5dcec09f11d5d14#file-custom_conf2-txt)
hosted with ❤ by [GitHub](https://github.com)

Once I saved my changes, I restarted my computer. After the reboot, the login screen appeared for one second and then logged in as my desired user account. That gave me back the automatic login experience I wanted.

For folks in a similar situation of needing automatic login to work on Ubuntu, hopefully this solution works for you like it did for me.

### Share this:

* [Print (Opens in new window)
  Print](https://derflounder.wordpress.com/2026/07/26/fixing-automatic-login-issues-on-ubuntu-26-04-lts/#print?share=print)
* Email a link to a friend (Opens in new window)
  Email
* More

* [Share on Facebook (Opens in new window)
  Fa...