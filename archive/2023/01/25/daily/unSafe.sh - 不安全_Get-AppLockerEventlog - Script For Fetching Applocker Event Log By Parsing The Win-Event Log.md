---
title: Get-AppLockerEventlog - Script For Fetching Applocker Event Log By Parsing The Win-Event Log
url: https://buaq.net/go-146617.html
source: unSafe.sh - 不安全
date: 2023-01-25
fetch_date: 2025-10-04T04:43:03.994065
---

# Get-AppLockerEventlog - Script For Fetching Applocker Event Log By Parsing The Win-Event Log

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

![](https://8aqnet.cdn.bcebos.com/379e72b22a2660ca7c66b6bb54af8d6e.jpg)

Get-AppLockerEventlog - Script For Fetching Applocker Event Log By Parsing The Win-Event Log

This script will parse all the channels of events from the win-event log to extract all the
*2023-1-24 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146617.htm)
阅读量:26
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhi4MMvYJurLn0dsN6dh8oYjYID1-WaUVMvpqTGyjwAdUkm9OugY8_Cz3KicNXHHhMRT4_Scx-b8iPl-SKLYyNogpNyAWwvRThXhMA8SjYQoxa1zS6Img9NOHNZqc1orumI1kEwP6oIiIYKl6lPDTdg2Penw11UZmuV0PNe8TGGz7Kk80hxp_2wimjlrQ=w640-h258)](https://blogger.googleusercontent.com/img/a/AVvXsEhi4MMvYJurLn0dsN6dh8oYjYID1-WaUVMvpqTGyjwAdUkm9OugY8_Cz3KicNXHHhMRT4_Scx-b8iPl-SKLYyNogpNyAWwvRThXhMA8SjYQoxa1zS6Img9NOHNZqc1orumI1kEwP6oIiIYKl6lPDTdg2Penw11UZmuV0PNe8TGGz7Kk80hxp_2wimjlrQ)

This script will parse all the channels of events from the win-event log to extract all the log relatives to AppLocker. The script will gather all the important pieces of information relative to the events for [forensic](https://www.kitploit.com/search/label/Forensic "forensic") or threat-hunting purposes, or even in order to troubleshoot. Here are the [logs](https://www.kitploit.com/search/label/Logs "logs") we fetch from win-event:

* EXE and DLL,
* MSI and Script,
* Packaged app-Deployment,
* Packaged app-Execution.

### The output:

* The result will be displayed on the screen
* And, The result will be saved to a csv file: **AppLocker-log.csv**

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjIvj6wuy7-6rA5s1cASxwAaCAzCJoEQZVxGYTCGF11mx4nk2u3-TYlu2PXxd0Dm6Rh_hx62BPRQx8P4qneEmMyk2_8xal2Fige6aZeMBsSPz2BU6ncGsHqKIMhREcz61LbB3SPiNwY3O4KnkqySYqDEmRzLQcWM4kGCTHhdyW0QH5S9kdj8PGhWboU2g=w640-h262)](https://blogger.googleusercontent.com/img/a/AVvXsEjIvj6wuy7-6rA5s1cASxwAaCAzCJoEQZVxGYTCGF11mx4nk2u3-TYlu2PXxd0Dm6Rh_hx62BPRQx8P4qneEmMyk2_8xal2Fige6aZeMBsSPz2BU6ncGsHqKIMhREcz61LbB3SPiNwY3O4KnkqySYqDEmRzLQcWM4kGCTHhdyW0QH5S9kdj8PGhWboU2g)

The juicy and useful information you will get with this script are:

* FileType,
* EventID,
* Message,
* User,
* Computer,
* EventTime,
* FilePath,
* Publisher,
* FileHash,
* Package
* RuleName,
* LogName,
* TargetUser.

## PARAMETERS

### HunType

This parameter specifies the type of events you are interested in, there are 04 values for this parameter:

**1. All**

This gets all the events of AppLocker that are interesting for threat-hunting, forensic or even troubleshooting. This is the default value.

```
.\Get-AppLockerEventlog.ps1 -HunType All
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi6xiSf9iT51Esi9yN72_iKlQfLjqOYMPfn8EMHnaM8BpXtEUMGUxnkS4MQRd2IdlAQz9tSysiFRr5fYMMKnyWREufg-A7q3AAnGugXgVxKVWv9nsxR8jdPAGIkbXcnOffAGkhBTV4gRZz0R1iTyjhYa2wCkGmmvQnzQkH0fCgd5UPq8RCNwJWIStgcng=w640-h162)](https://blogger.googleusercontent.com/img/a/AVvXsEi6xiSf9iT51Esi9yN72_iKlQfLjqOYMPfn8EMHnaM8BpXtEUMGUxnkS4MQRd2IdlAQz9tSysiFRr5fYMMKnyWREufg-A7q3AAnGugXgVxKVWv9nsxR8jdPAGIkbXcnOffAGkhBTV4gRZz0R1iTyjhYa2wCkGmmvQnzQkH0fCgd5UPq8RCNwJWIStgcng)

**2. Block**

This gets all the events that are triggered by the action of blocking an application by AppLocker, this type is critical for threat-hunting or forensics, and comes with high priority, since it indicates malicious attempts, or could be a good indicator of prior malicious activity in order to evade defensive mechanisms.

```
.\Get-AppLockerEventlog.ps1 -HunType Block |Format-Table -AutoSize
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgIhZ62jM57tuUacF_yfE468e7OOiAQCHOR_47tB99pgYTTpNLqrweutzWjRrATJAXvH2gsngXtJqjvKCJtFZYSVjg-ppeUhbVJ4lnkU6EMASSuIeQc9Uu2iPhPAfgLtVpCHBztwqkbyvLD0PbtjLVAAjRwz8r68TZIbz79oidiqY2urgMlcT3W7dOUlA=w640-h118)](https://blogger.googleusercontent.com/img/a/AVvXsEgIhZ62jM57tuUacF_yfE468e7OOiAQCHOR_47tB99pgYTTpNLqrweutzWjRrATJAXvH2gsngXtJqjvKCJtFZYSVjg-ppeUhbVJ4lnkU6EMASSuIeQc9Uu2iPhPAfgLtVpCHBztwqkbyvLD0PbtjLVAAjRwz8r68TZIbz79oidiqY2urgMlcT3W7dOUlA)

**3. Allow**

This gets all the events that are triggered by the action of Allowing an application by AppLocker. For threat-hunting or forensics, even the allowed applications should be monitored, in order to detect any possible bypass or configuration mistakes.

```
.\Get-AppLockerEventlog.ps1 -HunType Allow | Format-Table -AutoSize
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhi4MMvYJurLn0dsN6dh8oYjYID1-WaUVMvpqTGyjwAdUkm9OugY8_Cz3KicNXHHhMRT4_Scx-b8iPl-SKLYyNogpNyAWwvRThXhMA8SjYQoxa1zS6Img9NOHNZqc1orumI1kEwP6oIiIYKl6lPDTdg2Penw11UZmuV0PNe8TGGz7Kk80hxp_2wimjlrQ=w640-h258)](https://blogger.googleusercontent.com/img/a/AVvXsEhi4MMvYJurLn0dsN6dh8oYjYID1-WaUVMvpqTGyjwAdUkm9OugY8_Cz3KicNXHHhMRT4_Scx-b8iPl-SKLYyNogpNyAWwvRThXhMA8SjYQoxa1zS6Img9NOHNZqc1orumI1kEwP6oIiIYKl6lPDTdg2Penw11UZmuV0PNe8TGGz7Kk80hxp_2wimjlrQ)

**4. Audit**

This gets all the events generated when AppLocker would block the application if the enforcement mode were enabled (Audit mode). For threat-hunting or forensics, this could indicate any configuration mistake, neglect from the admin to switch the mode, or even a malicious action that happened in the [audit](https://www.kitploit.com/search/label/Audit "audit") phase (tuning phase).

```
 .\Get-AppLockerEventlog.ps1 -HunType Audit
```

## Resource

To better understand AppLocker :

* [Diving in AppLocker for](https://medium.com/%40elromaissa2/diving-in-applocker-for-blue-team-57a7328ce5c0 "Diving in AppLocker for") [Blue Team](https://www.kitploit.com/search/label/Blue%20Team "Blue Team") — Part 1
* [https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/using-event-viewer-with-applocker](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/using-event-viewer-with-applocker "https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/using-event-viewer-with-applocker")

## Contributing

This project welcomes contributions and suggestions.

Get-AppLockerEventlog - Script For Fetching Applocker Event Log By Parsing The Win-Event Log
![Get-AppLockerEventlog - Script For Fetching Applocker Event Log By Parsing The Win-Event Log](https://blogger.googleusercontent.com/img/a/AVvXsEhi4MMvYJurLn0dsN6dh8oYjYID1-WaUVMvpqTGyjwAdUkm9OugY8_Cz3KicNXHHhMRT4_Scx-b8iPl-SKLYyNogpNyAWwvRThXhMA8SjYQoxa1zS6Img9NOHNZqc1orumI1kEwP6oIiIYKl6lPDTdg2Penw11UZmuV0PNe8TGGz7Kk80hxp_2wimjlrQ=s72-w640-c-h258)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/01/get-applockereventlog-script-for.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)