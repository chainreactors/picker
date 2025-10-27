---
title: Service Order: Unplanned Item in SAP S/4 HANA Cloud
url: https://blogs.sap.com/2022/11/27/service-order-unplanned-item-in-sap-s-4-hana-cloud/
source: SAP Blogs
date: 2022-11-28
fetch_date: 2025-10-03T23:55:09.620312
---

# Service Order: Unplanned Item in SAP S/4 HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Service Order: Unplanned Item in SAP S/4 HANA Clou...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/47738&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Service Order: Unplanned Item in SAP S/4 HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/service-order-unplanned-item-in-sap-s-4-hana-cloud/ba-p/13534998)

![mukesh_mishra](https://avatars.profile.sap.com/7/6/id760edea437f12f53f140907c8c0c9d56a9bb3224763a4b886271f91be9fbdbb9_small.jpeg "mukesh_mishra")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[mukesh\_mishra](https://community.sap.com/t5/user/viewprofilepage/user-id/422119)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=47738)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/47738)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13534998)

‎2022 Nov 27
11:06 AM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/47738/tab/all-users "Click here to see who gave kudos to this post.")

2,127

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (1)

The feature Unplanned Item enables the service technician to put unexpected/unplanned stock managed service parts, expenses and service items into the service confirmation, which are not listed in the service order.

Services that are listed in a service order are *planned* items. Any service offered to an end customer which does not belong to the service order is considered as an *unplanned item* in the service order.

### **Prerequisites**

* Service order reference item: To enter an unplanned item in a service confirmation, a reference item in service order is required.

* The service order reference item must be a planned service item.

### **Need for Unplanned Item in Service Order**

An unplanned item is typically needed when the technician goes onsite and discovers that unexpected services are to be performed on the machine or equipment which were not planned initially. This is when an unplanned item needs to be added to the Service Confirmation.

When a service technician adds an unplanned item with reference to a service order reference item in a service confirmation, the same unplanned item is created automatically and assigned to the service order, resulting in the creation of an account assignment object for an unplanned item.

Depending on the type of service order reference item, there are three possibilities to create an unplanned item in the service order.

* If the service order reference item is a normal item, an unplanned item in the service order will be created.

* If the service order reference item belongs to a standard service bundle, an unplanned item in the service order will be included under the main item as sub item.

* If a service order reference item belongs to a fixed price service bundle, an unplanned item in a service order will not be created under the fixed price main item.

### **Use**

Service Contract Determination

* Service Contract determination is done for the unplanned service confirmation item.

Follow Up Process

* Unplanned items in the service order will not trigger the follow-up process, such as billing, or purchase requisition creation.

Executing Service Employee

* The Executing service employee is not determined automatically, this must be done manually.

* For unplanned items in service order, service team data will be copied from the service order reference item. The system automatically copies organization data in service order item from the service order header. And for unplanned item in service confirmation, copying org data will be handled by system based on the customizing settings maintained.

Integration

* Service order items that are specified as unplanned items are not replicated to SAP Field Service Management.

Pricing

* The newly added unplanned item(s) in service confirmation are pricing relevant.

* Unplanned items in the service order are not pricing relevant.

Profit Center

* Profit centers are copied from the reference item in main service order to the unplanned item in the service confirmation.

Deletion of Unplanned Items

* Can be done in a service confirmation before the unplanned item in the service order is set to **Released**. They are initially created with status "Open".

* Deletion of unplanned items in service orders is handled the same as planned items.

* The deletion of an unplanned item from a service confirmation will result in the removal of the unplanned item in a service order. However, deleting an unplanned item from the service order will not delete the item from the service confirmation.

#### **Scenario of How to Add Unplanned items to a Service Confirmation.**

#### **![](/legacyfs/online/storage/blog_attachments/2022/10/UpI1.jpg)**

In the F4 help for the product – configurable and non-stock spare parts product are excluded, so not selectable.

### ![](/legacyfs/online/storage/blog_attachments/2022/10/UpI2.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/10/UpI3.jpg)

Unplanned items added in service confirmation are copied to the service order and can be identified using the indicator for unplanned item(s), as shown below.

![](/legacyfs/online/storage/blog_attachments/2022/10/UpI4.jpg)

#### **Change of Unplanned Item in Service Order / Confirmation:**

* No changes are allowed via the WEBUI for unplanned items in a service order.

* All actions are disabled on the service order for the unplanned item.

* All the changes are done via the service confirmation item.

#### ![](/legacyfs/online/storage/blog_attachments/2022/10/UpI5.jpg)

#### **Feature Toggle Maintenance**

Unplanned item functionality is available only after activating the feature toggle with ID **CRMS4\_SRVC\_TRANS\_UNPLANNED\_ITEM** in the system as of SAP S/4 HANA Cloud 2208.

It is default functionality as of SAP S/4 HANA Cloud 2302 release.

#### **Required Configuration Step**

You have activated the feature with technical ID *CRMS4\_SRVC\_TRANS\_UNPLANNED\_ITEM* in the app *Activate New Features.*

![](/legacyfs/online/storage/blog_attachments/2022/09/Feature-Toggle.jpg)

### More information ![:backhand_index_pointing_down:](/html/@C4F818A309A90CCCB0A49E2B6A8FEF3E/emoticons/1f447.png ":backhand_index_pointing_down:")

![](/legacyfs/online/storage/blog_attachments/2022/10/UpI6-1.jpg) For more information, see the product assistance on the SAP Help Portal for [S/4HANA Cloud](http://help.sap.com/viewer/p/SAP_S4HANA_CLOUD) under *Service >> Service Order Management >> Manage Service Orders >> Unplanned Items*

Thank you readers for sparing time to read my blog post. I hope this was helpful and would lov...