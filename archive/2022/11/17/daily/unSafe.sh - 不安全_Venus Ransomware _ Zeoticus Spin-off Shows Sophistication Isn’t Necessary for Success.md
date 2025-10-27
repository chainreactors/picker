---
title: Venus Ransomware | Zeoticus Spin-off Shows Sophistication Isn’t Necessary for Success
url: https://buaq.net/go-135951.html
source: unSafe.sh - 不安全
date: 2022-11-17
fetch_date: 2025-10-03T22:58:12.161601
---

# Venus Ransomware | Zeoticus Spin-off Shows Sophistication Isn’t Necessary for Success

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

![](https://8aqnet.cdn.bcebos.com/ac7068c32836ee29a774a944d485cdd3.jpg)

Venus Ransomware | Zeoticus Spin-off Shows Sophistication Isn’t Necessary for Success

Venus ransomware has been launching data encryption attacks across the globe since at least August
*2022-11-16 23:27:40
Author: [www.sentinelone.com(查看原文)](/jump-135951.htm)
阅读量:37
收藏*

---

Venus ransomware has been launching data encryption attacks across the globe since at least August 2022. Last week, the Health Sector Cybersecurity Coordination Center issued an [advisory](https://www.hhs.gov/sites/default/files/venus-ransomware-analyst-note.pdf) stating that at least one healthcare entity in the United States had fallen victim to Venus ransomware, prompting wider warnings for healthcare and other organizations to be on their guard.

In this blog post, we provide further analysis, indicators of compromise, and TTPs associated with Venus ransomware to help organizations and security teams better understand and defend against this threat.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Venus-Ransomware-Zeoticus-Spin-off-Shows-Sophistication-Isnt-Necessary-for-Success-2.jpg)

## Overview

Venus ransomware, also known as Goodgame, has been attracting attention since August 2022 and related samples have been known since at least mid-2021. There are sufficient markers and other metadata present in Venus samples to suggest a genealogy with [Zeoticus ransomware](https://www.sentinelone.com/labs/zeoticus-2-0-ransomware-with-no-c2-required/), which dates back to early 2020.

Venus ransomware is in the tradition of what now might be termed the “legacy ransomware” model: a file locker sold on [underground markets](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/) as a standalone package rather than on a subscription or “ransomware-as-a-service” model. The package includes a compiled binary and access to decryptors. Unlike more modern [data extortion schemes](https://www.sentinelone.com/blog/ransoms-without-ransomware-data-corruption-and-other-new-tactics-in-cyber-extortion/), there is no public data leak site or double extortion methods known to be associated with operators of Venus ransomware at this time.

Underground adverts offering Venus ransomware for sale began appearing in May 2022.

![Venus ransomware forum advert](https://www.sentinelone.com/wp-content/uploads/2022/11/Venus-Ransoware_9.jpg)

Translated, the message shown in the image above states “We are looking for pentesters”,  a common euphemism for ransomware in the wake of a crackdown on overt ransomware discussion in many forums after certain [high profile attacks](https://www.sentinelone.com/blog/when-jbs-met-revil-ransomware-why-we-need-to-beef-up-critical-infrastructure-security/) brought [unwanted attention](https://www.sentinelone.com/blog/the-cybersecurity-executive-order-what-it-means-and-what-you-can-do/).

Aside from HC3’s warning last week of a healthcare organization being compromised by Venus ransomware operators, there is little indication that targets are industry or sector-specific. Initial access is reportedly publicly-exposed and vulnerable RDP (Remote Desktop Protocol) services, a common weakness found across many different types of organizations, regardless of industry or sector. Cybercriminals discover such vulnerable RDP services through tools like Shodan, direct scanning, COTS/Open-source tools, or by purchasing access from an [Initial Access Broker](https://www.sentinelone.com/blog/more-evil-markets-how-its-never-been-easier-to-buy-initial-access-to-compromised-networks/).

## Venus Ransomware | Technical Analysis

On launch, Venus ransomware samples will spawn a UAC (User Access Control) prompt in an attempt to elevate privileges before continuing execution.

![Venus ransomware elevate privileges UAC dialog](https://www.sentinelone.com/wp-content/uploads/2022/11/Venus-Ransoware_12.jpg)

Subsequently, the malware launches a child process with the following syntax:

```
file.exe g g g o n e123
```

In common with [Zeoticus](https://www.sentinelone.com/labs/zeoticus-2-0-ransomware-with-no-c2-required/), the ransomware then uses the `ping` to achieve a delay before deleting its own first-stage binary and hiding the console window from victims.

```
/c ping localhost -n 3 > nul & del C:\Users\[user]\Desktop\file.exe
```

Following this stage, a hardcoded list of processes is compared against what is running on the target and any applicable processes are shutdown via `taskkill.exe`.  A full list of processes targeted mirrors the hardcoded list found in Zeoticus samples.

```
agntsvc.exe
agntsvc.exe
agntsvc.exe
agntsvc.exe
dbeng50.exe
dbsnmp.exe
encsvc.exe
excel.exe
firefoxconfig.exe
infopath.exe
isqlplussvc.exe
msaccess.exe
mspub.exe
mydesktopqos.exe
mydesktopservice.exe
mysqld-nt.exe
mysqld-opt.exe
mysqld.exe
ocautoupds.exe
ocomm.exe
ocssd.exe
onenote.exe
oracle.exe
outlook.exe
powerpnt.exe
sqbcoreservice.exe
sqlagent.exe
sqlbrowser.exe
sqlservr.exe
sqlservr.exe
sqlwriter.exe
synctime.exe
tbirdconfig.exe
thebat64.exe
thunderbird.exe
winword.exe
wordpad.exe
xfssvccon.exe
```

Persistence is achieved by adding an entry for the ransomware payload in the registry (Windows [run key](https://attack.mitre.org/techniques/T1547/001/)).  For example:

```
Write Value HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\352.exe
```

Once encrypted, affected files will be appended with the `.venus` extension. Note that `.TXT` files are not always encrypted by Venus ransomware.

The malware also changes the icons of encrypted files with an image written to `%Windir%\` in the early stages of execution. The user’s Desktop wallpaper is likewise replaced by a `.jpg` image written to `%temp%`. Both are given file names with a random 20-character string that conform to the regex `\d{20}`, for example:

* 16773516481972502376.jpg
* 34004731821972527219.jpg
* 28604229151972527219.jpg

Once all files have been processed, the malware uses registry modification to change the wallpaper.

```
\REGISTRY\USER\[USERIDENTIFIER]\Control Panel\Desktop\Wallpaper = "C:\\Users\\[user]\\AppData\\Local\\Temp\\\\[20char string)].jpg"
```

![Venus ransomware file encrypted](https://www.sentinelone.com/wp-content/uploads/2022/11/Venus-Ransoware_1.jpg)

After the Desktop wallpaper is updated, the ransom note is displayed to the user.  The ransom note is an `.HTA` file similarly written to  `%temp%` with a 20-character string of digits for the file name.

![](https://www.sentinelone.com/wp-content/uploads/2022/11/Venus-Ransoware_11.jpg)

![Venus ransomware ransom note](https://www.sentinelone.com/wp-content/uploads/2022/11/Venus-Ransoware_8.jpg)

During the course of execution, the malware attempts basic local discovery such as finding the machine name and OS. Venus ransomware traverses available network shares via `NetShareEnum` and `wNetOpenEnum`.

Some variants of Venus will utilize WMI to query or redirect additional system services and details. The following command is one launched by Venus ransomware:

```
wmi - start iwbemservices::execquery - root\cimv2 : select __path, processid, csname, caption, sessionid, threadcount, workingsetsize, kernelmodetime, usermodetime, parentprocessid from win32_process where ( caption = "msftesql.exe" or caption = "sqlagent.exe" or caption = "sqlbrowser.exe" or caption = "sqlservr.exe" or caption = "sqlwriter.exe" or caption = "oracle.exe" or caption = "ocssd.exe" or caption = "dbsnmp.exe" or caption = "synctime.exe" or caption = "mydesktopqos.exe" or caption = "agntsvc.exe" ...