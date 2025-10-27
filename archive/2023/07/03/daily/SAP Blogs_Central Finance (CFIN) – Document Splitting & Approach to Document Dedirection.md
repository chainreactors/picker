---
title: Central Finance (CFIN) – Document Splitting & Approach to Document Dedirection
url: https://blogs.sap.com/2023/07/02/central-finance-cfin-document-splitting-approach-to-document-dedirection/
source: SAP Blogs
date: 2023-07-03
fetch_date: 2025-10-04T11:52:47.720772
---

# Central Finance (CFIN) – Document Splitting & Approach to Document Dedirection

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Central Finance (CFIN) - Document Splitting & Appr...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66925&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Central Finance (CFIN) - Document Splitting & Approach to Document Dedirection](/t5/enterprise-resource-planning-blog-posts-by-members/central-finance-cfin-document-splitting-approach-to-document-dedirection/ba-p/13548778)

![mayankjaiswal](https://avatars.profile.sap.com/2/c/id2c22a089d8baf9c51c0d8840ae907cd87cc8dca6545cff7a9b95d236d0e92e97_small.jpeg "mayankjaiswal")

[mayankjaiswal](https://community.sap.com/t5/user/viewprofilepage/user-id/803996)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66925)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66925)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548778)

‎2023 Jul 02
1:22 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66925/tab/all-users "Click here to see who gave kudos to this post.")

3,760

* SAP Managed Tags
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)

View products (1)

In this blog I’ll talk about one of the important sought out topic during finance transformation journey – Document Splitting function in Central finance.  The scope is limited to ‘Document split active in target system but not in source system’.

**Background**

In general SAP recommends to  work with a scenario in which document splitting is configured the same way in both source and target system, somehow this is not always possible. From S/4HANA 1909, because of different reasons or use cases, SAP has started supporting the scenario of document splitting as inactive in the source system and active in the Central Finance system.

The bigger question is what SAP has actually started supporting that were not there until 1809 and if  these are sufficient for a CFIN consultant to build the solution without getting into custom development. Let’s check out the challenges or reasons that trigger the flurry of replication errors, recent progress in this area and then talk about approach to custom solution.

**Challenges/ Reasons for Document split replication errors**

Splitting logic & configured rules are processed when documents are reposted in target from source. This leads to inbuilt validation check and subsequent error in case of non-fulfillment, few of the major reasons are:

1. When Central Finance transfers the initial balances and open items, the document splitting characteristics are not included

2. If user posts document in the source system that mixes several business transactions in one single posting, the splitter will not find an appropriate rule to apply. Although the posting was successful in the source system, it will not be posted successfully in the Central Finance system

3. If a splitting characteristic (e.g. profit center) is configured as mandatory (and balancing to zero), it needs to be supplied in the posting. However, if this characteristic is not used in the source system, the posting will not be successful.

4. Cross-company transactions between company codes with document splitting activated and company codes with document splitting not activated will lead to an error in Central Finance

**SAP Enhanced Validation**

1. Consistency check

From 1909, SAP has provided in its configuration consistency checks to verify the consistency of document splitting activation between the source system and Central Finance system. The following checks in the consistency check report for document splitting settings have been extended:

* Classification of G/L Accounts for Document Splitting - The item category is determined by the account number.

* Classification for Document Types for Document Splitting - Assigning business transaction variant to document types

* Document Splitting Characteristics for General Ledger Accounting - Assign account objects for splitting (e.g. profit center, segment)

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1.png)

2. Doc split check in Source System

In order to avoid documents being posted in the source system which would lead to potential document splitting errors in the target system, Central Finance from 2020 supports the same pre-checks in the source system as in the target system. These are processed directly during the posting of FI documents in the source system, when the split process check is activated for company code.

These are run time checks during the posting of FI documents in the source system and Consultant has an option either to define Warning or Error against those document which breach the split rule in source system. However, activating this check does not change postings on the source side.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2.png)

3. Simulation of Doc split

When posting fails due to an error in the document split, you can trigger a simulation of document splitting for the document in question, by choosing Simulate Document Splitting in the error message. The fields in the Simulate Document Splitting function are then automatically filled with the values from the error message, allowing you to trigger the simulation for the document in question, without having to enter any additional information. You can access the simulation from error message either at SAP AIF or from the monitor Initial Load Data.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3.png)

### **Custom Solution**

While the above enhancements facilitate the Document split validation of records or simulation, it does not provide any standard solution to overcome split errors and ensure seamless replication in target. This leave behind the necessity for essential Custom alignment between source & target for document split augmentation.

Broadly the Custom approach can be classified into:

A. Document Redirection to deal with Document types rebelling Split rules

B. Enrichment of missing Characteristics through Badi or standard default

***A. Document Redirection*** - Document splitting works with configured rules. These configured rules are based on the document type used for a business transaction, which requires certain level of posting discipline. Source systems that do not have document splitting active or does not have the characteristics mandatory, business users / interfaces have full freedom on how to create postings. However, the source freedom are not applicable anymore in the central system. Therefore, there are two options theoretically:

* Either introduce more discipline in the source systems which may not be possible at short span and required progressive adoption

* Based on the typology, **redirect** the original document type to another one in target that fits better to the postin...