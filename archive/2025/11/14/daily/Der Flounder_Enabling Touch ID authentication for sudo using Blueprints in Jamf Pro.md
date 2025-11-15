---
title: Enabling Touch ID authentication for sudo using Blueprints in Jamf Pro
url: https://derflounder.wordpress.com/2025/11/14/enabling-touch-id-authentication-for-sudo-using-blueprints-in-jamf-pro/
source: Der Flounder
date: 2025-11-14
fetch_date: 2025-11-15T03:07:31.523810
---

# Enabling Touch ID authentication for sudo using Blueprints in Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Declarative Device Management](https://derflounder.wordpress.com/category/declarative-device-management/), [Jamf Pro Blueprints](https://derflounder.wordpress.com/category/jamf-pro-blueprints/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/) > Enabling Touch ID authentication for sudo using Blueprints in Jamf Pro

## Enabling Touch ID authentication for sudo using Blueprints in Jamf Pro

November 14, 2025
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

One of the capabilities Apple added in macOS Sonoma was a [pluggable authentication module](https://en.wikipedia.org/wiki/Pluggable_Authentication_Module) (PAM) configuration option to [enable Touch ID authentication for the sudo tool](https://derflounder.wordpress.com/2017/11/17/enabling-touch-id-authorization-for-sudo-on-macos-high-sierra/) which would persist and [not be overwritten by software updates](https://derflounder.wordpress.com/2023/10/14/enabling-touch-id-authentication-for-sudo-on-macos-sonoma/).

To enable this option, there is a **/etc/pam.d/sudo\_local.template** file on macOS Sonoma and later which appears as shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # sudo\_local: local config file which survives system update and is included for sudo |
|  | # uncomment following line to enable Touch ID for sudo |
|  | #auth sufficient pam\_tid.so |

[view raw](https://gist.github.com/rtrouton/d0641e616ebdbdd3af44e613e743e273/raw/8118ca15c6f4a1e531e8ad611578fe515c849c4d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/d0641e616ebdbdd3af44e613e743e273#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

Copying the **/etc/pam.d/sudo\_local.template** file to **/etc/pam.d/sudo\_local** and uncommenting the indicated line allows Touch ID to work as authentication for the [sudo](https://ss64.com/osx/sudo.html) tool.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # sudo\_local: local config file which survives system update and is included for sudo |
|  | # uncomment following line to enable Touch ID for sudo |
|  | auth sufficient pam\_tid.so |

[view raw](https://gist.github.com/rtrouton/5be3a18f5b6d9163aba46411d785c085/raw/f8b6ffcd41668b32b3ab1e89c5e1b65326de28d3/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5be3a18f5b6d9163aba46411d785c085#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-14-at-8.07.02am.png?w=595 "Screenshot 2025-11-14 at 8.07.02 AM.png")

A number of Mac admins have written [scripts](https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/enable_and_disable_touch_id_for_sudo) to apply this PAM configuration to Macs, but there didn’t seem to be a good way to handle this without scripting. However, as part of Apple’s unveiling of Declarative Device Management (DDM) at WWDC 2023, Apple announced that DDM management included the ability to manage sets of tamper-resistant system configuration files for different system services. As of this date, the following services built into macOS can be managed this way:

* **sshd**
* **sudo**
* **PAM**
* **CUPS**
* **Apache httpd**
* **bash**
* **zsh**

[Jamf Pro’s Blueprints](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Jamf_Pro_Blueprints_Configuration_Guide.html) supports managing these services via the [Service configuration files component](https://learn.jamf.com/en-US/bundle/jamf-pro-blueprints-configuration-guide/page/Blueprints_Components_Pro.html). Since enabling Touch ID authentication for **sudo** is managed using a PAM configuration file, that means that enabling Touch ID authentication for the **sudo** tool can be accomplished via Blueprints. For more details, please see below the jump.

By default, macOS Tahoe 26.1 ships with a **/etc/pam.d/sudo\_local.template** file that looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # sudo\_local: local config file which survives system update and is included for sudo |
|  | # uncomment following line to enable Touch ID for sudo |
|  | #auth sufficient pam\_tid.so |

[view raw](https://gist.github.com/rtrouton/d0641e616ebdbdd3af44e613e743e273/raw/8118ca15c6f4a1e531e8ad611578fe515c849c4d/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/d0641e616ebdbdd3af44e613e743e273#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To prepare the desired PAM configuration, you can use the process described below:

1. Make a copy of the **/etc/pam.d/sudo\_local.template** file to a convenient location.
2. Uncomment the last line
3. Save the file and rename it to a file named **sudo\_local**.

The newly-created **sudo\_local** file should appear similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | # sudo\_local: local config file which survives system update and is included for sudo |
|  | # uncomment following line to enable Touch ID for sudo |
|  | auth sufficient pam\_tid.so |

[view raw](https://gist.github.com/rtrouton/5be3a18f5b6d9163aba46411d785c085/raw/f8b6ffcd41668b32b3ab1e89c5e1b65326de28d3/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/5be3a18f5b6d9163aba46411d785c085#file-gistfile1-txt)
hosted with ❤ by [GitHub](https://github.com)

To deploy this change with Blueprints, three things are needed.

1. A zip file which contains both the directory and file structure of the configuration file in question.

The PAM configuration file is stored in the **/etc** directory, with a directory inside named **pam.d**, with a file inside the **pam.d** directory named **sudo\_local**, so a zip file containing a directory named **etc**, with a directory inside named **pam.d**, with a file inside the **pam.d** directory named **sudo\_local**, is needed for this.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-14-at-9.07.02am.png?w=595 "Screenshot 2025-11-14 at 9.07.02 AM.png")

For this example, we’ll name the zip file as **enable\_touch\_id\_for\_sudo.zip**.

![](https://derflounder.wordpress.com/wp-content/uploads/2025/11/screenshot-2025-11-14-at-9.07.40am.png?w=...