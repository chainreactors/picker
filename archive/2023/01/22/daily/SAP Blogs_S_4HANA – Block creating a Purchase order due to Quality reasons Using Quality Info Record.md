---
title: S/4HANA – Block creating a Purchase order due to Quality reasons Using Quality Info Record
url: https://blogs.sap.com/2023/01/21/s-4hana-block-creating-a-purchase-order-due-to-quality-reasons-using-quality-info-record/
source: SAP Blogs
date: 2023-01-22
fetch_date: 2025-10-04T04:33:22.807545
---

# S/4HANA – Block creating a Purchase order due to Quality reasons Using Quality Info Record

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* S/4HANA – Block creating a Purchase order due to Q...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67021&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4HANA – Block creating a Purchase order due to Quality reasons Using Quality Info Record](/t5/enterprise-resource-planning-blog-posts-by-members/s-4hana-block-creating-a-purchase-order-due-to-quality-reasons-using/ba-p/13549806)

![mohan_kaliyamoorthy](https://avatars.profile.sap.com/f/9/idf9e04649bbeb4d847e047eb1fb7cd0a3358f460201bd9eab3a754ebe61b1feb7_small.jpeg "mohan_kaliyamoorthy")

[mohan\_kaliyamoorthy](https://community.sap.com/t5/user/viewprofilepage/user-id/729135)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67021)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67021)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549806)

‎2023 Jan 21
9:57 PM

0
Kudos

3,359

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Ariba Central Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Central%2520Procurement/pd-p/73555000100800001106)
* [Sourcing and Procurement - Purchase Contract Management](https://community.sap.com/t5/c-khhcw49343/Sourcing%2520and%2520Procurement%2520-%2520Purchase%2520Contract%2520Management/pd-p/f8d69eb6-6a87-4680-9d09-644b277489a5)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Ariba Central Procurement

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BCentral%2BProcurement/pd-p/73555000100800001106)
* [Sourcing and Procurement - Purchase Contract Management

  Software Product Function](/t5/c-khhcw49343/Sourcing%2Band%2BProcurement%2B-%2BPurchase%2BContract%2BManagement/pd-p/f8d69eb6-6a87-4680-9d09-644b277489a5)

View products (3)

**Introduction:**

In this blog, the steps outlined how to ‘Block creating a Purchase order for a specific Material and Supplier combination’ due to quality reasons in S/4HANA

When the Purchase order is created, the system checks whether a quality info record is required for the combination of material and supplier, and also checks whether the supplier and material combination is blocked or released for the procurement process.

**Pre-requisite:**

* Setup Supplier Master

* Setup Material Master

* Setup Quality Info record

**Process Steps:**

1. Configure Control keys in S/4 HANA

2. Set up the Procurement data in the material master QM View

3. Change Quality Info records for the combination of Material and Supplier

4. Create a Purchase and check the error message

**Step-1-Configure Control Keys**

SPRO >Quality Management > QM in Logistics > QM in Procurement > Define Control Keys**![](/legacyfs/online/storage/blog_attachments/2023/01/Picture_001A.jpg)**

**2.** **Set up the Procurement data in the material master QM View**

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture_001B.jpg)

**3. Change Quality Info record for the combination of Material and Supplier**    ![](/legacyfs/online/storage/blog_attachments/2023/01/Pic_002.jpg)

**4. Create a Purchase and check the error message**

![](/legacyfs/online/storage/blog_attachments/2023/01/Pict_003-1.jpg)

You can see the error message while trying to create a  Purchase order. The system prevents the creation for Purchase order

**Conclusion:**

* After going through the above blog, the user should have learned key concepts and setup in how to prevent creating a Purchase order for a material and supplier combination in the S/4HANA due to quality reasons

* Please provide your feedback/comments. You can ask Questions / Answers for the open Questions in the [SAP Community here](https://answers.sap.com/questions/ask.html)

**Reference:**

QM in Procurement - S/4HANA:

[https://help.sap.com/docs/SAP\_S4HANA\_ON-PREMISE/2bc3ee8d1c83404e8cf62418640004f2/9cb5bd53e3acb64ce10...](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/2bc3ee8d1c83404e8cf62418640004f2/9cb5bd53e3acb64ce10000000a174cb4.html)

* [quality info record](/t5/tag/quality%20info%20record/tg-p/board-id/erp-blog-members)
* [S4HANA Sourcing and Procurement](/t5/tag/S4HANA%20Sourcing%20and%20Procurement/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fs-4hana-block-creating-a-purchase-order-due-to-quality-reasons-using%2Fba-p%2F13549806%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2 hours ago
* [Int4 Suite Agents Empowers Functional Consultants To Test Integrated SAP S/4HANA Business Processes](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-agents-empowers-functional-consultants-to-test-integrated-sap-s/ba-p/14234100)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  11 hours ago
* [Agentic AI Testing for Greenfield S/4HANA Outbound Interfaces - Part 1](/t5/enterprise-resource-planning-blog-posts-by-members/agentic-ai-testing-for-greenfield-s-4hana-outbound-interfaces-part-1/ba-p/14232427)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Wednesday
* [From Insight to Impact: Measuring Business Outcomes with Data Driven Value Management](/t5/enterprise-resource-planning-blog-posts-by-sap/from-insight-to-impact-measuring-business-outcomes-with-data-driven-value/ba-p/14229044)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  a week ago
* [How to Create and Manage Blanket or Framework Purchase Orders in SAP S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-create-and-manage-blanket-or-framework-purchase-orders-in-sap-s/ba-p/14226571)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id...