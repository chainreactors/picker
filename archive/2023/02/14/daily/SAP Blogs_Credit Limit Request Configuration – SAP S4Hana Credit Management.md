---
title: Credit Limit Request Configuration – SAP S4Hana Credit Management
url: https://blogs.sap.com/2023/02/13/credit-limit-request-configuration-sap-s4hana-credit-management/
source: SAP Blogs
date: 2023-02-14
fetch_date: 2025-10-04T06:31:38.131580
---

# Credit Limit Request Configuration – SAP S4Hana Credit Management

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Credit Limit Request Configuration - SAP S4Hana Cr...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68415&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Credit Limit Request Configuration - SAP S4Hana Credit Management](/t5/enterprise-resource-planning-blog-posts-by-members/credit-limit-request-configuration-sap-s4hana-credit-management/ba-p/13568301)

![GOWRESHANHARAN83](https://avatars.profile.sap.com/9/7/id9792c41a6546d16e6731f7d07b4146b520d4498994c522896ad0176fa8429ade_small.jpeg "GOWRESHANHARAN83")

[GOWRESHANHARAN83](https://community.sap.com/t5/user/viewprofilepage/user-id/5537)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68415)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68415)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568301)

‎2023 Feb 13
9:35 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68415/tab/all-users "Click here to see who gave kudos to this post.")

27,462

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)

View products (3)

## **Introduction:**

Credit Management is a process in which Company sells a product/service to customers on a credit basis. The company collects payments from customers at a later time, after the sale of the product. The amount of credit fixed by a company for a customer is called a credit limit. The customer can purchase the product from a company within the credit limit, and when the credit limit is crossed, the order is blocked by the system.

The creditworthiness and payment behavior of your business partners have an immediate effect on the business results of your company. Efficient receivables and credit management reduce the risk of financial losses and help you to optimize business relationships with your business partners. SAP Credit Management (FIN-FSCM-CR) supports your company in determining the risk of losses on receivables from your business partners early and in making credit decisions efficiently and in some cases automated. With SAP Credit Management (FIN-FSCM-CR) you can operate centralized credit management. The business systems connected (for example Sales and Distribution, Logistics Execution, and Financial Accounting) report the commitment of a business partner to SAP Credit Management.

## **Credit Limit Request:**

Request for a change to the credit limit of a business partner in a credit segment.

                        You use the credit limit request if the credit limit is not to be changed immediately in the master data and requires a decision or approval process first. In most business cases customers need to apply for approval if any user increased the credit limit, this function will allow the financial manager to check and review the credit limit before it effects in the BP and will enable him to approve or reject the limit requested

## **Process Flow:**

When you create a credit limit request, the system transfers some master data that exists for the business partner in SAP Credit Management to the credit limit request. This includes the score, risk class, and credit limit.

When you create or change a credit limit request, you can carry out the following actions:

+ Enter the credit limit requested.

+ Enter notes

+ Link documents

Forward credit limit requests to another processor for approval, whereby this processor can enter an approved credit limit that is different from the limit requested.

If a processor closes the credit limit request, this corresponds to a refusal. If he confirms the credit limit request, this is approval and triggers the update of the approved credit limit in the master data of the business partner.

## **Prerequisite:**

|  |
| --- |
| Transaction Code: SU01 |

Before activating this function, you should first make sure that the Workflow user: SAP\_WFRT is active and have the required standard authorizations

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture-1-1.png)Click on Display. There You can find the user which was active.

### ![](/legacyfs/online/storage/blog_attachments/2023/02/Picture2-28.png)**Configuration Steps for Case Management Component:**

SAP Credit Management uses the component Case Management as a technical basis for the processing of the following objects:

+ Documented Credit Decision

+ **Credit Limit Request**

In this Customizing activity, you can find a summary of the activities that you have to execute for this in the Case Management component.

|  |
| --- |
| **Path => SAP NetWeaver under Application Server -> Basis Services -> Case Management.** |

## **Step 1: Attribute profile**

In this activity, you define which attributes you want to use for the credit limit request. You also define the display and maintenance properties of the individual attributes. If you also want to use customer-specific attributes for the documented credit decision in addition to the standard attributes.

### **Create Attribute Profile:**

|  |
| --- |
| **Path =>** SAP NetWeaver under Application Server -> Basis Services -> Case Management ->Create Attribute Profile. |

Execute Create attribute profile.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture3-21.png)

Click on New Entries to create a new attribute profile for the Credit Limit request.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture4-21.png)

Fill in the following data shown in the below image. And click on save.

|  |  |
| --- | --- |
| Attribute Profile | FIN\_CRED |
| Description | SAP Credit Management |
| Table Name | UKMCASEATTR00 |

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture5-10.png)

Click on Attribute Group and fill in the following data shown in the below image and click on save.

![](/legacyfs/online/storage/blog_attachments/2023/02/Picture6-12.png)

Click on Assign Attribute and fill in the following data shown below table and click on save.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Attribute Profile** | **Case Attribute** | **Group** | **Row** | **Column** | **required** | **Invisible** | **Drop** | **Check Box** | **Not Modifiable** | **Modifiable only on new** | **log** |
| FIN\_CRED | CASE\_TITLE | 1 | 1 | 1 |  |  |  |  |  |  |  |
| FIN\_CRED | CASE\_TYPE | 1 | 2 | 1 |  |  | X ...