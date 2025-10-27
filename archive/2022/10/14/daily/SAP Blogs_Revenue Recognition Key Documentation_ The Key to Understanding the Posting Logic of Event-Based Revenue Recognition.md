---
title: Revenue Recognition Key Documentation: The Key to Understanding the Posting Logic of Event-Based Revenue Recognition
url: https://blogs.sap.com/2022/10/13/revenue-recognition-key-documentation-the-key-to-understanding-the-posting-logic-of-event-based-revenue-recognition/
source: SAP Blogs
date: 2022-10-14
fetch_date: 2025-10-03T19:49:43.896875
---

# Revenue Recognition Key Documentation: The Key to Understanding the Posting Logic of Event-Based Revenue Recognition

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Revenue Recognition Key Documentation: The Key to ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/49285&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Revenue Recognition Key Documentation: The Key to Understanding the Posting Logic of Event-Based Revenue Recognition](/t5/enterprise-resource-planning-blog-posts-by-sap/revenue-recognition-key-documentation-the-key-to-understanding-the-posting/ba-p/13541645)

![Janina_Igers81](https://avatars.profile.sap.com/8/4/id84819afbfc3658724fdf7bff9dcfa6ac3c2e42e823d0cf9029be53de70d4cc2f_small.jpeg "Janina_Igers81")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Janina\_Igers81](https://community.sap.com/t5/user/viewprofilepage/user-id/789726)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=49285)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/49285)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13541645)

‎2022 Oct 13
10:20 PM

[14
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/49285/tab/all-users "Click here to see who gave kudos to this post.")

15,037

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP S/4HANA Cloud Public Edition Professional Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Professional%2520Services/pd-p/a421aaac-1912-4fca-b725-00056d7dadc3)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)

* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)
* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [SAP S/4HANA Cloud Public Edition Professional Services

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BProfessional%2BServices/pd-p/a421aaac-1912-4fca-b725-00056d7dadc3)

View products (3)

One of the basic notions of Event-Based Revenue Recognition in SAP S/4HANA Cloud is that you can control how revenues and costs are recognized for real-time transactions and during period-end closing of a financial period. These transactions are associated with events happening during the processing of a project, sales order, service document, or provider contract. Cost postings are continuously matched to revenues and reported as expenses, while revenues are posted to an income statement account.

Among the most important parameters for this automated revenue recognition process is the revenue recognition key. To put it very simply, a revenue recognition key allows you to control how revenue recognition values are calculated. But if you want to put it a little bit more elaborately and consider this important parameter and its business background in depth, you might start to wonder: Which income statement accounts are the revenues posted to? What about the balance sheet accounts?  And what’s the specific underlying logic for the calculation of the revenue recognition values?

To answer these questions, we have got something to help you. Using the links to the SAP Help Portal provided below, you can find detailed information explaining the posting logic for all available revenue recognition keys in SAP S/4HANA Cloud. This piece of documentation provides an introductory explanation for the revenue recognition key, an example of a business scenario with specific data, a graphic to illustrate the processing steps of the integration scenario and their respective postings to income statement and balance sheet accounts, as well as an explanation for each event and the triggered posting.

Sounds like something you'd be interested in, right? Then check out the following links:

[Revenue Recognition Methods for Customer Projects | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/5e6d33c7a74d4c528d496dde89c8957c.html)

[Revenue Recognition Methods for Revenue-Carrying Enterprise Projects | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/23cee4ab4c5443c6b68e274e69dcf19f.html)

[Revenue Recognition Methods for Sales Orders | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/31c49d58fe6145c0956ef44aa0296237.html)

[Revenue Recognition Methods for Service Contracts | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/5bf037affa8d41389f1594f844df37ee.html)

[Revenue Recognition Methods for Service Orders | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/9de26225237a4e28ba6a07aaf0c81832.html)

[Revenue Recognition Methods for Provider Contracts | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/1c35022d543a40fe8b50da10c9f87842.html)

**Want to know more about Event-Based Revenue Recognition?**

Learning about the revenue recognition keys and their posting logic wasn’t enough?

Then you can read even more about Event-Based Revenue Recognition on the SAP Help Portal: [Event-Based Revenue Recognition | SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/89d896ca9cd64318b1667df5ec00e4b2/7fd9ad1108b94403a2871cf348d4b891.html)

You can also check out the following video on YouTube:

[Event-Based Revenue Recognition for Customer Projects - YouTube](https://www.youtube.com/watch?v=nijkfwAERlE)

Take a look at these microlearnings:

[An Introduction to Event-Based Revenue Recognition](https://microlearning.opensap.com/media/An%2BIntroduction%2Bto%2BEvent-based%2BRevenue%2BRecognition%2B-%2BSAP%2BS%2B4HANA%2BFinancials/1_n5y0gy6r)

[Configuration Settings in Event-Based Revenue Recognition](https://microlearning.opensap.com/media/Configuration%2BSettings%2Bin%2BEvent-Based%2BRevenue%2BRecognition%2B-%2BSAP%2BS%2B4HANA%2BCloud%2BFinancials/1_r9ax4shb)

**Didn’t find everything you were looking for?**

Please don’t hesitate to post questions in the *Comments* section below.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [ebrr](/t5/tag/ebrr/tg-p/board-id/erp-blog-sap)
* [event-based revenue recognition](/t5/tag/event-based%20revenue%20recognition/tg-p/board-id/erp-blog-sap)
* [revenue recognition](/t5/tag/revenue%20recognition/tg-p/board-id/erp-blog-sap)
* [revenue recognition key](/t5/tag/revenue%20recognition%20key/tg-p/board-id/erp-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've...