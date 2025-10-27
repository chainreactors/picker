---
title: Auto dispute case for a chargeback through residual item
url: https://blogs.sap.com/2023/01/10/auto-dispute-case-for-a-chargeback-through-residual-item/
source: SAP Blogs
date: 2023-01-11
fetch_date: 2025-10-04T03:31:55.799335
---

# Auto dispute case for a chargeback through residual item

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Auto dispute case for a chargeback through residua...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68333&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Auto dispute case for a chargeback through residual item](/t5/enterprise-resource-planning-blog-posts-by-members/auto-dispute-case-for-a-chargeback-through-residual-item/ba-p/13566680)

![dgkrishnan](https://avatars.profile.sap.com/f/6/idf6fc836cc16962cf020a5056969e75714a666c5545e9cc066ee58bbdc767d47e_small.jpeg "dgkrishnan")

[dgkrishnan](https://community.sap.com/t5/user/viewprofilepage/user-id/723777)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68333)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68333)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566680)

‎2023 Jan 10
8:11 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68333/tab/all-users "Click here to see who gave kudos to this post.")

1,615

* SAP Managed Tags
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)

* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)

View products (1)

Author:          *Gopal Dhandapani*

Objective: This Article explains the processing of automating the creation of dispute case when you process incoming payment with residual item resulting in chargeback

**Business need for implementing end to end process for customer open item management including chargebacks**

Business has huge volume of customer invoices to be processed through the cash application process

Currently business is processing lot of chargebacks manually

Charge backs can be either from Lockbox process or from processing bank statements or manual incoming payment

Processing incoming payments together with creation of residual items with new document type

Capture the proper reason code in residual item line item if it is a chargeback

Managing residual items with new document type for ease of monitoring

Automation of dispute case creation for chargeback out of residual items

Automating the end to end process from incoming payment processing to creation of residual item to dispute case creation

Process flow diagram for Processing Residual payment with auto dispute case creation

![](/legacyfs/online/storage/blog_attachments/2023/01/Process-Flow-Pic1.png)

Business Process

Run Customer open items report FBL5N to review the current open items to check current status

![](/legacyfs/online/storage/blog_attachments/2023/01/FBL5NPic2.png)

Post Incoming payment F-28

![](/legacyfs/online/storage/blog_attachments/2023/01/F28Pic3.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/F28Pic4.png)

Document posted.  First document is for the incoming customer payment posting and second one is the separate document created for the residual item with separate document type

![](/legacyfs/online/storage/blog_attachments/2023/01/F28Pic5.png)

Document No: 4300003000

![](/legacyfs/online/storage/blog_attachments/2023/01/F28Pic6.png)

Document No: 4400004000

![](/legacyfs/online/storage/blog_attachments/2023/01/F28Pic7.png)

FBL5N – Current status of the open item – chargeback through separate residual item is created

![](/legacyfs/online/storage/blog_attachments/2023/01/F28Pic8.png)

Create dispute case – FDM\_AUTO\_CREATE

![](/legacyfs/online/storage/blog_attachments/2023/01/Dispute-Case-PIc-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Dispute-Case-PIc-10.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Dispute-Case-PIc-11.png)

Business Process 2

Auto dispute creation from clearing customer open items with chargeback from residual items

Clear Customer F-32

![](/legacyfs/online/storage/blog_attachments/2023/01/F32Pic12.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/F32Pic13.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/F32Pic14.png)

Two documents get posted.  First one is for clearing the customer open item.  Second document below is for the creation of chargeback as residual item with separate document type

![](/legacyfs/online/storage/blog_attachments/2023/01/F32Pic15.png)

Document No: 3000003001

![](/legacyfs/online/storage/blog_attachments/2023/01/F32Pic16-1.png)

Document No: 4400005001

![](/legacyfs/online/storage/blog_attachments/2023/01/F32Pic17.png)

Create Dispute

![](/legacyfs/online/storage/blog_attachments/2023/01/Dispute-Case-Pic18-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Dispute-Case-Pic19.png)

![](/legacyfs/online/storage/blog_attachments/2023/01/Dispute-Case-Pic20.png)

**Business Benefits:**

This process has been implemented for processing of customer incoming payments, clearing customer open items as well

With this process chargebacks are created with residual items

Chargebacks from residual items are converted to dispute case from background job

Manual intervention for creation of dispute case is eliminated

Business is able to better manage and monitor chargebacks / dispute cases

Business is able to manage higher volume of business

Business has huge volume of customer invoices to be processed through the cash application process

End to end process  has been automated from incoming payment processing to creation of residual item to dispute case creation

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fauto-dispute-case-for-a-chargeback-through-residual-item%2Fba-p%2F13566680%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Finance with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/finance-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14181008)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Aug 15
* [Partial Clearing for Vendors](/t5/enterprise-resource-planning-q-a/partial-clearing-for-vendors/qaq-p/14136403)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2025 Jun 25
* [Chargeback process with conditional contract management](/t5/enterprise-resource-planning-q-a/chargeback-process-with-conditional-contract-management/qaq-p/14105493)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2025 May 19
* [Down Payment not Completely cleared after Posting in F-54](/t5/enterprise-res...