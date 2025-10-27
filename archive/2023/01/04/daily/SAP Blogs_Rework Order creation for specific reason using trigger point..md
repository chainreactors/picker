---
title: Rework Order creation for specific reason using trigger point.
url: https://blogs.sap.com/2023/01/03/rework-order-creation-for-specific-reason-using-trigger-point./
source: SAP Blogs
date: 2023-01-04
fetch_date: 2025-10-04T02:59:25.821782
---

# Rework Order creation for specific reason using trigger point.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Rework Order creation for specific reason using tr...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67564&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Rework Order creation for specific reason using trigger point.](/t5/enterprise-resource-planning-blog-posts-by-members/rework-order-creation-for-specific-reason-using-trigger-point/ba-p/13557119)

![hitman45](https://avatars.profile.sap.com/1/3/id1372b76c93d7eb99477f13a872fbdb56a57f1c314251b51fa4c5aad388bda713_small.jpeg "hitman45")

[hitman45](https://community.sap.com/t5/user/viewprofilepage/user-id/45281)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67564)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67564)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557119)

‎2023 Jan 03
6:49 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67564/tab/all-users "Click here to see who gave kudos to this post.")

9,120

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)

View products (1)

In SAP rework orders are created using trigger point. This blog present, creation of rework order with help of trigger point but we will be using reason for variance to create rework order.

Status profile: A status profile contains the individual user statuses and the business transaction rules defined for those statuses. You can define multiple limit number of user status profiles that can be maintained in SAP system.

Rework order: As we all know that rework might be of different problems/issues. These issue can be solve by single operation or might take multiple operation. It is also possible that even after doing the rework our product can not be use or fulfil our desire results.

Business Requirement:

Client has 5 operations, in that for the last operation they want to do rework if there is any rework quantity for Burr/dent issue only. Rework order should be created automatically if there is burr on the material. For reworking the burr, they use a specific operation called buffing. They want that cost of rework should go to main/actual production order.

## Pre-requisites:

### 1.      Create Status Profile: (T-code-BS02)

First we need to create a status profile.

Create a status profile as Rework & give a user status ZRW (Rework Order Created). Select Object types as PP/PM: operation.

![](/legacyfs/online/storage/blog_attachments/2022/12/User-status.png)

### 2.      Create Reason for Variance: (T-code-OPK5)

As per the requirement we have to create a reason for variance i.e. burr on material.

Create a reason for variance as ZRW (Burr – Create Rework Order). Assign the user status (Rework) & select the user status (ZRW) to this reason.

![](/legacyfs/online/storage/blog_attachments/2022/12/Reason-of-Variance-2.png)

### 3.      Create a ROS for rework (T-code-CA11).

As they will be using only buffing operation so we will create an reference operations set (ROS) with buffing as operation.

Rework ROS: Assign rework work center & give name to the operation.

![](/legacyfs/online/storage/blog_attachments/2022/12/ROS.png)

### 4.      Create Trigger Point (T-code-CO31)

In trigger point select function as: Create order with reference & assign the user status profile ZRW that we have created with help of status profile.

![](/legacyfs/online/storage/blog_attachments/2022/12/Trigger-Point.png)

In parameter maintain below details:

1. Assign User status as ZRW.

2. Group & Group Counter: ROS that we have created.

3. Order Type: ZRW (Rework Order Type).

![](/legacyfs/online/storage/blog_attachments/2022/12/TP-Parameter.png)

## Setup:

### 1.      Assign status profile to standard order type in (T-code-OPJH).

As we are dealing at operation level therefore assign status profile to operation level.

![](/legacyfs/online/storage/blog_attachments/2022/12/US-to-Order-type.png)

### 2.      In main routing assign, the trigger point to last operation OP50                               (T-code-CA02).

Open Routing>>>Go to operation overview screen>>>click on go to>>>select trigger point overview.

![](/legacyfs/online/storage/blog_attachments/2022/12/TP-to-Routing.png)

Assign the trigger point to last operation (OP50).

![](/legacyfs/online/storage/blog_attachments/2022/12/TP-in-routing.png)

We are able to see that trigger point is assigned to operation 50 which is our last operation.

## Testing scenario:

We have a production order of 50 qty. & in that we have found 10 qty. that need to be reworked for burr.

First do the following steps:

* Create a production order with standard order type for production (PP01).

* Release the production order.

* Do the goods issue to production order with help of MIGO.

* Also, Confirm the first four (OP10, OP20, OP30, OP40) operations in CO11N.

We are considering that we have not found any burr related issue in the first four operations.

### 1.      Go to confirmation of last operation (CO11N).

As mentioned above maintain rework quantity as 10qty.

Once you save the confirmation with Rework quantity & reason for variance as Burr (Create Rework Order).

![](/legacyfs/online/storage/blog_attachments/2022/12/Coo11n.png)

Trigger point will be triggered & will create a Re-work production order.

![](/legacyfs/online/storage/blog_attachments/2022/12/TPF.png)

### 2.      Now to see the re-work order go to COOIS.

We can see that the rework order has been created with order type ZRW of 10 qty.

![](/legacyfs/online/storage/blog_attachments/2022/12/COOIS.png)

### 3.      Open rework order & go to settlement header.

We can see that rework order needs to be settled to parent production order (Main order PP01).

That means the cost for rework will be booked to main order.

![](/legacyfs/online/storage/blog_attachments/2022/12/Settlement-rule.png)

Note:

Automatic & manual creation of order can be controlled by trigger point with ACTIVATE  function in parameters.

![](/legacyfs/online/storage/blog_attachments/2022/12/Activate.png)

### 4.      Check main production order:

User status has been updated as ZRW for the operation.

![](/legacyfs/online/storage/blog_attachments/2022/12/Main-order.png)

## Process Flow:

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2022-12-22-152436.png)

##

##

##

##

##

##

##

##

##

**Conclusion:**
This blog post shows the creation of rework order for any specific reason using trigger point. Production order status gets updated once we give reason for variance while confirmation. This updated user status triggers the trigger point to create a rework production order as per the parameters maintained in trigger point.

To check similar kind of content rela...