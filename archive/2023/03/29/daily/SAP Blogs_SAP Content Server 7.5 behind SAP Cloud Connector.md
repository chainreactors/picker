---
title: SAP Content Server 7.5 behind SAP Cloud Connector
url: https://blogs.sap.com/2023/03/28/sap-content-server-7.5-behind-sap-cloud-connector/
source: SAP Blogs
date: 2023-03-29
fetch_date: 2025-10-04T11:00:49.195717
---

# SAP Content Server 7.5 behind SAP Cloud Connector

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP Content Server 7.5 behind SAP Cloud Connector

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51699&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Content Server 7.5 behind SAP Cloud Connector](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-content-server-7-5-behind-sap-cloud-connector/ba-p/13559007)

![TobiasWin](https://avatars.profile.sap.com/0/3/id03aaf798aa6cb982343feeed54973970b85adc5170e5f9e59403f4936fbe75cd_small.jpeg "TobiasWin")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[TobiasWin](https://community.sap.com/t5/user/viewprofilepage/user-id/196667)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51699)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51699)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559007)

‎2023 Mar 29
12:01 AM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51699/tab/all-users "Click here to see who gave kudos to this post.")

2,062

* SAP Managed Tags
* [PLM Document Management System (DMS)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Document%2520Management%2520System%2520%28DMS%29/pd-p/318021688820573698933533760680517)

* [PLM Document Management System (DMS)

  Software Product Function](/t5/c-khhcw49343/PLM%2BDocument%2BManagement%2BSystem%2B%252528DMS%252529/pd-p/318021688820573698933533760680517)

View products (1)

With the move of SAP systems from on-Premise to the Cloud, hybrid scenarios are becoming more prevalent. One such scenario arises when the SAP Content Server remains located on-Premise, and needs to be published to the Internet so that it can be reached by Cloud-based systems. One way to achieve this is to use the SAP Cloud Connector.

But there is a problem. The Cloud Connector periodically sends HTTP requests to the internal host to check its availability, These HTTP requests are generated as http/<https://internal_host:port>. However, by default, Content Server 7.5 only processes URLs that start with whatever prefix is defined with parameter icm/HTTP/contentserver\_0 (typically /sapcs or /ContentServer/ContentSerer.dll.) Every other prefix result in a **500 Internal Server Error**. In the Cloud Connector, the Content Server therefore remains in status **Not Reachable**.

Since the Cloud Connector does not offer the possibility to choose the URL prefix that is used to check the availability of the internal host, we need to make sure that the Content Server responds with **200 OK** to the requests without prefix. The easiest solution is to configure a file access handler in the Content Server that returns an empty file:

```
icm/HTTP/file_access_0 = PREFIX=/, DOCROOT=$(DIR_GLOBAL)/status, BROWSEDIR=1, DIRINDEX=index.txt
```

Any directory can be specified with DOCROOT, but it should be an empty directory that has no sub directories or files in it. In this directory, create an empty file with name index.txt. If desired, the file could contain some kind of status text that would be returned as response body, but this is not necessary for the Cloud Connector.

Documentation for the file access handler:
[https://help.sap.com/docs/SAP\_NETWEAVER\_750/683d6a1797a34730a6e005d1e8de6f22/4ed6be92ad5e4bf4aebd8bb...](https://help.sap.com/docs/SAP_NETWEAVER_750/683d6a1797a34730a6e005d1e8de6f22/4ed6be92ad5e4bf4aebd8bb39cfbda4c.html?version=7.5.9&locale=en-US)

With this file access handler in place (and after a restart of the Content Server to activate the change in the profile), the Content Server will return **200 OK** and the content of the file index.txt for URL prefix "/". The availability checks of the Cloud Connector will now be successful, and the internal host will become **Reachable**.

*Remark: As a side effect, all other prefixes (except the prefix defined with icm/HTTP/contentserver\_0 of course) will lead to error **404 Not Found** instead of the **500 Internal Server Error**. That should not be an issue for the functionality of the Content Server, with or without Cloud Connector.*

*Remark to earlier releases of SAP Content Server: SAP Content Server 6.5 does not have this problem with the Cloud Connector because it is based on a plugin within the Apache HTTP Server (Unix) or Microsoft IIS (Windows), both of which are typically configured with a default site that successfully responds to URL prefix "/".*

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [SAP Content Server](/t5/tag/SAP%20Content%20Server/tg-p/board-id/erp-blog-sap)
* [SAP Content Server 753](/t5/tag/SAP%20Content%20Server%20753/tg-p/board-id/erp-blog-sap)
* [SAP Content Server 754](/t5/tag/SAP%20Content%20Server%20754/tg-p/board-id/erp-blog-sap)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fsap-content-server-7-5-behind-sap-cloud-connector%2Fba-p%2F13559007%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Unlocking Efficiency: New SAP Signavio Content for Agricultural Origination & Trading](/t5/enterprise-resource-planning-blog-posts-by-sap/unlocking-efficiency-new-sap-signavio-content-for-agricultural-origination/ba-p/14233482)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [Preliminary What’s New Information for SAP S/4HANA Cloud Public Edition 2508.2](/t5/enterprise-resource-planning-blog-posts-by-sap/preliminary-what-s-new-information-for-sap-s-4hana-cloud-public-edition/ba-p/14230435)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning...