---
title: SAP EBS Electronic Bank Statement Integration Job Log
url: https://blogs.sap.com/2023/01/13/sap-ebs-electronic-bank-statement-integration-job-log/
source: SAP Blogs
date: 2023-01-14
fetch_date: 2025-10-04T03:52:30.775699
---

# SAP EBS Electronic Bank Statement Integration Job Log

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP EBS Electronic Bank Statement Integration Job ...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68515&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP EBS Electronic Bank Statement Integration Job Log](/t5/enterprise-resource-planning-blog-posts-by-members/sap-ebs-electronic-bank-statement-integration-job-log/ba-p/13569843)

![abdellah_khebbari](https://avatars.profile.sap.com/a/f/idaf8994645bcd77785a3d65ba8103136bb99f777a434fdbe63afc14fefb1e3f3d_small.jpeg "abdellah_khebbari")

[abdellah\_khebbari](https://community.sap.com/t5/user/viewprofilepage/user-id/192404)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68515)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68515)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569843)

‎2023 Jan 13
11:51 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68515/tab/all-users "Click here to see who gave kudos to this post.")

4,906

* SAP Managed Tags
* [Treasury Management](https://community.sap.com/t5/c-khhcw49343/Treasury%2520Management/pd-p/e983480f-9abd-4f9f-9935-8486b6708870)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [Treasury Management

  Product Category](/t5/c-khhcw49343/Treasury%2BManagement/pd-p/e983480f-9abd-4f9f-9935-8486b6708870)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/01/ARAL_FRONT_PAGE_3.png)

Sometimes, after EBS integration Job, some bank transactions may fall into errors like you can see below:

***Figure1***![](/legacyfs/online/storage/blog_attachments/2023/01/FEBAN-1.png)

After investigation into job spools, you will find the integrated bank transactions. But, you may have difficulties to find errors log for the not integrated ones.

![](/legacyfs/online/storage/blog_attachments/2023/01/SM37-1.png)

Display spool![](/legacyfs/online/storage/blog_attachments/2023/01/SM37_1.png)

After selection on the approprate bank house bank, the bank transaction code B1 with the amount 80,90 (green light in the figure 1) is shown in the integration report like below:

![](/legacyfs/online/storage/blog_attachments/2023/01/SPOL.png)

But like we can see in the figure 2, several other bank transactions have not been integrated by the EBS Job and the errors log is not available:

***Figure2***![](/legacyfs/online/storage/blog_attachments/2023/01/FEBAN_1-1.png)

To find EBS Integration JOB LOG, one of the possible options of investigations can be explained in three steps like following:

## Step 1 : Get short key for the not integrated bank transactions

In the transaction SE16N, FEBKO table can be used by entering some data in the selection areas like below:

![](/legacyfs/online/storage/blog_attachments/2023/01/FEBKO.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/FEBKO_1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/FEBKO_2.png)

As a result of this query, the bank transactions shown in the figure 2 are clearly visible here and the short key is displayed:

*Total Debit : 4000 and Total Credit 1632*![](/legacyfs/online/storage/blog_attachments/2023/01/FEBKO_RESULT.png)

## Step 2 : Control data by using the short key in FEBEP

By using the short key got in the step 1 like below:

![](/legacyfs/online/storage/blog_attachments/2023/01/FEBEP.png)

the table FEBEP shows in details the bank transactions in the figure 2:

![](/legacyfs/online/storage/blog_attachments/2023/01/FEBEP_RESULT.png)

## Step 3 : Display EBS Job Erros Log by using the Tcode AFAL

In this step, the short key got before can be used like a selection criteria like below:

![](/legacyfs/online/storage/blog_attachments/2023/01/ARAL_SLECT.png)

After launching this report, the three bank transaction shown in the figure 2 are now visibles with their errors log.

![](/legacyfs/online/storage/blog_attachments/2023/01/ARAL_RESULT.png)

For example, the error in the third transaction is caused by not existing GL account.

* [sap bank analyzer](/t5/tag/sap%20bank%20analyzer/tg-p/board-id/erp-blog-members)
* [SAP BANKS](/t5/tag/SAP%20BANKS/tg-p/board-id/erp-blog-members)
* [sap fico](/t5/tag/sap%20fico/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fsap-ebs-electronic-bank-statement-integration-job-log%2Fba-p%2F13569843%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Japan Bank Charges in Payment Run](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-run/ba-p/14231441)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Int4 Suite — your SAP Joule testbed and skills builder](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-your-sap-joule-testbed-and-skills-builder/ba-p/14229790)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Sunday
* [VIM Foundation & Invoice Solution Configuration Overview](/t5/enterprise-resource-planning-blog-posts-by-sap/vim-foundation-amp-invoice-solution-configuration-overview/ba-p/14229743)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Sunday
* [Localization in SAP S/4HANA: Strategic Enabler or Deployment Bottleneck?](/t5/enterprise-resource-planning-blog-posts-by-sap/localization-in-sap-s-4hana-strategic-enabler-or-deployment-bottleneck/ba-p/14218573)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Oman localization in SAP S/4HANA Cloud: what matters for Implementation and beyond](/t5/enterprise-resource-planning-blog-posts-by-sap/oman-localization-in-sap-s-4hana-cloud-what-matters-for-implementation-and/ba-p/14215901)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_O...