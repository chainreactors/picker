---
title: SAP Fiori Collaboration With Finance Payment Proposal Workflow
url: https://blogs.sap.com/2022/12/08/sap-fiori-collaboration-with-finance-payment-proposal-workflow/
source: SAP Blogs
date: 2022-12-09
fetch_date: 2025-10-04T00:59:51.121074
---

# SAP Fiori Collaboration With Finance Payment Proposal Workflow

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Fiori Collaboration With Finance Payment Propo...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163502&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori Collaboration With Finance Payment Proposal Workflow](/t5/technology-blog-posts-by-members/sap-fiori-collaboration-with-finance-payment-proposal-workflow/ba-p/13570167)

![rajannyasarkar](https://avatars.profile.sap.com/e/d/ided78607f352d3ff268d26205806dccb547d018b28de90902e9a47500fe3863bb_small.jpeg "rajannyasarkar")

[rajannyasarkar](https://community.sap.com/t5/user/viewprofilepage/user-id/45711)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163502)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163502)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570167)

‎2022 Dec 08
8:35 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163502/tab/all-users "Click here to see who gave kudos to this post.")

11,349

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP Fiori for request approvals](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520request%2520approvals/pd-p/67838200100800006469)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP Business Workflow](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Workflow/pd-p/271076705480744283548543960420215)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for request approvals

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2Brequest%2Bapprovals/pd-p/67838200100800006469)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [SAP Business Workflow

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusiness%2BWorkflow/pd-p/271076705480744283548543960420215)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)

View products (6)

**Introduction :**

As you already aware regarding the Payment Proposal Workflow in SAP Finance, earlier it was triggered from SAP GUI and the decision whether it should be approved or rejected, this action was performed from SAP GUI itself. However, I came across this solution in S4 with Fiori integration with Payment Proposal Workflow.

In this solution, once the workflow is triggered from SAP GUI, it will be sent to Fiori inbox of the respective Approver. Now from Fiori inbox, approver can review the workflow and accordingly approve or reject the proposal from Fiori itself.

Hence I wanted to share my experience and concept on how this Fiori collaboration with business workflow can be implemented in S4. Hope this blog will be beneficial to everyone.

1. **Current Functionality (AS-IS):**

Standard workflow WS23200018 creates payment proposal workitem in My Inbox Fiori app with buttons like below. There is no explicit Approve and Reject button. Approvers needed to go to the ‘Open Task’ and approves from there or from SAP GUI. Till now Rejection was not possible from here.

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-1-Fiori_My_Inbox.png)

                                                             Fig 1: Fiori My Inbox

2. **Business Needs & Requirements (TO-BE)****:**

As per the business requirement, need to add ‘Approve’ and ‘Reject’ button explicitly in this workitem and Functionality needs to be implemented like below –

1. Once the Payment Proposal is created in SAP, a workitem is sent to My Inbox of Approver with Approve & Reject Button. Once this is sent, a notification mail needs to be triggered to Approver’s outlook mail that a workitem is ready for your approval.

2. Once he Approves, a mail needs to be triggered to initiator and a group mail id that this workitem is approved. For this approval, Payment run is processed in background. Once all process is done, a confirmation mail is sent to initiator that the whole process is completed.

3. Once he Rejects, a mail needs to be triggered to initiator and a group mail id that this workitem is rejected. Once this is rejected, no payment run will be triggered. Initiator can delete the proposal from F110 and recreate it and send for approval accordingly.

3. **Proposed Solution****:**

* Standard workflow and sub workflow needs to be copied to Custom workflow and sub workflow. Make required changes in custom ones.

* Approve and Reject custom buttons will be added for Fiori by setting configuration in SPRO.

* A Filter BADI needs to be implemented for these two buttons functionality.

4. **Implemented Solution Steps:**

          Flow Chart of Entire Process -

![](/legacyfs/online/storage/blog_attachments/2022/12/Flow-Chart-Workflow.png)

* **Solution Approach: Requirement** **1:**

**Once the Payment Proposal is created in SAP, a workitem is sent to My Inbox of Approver with Approve & Reject Button. Once this is sent, a notification mail needs to be triggered to Approver’s outlook mail that a workitem is ready for your approval.**

* Goto F110 Tcode – we create payment proposal

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-2-Proposal-Creation-F110-Tcode.png)

                                               Fig 2:  Proposal Creation - F110 Tcode

* For this development, we have created custom workflow WS90200005 and subworkflow WS90200006 by coping below standard workflow WS23200018 and subworkflow WS23200017.

* Once the proposal is created from F110, a workitem will be sent to My Inbox Fiori with **Approve** and **Reject**

To add this functionality, Approve and Reject button to a specific workitem ‘Payment Proposal Processing’ of the sub WF WS90200006, we need to do a settings in SPRO with the Corresponding Task No. and Step No.

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-3-Proposal-Processing-Task-Step.png)

                                            Fig 3: Proposal Processing Task & Step

Copy this Task no – TS23200014,

Step no – 000053,

Workflow no - WS90200006.

Go to **SPRO -> Maintain Task Names and Decision Options** -> Follow the below steps

**![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-4-Workflow-Task-Step-config-path-in-SPRO.png)**

                                     Fig 4: Workflow Task & Step config path in SPRO

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-5-Adding-Custom-Decision-Keys-in-SPRO.png)

                                       Fig 5: Adding Cus...