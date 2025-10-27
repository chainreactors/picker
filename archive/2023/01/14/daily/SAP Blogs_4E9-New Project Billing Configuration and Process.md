---
title: 4E9-New Project Billing Configuration and Process
url: https://blogs.sap.com/2023/01/13/4e9-new-project-billing-configuration-and-process/
source: SAP Blogs
date: 2023-01-14
fetch_date: 2025-10-04T03:52:43.193478
---

# 4E9-New Project Billing Configuration and Process

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* 4E9-New Project Billing Configuration and Process

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/65017&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [4E9-New Project Billing Configuration and Process](/t5/enterprise-resource-planning-blog-posts-by-members/4e9-new-project-billing-configuration-and-process/ba-p/13524605)

![IMSunilY](https://avatars.profile.sap.com/a/a/idaa583541827f1c6dde0b946e84d1fc6048c38a7ad366d8d471abb1b2a993d08a_small.jpeg "IMSunilY")

[IMSunilY](https://community.sap.com/t5/user/viewprofilepage/user-id/150887)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=65017)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/65017)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13524605)

‎2023 Jan 13
9:29 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/65017/tab/all-users "Click here to see who gave kudos to this post.")

4,896

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Professional Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Professional%2520Services/pd-p/a421aaac-1912-4fca-b725-00056d7dadc3)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition Professional Services

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BProfessional%2BServices/pd-p/a421aaac-1912-4fca-b725-00056d7dadc3)

View products (3)

## Introduction:

This blog is specifically focused on new solution by SAP which was released as Scope item 4E9, called New Project Billing. This new App Manage Project Billing has many features. for details you may refer Blog Post by Mr. Andreas Hammerschmidt  “[Project Billing for Customer Projects in SAP S/4HANA Cloud](https://blogs.sap.com/2020/08/11/project-billing-for-customer-projects-in-sap-s-4hana-cloud/)”.

We are here to get deep understanding of Creating Billing Profile, which is similar to Dynamic Item Processor Profile in onPrem Solution. After Settings required for this process, we will be going through Process Run.

NOTE: Process included is for Time and Expense Project, but We can also refer the same for Fixed Price and Payment on Account or Billing for Down payment also.

## Create Billing Profile:

Open Manage your Solution -> Configure your Solution

Select Application Area = Enterprise Portfolio & Project Management

Now you will able to see "Billing" as Sub Application Area

![](/legacyfs/online/storage/blog_attachments/2022/09/Screenshot-2022-09-23-182954.png)

Click Configure

Create Project Billing Profile-CMPRJBL001

![](/legacyfs/online/storage/blog_attachments/2022/09/Screenshot-2022-09-23-182954-1.png)

Select Project Billing Profile and Click on Project Billing Material Determination

![](/legacyfs/online/storage/blog_attachments/2022/09/Screenshot-2022-09-23-182954-2.png)

**Material Determination**

Here we have to define Material within this profile, where System will record incoming costs or quantities or both. M*aterial Direct*option allows the system to transfer the material directly to the billing document.

For quantity and costs column, Below are the Descriptions:

* Transfer Costs Only

* + This option transfers only the costs to be billed (where quantity is set to 1) for further billing processes. If the cost equals zero, the items are not transferred for further billing.

* Transfer Quantity Only

* + This option transfers only the quantities to be billed for further billing processes.  If the quantity equals zero, the items are not transferred for further billing.

* Transfer Costs and Quantity

* + This option transfers both costs and quantities to be billed for further billing processes.

* For Costs <> 0: Transfer Costs and Quantity

* + This option transfers both costs and quantities to be billed for further billing processes (when the cost is not equal to zero).

* For Quantity <> 0: Transfer Costs and Quantity

The option transfers both the costs and quantities to be billed for further billing processes (when the quantity is not equal to zero).

Material:

you can define material to be determined after fulfilling criteria, this will be alphanumeric

Note: You cannot use the A001 and A002 materials in this field for new material determination, as these types are reserved for On Account items.

**Material Determination Criteria**

Additionally, you can add specific criteria that enables the material to be determined.

Use the following fields to define the material determination criteria:

* Activity type

* G/L account Number

* Material Number

Based on the criteria you define for the material to be determined, the material is determined accordingly and transferred for further billing processes.

In case, System does not find any criteria fulfilling, then cost posting will fails to determine material for Billing.

Note: In case you made changes to Billing profile then repricing is must to be run otherwise you would get price inconsistency.

For Example: In our case we were having requirements where Internal as well as Contingent workers were working to fulfil the client requirements and using all the standard Roles/Activity types were in use for both the scenarios. In this case we have to define all the 20 roles (T001-T020) with Cost Element Groups YBPS\_T000 (Internal Employees), YBPS\_S001 (Contingent Worker) and YBPS\_S000 (Contingent Worker).

in this condition we have maintained as below:

|
 PB Profile |
 Line |
 Mat. dir. |
 Qty/Costs |
 Material |
 Field Name |
 Set Name |
 Value |
 Related to? |

|
 CMPRJBL001 |
 1 |
  |
 Transfer Costs and Quantity |
 T001 |
 GLACCOUNT |
 YBPS\_T000 |
  |
 Internal Employee |

|
  |
  |
  |
  |
  |
 ACTIVITYTYPE |
  |
 T001 |

|
 CMPRJBL001 |
 2 |
  |
 Transfer Costs and Quantity |
 T001 |
 GLACCOUNT |
 YBPS\_S000 |
  |
 Contingent Worker |

|
  |
  |
  |
  |
  |
 MATERIAL |
  |
 T001 |

|
 CMPRJBL001 |
 3 |
  |
 Transfer Costs and Quantity |
 T001 |
 GLACCOUNT |
 YBPS\_S001 |
  |

|
  |
  |
  |
  |
  |
 MATERIAL |
  |
 T001 |

|
 CMPRJBL001 |
 4 |
  |
 Transfer Costs and Quantity |
 U001 |
 GLACCOUNT |
 YBPS\_UBBT |
  |
 Usage Based Expense |

|
  |
  |
  |
  |
  |
 ACTIVITYTYPE |
  |
 U001 |

|
 CMPRJBL001 |
 5 |
  |
 Transfer Costs Only |
 E001 |
 GLACCOUNT |
 YBPS\_E\*\*\* |
  |
 Expense |

|
 CMPRJBL001 |
 6 |
 Yes |
 Transfer Costs and Quantity |
 L\* or H\* |
 GLACCOUNT |
 YBPS\_L\*\*\* or YBPS\_H\*\*\* |
  |
 License/Hard...