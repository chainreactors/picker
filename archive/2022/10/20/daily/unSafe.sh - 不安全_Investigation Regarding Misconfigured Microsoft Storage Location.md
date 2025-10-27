---
title: Investigation Regarding Misconfigured Microsoft Storage Location
url: https://buaq.net/go-131702.html
source: unSafe.sh - 不安全
date: 2022-10-20
fetch_date: 2025-10-03T20:21:00.324165
---

# Investigation Regarding Misconfigured Microsoft Storage Location

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

Investigation Regarding Misconfigured Microsoft Storage Location

Summary Security researchers at SOCRadar informed Microsoft on Se
*2022-10-19 22:4:0
Author: [msrc-blog.microsoft.com(查看原文)](/jump-131702.htm)
阅读量:16
收藏*

---

### Summary

Security researchers at SOCRadar informed Microsoft on September 24, 2022, of a misconfigured Microsoft endpoint. This misconfiguration resulted in the potential for unauthenticated access to some business transaction data corresponding to interactions between Microsoft and prospective customers, such as the planning or potential implementation and provisioning of Microsoft services.

Upon being notified of the misconfiguration, the endpoint was quickly secured and is now only accessible with required authentication. Our investigation found no indication customer accounts or systems were compromised. We have directly notified the affected customers.

### Customer Impact

The business transaction data included names, email addresses, email content, company name, and phone numbers, and may have included attached files relating to business between a customer and Microsoft or an authorized Microsoft partner. The issue was caused by an unintentional misconfiguration on an endpoint that is not in use across the Microsoft ecosystem and was not the result of a security vulnerability.  We are working to improve our processes to further prevent this type of misconfiguration and performing additional due diligence to investigate and ensure the security of all Microsoft endpoints.

We appreciate SOCRadar informing us about the misconfigured endpoint, but after reviewing their blog post, we first want to note that SOCRadar has greatly exaggerated the scope of this issue.  Our in-depth investigation and analysis of the data set shows duplicate information, with multiple references to the same emails, projects, and users. We take this issue very seriously and are disappointed that SOCRadar exaggerated the numbers involved in this issue even after we highlighted their error.

More importantly, we are disappointed that SOCRadar has chosen to release publicly a “search tool” that is not in the best interest of ensuring customer privacy or security and potentially exposing them to unnecessary risk.  We recommend that any security company that wants to provide a similar tool follow basic measures to enable data protection and privacy:

1. to implement a reasonable verification system to ensure that a user is who it purports to be;
2. to follow data minimization principles by scoping the results delivered solely to information pertaining to *that* verified user only;
3. where that company is not in a position to determine with reasonable fidelity which customers had affected data, to not then surface to a given user information (including metadata/filenames) that may belong to another customer.

We have focused our attention on directly notifying impacted customers and provided them with instructions for contacting Microsoft with questions or concerns. If you did not receive a Message Center communication, our investigation did not identify an impact to you or your organization.

-MSRC

文章来源: https://msrc-blog.microsoft.com/2022/10/19/investigation-regarding-misconfigured-microsoft-storage-location-2/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)