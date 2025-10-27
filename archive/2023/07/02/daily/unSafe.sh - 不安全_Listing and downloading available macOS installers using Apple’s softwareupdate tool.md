---
title: Listing and downloading available macOS installers using Apple’s softwareupdate tool
url: https://buaq.net/go-170932.html
source: unSafe.sh - 不安全
date: 2023-07-02
fetch_date: 2025-10-04T11:51:19.853821
---

# Listing and downloading available macOS installers using Apple’s softwareupdate tool

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

![](https://8aqnet.cdn.bcebos.com/e3aaac72e5bd4ede8d2e45cd2699f84d.jpg)

Listing and downloading available macOS installers using Apple’s softwareupdate tool

Home > Mac administration, macOS, Scripting > Listing and downloading available macOS instal
*2023-7-1 05:12:18
Author: [derflounder.wordpress.com(查看原文)](/jump-170932.htm)
阅读量:28
收藏*

---

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Listing and downloading available macOS installers using Apple’s softwareupdate tool

## Listing and downloading available macOS installers using Apple’s softwareupdate tool

As of macOS Catalina and Big Sur, Apple added some useful functionality to the [softwareupdate](https://ss64.com/osx/softwareupdate.html) tool which allows you to [list the macOS installers](https://derflounder.wordpress.com/2021/03/03/listing-the-full-os-installers-available-from-apples-software-update-feed-on-macos-big-sur/) (starting on macOS Big Sur) available to a particular Mac and then to [download them](https://scriptingosx.com/2019/10/download-a-full-install-macos-app-with-softwareupdate-in-catalina/) (starting on macOS Catalina.)

I’ve used both functions frequently when I needed to identify and download new macOS installers, so I decided to write a script which makes the task easier. For more details, please see below the jump.

The script uses the **softwareupdate** tool to list all macOS installers that are available to the Mac you’re running the script on, along with the version number information you would need to provide to the **softwareupdate** tool in order to download that macOS version’s installer.

![Screen Shot 2023 06 30 at 4 43 04 PM](https://derflounder.files.wordpress.com/2023/06/screen-shot-2023-06-30-at-4.43.04-pm.png?w=595&h=278 "Screen Shot 2023-06-30 at 4.43.04 PM.png")

If you enter version information when prompted, the script will download the specified macOS installer and install the corresponding macOS installer application into **/Applications**.

![Screen Shot 2023 06 30 at 4 56 57 PM](https://derflounder.files.wordpress.com/2023/06/screen-shot-2023-06-30-at-4.56.57-pm.png?w=595&h=325 "Screen Shot 2023-06-30 at 4.56.57 PM.png")

![Screen Shot 2023 06 30 at 4 35 48 PM](https://derflounder.files.wordpress.com/2023/06/screen-shot-2023-06-30-at-4.35.48-pm.png?w=595&h=302 "Screen Shot 2023-06-30 at 4.35.48 PM.png")

This script is available below and also from GitHub at the following location:

<https://github.com/rtrouton/rtrouton_scripts/tree/main/rtrouton_scripts/download_macos_installers>

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # This script uses the softwareupdate command to display available macOS installers |
|  | # for a particular Mac and then offers the option to download them. |
|  |  |
|  | available\_os\_installers=$(mktemp) |
|  |  |
|  | # Set exit status |
|  | error=0 |
|  |  |
|  | #Check for available macOS installers |
|  |  |
|  | /usr/sbin/softwareupdate –list-full-installers > "$available\_os\_installers" |
|  |  |
|  | clear |
|  |  |
|  | echo "The following macOS installers are available for this Mac:" |
|  | echo "" |
|  | cat "$available\_os\_installers" | tail -n +3 | awk -F ': |, |KiB' '($1 == "\* Title") { print $2" "$4" Build "$9 ": "(int(($6 / 1000 / 1000) \* 10 + 0.5) / 10) " GB" }' |
|  | echo "" |
|  | echo "Version numbers:" |
|  | grep -oE '\d+\.(\d|\.)\*\d' "$available\_os\_installers" |
|  | echo "" |
|  | read -p "Please enter the version number of the macOS installer you wish to download: " macos\_version |
|  |  |
|  | # Verify that data entered contains only numbers and periods by extracting all the numbers and |
|  | # periods and seeing if there's anything left over. If there is, not a valid version number. |
|  |  |
|  | macos\_version\_check=$(echo "$macos\_version" | sed 's/[0-9]//g' | tr -d '.') |
|  |  |
|  | # If the version check returns no data, a version number containing only numbers and periods was entered. |
|  |  |
|  | if [[ -z "$macos\_version\_check" ]]; then |
|  | echo "Downloading installer…" |
|  | /usr/sbin/softwareupdate –fetch-full-installer –full-installer-version ${macos\_version} |
|  | else |
|  | echo "$macos\_version is not a valid version number. Exiting…" |
|  | error=1 |
|  | fi |
|  |  |
|  | exit $error |

Thanks to the folks in the **#bash** channel in the Mac Admins Slack for helping improve various parts of this script.

文章来源: https://derflounder.wordpress.com/2023/06/30/listing-and-downloading-available-macos-installers-using-apples-softwareupdate-tool/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)