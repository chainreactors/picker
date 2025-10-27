---
title: Visibility of charge hierarchy in SAP TM for tendering
url: https://blogs.sap.com/2023/04/20/visibility-of-charge-hierarchy-in-sap-tm-for-tendering/
source: SAP Blogs
date: 2023-04-21
fetch_date: 2025-10-04T11:34:27.463191
---

# Visibility of charge hierarchy in SAP TM for tendering

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* Visibility of charge hierarchy in SAP TM for tende...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/4799&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Visibility of charge hierarchy in SAP TM for tendering](/t5/supply-chain-management-blog-posts-by-sap/visibility-of-charge-hierarchy-in-sap-tm-for-tendering/ba-p/13551782)

![praveshnegi](https://avatars.profile.sap.com/9/6/id96addd6e7166a7894708922d3f044bd05d5a63dba88df8f3690e9a0295829abc_small.jpeg "praveshnegi")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[praveshnegi](https://community.sap.com/t5/user/viewprofilepage/user-id/151907)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=4799)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/4799)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551782)

‎2023 Apr 20
11:27 PM

[1
Kudo](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/4799/tab/all-users "Click here to see who gave kudos to this post.")

2,317

* SAP Managed Tags
* [SAP Transportation Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Transportation%2520Management/pd-p/01200615320800000686)

* [SAP Transportation Management

  SAP Transportation Management](/t5/c-khhcw49343/SAP%2BTransportation%2BManagement/pd-p/01200615320800000686)

View products (1)

## Introduction

In this blog post we talk about the freight tendering with SAP S/4HANA Transportation Management with focus on sending and receiving charge hierarchy during the tendering process. Freight tendering process is also explained in our SAP application documentation which you can find [here](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/6c921d2b67584ec2a2a7c0bcc8a0b8dc.html?locale=en-US).

![](/legacyfs/online/storage/blog_attachments/2023/04/Tendering-Process.png)

Tendering Process

At the time of creation of a tendering plan, you would be interested in proposing a price limit to the involved parties (carriers). The price limit can be an absolute price limit or charge hierarchy.

* Absolute Price Limit
  Total amount is sent to the carriers as price limit via EDI message.

* Charge Hierarchy
  Complete charge hierarchy created during the charge calculation is sent out to the carriers via EDI message. You can view the charge hierarchy before publishing your tender.

*Note: Instead of using EDI messages, also the [FIORI carrier collaboration app](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/84d9d78a1e0c4088af16683810a6eaec.html?locale=en-US) could be used by the carrier representative.*

## Pre-requisites

The pre-requisite steps for using charge hierarchy during tendering process are also explained in the documentation link: [Calculation of Price Limits](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/e3dc5400c1cc41d1bc0ae0e7fd9aa5a2/7581d93f88344ca4880b2f09d5243cf4.html?locale=en-US).

## Steps

You start by creation of tendering plan. Important thing to note if you want to enable charge hierarchy is highlighted in the following screenshot.

## ![](/legacyfs/online/storage/blog_attachments/2023/04/Tendering-Plan-2.png)

Tendering Plan

Price Details can be set to 'Charge Hierarchy' which specifies that you would want to transmit and receive price limit using complete charge hierarchy.

Carrier specific freight agreement indicator specifies whether you would want charge calculation engine to use existing freight agreements between involved parties in tendering plan and requesting organisation.

Action "Propose -> Price Limit" performs the charge calculation for the involved parties in the tendering plan. This step is mandatory before you publish the tendering plan.

Post this step you publish the tendering plan. This shall send request to carrier as an EDI message as shown below which comprises of transportation charges.

![](/legacyfs/online/storage/blog_attachments/2023/04/Request-for-Quotation.png)

Request for Quotation

Carrier would then receive the request for quote and shall be able to send a quote using the same hierarchy of charges to confirm their participation as long as visibility settings in your tendering plan allows carrier to make proposal to the price limit.

![](/legacyfs/online/storage/blog_attachments/2023/04/Quotation-for-Confirmation.png)

Quotation for Confirmation

The quotations can then be evaluated and awarded as per normal process. Once awarding is done, the charges proposed by carrier are copied to the freight order charges.

## Conclusion

With the steps described above, you can communicate your charges structure to the carriers during the tendering process. This would allow you to also receive quotations in the same charges structure if you allow your carriers to respond with deviating price limits.

Feel free to share feedback or thoughts in a comment

**Related topics**

[SAP Transportation Management Topic Page](https://community.sap.com/topics/transportation-management)
[Ask questions about SAP Transportation Management and follow](https://answers.sap.com/tags/01200615320800000686)
Read other [SAP Transportation Management blog posts](https://blogs.sap.com/tags/01200615320800000686) and follow
Please follow my pravesh for future posts

Labels

* [Technology Updates](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-sap%2Fvisibility-of-charge-hierarchy-in-sap-tm-for-tendering%2Fba-p%2F13551782%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [The Ultimate Guide to SAP S/4HANA Logistics with Extended Warehouse Management (EWM)](/t5/supply-chain-management-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-logistics-with-extended-warehouse/ba-p/14223412)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  2 weeks ago
* [5C Framework for SAP Integrated Business Planning Data Validation Strategy](/t5/supply-chain-management-blog-posts-by-members/5c-framework-for-sap-integrated-business-planning-data-validation-strategy/ba-p/14212656)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  2 weeks ago
* [Unlocking Shipment Visibility with Shippeo and SAP Business Network Global Track and Trace](/t5/supply-chain-management-blog-posts-by-sap/unlocking-shipment-visibility-with-shippeo-and-sap-business-network-global/ba-p/14186181)
  in [Supply Chain Management Blog Posts by SAP](...