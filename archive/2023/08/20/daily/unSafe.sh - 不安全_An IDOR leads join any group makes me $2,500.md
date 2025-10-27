---
title: An IDOR leads join any group makes me $2,500
url: https://buaq.net/go-174802.html
source: unSafe.sh - 不安全
date: 2023-08-20
fetch_date: 2025-10-04T11:58:54.996479
---

# An IDOR leads join any group makes me $2,500

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

![]()

An IDOR leads join any group makes me $2,500

IDOR stands for “Insecure Direct Object References.” It’s a type of security vulnerability that occu
*2023-8-19 03:29:30
Author: [infosecwriteups.com(查看原文)](/jump-174802.htm)
阅读量:33
收藏*

---

[![M7arm4n](https://miro.medium.com/v2/resize:fill:88:88/1*M_MP-PvKnGRNvTWFHcVI7g.jpeg)](https://m7arm4n.medium.com/?source=post_page-----406eb9e463a3--------------------------------)[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:48:48/1*A6LVtmXcJ3QJy_sdCyFx1Q.png)](https://infosecwriteups.com/?source=post_page-----406eb9e463a3--------------------------------)

> IDOR stands for “Insecure Direct Object References.” It’s a type of security vulnerability that occurs when an application allows an attacker to access or manipulate resources directly by modifying input parameters, such as URLs, without proper authorization. In other words, an attacker can bypass access controls and gain unauthorized access to objects (such as files, databases, or other resources) that they should not have access to.
>
> IDOR vulnerabilities typically arise when an application relies on user-supplied input to determine which object or resource to retrieve but does not properly validate or authorize the user’s access to that object. This can occur when an application exposes internal identifiers, like database record IDs, in URLs or parameters without properly checking whether the current user has permission to access those resources.

**Overview of the Vulnerability**

This website has a feature to create a private group, and group management can allow other users to access them by sending invitations, normally the information of private groups is confidential and inaccessible. When you are invited to a private group, in a part of the site you can see your invitations and accept or reject them. When you click Accept, the following message will be sent:

```
POST /GroupInvitations HTTP/1.1
```

the c2mId parameter is a code for the invited group and is vulnerable to IDOR, The attacker by changing this value to upper or downer can easily access other private groups.

**Steps to reproduce**

1. Create 3 accounts: Manager, Attacker, user.
2. Create 2 groups with the Manager account.
3. Invite the Attacker user to group A.
4. From attacker accepts the invitation and sends the request to the repeater.
5. Back to the manager Account and invite the user to group B.
6. Back to the repeater and add one digit to c2mId.
7. Go to the attacker account and see group B.

As a manager I created 2 different groups, Group-AAAA & Group-BBBB and both were private so other users were unable to leave comments and create topics, etc.

I invited the attacker to Group-AAAA to show you the flow of accepting and saving the request to the Burp repeater. So the attacker has access to Group-AAAA. The manager invited another user to Group-BBBB, but the attacker did not invite them to this group.

the attacker increased one to the c2mId value parameter and sent the request. Now the attacker refresh my group’s Page. The attacker of our story has access to Group-BBBB and can leave comments create topics etc. :D I should note that the value of c2mId is not one use. Even if a normal user accepts the innovation attacker can use this value again to access the groups.

文章来源: https://infosecwriteups.com/an-idor-leads-join-any-group-makes-me-2-500-406eb9e463a3?source=rss----7b722bfd1b8d--bug\_bounty
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)