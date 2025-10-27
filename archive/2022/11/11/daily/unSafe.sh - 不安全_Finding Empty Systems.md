---
title: Finding Empty Systems
url: https://buaq.net/go-135102.html
source: unSafe.sh - 不安全
date: 2022-11-11
fetch_date: 2025-10-03T22:21:16.760822
---

# Finding Empty Systems

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

![](https://8aqnet.cdn.bcebos.com/9df998d35c6948aa45ba19eba2699503.jpg)

Finding Empty Systems

10 November 2022We've been on penetration tests before and have found the need to find a system th
*2022-11-10 23:19:26
Author: [fortynorthsecurity.com(查看原文)](/jump-135102.htm)
阅读量:16
收藏*

---

10 November 2022

We've been on penetration tests before and have found the need to find a system that doesn't have a user currently logged in. Why, you might ask? Well, it's a penetration test, so hiding our actions isn't a concern of ours, and we needed to find another domain-joined system to perform some sort of post-exploitation action. So, we were able to capture a list of domain-joined systems (one way can be done with [EDD](https://github.com/FortyNorthSecurity/EDD)'s [GetDomainComputers](https://github.com/FortyNorthSecurity/EDD/blob/master/EDD/Functions/GetDomainComputers.cs) function) and began trying to remote desktop into a few systems.

![](https://media.giphy.com/media/IktbAtAD3vjoOv7tsv/giphy.gif)

**A lot of the projects we code come as a result of hating to do anything manually**. We tried to remote desktop into maybe 5 - 7 systems, and found that all of them were currently being used by employees. We didn't want to interrupt someone from working, so kicking accounts off the system wasn't an option for us. **After trying 5 - 7 systems, we stopped trying to manually guess and find a system, and began coding a way to find an unused system**.

**This resulted in the latest module added into EDD being the [FindEmptySystems](https://github.com/FortyNorthSecurity/EDD/blob/master/EDD/Functions/FindEmptySystem.cs) function**.

This function works by enumerating domain-joined systems via LDAP and attempting to connect to each system via WMI. It queries the remote system's Win32\_LoggedOnUser class to enumerate accounts with a session on the remote system. One obvious requirement for this is that the account you are using to search for a vacant system would need to have admin access on the system it is targeting to retrieve the data.

![](https://fortynorthsecurity.com/blog/content/images/2022/10/Gathered-Data.png)

Output for Win32\_LoggedOnUser Class

One thing that you can observe, is when you try to retrieve this data via any account, in the results it will show that your account has a session on the system. We're trying to account for that by filtering out those results where the session returned has the same username as your current account that you are querying the system with. Now, this obviously leads an edge case where the account you are using could be legitimately logged into the system, but based on our testing, the results are accurate enough that if you encounter this edge case, the next system you test should be fine.

The WMI query will also show local accounts that have active session on the system, so the module filters the results to only review active sessions used by domain accounts.

In the end, you should see something similar to the following when you run EDD.

![](https://fortynorthsecurity.com/blog/content/images/2022/10/edd-output.png)

Hope that this can be useful for you. If you have any questions, don't hesitate to [reach out](https://www.fortynorthsecurity.com/contact)!

文章来源: https://fortynorthsecurity.com/blog/finding-empty-systems/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)