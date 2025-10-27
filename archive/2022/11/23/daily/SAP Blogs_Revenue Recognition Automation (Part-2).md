---
title: Revenue Recognition Automation (Part-2)
url: https://blogs.sap.com/2022/11/22/revenue-recognition-automation-part-2/
source: SAP Blogs
date: 2022-11-23
fetch_date: 2025-10-03T23:29:11.827557
---

# Revenue Recognition Automation (Part-2)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Revenue Recognition Automation (Part-2)

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67420&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Revenue Recognition Automation (Part-2)](/t5/enterprise-resource-planning-blog-posts-by-members/revenue-recognition-automation-part-2/ba-p/13555257)

![faisal_aslam12478](https://avatars.profile.sap.com/2/5/id256f07037a2e3a4963aba48ad71ecb6111b9605c9e426c58d4646eed5c8edd30_small.jpeg "faisal_aslam12478")

[faisal\_aslam12478](https://community.sap.com/t5/user/viewprofilepage/user-id/826267)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67420)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67420)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555257)

‎2022 Nov 22
8:19 PM

0
Kudos

1,387

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

**Summary**

Revenue is at the heart of all business processes. The collecting of data from many sources is made easier by automated revenue recognition, smoothly. This makes it easier to manage revenue contracts Using automation, you can free up time and resources, allowing you to focus on other tasks and operations.

The Objective of this Blog is to elaborate a mechanism to upload the amount of revenue to be recognized for each sales order line item based on predefined calculations. This blog starts by providing a brief understanding of Revenue Recognition Automation. To accomplish this, previously we have to manually enter the revenue to be recognized at the sales order item level per month. This process is time consuming and error prone. In this blog we will show you how revenue is recognized in an automated process and enhancements that have been introduced.

**Process Involves:**

* Create Sales Order

* Create Project

* Run Revenue Recognition Automation

**Enhancements For Revenue Recognition Automation:**

For this purpose, we have created a Process Flow for Revenue Recognition.

 **Custom Work Center:**

A Custom Work Center have been created with two Views

* Generate Revenue List

* Post Revenue

 **Process Flow For Sales Order and Project:**

Create Sales Order with Project and Note Down the Project and Sales Order ID

Navigate Sales Order Work Center > New > Sales Order

![](/legacyfs/online/storage/blog_attachments/2022/11/PF1-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/PF2-1.png)

 **Process Flow To Generate Revenue List:**

Navigate To  Revenue Recognition Automation Work Center > Click on Generate Revenue List > Click on List Data > Then Click on Generate Data.

![](/legacyfs/online/storage/blog_attachments/2022/11/PF3.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/PF4.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/PF5.png)

**Process Flow For Post Revenue:**

Navigate the Revenue Recognition Automation Work Center > Click on Revenue Recognition Automation > Click on Mark for Posting > Then Click on Posted

![](/legacyfs/online/storage/blog_attachments/2022/11/PF6.png)

I hope it would be helpful for those who want to understand the basic process of ‘Revenue recognition Automation’ in SAP Business ByDesign.

Do follow and Stay connected through your valuables comments and thoughts in comment section.

[https://help.sap.com/docs/SAP\_BUSINESS\_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2ccb31fb722d10148fa...](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2ccb31fb722d10148fa58affc53c007a.html)

[https://help.sap.com/docs/SAP\_BUSINESS\_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2c2c5b1f722d101481f...](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2c2c5b1f722d101481fb945868a9e629.html)

[https://help.sap.com/docs/SAP\_BUSINESS\_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d00fa4e722d10148c8...](https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN/2754875d2d2a403f95e58a41a9c7d6de/2d00fa4e722d10148c80a5926e8c7984.html)

<https://blogs.sap.com/2018/06/08/understanding-revenue-recognition-over-time-an-explanatory-example/>

<https://blogs.sap.com/2022/11/02/revenue-recognition-for-sale-order-based-on-accrual-method-part-1/>

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Frevenue-recognition-automation-part-2%2Fba-p%2F13555257%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Question on Scope Item 4GQ – Event-Based Revenue Recognition](/t5/enterprise-resource-planning-q-a/question-on-scope-item-4gq-event-based-revenue-recognition/qaq-p/14232132)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [VIM Foundation & Invoice Solution Configuration Overview](/t5/enterprise-resource-planning-blog-posts-by-sap/vim-foundation-amp-invoice-solution-configuration-overview/ba-p/14229743)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Sunday
* [How to trace the service confirmation document and its accounting impact in SAP S/4HANA Cloud Public](/t5/enterprise-resource-planning-q-a/how-to-trace-the-service-confirmation-document-and-its-accounting-impact-in/qaq-p/14221163)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [Mid-Market SaaS Companies: Running SaaS with Cloud Agility vs. Duct-Tape Systems – Best Practice](/t5/enterprise-resource-planning-blog-posts-by-sap/mid-market-saas-companies-running-saas-with-cloud-agility-vs-duct-tape/ba-p/14218380)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [BKP - Customer Returns Project Solution for Advanced Intercompany Sales](/t5/enterprise-resource-planning-blog-posts-by-sap/bkp-customer-returns-project-solution-for-advanced-intercompany-sales/ba-p/14218028)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6...