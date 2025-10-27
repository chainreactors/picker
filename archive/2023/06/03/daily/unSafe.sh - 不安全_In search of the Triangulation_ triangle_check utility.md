---
title: In search of the Triangulation: triangle_check utility
url: https://buaq.net/go-166989.html
source: unSafe.sh - 不安全
date: 2023-06-03
fetch_date: 2025-10-04T11:44:53.893176
---

# In search of the Triangulation: triangle_check utility

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

![](https://8aqnet.cdn.bcebos.com/795835b7568a792930fecfaee30f98f4.jpg)

In search of the Triangulation: triangle\_check utility

Software
*2023-6-2 20:16:15
Author: [securelist.com(查看原文)](/jump-166989.htm)
阅读量:26
收藏*

---

![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/02121349/triangle_check_featured-800x450.jpg)

[Software](https://securelist.com/category/software/)

[Software](https://securelist.com/category/software/)

02 Jun 2023

minute read

![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/02121349/triangle_check_featured-1200x600.jpg)

In our [initial blogpost](https://securelist.com/operation-triangulation/109842/) about “Operation Triangulation”, we published a comprehensive guide on how to manually check iOS device backups for possible indicators of compromise using MVT. This process takes time and requires manual search for several types of indicators. To automate this process, we developed a dedicated utility to scan the backups and run all the checks. For Windows and Linux, this tool can be downloaded as [a binary build](https://github.com/KasperskyLab/triangle_check/releases), and for MacOS it can be simply installed as [a Python package](https://pypi.org/project/triangle-check/).

## How to back up your device

### Windows

On Windows, the easiest way to do a backup is via iTunes:

1. Connect your device to a computer that has iTunes installed. Unlock your device and, if needed, confirm that you trust your computer.

   [![](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/02120803/triangle_check_01.png)](https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2023/06/02120803/triangle_check_01.png)

   Window asking to trust the computer
2. Your device should now be displayed in iTunes. Right click on it and press “Back Up”.
3. The created backup will be saved to the %appdata%\Apple Computer\MobileSync\Backup directory.

### macOS

If your macOS version is lower than Catalina (10.15), you can create a backup using iTunes, using instructions for Windows. Starting from Catalina, backups can be created through Finder:

* Connect your device to the computer and, if needed, confirm that you trust the computer.
* Your device should now be displayed in Finder. Select it and then click “*Create a backup*“.
* The created backup will be saved to the *~/Library/Application Support/MobileSync/Backup/* directory.

### Linux

To create a backup on Linux, you will need to install the libimobiledevice library. In order to create backups of devices with the latest versions of iOS installed, you will need to compile this library from [source code](https://github.com/libimobiledevice/libimobiledevice) (you can find the build instructions in the Installation/Getting Started section).
After you install the library and connect your device to the computer, you can create a backup using the `idevicebackup2 backup --full`  command.
During the backup process, you may need to enter your device passcode multiple times.

## How to use our triangle\_check utility

After you do a backup of your device using the instructions above, you will need to install and launch our triangle\_check utility.

### The triangle\_check Python package

No matter what operating system you have, you can install the triangle\_check Python package that we have published to the Python Package Index (PyPi). To do that, you need to have internet access as well as have [the pip utility](https://pip.pypa.io/en/stable/installation/) installed.
You can install the utility using two methods:

* From PyPI (recommended):
  Run the `python -m pip install triangle_check` command.
* Building from Github:
  Run the following commands:
  `git clone https://github.com/KasperskyLab/triangle_check
  cd triangle_check
  python -m build
  python -m pip install dist/triangle_check-1.0-py3-none-any.whl`

After installing, you can launch the utility with the following command:
`python -m triangle_check`.

### Binary builds

If you have Windows or Linux, you can also use the binary builds of the triangle\_check utility that we [have published on GitHub](https://github.com/KasperskyLab/triangle_check/releases). Follow the instructions below to use it:
**Windows**

1. Download the triangle\_check\_win.zip archive from the GitHub releases page and unpack it.
2. Launch the command prompt (cmd.exe) or PowerShell.
3. Change your directory to the one with the unpacked archive (e.g. `cd %userprofile%\Downloads\triangle_check_win`).
4. Launch triangle\_check.exe, specifying the path to the backup as an argument (e.g. `triangle_check.exe "%appdata%\Apple Computer\MobileSync\Backup\00008101-000824411441001E-20230530-143718"` ).

**Linux**

1. Download the triangle\_check\_win.zip archive from the GitHub releases page and unpack it.
2. Launch the terminal.
3. Change your directory to the one with the unpacked archive (e.g. `cd ~/Downloads/triangle_check_linux`).
4. Allow the utility to be executed with the `chmod +x triangle_check` command.
5. Launch the utility, specifying the path to the backup as an argument (e.g. `./triangle_check ~/Desktop/my_backup/00008101-000824411441001E-20230530-143718` ).

## Interpreting the results

The utility outputs “DETECTED” when it locates specific indicators of compromise, and that would mean that the device was infected.
Also, it may print out “SUSPICION” that would mean that a combination of less specific indicators points to a likely infection. Finally, if the message displayed is “No traces of compromise were identified”, then the utility did not find any signs of ‘Operation Triangulation’ compromise.

- [![](https://kasperskycontenthub.com/securelist/files/2020/09/Hunt-APT_YARA_Early_live_v3.jpg)](https://xtraining.kaspersky.com/courses/hunt-apts-with-yara-like-a-great-ninja?redef=1&THRU&reseller=gl_xc-overview_acq_ona_smm__onl_b2b_securelist_banner_______&utm_source=securelist&utm_medium=blog&utm_campaign=gl_course-overview_ay0073&utm_content=banner&utm_term=gl_securelist_organic_elqwbvemf73woii)

##### Reports

While monitoring the traffic of our own corporate Wi-Fi network, we noticed suspicious activity that originated from several iOS-based phones. We created offline backups of the devices, inspected them and discovered traces of compromise.

GoldenJackal is an APT group, active since 2019, that usually targets government and diplomatic entities in the Middle East and South Asia. The main feature of this group is a specific toolset of .NET malware, JackalControl, JackalWorm, JackalSteal, JackalPerInfo and JackalScreenWatcher.

Kaspersky analysis of the CloudWizard APT framework used in a campaign in the region of the Russo-Ukrainian conflict.

For more than five years, the Global Research and Analysis Team (GReAT) at Kaspersky has been publishing quarterly summaries of advanced persistent threat (APT) activity. These summaries are based on our threat intelligence research; and they provide a representative snapshot of what we have published and discussed in greater detail in our private APT reports.

文章来源: https://securelist.com/find-the-triangulation-utility/109867/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)