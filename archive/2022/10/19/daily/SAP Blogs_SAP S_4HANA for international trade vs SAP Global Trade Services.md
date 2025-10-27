---
title: SAP S/4HANA for international trade vs SAP Global Trade Services
url: https://blogs.sap.com/2022/10/18/sap-s-4hana-for-international-trade-vs-sap-global-trade-services/
source: SAP Blogs
date: 2022-10-19
fetch_date: 2025-10-03T20:14:47.944143
---

# SAP S/4HANA for international trade vs SAP Global Trade Services

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* SAP S/4HANA for international trade vs SAP Global ...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7629&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA for international trade vs SAP Global Trade Services](/t5/financial-management-blog-posts-by-sap/sap-s-4hana-for-international-trade-vs-sap-global-trade-services/ba-p/13536277)

![Trond](https://avatars.profile.sap.com/2/2/id2286b6c4e2c8db0f24622fb604523d2dded37e5e23577c740fe58bee5d0bbbf8_small.jpeg "Trond")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Trond](https://community.sap.com/t5/user/viewprofilepage/user-id/142795)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7629)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7629)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13536277)

‎2022 Oct 18
7:36 PM

[38
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7629/tab/all-users "Click here to see who gave kudos to this post.")

48,131

* SAP Managed Tags
* [SAP Global Trade Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Global%2520Trade%2520Services/pd-p/01200615320800000574)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP Global Trade Services

  SAP Global Trade Services](/t5/c-khhcw49343/SAP%2BGlobal%2BTrade%2BServices/pd-p/01200615320800000574)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (2)

This blog provides guidance on when SAP S/4HANA for international trade is sufficient and when SAP Global Trade Services (GTS) is the right choice. Ultimately, it boils down to the functional requirements that need to be covered.

SAP S/4HANA for international trade is part of the SAP S/4HANA core and is included in the SAP S/4HANA user license. The functional scope is identical for SAP S/4HANA on-premise/PCE and SAP S/4HANA public cloud. SAP S/4HANA for international trade is not a replacement for SAP GTS. SAP Global Trade Services are here to stay and remains the flagship product of SAP in the area of cross-border compliance and customs management.

SAP S/4HANA for international trade is meant to cover basic requirements for export control, Intrastat reporting and product classification. In this regard, international trade is comparable with the SD-Foreign Trade functionality in SAP ECC. However, Foreign Trade and international trade are not functionally identical or similar feature by feature.

## Classification

![](/legacyfs/online/storage/blog_attachments/2022/10/Skjermbilde-2022-10-12-kl.-08.16.10.png)

Classification in SAP S/4HANA for international trade vs SAP GTS

SAP S/4HANA for international trade supports classification limited to commodity codes, HS tariff codes and Export Control Classification Numbers (ECCN). For many companies, this is sufficient.

SAP GTS supports a more comprehensive range of classifications; conceptually, any numbering scheme can be defined. GTS also supports the correlation between numbering schemes, for instance, that a specific assignment of an HS-code triggers mandatory maintenance of another classification, for example, FDA codes or ECCN.

With SAP GTS, you can also automatically re-classify products with the help of re-classification files from content providers. Changes in the Harmonized Tariff systems occur regularly, and the re-classification option is beneficial.

## Compliance Management

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-14-at-18.34.33.png)

Compliance Management in SAP S/4HANA for international trade vs SAP GTS

SAP S/4HANA for international trade provides basic compliance management capabilities; however, without integration into SAP Watch List Screening or SAP GTS, no check against sanctioned party lists is available. The legal export controls may suffice if products are only ECCN-controlled. For embargoes, international trade supports the relatively simple scenario of a full embargo (without the need for country pairs). On the other hand, SAP Global Trade Services is the obvious choice for customers facing more complex compliance regulations, such as ITAR or US re-export regulations, etc.

For a more comprehensive comparison, please take a look at this post:[https://blogs.sap.com/2022/10/05/how-to-comply-with-embargo-sanctioned-party-lists-and-export-contro...](https://blogs.sap.com/2022/10/05/how-to-comply-with-embargo-sanctioned-party-lists-and-export-control-in-sap/)

## Intrastat

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-14-at-18.27.45.png)

Intrastat reporting in SAP S/4HANA for international trade vs SAP GTS

Intrastat reporting capabilities are crucial within the European Union since it is a legal requirement to report intra-community movements. From a functional perspective, SAP S/4HANA for international trade and SAP GTS are equal in regards to Intrastat reporting. The only upside of choosing SAP GTS is that GTS can report across multiple instances of ERP and, therefore, support scenarios where reporting needs to take place across, for example, an SAP ECC instance and another instance of SAP S/4HANA. If Intrastat reporting is your only cross-border related functional requirement, acquiring GTS for only this purpose would probably not make much sense.

## Functionality Covered by SAP Global Trade Services Only

![](/legacyfs/online/storage/blog_attachments/2022/10/Screenshot-2022-10-14-at-18.25.36.png)

Functionality supported by SAP GTS only.

And then, we will look at some global trade-related functionality only available in SAP GTS.

SAP GTS is the only option for companies that would like to generate the declarations for import, transit or export themselves, either for self-filing (in selected countries) or through submission through a customs broker. Self-filers typically save a lot on transactional broker fees, can expedite their goods faster and are more in control of the accuracy of the declaration and the calculation of duties. Self-filing does, on the other hand, require in-house competence and approval by customs authorities.

Exploring the business benefits of a customs warehouse (inventory under customs control) or even moving into processing under customs control, such as IPR or OPR, will require using SAP GTS. The potential cost and complexity of running SAP GTS are generously rewarded, as these options represent financial savings and simplifications in the supply chain and manufacturing processes.

Preferential Management, utilizing preferential origin as enabled through Free Trade Agreements, is becoming increasingly relevant for companies. But, again, SAP GTS is the only option as this is not supported in SAP S/4HANA for international trade. Furthermore, the potential saving...