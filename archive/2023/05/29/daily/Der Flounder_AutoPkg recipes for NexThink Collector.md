---
title: AutoPkg recipes for NexThink Collector
url: https://derflounder.wordpress.com/2023/05/28/autopkg-recipes-for-nexthink-collector/
source: Der Flounder
date: 2023-05-29
fetch_date: 2025-10-04T11:36:38.328699
---

# AutoPkg recipes for NexThink Collector

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [AutoPkg](https://derflounder.wordpress.com/category/autopkg/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Packaging](https://derflounder.wordpress.com/category/packaging/) > AutoPkg recipes for NexThink Collector

## AutoPkg recipes for NexThink Collector

May 28, 2023
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A while back, I posted about [how to build an installer for NexThink Collector](https://derflounder.wordpress.com/2022/12/03/creating-a-nexthink-installer-for-deployment-via-jamf-pro/), but my preference is to not do manual packaging if I can avoid it. Instead, my preference is to have AutoPkg handle packaging tasks whenever possible for the following reasons:

1. I can ensure that the packaging task is handled the same way every time.
2. Once I have the correct recipe written for AutoPkg, all I should need to do for future versions of the app is to run the AutoPkg recipe, wait a few minutes and then collect a properly-built installer.

With that in mind, I decided to revisit building an installer for NexThink Collector but this time build AutoPkg recipes which handle the following:

1. Creating an installer package for NexThink Collector
2. Creating an uninstaller for NexThink Collector

I was able to do this, so for those interested, please see below the jump for more details.

I’ve built several AutoPkg recipes for NexThink Collector:

* **NexThinkCollector.download**: Downloads the latest NexThink Collector installer disk image
* **NexThinkCollector.pkg**: Builds an installer package for NexThink Collector
* **NexThinkCollectorUninstaller.pkg**: Builds an uninstaller package for NexThink Collector
* **NexThinkCollector.sign**: Signs the installer package produced by the NexThinkCollector.pkg recipe
* **NexThinkCollectorUninstaller.sign**: Signs the uninstaller package produced by the NexThinkCollectorUninstaller.pkg recipe

All the recipes are available at the following location:

<https://github.com/autopkg/rtrouton-recipes/tree/master/NexThinkCollector>

The one which needs the most configuration via an AutoPkg override is the following:

* **NexThinkCollector.pkg**

This is because the details of installing and configuring NexThink are going to vary between shops, because different shops are going to configure different options for NexThink. The various Input variable options will provide hopefully all the possible configuration options needed.

To map between the Input variables and the NexThink command line installation configuration options, please see the table below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | AutoPkg Input Variable | NexThink Command Line Installation Configuration Option | What it defines | Required |
| --- | --- | --- | --- | --- |
|  | NTSERVERADDRESS | address | Fully-qualified domain name of your NexThink instance. | Yes |
|  | NTUDPPORT | port | UDP port of your NexThink Instance | No |
|  | NTTCPPORT | tcp\_port | TCP port of your NexThink Instance | Yes |
|  | NTPROXYPACADDRESS | proxy\_pac\_address | The URL of a PAC address for automatic configuration of proxy settings. | No |
|  | NTPROXYADDRESS | proxy\_address | The fully-qualified domain name of a proxy for manual configuration of proxy settings | No |
|  | NTPROXYPORT | proxy\_port | The port number where a proxy is listening for connections for manual configuration of proxy settings. | No |
|  | NTREMOTEACTIONS | ra\_execution\_policy | Configuring the NexThink Collector remote actions settings | No |
|  | NTENGAGE | engage | Configuring the NexThink Collector campaign settings | No |
|  | NTASSIGNMENT | use\_assignment | Configuring the NexThink Collector automatic collector assignment | No |
|  | NTDATAOVERTCP | data\_over\_tcp | Configuring NexThink Collector to send all data over TCP | No |
|  | NTSTRINGTAG | string\_tag | Configure NexThink Collector label (max 2048 characters) to identify an individual or batch installation of Collectors | No |

[view raw](https://gist.github.com/rtrouton/2b02cf30ea49e4b8527eac638fa80496/raw/4e4fa5ba63b272c923e744a60a382802e6e3473e/autopkg_pkg_recipe_input_variables1.csv)
 [autopkg\_pkg\_recipe\_input\_variables1.csv](https://gist.github.com/rtrouton/2b02cf30ea49e4b8527eac638fa80496#file-autopkg_pkg_recipe_input_variables1-csv)
hosted with ❤ by [GitHub](https://github.com)

Note: There are two NexThink command line installation configurations that are not directly covered:

* **rootca**
* **key**

For the **rootca** command line installation configuration option, all the documentation I’ve found in the context of [installing the NexThink Collector software on macOS](https://docs.nexthink.com/platform/latest/installing-collector-on-macos) is the following:

**Graphical installation documentation**

* Root CA: Leave this field empty.

**Command-line installation**

* rootca: Not required.

Since the **rootca** option doesn’t seem to be required at all and there’s no documentation available on how to configure it for the NexThink Collector software on macOS, I’m leaving it out of the AutoPkg recipe.

For the **key** command line installation configuration option, this functionality is covered by the following required Input variables:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  | AutoPkg Input Variable | What it defines | Required |
| --- | --- | --- | --- |
|  | NTCUSTOMERKEYDATA | Contents of the NexThink Customer Key file | Yes |
|  | NTCUSTOMERKEYNAME | Filename of the NexThink Customer Key file | Yes |

[view raw](https://gist.github.com/rtrouton/4cfcabcebb22e7d34dce0e296f2c0992/raw/91159f8bc2cc958ada18aff3e9e3f8d2039c77e0/autopkg_pkg_recipe_input_variables2.csv)
 [autopkg\_pkg\_recipe\_input\_variables2.csv](https://gist.github.com/rtrouton/4cfcabcebb22e7d34dce0e296f2c0992#file-autopkg_pkg_recipe_input_variables2-csv)
hosted with ❤ by [GitHub](https://github.com)

If both Input variables are filled in, then the **postinstall** script used by the installer package generated by this AutoPkg recipe will call the **key** command line installation configuration option and use it to configure the NexThink Collector software with the proper Customer Key information.

To see how this looks in a recipe override of the NexThinkCollector.pkg recipe, let’s create one with the following Input variables set:

* NTSERVERADDRESS: **server.nexthink.com**
* NTTCPPORT: **443**
* NTREMOTEACTIONS: **disabled**
* NTENGAGE: **disable**
* NTASSIGNMENT: **enable**
* NTDATAOVERTCP: **enable**
* NTCUSTOMERKEYNAME: **nexthink-customer-key.txt**
* NTCUSTOMERKEYDATA:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%2...