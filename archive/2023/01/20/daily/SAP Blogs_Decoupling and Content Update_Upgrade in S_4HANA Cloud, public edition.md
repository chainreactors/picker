---
title: Decoupling and Content Update/Upgrade in S/4HANA Cloud, public edition
url: https://blogs.sap.com/2023/01/19/decoupling-and-content-update-and-upgrade-in-s-4hana-cloud-public-edition/
source: SAP Blogs
date: 2023-01-20
fetch_date: 2025-10-04T04:22:51.076398
---

# Decoupling and Content Update/Upgrade in S/4HANA Cloud, public edition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Decoupling and Content Update/Upgrade in S/4HANA C...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53321&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Decoupling and Content Update/Upgrade in S/4HANA Cloud, public edition](/t5/enterprise-resource-planning-blog-posts-by-sap/decoupling-and-content-update-upgrade-in-s-4hana-cloud-public-edition/ba-p/13569883)

![Ying](https://avatars.profile.sap.com/5/e/id5ebdfc9e14ee56abf1a20b7a663064899f138a34605c98ded622ef10f68feff3_small.jpeg "Ying")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Ying](https://community.sap.com/t5/user/viewprofilepage/user-id/78188)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53321)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53321)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569883)

‎2023 Jan 19
8:26 PM

[13
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53321/tab/all-users "Click here to see who gave kudos to this post.")

2,525

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)

View products (2)

In one of my last year's blogs on [Upgrade of S/4HANA Cloud, public edition (3 system landscape)](https://blogs.sap.com/2022/10/28/upgrade-of-s-4hana-cloud-public-edition-3-system-landscape/), I touched upon the topic of Decoupling where upgrade/update of Software vs. Content are delivered separately. In this blog, I would like to use a hypothetical scenario to describe in more details how decoupling works, which personally I believe, it is another effort of SAP trying to improve in the Cloud ERP world, delivering innovations in a continuous base yet allow customer to "consume" these new innovations as needed.

Imagine there is business functionality in Purchasing where an approval step is required when total value of Purchase Order is over certain dollar amount. To make things flexible per different customer's need, there is a Configuration Activity where customer can decide the dollar amount based on different Purchase Order Type. For example, direct material purchases may have high amount, while expense type of purchase probably requires approval at a lower amount.

To provide that functionality, SAP delivers new approval screen, new logic in code and new table structure. Examples of Purchase Order Types are included in table with initial value \* in the Amount so that this functionality is only in use when customer choose to maintain the actual amount in the table. In other words, by default if customer don't do anything, this functionality will be bypassed with the initial \* value.

What Decoupling means is that the initial value in the table with examples of Purchase Order Types and \* value in Amount is delivered by SAP as "reference" content. It is deployed to S/4HANA System from the SAP Central Business Configuration tool. Customers can at a later point, define the Amount for Purchas Order Types when they are ready to utilize the functionality. This customer specific data in same table is considered as "active" or "business" content.

![](/legacyfs/online/storage/blog_attachments/2023/01/decoupling.jpg)

Let's assume that in the next update or upgrade, this functionality is improved. Now, not only customers can control the approval by Purchase Order Type, they can also control it via Material Type. For example, directly purchase of raw materials can have a different threshold compares to other Material Types. (See #3 in picture below).

To make that feature available to customer, from Software side, screen, code and table need to be updated. As for the initial value of reference content in the configuration table, it also needs to be adjusted to include \* value in the new Material Type column. (See #1 in picture below). So, by default the original functionality and the enhanced feature won't impact customer if they choose not to implement it.

What happens to customer who already have implemented the older version of functionality? Updated content with initial \* value in the new Material Type field of the new structure will be in a Transport Request, deployed from SAP Central Business Configuration to S/4HANA system during an update or upgrade. (See #2 in table below). Existing functionality of different $ Amount is still applicable to Purchase Order Type only. Customer can at a later point decide to include additional control at Material Type level, or they can choose to operate as it is.

![](/legacyfs/online/storage/blog_attachments/2023/01/upgrade-2.jpg)

Now with that understanding, hopefully the respective Activate content [update](https://go.support.sap.com/roadmapviewer/#/group/658F507A-D6F5-4B78-9EE1-0300C5F1E40F/roadmap/82b2db84548d41209cda972f0fac428b:FA163ED752201EDABFE83D133CFCFD51/node/FA163ED752201EDBBF8F41FDDAB71920) and [upgrade](https://go.support.sap.com/roadmapviewer/#/group/1B9D1B79-D03B-42F6-937C-08DE7C252BB6/roadmap/b6cc8dc5bbb749a59e1e21a4796c796f:FA163ED752201EDBA8A6D0815E450F41/node/FA163ED752201EEBA9D28C1A4AF94543) tasks will make more sense to you when managing your transport request from updates and upgrades when you preparing for the next delivery of SAP innovations.

For an overview of upgrade, check out my previous blog on [Upgrade of S/4HANA Cloud, public edition (3 system landscape)](https://blogs.sap.com/2022/10/28/upgrade-of-s-4hana-cloud-public-edition-3-system-landscape/), and the [upgrade roadmap](https://go.support.sap.com/roadmapviewer/#/group/1B9D1B79-D03B-42F6-937C-08DE7C252BB6/roadmapOverviewPage/b6cc8dc5bbb749a59e1e21a4796c796f).

**SAP Activate Minute**

Check-out our bite-size videos on SAP Activate Minute on our [YouTube playlist](https://www.youtube.com/playlist?list=PLpQebylHrdh7EjybM29pPxT72p35fDMkO). New videos are dropping every two weeks in 2023.

**Stay tuned for more updates and blogs.**

Follow the [SAP Activate](https://community.sap.com/topics/activate) page on the SAP Community. Remember to turn on your notification to receive updates or information about items requiring your attention. To enable notifications, follow the steps on the [SAP Community Resources](https://community.sap.com/resources/getting-started#Your_Notification_Settings) page.

Check out the [Q&A](https://answers.sap.com/tags/714d86bf-f0de-4038-81e4-25c791c15f0c) section of our community for some frequently asked questions or raise your own.

You can ...