---
title: Approval Process for Upload Prices in Sales from template-based spreadsheet
url: https://blogs.sap.com/2022/11/30/approval-process-for-upload-prices-in-sales-from-template-based-spreadsheet/
source: SAP Blogs
date: 2022-12-01
fetch_date: 2025-10-04T00:11:25.627154
---

# Approval Process for Upload Prices in Sales from template-based spreadsheet

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Approval Process for Upload Prices in Sales from t...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52661&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Approval Process for Upload Prices in Sales from template-based spreadsheet](/t5/enterprise-resource-planning-blog-posts-by-sap/approval-process-for-upload-prices-in-sales-from-template-based-spreadsheet/ba-p/13565042)

![MENGRI](https://avatars.profile.sap.com/1/d/id1dec5b78303484df5df026e326a9345fd9fd899149cfd92bc72fb9d52e3cd410_small.jpeg "MENGRI")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[MENGRI](https://community.sap.com/t5/user/viewprofilepage/user-id/43195)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52661)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52661)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565042)

‎2022 Nov 30
7:43 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52661/tab/all-users "Click here to see who gave kudos to this post.")

3,130

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sales](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)
* [SD Sales](https://community.sap.com/t5/c-khhcw49343/SD%2520Sales/pd-p/167431589774684563301227734202839)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SD Sales

  Software Product Function](/t5/c-khhcw49343/SD%2BSales/pd-p/167431589774684563301227734202839)
* [SAP S/4HANA Cloud Public Edition Sales

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

View products (3)

As pricing specialist, you can maintain price by uploading spreadsheet. Price, as sensitive information, should follow Four Eyes Principal. Therefore, we can use Approval Process on the uploading function. In this blog, we focus on Approval Process. For uploading basic function, please refer to this [blog](https://blogs.sap.com/2020/11/02/upload-prices-in-sales-from-template-based-spreadsheet/).

## Background and Configuration

Please see [background blog](https://blogs.sap.com/2022/03/14/flexible-workflow-in-sap-s-4hana-sales-price/?source=email-global-notification-bp-new-in-tag-followed) and [configuration blog](https://blogs.sap.com/2022/11/10/workflow-configuration-for-sap-s-4hana-sales-price/).

## ​Main Process

You should know different Release Status before you move to this chapter.​

|
 Release Status |
 Description |

|
 (space) |
 Released |

|
 A |
 Blocked |

|
 D |
 In Review |

|
 E |
 Rejected |

|
 F |
 Request Deletion |

### Create Case

#### ![](/legacyfs/online/storage/blog_attachments/2022/11/Create-1.png)

### Update Case

#### ![](/legacyfs/online/storage/blog_attachments/2022/11/Update-2.png)

Note:

In Excel Upload case, we skip “Blocked” Release Status, and condition record will trigger workflow directly.

There is no deletion action, so “Request Deletion” is not used.

## Operation

Step1: Prepare Excel for create case and upload it.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step1.png)

Step2: Check condition record in Manage Prices - Sales app. User can see an "In Review" condition record.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step2-1.png)

Step3: Approver checks request in My Inbox app and click "Approve".

![](/legacyfs/online/storage/blog_attachments/2022/11/Step3.png)

Step4: Check condition record in Manage Prices - Sales app. User can see a "Released" condition record.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step4.png)

Step5: Download condition record and change condition amount, then upload it.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step5.png)

Step6: Check condition record in Manage Prices - Sales app. User can see a new "In Review" condition record and an original "Released" condition record.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step6.png)

Step7: Approver checks request in My Inbox app and click "Approve".

![](/legacyfs/online/storage/blog_attachments/2022/11/Step7.png)

Step8: Check condition record in Manage Prices - Sales app. User can see a "Released" condition record and find its amount changed.

![](/legacyfs/online/storage/blog_attachments/2022/11/Step8.png)

## Validation and Limitation​

### In create case

1. User don’t need to input Release Status, all condition records will be checked whether they are satisfied workflow.

### In update case

1. User is not allowed to change Release Status manually.​

2. Compared Excel data with DB data, unchanged condition record will not trigger workflow. If a “Released” condition record satisfies workflow, any change (include its supplement, scale, condition description and so on) will trigger workflow.

3. “In Review” / “Rejected” records are not allowed to change.

4. If a condition record has last change and is still in approval, it is not allowed to change again.

### In both case

1. When a condition record is overlapped with “In Review” record, the condition record cannot be saved.

## Conclusion

In this blog, we introduce the main process about Approval Process for Upload Prices in Sales. You can follow the Operation part step by step, then you will understand 2 cases clear.

Welcome to your questions and feedback to Comments.

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [sales price](/t5/tag/sales%20price/tg-p/board-id/erp-blog-sap)
* [sales price workflow](/t5/tag/sales%20price%20workflow/tg-p/board-id/erp-blog-sap)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fapproval-process-for-upload-prices-in-sales-from-template-based-spreadsheet%2Fba-p%2F13565042%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [How to withdraw the a...