---
title: Harmonized Serial Number Profile Configuration In Embedded EWM
url: https://blogs.sap.com/2023/06/17/harmonized-serial-number-profile-configuration-in-embedded-ewm/
source: SAP Blogs
date: 2023-06-18
fetch_date: 2025-10-04T11:45:59.507916
---

# Harmonized Serial Number Profile Configuration In Embedded EWM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Harmonized Serial Number Profile Configuration In ...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4763&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Harmonized Serial Number Profile Configuration In Embedded EWM](/t5/supply-chain-management-blog-posts-by-members/harmonized-serial-number-profile-configuration-in-embedded-ewm/ba-p/13562836)

![uttarathiagaraj](https://avatars.profile.sap.com/6/0/id60fe1194afa3a814078790e66bdbf6183fd4af606dc0bcf8a59269a0b1081127_small.jpeg "uttarathiagaraj")

[uttarathiagaraj](https://community.sap.com/t5/user/viewprofilepage/user-id/146248)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4763)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4763)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562836)

‎2023 Jun 17
3:38 PM

[1
Kudo](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4763/tab/all-users "Click here to see who gave kudos to this post.")

9,264

* SAP Managed Tags
* [SAP Extended Warehouse Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Extended%2520Warehouse%2520Management/pd-p/01200615320800000705)
* [EWM - Basic Functions](https://community.sap.com/t5/c-khhcw49343/EWM%2520-%2520Basic%2520Functions/pd-p/212269919429502086862800135639950)

* [SAP Extended Warehouse Management

  SAP Extended Warehouse Management](/t5/c-khhcw49343/SAP%2BExtended%2BWarehouse%2BManagement/pd-p/01200615320800000705)
* [EWM - Basic Functions

  Software Product Function](/t5/c-khhcw49343/EWM%2B-%2BBasic%2BFunctions/pd-p/212269919429502086862800135639950)

View products (2)

**Purpose:** As part of 2020 release, SAP introduced harmonized serial number profile. With this profile, only one serial number profile will be assigned to a product on the ERP side in General Plant Data / Storage 2 (Plant data/Stro.2) view. EWM processes read the serialization settings from plant data (MARC) and updates in product master. To learn more this, please see: [Harmonized Serial number profile introduced with Extended warehouse management (EWM) in S/4HANA 2020...](https://blogs.sap.com/2020/10/11/harmonized-serial-number-profile-introduced-with-extended-warehouse-management-ewm-in-s-4hana-2020-release/). In this blog, we will enable Harmonized Serial Number Profile for an Embedded EWM System and update Quantity Offsetting Rules to allow serialization in deliveries.

**Required Configuration:**

*Configuration #1:* *Enable Harmonized Serialization in EWM*

SPRO Menu Path: SCM EWM > EWM > Master data > Product > Serial number profiles > Harmonized serial number profiles > Enable Harmonized Serialization in EWM

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-35.png)

*Configuration #2:* *Define Serial Number Profiles*

SPRO Menu Path: SCM EWM > EWM > Master data > Product > Serial number profiles > Harmonized serial number profiles > Define serial number profiles

* Define the serial number profile you would like to use and fill out necessary fields on the main page. Then select the serial number profile, and click on “Serializing procedures” in the Dialog Structure section on the left. From there, update options per your requirements.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture2-25.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture3-28.png)

* The important thing to include when creating your serial number profile is to make sure the “Warehouse Serial Number Profile” box checked otherwise this feature will not work in Embedded EWM. To get this checkbox checked, select the created profile, and click on “Warehouse Serialization Settings” in the Dialog Structure section on the left. From there, update options per your requirements.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-22.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture5-14.png)

*Configuration #3:* *Serial Numbers: Settings for Warehouse Number*

SPRO Menu Path: SCM EWM > EWM > Master data > Product > Serial number profiles > Harmonized serial number profiles > Serial Numbers: Settings for Warehouse Number

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture6-20.png)

* Here, update warehouse specific details based on your requirements (e.g. length of serial number)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture7-17.png)

*Configuration #4: Update Quantity Offsetting Rules for Documents to Allow Serialization*

If you do not do the following configuration in an embedded EWM system, then your deliveries will get in stuck in SMQ2 with the below error. This configuration will need to be done for each delivery’s item type. I will show how to do this for standard EWM inbound deliveries (doc category: PDI & item type: IDLV)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture13-11.png)

Step 1: Locate Qty Offsetting Profile for the delivery’s item type.

SPRO Menu Path: SCM EWM > EWM > Goods Receipt Process > Inbound Delivery > Define Item Types for Inbound Delivery Process. Find the “Qty. Offset Prf” and make a note of it.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture9-14.png)

Step 2: Update Quantity Offsetting Profiles

SPRO Menu Path:  SCM EWM > EWM > Cross-Process Settings > Delivery – Warehouse Request > Quantity Offsetting > Define Quantity Offsetting Profiles. Search for /SCWM/INB\_PRD\_DLV. Select profile and double click on “Assignment of Quantity Roles” from the left Dialog Structure. Scroll until finding Qty Role “SN” and validate that checkbox is unselected

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture10-12.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture11-11.png)

Below are some common quantity profiles with their descriptions

/SCWM/OUT\_PRD\_DLV (Outbound Del. Order Std Item EWM Std)

/SCWM/OUT\_PRD\_DLV\_PS (Item Production Supply (Outb. Del. Ord.))

/SCWM/INB\_PRD\_DLV\_PROD (Inb. Deliv. Standard Item GR Production)

/SCWM/INB\_PRD\_DLV (Inb. Delivery Standard Item EWM Standard)

**Other Notes/Tips:**

1. After activating harmonized serialization and creating your serial number profile, ensure that you assign serial number profile to the product (in material master) **before** you have any EWM transactional data (including stock) for this material. If you assign the serial number to a product or enable harmonized serialization after stock is in the warehouse, then EWM will not recognize these updates. However, there is way to “sync” the serial number profiles from ERP to EWM when your warehouse has stock loaded for a particular product using the “Repair Serial Number Profile” functionality, but this functionality has a lot of prerequisites and may not be feasible for all. See #2 for instructions on how to use this functionality. To learn more about this functionality, please see: [New EWM Functionalities in S4H 2020-Series1 | SAP Blogs](https://blogs.sap.com/2021/03/11/new-ewm-functionalities-in-s4h-2020-series1/)

2. To get to “Repair Se...