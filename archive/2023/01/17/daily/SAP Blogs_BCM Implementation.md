---
title: BCM Implementation
url: https://blogs.sap.com/2023/01/16/bcm-implementation/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:25.311440
---

# BCM Implementation

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* BCM Implementation

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68579&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [BCM Implementation](/t5/enterprise-resource-planning-blog-posts-by-members/bcm-implementation/ba-p/13571279)

![dgkrishnan](https://avatars.profile.sap.com/f/6/idf6fc836cc16962cf020a5056969e75714a666c5545e9cc066ee58bbdc767d47e_small.jpeg "dgkrishnan")

[dgkrishnan](https://community.sap.com/t5/user/viewprofilepage/user-id/723777)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68579)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68579)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571279)

‎2023 Jan 16
10:35 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68579/tab/all-users "Click here to see who gave kudos to this post.")

9,921

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [FIN Accounts Receivable and Payable](https://community.sap.com/t5/c-khhcw49343/FIN%2520Accounts%2520Receivable%2520and%2520Payable/pd-p/173284387196962001652277559265438)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [FIN Accounts Receivable and Payable

  Software Product Function](/t5/c-khhcw49343/FIN%2BAccounts%2BReceivable%2Band%2BPayable/pd-p/173284387196962001652277559265438)

View products (2)

**Vendor payment process through BCM**

Objective: This Article explains the processing of Vendor Payment using Bank Communication Management (BCM - End to End process from Vendor invoice to Vendor payment)

**The business need for implementing BCM for processing Vendor payments**

Automation of Vendor payments with less manual intervention

Approval of Vendor payments through the workflow for AP Manager

To Group the payments (multiple payment runs) for the workflow approval by AP Manager  followed by approval of payment batches by Treasury Manager

Approved payments/batches are transmitted to the bank for further processing

Need to avoid multiple bank interfaces

Challenges for the business

Limit access to payment files with efficient access control process

Lack of one place to manage payment approvals and interfaces

Managing approved signatories with high staff turn over

End-End Business Process steps:

1. Vendor Master– The payment method field is identified with Payment type T for wire payments using BCM. (Transaction code: XK03(ECC)/BP (S/4 HANA)

Vendor Master displayed using ECC Transaction-XK03

![](/legacyfs/online/storage/blog_attachments/2023/01/XK03Pic1.png)

Vendor Master displayed using Transaction-BP

![](/legacyfs/online/storage/blog_attachments/2023/01/BPPIc2.png)

2.  Reserve Identification for cross-payment run media. All payment runs identified with the prefix “:”       will be processed through BCM. (Transaction Code: OBPM5)

![](/legacyfs/online/storage/blog_attachments/2023/01/OBPM5Pic3.png)

3.     Vendor Invoice posted and payment run executed. Payment run identification starts with                    Identification: for cross-payment run media processing using BCM. (Transaction: F110)

Payment proposal for payment run created with the prefix: indicating that the payment run will be processed through BCM.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture31-1.png)

List of Vendor invoices in payment proposal

![](/legacyfs/online/storage/blog_attachments/2023/01/F110-Pic5.png)

Payment run processed and payments generated.

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic6.png)

4.      Batching Process: The batching process in BCM is used to group several payment runs into               one or more payment media.

Payment run IDs that are reserved for BCM are put together in a collector identified by Merge ID.

Creation of cross-payment run payment media- (Transaction FBPM1)

The payment runs are selected using the criteria and batches are generated using the batch rules defined in the customization.

In the below screen, we are selecting only the payment run we created above to be processed using the BCM.

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic7.png)

In the below screen, shows the status of payment for cross-payment run payment media. The status indicator is green with the payment ID created and populated in the ID payment field. If the status indicator of the payment run is red, it means that the payment run has been identified for the cross-payment run but not yet on the payment medium (Transaction FBPM2)

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic8.png)

5.      Transaction BNK\_MONIP gives an overview of all payments that are managed through BCM.             Payments can be restricted by the collector, the date, the payment run date, ID, file, batch, and           other criteria.

In the below screen, the green status shows that the payment is in the file along with the payment information.

Payment document number, payment run ID, Account ID, House Bank, Payment run date, etc.

![](/legacyfs/online/storage/blog_attachments/2023/01/F110PIc71.png)

6.      Batch approval in BCM -Multiple business resources are involved in the approval of batches               and generation of payment media. This depends on batch approval amounts, for example, If               the total batch amount is less than $25,000 it requires a single approval and if the amount is               greater than $25,000 it will require two approvals. The number of resources involved in                       approval depends on the organization’s needs.

BCM offers tools that allow users to approve the payments associated with the batches. Once the payments are batched it can be decided whether the batch must go through approval. The payment media is generated only after the batch has been approved by the final approver.

Payment batches are routed to approvers based on the approval matrix and the approvers can approve the batches by going to transaction BNK\_APP

The below screen shows the payment batch in BNK\_APP for approval.

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic9.png)

7.      Approval Reporting: report BNK\_MONIA gives a list of payment batches and the users that                 approved the batches with date and time information

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic11.png)

The screen shot below shows the batch created for our payment run has been approved by the user.

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic12.png)

8.      Status Tracking:

The batch and payment monitor provides an overview of batch life cycle-creation, approval, sending, and completion.  ( Transaction: BNK\_MONI)

![](/legacyfs/online/storage/blog_attachments/2023/01/F110Pic13.png)

Business Benefits:

Vendor open items due for payment on the day of the payment run are automatically picked up by the system.

Payment proposal appr...