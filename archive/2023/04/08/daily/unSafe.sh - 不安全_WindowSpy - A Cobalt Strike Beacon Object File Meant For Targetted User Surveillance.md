---
title: WindowSpy - A Cobalt Strike Beacon Object File Meant For Targetted User Surveillance
url: https://buaq.net/go-157576.html
source: unSafe.sh - 不安全
date: 2023-04-08
fetch_date: 2025-10-04T11:29:51.808016
---

# WindowSpy - A Cobalt Strike Beacon Object File Meant For Targetted User Surveillance

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

![](https://8aqnet.cdn.bcebos.com/6310328a789d859eb4c557a82f5776db.jpg)

WindowSpy - A Cobalt Strike Beacon Object File Meant For Targetted User Surveillance

WindowSpy is a Cobalt Strike Beacon Object File meant for targetted user surveillance. The g
*2023-4-7 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-157576.htm)
阅读量:35
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiLwyVZfcXObic4nH0ONE4kX9ExgWvRhGf0vdoVjJq6anDqa17ll_7nFVxcDpxecBnZEmKuQCCNRLeLIJOZyG3JWit9KP09YDECtF5bWPMxAa26PbrXbY1YiczjtcyyZTv7FdZ04-EVOyq0zGVo2E9SrDIvJrH8HYRVj1xrhgIpBWjpJzSaalMr1mNwRA=w640-h636)](https://blogger.googleusercontent.com/img/a/AVvXsEiLwyVZfcXObic4nH0ONE4kX9ExgWvRhGf0vdoVjJq6anDqa17ll_7nFVxcDpxecBnZEmKuQCCNRLeLIJOZyG3JWit9KP09YDECtF5bWPMxAa26PbrXbY1YiczjtcyyZTv7FdZ04-EVOyq0zGVo2E9SrDIvJrH8HYRVj1xrhgIpBWjpJzSaalMr1mNwRA)

WindowSpy is a [Cobalt Strike](https://www.kitploit.com/search/label/Cobalt%20Strike "Cobalt Strike") Beacon Object File meant for targetted user surveillance. The goal of this project was to trigger surveillance capabilities only on certain targets, e.g. browser login pages, confidential documents, vpn logins etc. The purpose was to increase [stealth](https://www.kitploit.com/search/label/Stealth "stealth") during user surveillance by preventing detection of repeated use of surveillance capabilities e.g. screenshots. It also saves the [red team](https://www.kitploit.com/search/label/Red%20Team "red team") time in sifting through many pages of user surveillance data, which would be produced if keylogging/screenwatch was running at all times.

Each time a beacon checks in, the BOF runs on the target. The BOF comes with a [hardcoded](https://www.kitploit.com/search/label/Hardcoded "hardcoded") list of strings that are common in useful window titles e.g. login, administrator, control panel, vpn etc. You can customize this list and recompile yourself. It enumerates the visible [windows](https://www.kitploit.com/search/label/Windows "windows") and compares the titles to the list of strings, and if any of these are detected, it triggers a local aggressorscript function defined in WindowSpy.cna named spy(). By default, it takes a screenshot. You may customize this function however you want, e.g. keylogging, WireTap, webcam, etc.

The spy() function has 1 argument, $1 being the beacon id of the beacon that triggered it.

1. load the WindowSpy.cna script into Cobalt Strike

1. open the WindowSpy.sln solution file in Visual Studio
2. Build for target BOF (x64/x86)

1. Leave it to run. It should automatically run on each beacon checkin and trigger accordingly.

I built this because I was bored, and was messing with user surveillance. If there are bugs, open an issue. If there are any issues with the design, feel free to open an issue too.

WindowSpy - A Cobalt Strike Beacon Object File Meant For Targetted User Surveillance
![WindowSpy - A Cobalt Strike Beacon Object File Meant For Targetted User Surveillance](https://blogger.googleusercontent.com/img/a/AVvXsEiLwyVZfcXObic4nH0ONE4kX9ExgWvRhGf0vdoVjJq6anDqa17ll_7nFVxcDpxecBnZEmKuQCCNRLeLIJOZyG3JWit9KP09YDECtF5bWPMxAa26PbrXbY1YiczjtcyyZTv7FdZ04-EVOyq0zGVo2E9SrDIvJrH8HYRVj1xrhgIpBWjpJzSaalMr1mNwRA=s72-w640-c-h636)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/04/windowspy-cobalt-strike-beacon-object.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)