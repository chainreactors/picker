---
title: SAP Commerce Cloud 2211 – A Not-So-Brief Summary
url: https://blogs.sap.com/2022/12/06/sap-commerce-cloud-2211-a-not-so-brief-summary/
source: SAP Blogs
date: 2022-12-07
fetch_date: 2025-10-04T00:40:27.925867
---

# SAP Commerce Cloud 2211 – A Not-So-Brief Summary

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* SAP Commerce Cloud 2211 - A Not-So-Brief Summary

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/13119&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commerce Cloud 2211 - A Not-So-Brief Summary](/t5/crm-and-cx-blog-posts-by-sap/sap-commerce-cloud-2211-a-not-so-brief-summary/ba-p/13560724)

![cuikenjian](https://avatars.profile.sap.com/e/9/ide9a9cab2d329e62de1f05e6c09818d7c937495a31d36cdf1e897b7b12e99b944_small.jpeg "cuikenjian")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[cuikenjian](https://community.sap.com/t5/user/viewprofilepage/user-id/41892)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=13119)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/13119)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560724)

‎2022 Dec 06
8:23 PM

[27
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/13119/tab/all-users "Click here to see who gave kudos to this post.")

10,981

* SAP Managed Tags
* [SAP Commerce](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)

* [SAP Commerce

  SAP Commerce](/t5/c-khhcw49343/SAP%2BCommerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-11-28-at-21.33.31.png)

## Abstract

SAP Commerce Cloud 2211 version was released just not long ago, there is a great summary about the major new features in the release note [here](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/10886447b5174d2a921d48926f30eb6a/cc9655536f8044419f1ca36977b524c7.html), or there is also the feature announcement table with the concrete details and links in the typical What's New help page [here](https://help.sap.com/whats-new/3d7190d2aab14c7d92f918cc3fa9a024?locale=en-US).

But what if you want to find out more beyond the brief summary in the release note, but you don't have much time to go over the concrete details of the new features row-by-row in the feature table? This blog post will go into a bit more detail of the new features and hopefully can give you a not-so-brief summary of what you want.

Note: you can also use this blog post as study material for attending the following stay current programs:

* [SAP Commerce Cloud for Business User 2211 Stay Current](https://staycurrent-prod.cfapps.eu10.hana.ondemand.com/#/learn?programId=C4H320D_SC_EN_2211) (intro blog post [here](https://blogs.sap.com/2022/12/07/stay-current-with-sap-commerce-cloud-business-user-2211/))

* [SAP Commerce Cloud Developer 2211 Stay Current](https://staycurrent-prod.cfapps.eu10.hana.ondemand.com/#/learn?programId=C4H340D_SC_EN_2211) (intro blog post [here](https://blogs.sap.com/2022/12/07/stay-current-with-sap-commerce-cloud-developer-2211/))

to keep you sap commerce cloud certification(s) up2date.

## First of all

SAP Commerce Cloud 2211 version is the **first** **cloud-only** version. What does it mean? There are 2 points worth mentioning:

First, it's **only** available in SAP Commerce Cloud in the Public Cloud. If you are running On-Prem, or if you are deploying on other non-SAP managed infrastructures/servers? it's not possible to upgrade you commerce cloud to the 2211 version.

Second, you might also have noticed, if you check the normal SAP Commerce Help Portal Page [here](https://help.sap.com/docs/SAP_COMMERCE), you will find that the 2205 version is the latest version. Only if you check the **SAP Commerce** **Cloud** [Help Portal Page](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD), you will find the 2211 version as below:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-02-at-22.23.27.png)

SAP Commerce Cloud 2211 Help Portal

Alright, let's now go into the following areas to highlight the important new features of the 2211 release:

* SAP Commerce Cloud Composable Storefront

* GUI

* CMS

* B2B Commerce

* yForms

* Platform

* Cloud Portal

* Intelligent Selling Services for SAP Commerce Cloud

* Integration

## SAP Commerce Cloud, Composable Storefront

In addition to **deprecating** the accelerator storefront and the related addon extensions, as well as OCC template extensions since 2205 (concrete details [here](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/7e47d40a176d48ba914b50957d003804/1f1c6885781a4267a99c5d619d1f1edd.html)), the **SAP Commerce Cloud, Composable Storefront** is released in 2211 version.

There are some key facts about this new storefront:

* it is **based on** the Spartacus open source project, but **different** from the Spartacus storefront, because:

* it is included as an **official** product in SAP Commerce Cloud.

* it has its own help portal page now [here](https://help.sap.com/docs/SAP_COMMERCE_COMPOSABLE_STOREFRONT), which is **not** the Spartacus open source page.

* its current version is **5.0**, different from the latest version 4.3 of Spartacus.

* It can be downloaded from the Repository Based Shipment Channel (RBSC), the concrete steps are [here](https://help.sap.com/docs/SAP_COMMERCE_COMPOSABLE_STOREFRONT/cfcf687ce2544bba9799aa6c8314ecd0/5de67850bd8d487181fef9c9ba59a31d.html#loio5de67850bd8d487181fef9c9ba59a31d). (which is different from Spartacus)

* It is not possible to build the JavaScript-based storefronts with Node.js 12 any more, you need to use Node.js 16 or 14(14.15) instead (but please note: support for node14 ends in 2023). This affects directly the nodeVersion property in manifest.json file.

Simply speaking, SAP Commerce Cloud, Composable Storefront becomes the strategic storefront going forward for SAP Commerce Cloud.

## GUI

We will brief about the 6 following features:

1. When you open Backoffice (or SmartEdit), you will first notice a slightly different look & feel, as all SAP GUIs will share the more consistent look. You can see that there are different but more intuitive icons everywhere:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-04-at-21.48.08.png)

2. The new theme "SAP Morning Horizon" is now the default theme in Backoffice/SmartEdit:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-04-at-21.53.25.png)

3. There is a new side navigation widget in Backoffice, in case you want to have more focus/space in the center working area:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-04-at-21.54.51.png)

4. When you use the collection browser widget (the one that shows the search result), it's now even possible to directly configure what columns in which order should be displayed.

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-04-at-21.58.08-1.png)

And you will even see the same configuration next time yo...