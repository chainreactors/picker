---
title: SAP S/4 HANA EWM-QM Configuration Setup in 2020
url: https://blogs.sap.com/2023/03/26/sap-s-4-hana-ewm-qm-configuration-setup-in-2020/
source: SAP Blogs
date: 2023-03-27
fetch_date: 2025-10-04T10:46:05.920362
---

# SAP S/4 HANA EWM-QM Configuration Setup in 2020

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* SAP S/4 HANA EWM-QM Configuration Setup in 2020

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4682&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4 HANA EWM-QM Configuration Setup in 2020](/t5/supply-chain-management-blog-posts-by-members/sap-s-4-hana-ewm-qm-configuration-setup-in-2020/ba-p/13557052)

![SaikiranGummadi6](https://avatars.profile.sap.com/d/a/idda5483fe14a99b4d62e1ca6f3a020531388dfaf152677e390c2b9b0901ea0140_small.jpeg "SaikiranGummadi6")

[SaikiranGummadi6](https://community.sap.com/t5/user/viewprofilepage/user-id/792016)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4682)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4682)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557052)

‎2023 Mar 26
2:24 PM

[20
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4682/tab/all-users "Click here to see who gave kudos to this post.")

48,324

* SAP Managed Tags
* [EWM - Quality Management](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Quality%2520Management/pd-p/8dbbb533-ae73-41e6-aaf4-f085c0b172a8)
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Delivery Processing](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Delivery%2520Processing/pd-p/674879738150278190016884561790060)
* [EWM - Shipping and Receiving](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Shipping%2520and%2520Receiving/pd-p/551700313515132864819929295213440)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Delivery Processing

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BDelivery%2BProcessing/pd-p/674879738150278190016884561790060)
* [EWM - Shipping and Receiving

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BShipping%2Band%2BReceiving/pd-p/551700313515132864819929295213440)
* [EWM - Quality Management

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BQuality%2BManagement/pd-p/8dbbb533-ae73-41e6-aaf4-f085c0b172a8)

View products (4)

**Quality Management plays a key role in the warehouse for different business like pharmaceutical,Bevergaes and FMCG.**

The Main purpose of the blog is to explain about EWM-QM Configuration setup and transaction processing with one example

To achieve this we have to go with following steps

1)Create a Material Master with Quality Management and Inspection type

2) Define External Storage Process Steps

3) Define & Assign Storage Process Definition

4) Define Process Oriented Storage Control

5) Define & Determination of Warehouse Process Type

6)Maintain process type indicators and Quality Inspection group at product master level

7)Define work center for Quality Storage type(8020) and bin

8)Define Putaway Strategies

9)Generate Inspection Object Types Version

10)Maintain Inspection Object Types Version

11)Define and Activate Warehouse-Dependent IOTs

12)Define Quality Inspection Group

13)Maintain Follow-Up Actions

14)Maintain Inspection Results

15)Testing

**NOTE:NO NEED TO ACTIVATE BC SET IN S4HANA**

**NOTE:NEED TO ACTIVATE BC SET IN Decentrailsed system**

**Decentralised system:**

![](/legacyfs/online/storage/blog_attachments/2023/03/1-57.png)

1)Create a Material Master with Quality Management and Inspection type

Create a material master -371 with Quality Management view and Inspection Type

![](/legacyfs/online/storage/blog_attachments/2023/03/2-34.png)

2) Define External Storage Process Steps

Define External Storage Process Steps

IMG Path: SPRO→SCM EWM →Extended Warehouse Management → Cross Process Settings → Warehouse task →Define External storage process step.

![](/legacyfs/online/storage/blog_attachments/2023/03/MicrosoftTeams-image-7.png)

3) Define & Assign Storage Process Definition

Define & Assign Storage Process Definition

IMG Path: SPRO→SCM EWM →Extended Warehouse Management→ Cross Process Settings → Warehouse task → Define Storage Process Definition→Assign Storage Process step

![](/legacyfs/online/storage/blog_attachments/2023/03/3-35.png)

4)Define Process Oriented Storage Control

IMG Path: SPRO→SCM EWM → Extended Warehouse Management→Cross Process Settings → Warehouse task → Define process-oriented storage control

![](/legacyfs/online/storage/blog_attachments/2023/03/4-26.png)

5) Define & Determination of Warehouse Process Type

Define & Determination of Warehouse Process Type

![](/legacyfs/online/storage/blog_attachments/2023/03/5-25.png)

WPT Control indicator

![](/legacyfs/online/storage/blog_attachments/2023/03/6-19.png)

Assign Control Indicator to WPT

![](/legacyfs/online/storage/blog_attachments/2023/03/7-18.png)

6)Maintain process type indicators and Quality Inspection group at product master level

![](/legacyfs/online/storage/blog_attachments/2023/03/38.png)

7)Define work center for Quality Storage type(8020) and bin

![](/legacyfs/online/storage/blog_attachments/2023/03/8-14.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/9-17.png)

8)Define Putaway Strategies

![](/legacyfs/online/storage/blog_attachments/2023/03/36-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/37.png)

Quality Management Setup in EWM

9)Generate Inspection Object Types Version

SPRO:IMG→Cross process settings→Quality Management→ Basics and Integration→Generate Inspection Object Types Version

![](/legacyfs/online/storage/blog_attachments/2023/03/10-16.png)

10)Maintain Inspection Object Types Version

SPRO:IMG→Cross process settings→Quality Management→Basics and Integration→ Maintain Inspection Object Types Version![](/legacyfs/online/storage/blog_attachments/2023/03/11-14.png)

11)Define and Activate Warehouse-Dependent IOTs

SPRO:IMG→Cross process settings→Quality Management→ Basics and Integration→ Define and Activate Warehouse-Dependent IOTs

![](/legacyfs/online/storage/blog_attachments/2023/03/12-13.png)

12)Define Quality Inspection Group

SPRO:IMG→Cross process settings→Quality Management→ Inspection Planning→ Define Quality Inspection Group

![](/legacyfs/online/storage/blog_attachments/2023/03/13-15.png)

13)Maintain Follow-Up Actions

SPRO:IMG→Cross process settings→Quality Management→ Inspection Results→ Maintain Follow-Up Actions→ Define Follow-Up Actions

![](/legacyfs/online/storage/blog_attachments/2023/03/14-12.png)

14)Maintain Inspection Results

SPRO:IMG→Cross process settings→Quality Managementà Inspection Results→ Maintain Follow-Up Actions→Assign Logistical Follow-Up Actions

![](/legacyfs/online/storage/blog_attachments/2023/03/15-12.png)

SPRO:IMG→Cross process settings→Quality Management→Inspection Results→ Maintain Follow-Up Actions →Assign Default Work Center for Inspections

![](/legacyfs/online/storage/blog_attachments/2023/03/16-9.png)

We need to maintain quality inspection rule in sap easy access it’s a mandatory s...