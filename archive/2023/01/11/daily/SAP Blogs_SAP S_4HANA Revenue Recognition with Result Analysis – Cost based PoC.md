---
title: SAP S/4HANA Revenue Recognition with Result Analysis – Cost based PoC
url: https://blogs.sap.com/2023/01/10/sap-s-4hana-revenue-recognition-with-result-analysis-cost-based-poc/
source: SAP Blogs
date: 2023-01-11
fetch_date: 2025-10-04T03:31:49.902310
---

# SAP S/4HANA Revenue Recognition with Result Analysis – Cost based PoC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Revenue Recognition with Result Analys...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52412&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Revenue Recognition with Result Analysis – Cost based PoC](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-revenue-recognition-with-result-analysis-cost-based-poc/ba-p/13563720)

![manoharmvrk59](https://avatars.profile.sap.com/0/d/id0d8e4410bf159ebefb8a22c11a2ce1619916bfd5b130a18d7ba23112266e5085_small.jpeg "manoharmvrk59")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[manoharmvrk59](https://community.sap.com/t5/user/viewprofilepage/user-id/47145)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52412)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52412)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563720)

‎2023 Jan 10
9:09 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52412/tab/all-users "Click here to see who gave kudos to this post.")

13,793

* SAP Managed Tags
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)

* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)

View products (1)

**I****ntroduction**:

In this blog you will see how SAP calculates the Project WBS Result Analysis and settlement postings as per the Multiple valuations like Legal Valuation, Group valuation and Profit center valuation and it also provides required configuration details relating to Result Analysis.

**What you will learn from this Blog?**

You will learn following key concept by going through this Blog.

1. Business requirement

2. Business Process flow

3. Result Analysis calculation example

4. Result analysis calculation process steps & financial impact.

5. Key Configuration Consideration & steps.

6. Conclusion.

1. **Business requirement**:

As per the Accounting standard the Revenue should be recognized based on different methods and in this blog we are focusing on Cost based POC. We can understand better with the following example.

Let’s assume ABC ltd company manufacture heavy Equipment’s which may take longer periods to manufacture and assemble the equipment. Here the business requirement is to Calculate and recognize the Revenue as per Incurred Actual Cost with multiple valuations like Legal, Group and Profit center.

2. **Business process flow**:

In the Engineering to manufacture scenario the component production process are assigned to a specific Project which will be the WBS element in SAP. Hence the Component manufacturing cost and relevant stock movements and inventory will always be assigned to Project (WBS).

Hence at each phase of the project you will incur various cost which may differ per valuation (Legal, Group and PCA) that will determine the Percentage of actual completion along with ‘***Calculated Revenue’*** for each valuation.

3. **Result Analysis Calculation:**

As per the Valuations based on the Cost based POC, the below is the example with calculation.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture1-1.png)

Here in the above mentioned excel you can see the material consumptions got booked against the P&L GL account 5430000 in plant: 1210 for material FG1 and FG2 having different amounts in legal, Group and PC valuation (as you have Transfer pricing mark-up scenario).

**Note:**

**Planned cost and revenue** of the project are maintained in CJ40 and CJ42 transaction with the WBS and GL account combination. The raw material component plan cost can also directly fetch from the Network orders depending on the Business requirement. Similarly the plan revenues can also fetch from the Sales order depending on the customization setup.

**Actual cost and revenue** The Actual expenses relating to the project are booked to WBS and Revenue relating to the project is also posted to WBS from SD billing.

**RA Calculation Formula’s as per Cost based Percentage of completion:**

**Cost based POC%** = (Actual Cost/Plan cost) \*100

**Revenue recognization as per Percentage of completion** = Plan Revenue\*POC%

***Revenue in excess of billing or Revenue surplus scenario***:

**Case i**: If Calculated Revenue < Actual Revenue (This is Revenue surplus scenario. Hence you need to reduce/debit revenue from P&L).

Accounting entry:

Dr. Sales Revenue        (P&L)

Cr. Deferred Revenue  (B/S)

**Case II**: If Calculated Revenue > Actual Revenue ( This is Revenue in Excess of Billing scenario. Hence you need to increase/Credit the Revenue from P&L).

Accounting entry:

Dr. Accured Revenue (B/S)

Cr. Sales Revenue       (P&L)

**4. Result analysis calculation process steps & financial impact:** Result Analysis Calculation as per Valuation: Transaction KKA2 – Period end closing activity

In this example Result Analysis is performed on the higher level WBS element. Here in this system technically will roll up the cost and revenues from lower level WBS to the next higher WBS.

System will consider the planned cost, planned revenue, actual cost, actual revenue and will calculate the POC%, Revenue Affecting Net incomes, Cost Affecting Net income and Calculated Profit/loss. This transaction just save the results and won’t generate accounting settlement entries.

**Result analysis calculation as per Legal Valuation:**

![](/legacyfs/online/storage/blog_attachments/2023/01/Legal-val.png)

**Result Analysis Calculation as per Group Valuation:**

![](/legacyfs/online/storage/blog_attachments/2023/01/Group-Val.png)

**Result Analysis Calculation as per Profit center valuation:**

![](/legacyfs/online/storage/blog_attachments/2023/01/PCA-val.png)

**Project Settlement - CJ88:** Here system will flow the Actual Cost and Calculated Revenue to COPA.

![](/legacyfs/online/storage/blog_attachments/2023/01/CJ88.png)

**FI Adjustment entry**: Only Financial posting – No COPA posting

![](/legacyfs/online/storage/blog_attachments/2023/01/FI-Entry.png)

**COPA posting**: When you do the Settlement system will post the COPA document with Revenue and Cost as per Cost based POC method as per valuations. You can see below amounts as per company code currency (legal); Group currency group valuation (currency type: 31)and Group currency, profit center valuation( currency type: 32).

![](/legacyfs/online/storage/blog_attachments/2023/01/COPA-Posting.png)

**5. Key Configuration Consideration & steps**:

**Multiple Valuation Approaches/Transfer prices**:

In this configuration step you need to define the ‘Currency and Valuation Profile’ and to assign to the controlling Area.

**Define Ledger to CO Version**:

Here in the below you can see the Leading ledger 0L got assigned to the multiple versions and Valuations like Legal, Group and PC Valuation.

![](/legacyfs/online/storage/blog_attachments/2023/01/Version.png)

1. **Material Ledger type**:
...