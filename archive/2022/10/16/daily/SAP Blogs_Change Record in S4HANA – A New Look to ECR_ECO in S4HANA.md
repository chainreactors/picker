---
title: Change Record in S4HANA – A New Look to ECR/ECO in S4HANA
url: https://blogs.sap.com/2022/10/15/change-record-in-s4hana-a-new-look-to-ecr-eco-in-s4hana/
source: SAP Blogs
date: 2022-10-16
fetch_date: 2025-10-03T20:02:04.076348
---

# Change Record in S4HANA – A New Look to ECR/ECO in S4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Change Record in S4HANA - A New Look to ECR/ECO in...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66448&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Change Record in S4HANA - A New Look to ECR/ECO in S4HANA](/t5/enterprise-resource-planning-blog-posts-by-members/change-record-in-s4hana-a-new-look-to-ecr-eco-in-s4hana/ba-p/13543240)

![Abhishek_Parab](https://avatars.profile.sap.com/b/6/idb6d3875030ac79d847ff4375d2222e3ee13743660641ac5a8e1f232bc2de5488_small.jpeg "Abhishek_Parab")

[Abhishek\_Parab](https://community.sap.com/t5/user/viewprofilepage/user-id/633990)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66448)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66448)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543240)

‎2022 Oct 15
9:00 PM

[21
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66448/tab/all-users "Click here to see who gave kudos to this post.")

25,813

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [PLM (Product Lifecycle Management)](https://community.sap.com/t5/c-khhcw49343/PLM%2520%28Product%2520Lifecycle%2520Management%29/pd-p/237172457501282589953116013994631)
* [PLM Quality Management (QM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Quality%2520Management%2520%28QM%29/pd-p/484135010855456218597016630642366)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [PLM (Product Lifecycle Management)

  Software Product Function](/t5/c-khhcw49343/PLM%2B%252528Product%2BLifecycle%2BManagement%252529/pd-p/237172457501282589953116013994631)
* [PLM Quality Management (QM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BQuality%2BManagement%2B%252528QM%252529/pd-p/484135010855456218597016630642366)

View products (3)

Hi Folks,

As most of the folks are aware of the ECR and ECO functionality for the change Management for the BOM, Master recipe, Material Master etc. This functionality was phased out in S4/HANA, and Engineering Record was introduced. This too had some things missing like analyzing the impact etc., so from HANA 2020 SAP introduced Change record for the entire Change management Process which is more flexible. This Blog Captures the functionality of Change record from HANA 2020. There are few additional things like Impact Analyzer, change number Creation at Item Level etc. which is possible only in HANA 2021 The main purpose of this Blog is to setup a base for the future consultants in order to help them in achieving the functionality.

## Benefits of Change Record

![](/legacyfs/online/storage/blog_attachments/2022/10/Capture-5.png)

Image Courtesy  : SAP                       Image 1

## Key Features

![](/legacyfs/online/storage/blog_attachments/2022/10/2-27.png)

image Courtesy : SAP-----------Image 2

## Fiori App Required

1. Global Process route Workbench

2. Myinbox

3. Manage Change Record / engineering Changes,

4. Manage Team and Responsibilities

## Required configuration

### 1 . Define Number Range for the change Record

Path : SPRO  >  Logistics General  > PLM > Change Record  > Basic Settings >  Define Number Range Interval for Change Record

![](/legacyfs/online/storage/blog_attachments/2022/10/3-21.png)

                                                      *Image 3*

### 2. Define Object types

Path : SPRO  >  Logistics General  > PLM > Change Record  > Basic Settings >  Define Object types

![](/legacyfs/online/storage/blog_attachments/2022/10/4-18.png)

*Image 4*

Note : The object types are predefined ![](/legacyfs/online/storage/blog_attachments/2022/10/5-22.png)

*Image 5*

## 3. Define Object Categories

Path : SPRO  >  Logistics General  > PLM > Change Record  > Basic Settings > Define Object Categories

![](/legacyfs/online/storage/blog_attachments/2022/10/5-23.png)

*Image 6*

Note :  These are predefined Category

## 4, Define User Status

Path : SPRO  >  Logistics General  > PLM > Change Record  > User status > Define User Status

![](/legacyfs/online/storage/blog_attachments/2022/10/6-26.png)

*Image 7*

## 5. Define User Action

Path : SPRO  >  Logistics General  > PLM > Change Record  > User status > Define User Action

![](/legacyfs/online/storage/blog_attachments/2022/10/7-15.png)

*Image 8*

The User Action Text Defined appear on the front end screen of the Change Record

## 6 Define User Action Profile

Path : SPRO  >  Logistics General  > PLM > Change Record  > User status > Define User Status Profile

![](/legacyfs/online/storage/blog_attachments/2022/10/8-11.png)

*Image 9*

![](/legacyfs/online/storage/blog_attachments/2022/10/9-11.png)

*Image 10*

![](/legacyfs/online/storage/blog_attachments/2022/10/10-8.png)

*Image 11*

![](/legacyfs/online/storage/blog_attachments/2022/10/11-7.png)

*Image 12*

As seen in the above screenshot, conditions help to navigate to different status from the current status, as in this case the status is 10, so when the change record is in status 10, then it can be moved to either 10,30,15 manually or via background task.

## 7 Define Item Relevance

Path : SPRO  >  Logistics General  > PLM > Change Record  > Setting for engineering Changes  > Define Item Relevance.

![](/legacyfs/online/storage/blog_attachments/2022/10/12-10.png)

*Image 13*

This item relevance is used for the Items mentioned in the change record as shown in the image below for each of the object types. The control whether the enable the display the field of change relevance is covered by the configuration Define Engineering Record Type Section in ***Image 18***

![](/legacyfs/online/storage/blog_attachments/2022/10/13-7.png)

*Image 14*

### 8 Define Engineering Record types.

Path : SPRO  >  Logistics General  > PLM > Change Record  > Setting for engineering Changes  > Define Engineering Record Types

![](/legacyfs/online/storage/blog_attachments/2022/10/15-4.png)

*Image 15*

The change number and the status profile defined are assigned to the change record type Z01.

The check "ProcStatus" is used to control whether the item processing status is required or not as shown in the below image

![](/legacyfs/online/storage/blog_attachments/2022/10/14-8.png)

image 16

SAP recommends the use of Process route for the Engineering change's so the Check box Proc Route is enable for the Change record type  : Z01.

Para Check column is used to enable the check whether same Object is used parallelly in other change number which is open or in process

![](/legacyfs/online/storage/blog_attachments/2022/10/16-6.png)

image 17

The Reference Object that will be used for the change record type are updated. You can create Multiple change record type having different Reference Object

![](/legacyfs/online/storage/blog_attachments/2022/10/17-6.png)...