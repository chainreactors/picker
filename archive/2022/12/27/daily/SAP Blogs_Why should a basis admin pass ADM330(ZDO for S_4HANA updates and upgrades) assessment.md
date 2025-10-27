---
title: Why should a basis admin pass ADM330(ZDO for S/4HANA updates and upgrades) assessment
url: https://blogs.sap.com/2022/12/26/why-should-a-basis-admin-pass-adm330zdo-for-s-4hana-updates-and-upgrades-assessment/
source: SAP Blogs
date: 2022-12-27
fetch_date: 2025-10-04T02:32:55.231489
---

# Why should a basis admin pass ADM330(ZDO for S/4HANA updates and upgrades) assessment

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Why should a basis admin pass ADM330(ZDO for S/4HA...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67619&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Why should a basis admin pass ADM330(ZDO for S/4HANA updates and upgrades) assessment](/t5/enterprise-resource-planning-blog-posts-by-members/why-should-a-basis-admin-pass-adm330-zdo-for-s-4hana-updates-and-upgrades/ba-p/13558058)

![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")

[rajarajeswari\_kaliyaperum](https://community.sap.com/t5/user/viewprofilepage/user-id/654809)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67619)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67619)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558058)

‎2022 Dec 26
11:39 AM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67619/tab/all-users "Click here to see who gave kudos to this post.")

9,073

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Basis Technology](https://community.sap.com/t5/c-khhcw49343/Basis%2520Technology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Basis Technology

  Topic](/t5/c-khhcw49343/Basis%2BTechnology/pd-p/7bf2eaed-4604-44ae-bad7-d2d2d5c58c54)

View products (3)

In this blog, I wish to discuss the assessment ADM330 which focuses on enabling a basis expert/consultant to get authorized to run ZDO upgrades on S/4HANA starting from S/4HANA2020.

Upgrades form a crucial technical activity that almost all the SAP basis experts must be performing in their customer landscape. Most of the customers are worried about technical downtime during these upgrades and are looking for ways to effectively optimize the downtime. To aid customers and partners in this area SAP is providing MDS services that are carried out by SAP themselves. However, with the release of this exam to partners, customers now need not have to fully rely on SAP to perform Zero-downtime upgrades or updates for their S/4HANA systems starting from version 2020.

By writing this exam, the basis SME gets authorization in the form of a password that SAP will provide when he/she raises a ticket under the component BC-UPG-DTM-TLA. Other details that must be supplied in this ticket is

a. SID

b.SUM version

c. Knowledge badge.

The password thus attained must be supplied into SUM.

Once we open the SUM UI, post supplying the XML, SUM will prompt for 3 options and we must choose "Downtime-optimized" option and within that , we must choose "Zero Downtime Option(ZDO). Once we choose this option, we will be asked for the above specified password.

***NOTE:**One must understand that the near-zero downtime(nZDO) is different from this zero downtime approach(ZDO).*

If you need more technical details on this ZDO, check out my below blog.

<https://blogs.sap.com/2022/12/26/technical-details-on-s-4hana-zdozero-downtime-upgrades-updates/>

Going back to why this exam is important for a basis expert is

1. This might be the way forward with respect to upgrades/updates where the customer is aiming for zero downtime.

1. It is straightforward and easy to understand for someone who has already performed an upgrade via SUM

1. The assessment is simple and easy to clear with just 12 straightforward questions. Anyone who have gone through the ADM330 can quickly clear this in the first attempt. its duration is 0.25mins

1. This is free for anyone with a professional learning hub access

For more information please refer OSS note 2707731(<http://help.sap.com/disclaimer?site=https://launchpad.support.sap.com/#/notes/2707731> ). This OSS note also has a direct link to this course and assessment.

More information and guides can be found in below link.

<https://support.sap.com/en/tools/software-logistics-tools.html>

![](/legacyfs/online/storage/blog_attachments/2022/12/1-17.jpg)

ZDO option is available for usage via the normal SUM2.0 tool. This does have a need for additional licenses.

If you already have learning hub access, search for learning content -> ADM330. Once you complete the learning journey, search for ADM330 assessment and take up the 30 mins assessment.

![](/legacyfs/online/storage/blog_attachments/2022/12/1-25.jpg)

Thanks for reading. If you find this useful, do not forget to hit a like or leave a comment.

Rajarajeswari Kaliyaperumal
Author of the book 'SAP HANA 2.0 Installation and Administration A Practical Guide'

[Now available in Amazon Kindle, India](https://amzn.in/d/7kSqOQk) and [Amazon Kindle, US](https://a.co/d/azRLgj0)

* [ADM330](/t5/tag/ADM330/tg-p/board-id/erp-blog-members)
* [downtime optimized](/t5/tag/downtime%20optimized/tg-p/board-id/erp-blog-members)
* [S4HANA](/t5/tag/S4HANA/tg-p/board-id/erp-blog-members)
* [SDMI](/t5/tag/SDMI/tg-p/board-id/erp-blog-members)
* [Upgrade](/t5/tag/Upgrade/tg-p/board-id/erp-blog-members)
* [zdo](/t5/tag/zdo/tg-p/board-id/erp-blog-members)
* [zero downtime](/t5/tag/zero%20downtime/tg-p/board-id/erp-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fwhy-should-a-basis-admin-pass-adm330-zdo-for-s-4hana-updates-and-upgrades%2Fba-p%2F13558058%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Preliminary What’s New Information for SAP S/4HANA Cloud Public Edition 2508.2](/t5/enterprise-resource-planning-blog-posts-by-sap/preliminary-what-s-new-information-for-sap-s-4hana-cloud-public-edition/ba-p/14230435)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [SAP S/4HANA Cloud Public Edition 2508.1: Final What's New & Product Assistance available](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-cloud-public-edition-2508-1-final-what-s-new-amp-product/ba-p/14218345)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Preliminary What’s New Information for SAP S/4HANA Cloud Public Edition 2508.1](/t5/enterprise-resource-planning-blog-posts-by-sap/preliminary-what-s-new-information-for-sap-s-4hana-cloud-public-edition/ba-p/1...