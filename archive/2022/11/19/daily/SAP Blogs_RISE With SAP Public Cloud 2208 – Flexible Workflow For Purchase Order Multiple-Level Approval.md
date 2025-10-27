---
title: RISE With SAP Public Cloud 2208 – Flexible Workflow For Purchase Order Multiple-Level Approval
url: https://blogs.sap.com/2022/11/18/rise-with-sap-public-cloud-2208-flexible-workflow-for-purchase-order-multiple-level-approval/
source: SAP Blogs
date: 2022-11-19
fetch_date: 2025-10-03T23:13:00.063782
---

# RISE With SAP Public Cloud 2208 – Flexible Workflow For Purchase Order Multiple-Level Approval

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* RISE With SAP Public Cloud 2208 - Flexible Workflo...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68044&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [RISE With SAP Public Cloud 2208 - Flexible Workflow For Purchase Order Multiple-Level Approval](/t5/enterprise-resource-planning-blog-posts-by-members/rise-with-sap-public-cloud-2208-flexible-workflow-for-purchase-order/ba-p/13562807)

![vishweswaran_krishnan](https://avatars.profile.sap.com/5/9/id59578e01d4b1da1af5fd62dceba7c7a56c7eb4bbc5ea7e6e4547b371d62ac24d_small.jpeg "vishweswaran_krishnan")

[vishweswaran\_krishnan](https://community.sap.com/t5/user/viewprofilepage/user-id/826165)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68044)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68044)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562807)

‎2022 Nov 18
8:27 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68044/tab/all-users "Click here to see who gave kudos to this post.")

8,870

* SAP Managed Tags
* [RISE with SAP](https://community.sap.com/t5/c-khhcw49343/RISE%2520with%2520SAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)
* [MM (Materials Management)](https://community.sap.com/t5/c-khhcw49343/MM%2520%28Materials%2520Management%29/pd-p/477297786799213261950044802925335)

* [MM (Materials Management)

  Software Product Function](/t5/c-khhcw49343/MM%2B%252528Materials%2BManagement%252529/pd-p/477297786799213261950044802925335)
* [RISE with SAP

  Topic](/t5/c-khhcw49343/RISE%2Bwith%2BSAP/pd-p/1e76886f-86ac-4839-9833-8bf95f5eb775)

View products (2)

#### **Hello All**,

In This Blog, we will see how to Assign Flexible Workflow For Purchase Order Approval Process Multiple- Level in RISE with SAP Public Cloud system. Basically, the Purchase Order Process Workflow feature is used to Trigger purchase orders that meet pre-defined conditions to follow a specific approval/review process.

\*For example: if all Purchase Order is Created Using Company Code (example – 9260) it needs to be reviewed before release, you can set up the application to enforce that workflow/approval process.

#### **Introduction:**

Flexible workflow **supports the development of one-step or multi-step approval processes** and depending on the requirements in each step one or more approvers can be assigned to the processes for purchase Orders.

This blog will explain how to use Purchase Order Process Workflow feature in RISE with SAP Public Cloud System for Multi-level Approval.

#### **CONTENTS DISCUSSED IN THIS BLOG:**

\* Manage Workflow For Purchase Order

- Through Fiori app - Define condition , Assign User and activate the workflow

\* Manage Purchase Orders

- Through Fiori app - Create Purchase Order

\* My Inbox - Purchase Order Approval

- Through Fiori App - Approve Purchase Order

**1: MANAGE WORKFLOWS FOR PURCHASE ORDERS:**

* To define Release condition, Run Fiori App (APP ID- F2872) – ‘**MANAGE WORKFLOWS FOR PURCHASE ORDERS’**

![](/legacyfs/online/storage/blog_attachments/2022/11/1-20.png)

* Below screen will appear, select ‘**CREATE**’ to define workflow for purchase order.

![](/legacyfs/online/storage/blog_attachments/2022/11/2-23.png)

* Enter the ‘**WORKFLOW NAME**’ and select the Validity Period for the workflow as shown below – ‘**Valid From**’ and ‘**To Date**’.

![](/legacyfs/online/storage/blog_attachments/2022/11/3-15.png)

* Select the Conditions For which the Purchase Order is to be sent for the approval.

* Here I have selected the condition ‘**COMPANY CODE OF PURCHASE ORDER**’

* Next In the Workflow Steps, To create the Approval Level Based on Role Or User.

* Select ‘**CREATE**’

![](/legacyfs/online/storage/blog_attachments/2022/11/4-15.png)

* For Maintaining 1st Level Approver, In the Header Tab

* Enter the ‘**STEP NAME**’ (example – Level 1) and

* Enter the ‘**STEP TYPE**’ (example – Release of purchase order)

![](/legacyfs/online/storage/blog_attachments/2022/11/5-11.png)

* In the Recipients Tab,

* Select ‘**ASSIGNMENT BY**’ -whether the approval is Based on User or Role

* Enter the ‘**USER ID**’ as shown below:

* Select the conditions and click ‘**CREATE**’.

![](/legacyfs/online/storage/blog_attachments/2022/11/6-9.png)

* For Maintaining 2nd Level Approval,

* Select ‘**CREATE**’

![](/legacyfs/online/storage/blog_attachments/2022/11/7-13.png)

* In the Header Tab

* Enter the ‘**STEP NAME**’ (example – Level 2) and

* Enter the ‘**STEP TYPE**’ (example – Release of purchase order)

![](/legacyfs/online/storage/blog_attachments/2022/11/8-14.png)

* In the Recipients Tab,

* Select ‘**ASSIGNMENT BY**’ -whether the approval is Based on User or Role

* Enter the ‘**USER ID**’ as shown below:

* Select the conditions and click ‘**CREATE**’.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-28.png)

* You can view the created workflow steps in the main page.

* Click ‘**SAVE**’.

![](/legacyfs/online/storage/blog_attachments/2022/11/10-5.png)

* Select ‘**ACTIVATE**’ in the main screen for the created workflow to function.

![](/legacyfs/online/storage/blog_attachments/2022/11/11-7.png)

* You can view the status ‘**ACTIVE**’ of the created workflow as shown below:

![](/legacyfs/online/storage/blog_attachments/2022/11/12-7.png)

* Finally conditions has been defined successfully and workflow should trigger (based on conditions defined).

**2. TEST CASE:**

\* Create Purchase order using standard App (APP ID -F0842A) ‘**Manage Purchase Order**’ and           make sure defined conditions has been taken care (Company code of Purchase Order is                   ‘9260’). After saving the Purchase Order, Status at header level of Created Purchase order will           be “In Approval” as shown below:

![](/legacyfs/online/storage/blog_attachments/2022/11/13-7.png)

* To view approver details and workflow Step, go to Tab ‘**Approval Details**’ and you can see which step is triggered and Recipient name also.

![](/legacyfs/online/storage/blog_attachments/2022/11/14-6.png)

* 1st Level Approver will get the notification at the home screen as shown below:

![](/legacyfs/online/storage/blog_attachments/2022/11/15-5.png)

* By clicking on Notification, approver will be taken to Fiori App (APP ID -F0402A) “**My Inbox - Approve Purchase Order**”.

![](/legacyfs/online/storage/blog_attachments/2022/11/16-5.png)

* Approve the Purchase order by selecting ‘**Approve**’ Button on Bottom right.

* A pop-up will appear in the screen and we can add any note in the window and submit.

![](/legacyfs/online/storage/blog_attachments/2022/11/17-5.png)

* Check Purchase Order and Status will be changed to Purchase Order Released for **Level 1**.

![](/legacyfs/online/storage/blog_attachments/2022/11/18-2.png)

* For the **Second Level Approval**, Same process needs to be done once the user gets the notification in his respective ID or In ‘**MY INBOX**’ for the approval of Purchase order.

* You can view the Status ...