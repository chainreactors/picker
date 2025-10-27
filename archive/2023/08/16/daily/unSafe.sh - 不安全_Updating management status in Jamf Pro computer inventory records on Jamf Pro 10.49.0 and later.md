---
title: Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later
url: https://buaq.net/go-174523.html
source: unSafe.sh - 不安全
date: 2023-08-16
fetch_date: 2025-10-04T11:59:11.688823
---

# Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/89d09bb73103d35b656b91429e4e661c.jpg)

Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

Home > Jamf Pro, Jamf Pro Classic API, Scripting > Updating management status in Jamf Pro co
*2023-8-15 23:39:57
Author: [derflounder.wordpress.com(查看原文)](/jump-174523.htm)
阅读量:24
收藏*

---

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

## Updating management status in Jamf Pro computer inventory records on Jamf Pro 10.49.0 and later

As of Jamf Pro 10.49.0, the following mass action has been removed:

* **Edit the Management Account Information**

![Screen Shot 2021 09 28 at 10 39 53 AM](https://derflounder.files.wordpress.com/2023/08/screen-shot-2021-09-28-at-10.39.53-am.png?w=595 "Screen Shot 2021-09-28 at 10.39.53 AM.png")

I had been using this to update the status of unmanaged Macs to now be managed Macs, by editing the username and password assigned to the computer inventory record. As part of this, the remote management status of the computer inventory record would change from **Unmanaged** to **Managed**.

As of Jamf Pro 10.49.0, the management account information has been removed from the computer inventory record, with the resulting removal of the mass-action to edit the management account information. However, this has left me without a mass-action to change unmanaged Macs to managed Macs.

Fortunately, there’s a way to change this via the Jamf Pro Classic API. The relevant API command to change the management status in a Jamf Pro computer inventory record should look like this:

It’s sending the following XML block to update the relevant computer inventory record and make the management change:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | <computer> |
|  | <general> |
|  | <remote\_management> |
|  | <managed>true</managed> |
|  | </remote\_management> |
|  | </general> |
|  | </computer> |

Previously, you also needed to send along the management username and management password, but since those have been removed as of Jamf Pro 10.49.0, those are no longer needed.

I have filed a feature request with Jamf to get back an equivalent mass-action to update the management status. For those interested, it is the following:

**JN-I-27551**: <https://ideas.jamf.com/ideas/JN-I-27551>

While I wait to see what Jamf does with the feature request, I was able to use the API information discussed above to create a script which a) updates the management status in specified computer inventory records and b) generates a report of the Macs whose computer inventory records were updated. For more details, please see below the jump.

The script is named **Set\_Jamf\_Pro\_Computers\_To\_Managed\_Status.sh** and is available via the link below:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/Casper_Scripts/Set_Jamf_Pro_Computers_To_Managed>

The script is designed to take in a set of Jamf Pro ID numbers in a plaintext file, where the Jamf Pro ID numbers correspond the Macs where you want to change the management status in their Jamf Pro computer inventory records. The plaintext file should look similar to this:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

|  |  |
| --- | --- |
|  | 416462 |
|  | 842736 |
|  | 434703 |
|  | 338517 |
|  | 481915 |
|  | 596669 |

Five items are required to use this script:

* Jamf Pro 10.49.0 or later
* A text file containing the Jamf Pro IDs of the computer(s) you wish to delete.
* The URL of the appropriate Jamf Pro server.
* The username of an account on the Jamf Pro server with sufficient privileges to delete computers from the Jamf Pro server.
* The password for the relevant account on the Jamf Pro server.

Jamf Pro account privileges required by the Jamf Pro server account referenced above:

**Jamf Pro Server Objects**:

Computers: **Read**, **Update**

Users: **Update**

Once the five specified items are available, the script can be run using the following command:

This file contains bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

You should see output like this:

As part of the script’s run, a report will be generated and you’ll be notified of where it is stored. The report will be in [TSV format](https://en.wikipedia.org/wiki/Tab-separated_values) and appear similar to what’s shown below:

文章来源: https://derflounder.wordpress.com/2023/08/15/updating-management-status-in-jamf-pro-computer-inventory-records-on-jamf-pro-10-49-0-and-later/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)