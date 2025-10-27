---
title: SAP CAR – Transaction data change – Task status
url: https://blogs.sap.com/2023/04/08/sap-car-transaction-data-change-task-status/
source: SAP Blogs
date: 2023-04-09
fetch_date: 2025-10-04T11:29:52.625205
---

# SAP CAR – Transaction data change – Task status

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* SAP CAR - Transaction data change - Task status

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6376&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP CAR - Transaction data change - Task status](/t5/crm-and-cx-blog-posts-by-members/sap-car-transaction-data-change-task-status/ba-p/13571381)

![maciej_jarecki](https://avatars.profile.sap.com/b/9/idb9d48d678d4062ad20b51a9cd47d424243ae21e0960c6327c578ca0b0a11c141_small.jpeg "maciej_jarecki")

[maciej\_jarecki](https://community.sap.com/t5/user/viewprofilepage/user-id/206461)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6376)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6376)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571381)

‎2023 Apr 08
7:01 AM

[1
Kudo](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6376/tab/all-users "Click here to see who gave kudos to this post.")

3,870

* SAP Managed Tags
* [SAP Customer Activity Repository](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Activity%2520Repository/pd-p/67837800100800005767)
* [SAP Point-of-Sale](https://community.sap.com/t5/c-khhcw49343/SAP%2520Point-of-Sale/pd-p/01200615320800000725)

* [SAP Customer Activity Repository

  SAP Customer Activity Repository](/t5/c-khhcw49343/SAP%2BCustomer%2BActivity%2BRepository/pd-p/67837800100800005767)
* [SAP Point-of-Sale

  SAP Point-of-Sale](/t5/c-khhcw49343/SAP%2BPoint-of-Sale/pd-p/01200615320800000725)

View products (2)

**Introduction:**

Most of companies are exchanging huge amount of data between systems as data is an information and to execute any business process is more then mandatory. Connecting systems in SAP world is usually executed via SAP middleware like SAP PI/PO or any newer and renamed version of it like CPI. These systems are very powerful and sophisticated but not each industry needs it. Example of such an industry is Retail business that received number of data mainly from single source which is POS system. Increasing usability of SAP CAR system across companies and business processes that SAP CAR is involved in caused more effort spent on the maintenance and support.

**Objective:**

SAP CAR receives POS transactions related to number of processes mainly sales but as well good movements operations or finance transactions. Each POS transaction is a set of data that is processed by tasks. Tasks are processed independently but sometimes during the execution of any task error can occur due to the wrong data which needs to be changes and because the task dependency some of them need to be reversed first.

Selection of the task depends on the Customization of POS transactions and for here we use following assignment.

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-1.png)

The focus of this article is to describe when you can do a change of POS transaction data based on task status and what is the procedure of reversing/ canceling the task.

Both configuration parameters are set on task definition level.

Cancelation procedure:

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-2.png)

When checkbox is selected then reversal/cancelation means the task needs to get status ready to be cancelled first. Task is executed and same code of task is executed with information it’s reversed execution and as well system process values with opposite sign.

Changeability of data for task:

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-3.png)

Describes when data can be changed.

* Always changeable – No restriction to change a data

* Only changeable if task has status ready – in this case we can change data only if task is in status ready neither rejected nor cancelled nor processed etc.

* Changeable if Task Not Processed or Canceled – data of POS transaction can be changed when task status is ready or rejected.

**Example:**

For the purpose of this article I created four dummy tasks. Each of them has a different value in regards to mentioned before parameters and on top of it one is with “type of task” is set to manual trigger as it has special way of processing the cancelation.

Task 1 – No reverse required, and data is always changeable

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-4.png)

Task 2 – No reverse required but data can only be changed if task status is ready

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-5.png)

Task 3 – To cancel the task reversal process is required and changeability is the less restricted to status of ready or rejected.

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-7.png)

Task 4 – it’s like Task 3 with the single difference of Type of task processing set to Manual Processing

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-8.png)

Cancelation:

If reversal is required for a task as wrote before task needs to get first canceled. With cancelation system executes same piece of code as for regular task but with information it’s reversal and with values multiple by -1 to get opposite sign. Special feature is manual task that can be changed to canceled without request of cancelation.

![](/legacyfs/online/storage/blog_attachments/2023/04/f1-9.png)

* [CAR](/t5/tag/CAR/tg-p/board-id/crm-blog-members)
* [POSLOG](/t5/tag/POSLOG/tg-p/board-id/crm-blog-members)
* [sap car](/t5/tag/sap%20car/tg-p/board-id/crm-blog-members)
* [Task](/t5/tag/Task/tg-p/board-id/crm-blog-members)
* [Task data](/t5/tag/Task%20data/tg-p/board-id/crm-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fcrm-and-cx-blog-posts-by-members%2Fsap-car-transaction-data-change-task-status%2Fba-p%2F13571381%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP ABAP Developer for Custom Module Development](/t5/crm-and-cx-q-a/sap-abap-developer-for-custom-module-development/qaq-p/14226707)
  in [CRM and CX Q&A](/t5/crm-and-cx-q-a/qa-p/crm-questions)  a week ago
* [Implementing SAP Emarsys Loyalty Management - Part 1](/t5/crm-and-cx-blog-posts-by-sap/implementing-sap-emarsys-loyalty-management-part-1/ba-p/14216345)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)  3 weeks ago
* [Notifications are not being sent on status changes triggered by the script.](/t5/crm-and-cx-q-a/notifications-are-not-being-sent-on-status-changes-triggered-by-the-script/qaq-p/14215280)
  in [CRM and CX Q&A](/t5/crm-and-cx-q-a/qa-p/crm-questions)  3 weeks ago
* [Leveraging Asynchronous Request-Reply Pattern for Order Management Foundation (OMF)](/t5/crm-and-cx-blog-posts-by-sap/leveraging-asynchronous-request-reply-pattern-for-order-management/ba-p/14207673)
  in [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-...