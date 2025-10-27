---
title: SAP BN4L – Manage Dock Appointments: Enabling Role-Based Access
url: https://blogs.sap.com/2022/12/01/sap-bn4l-manage-dock-appointments-enabling-role-based-access/
source: SAP Blogs
date: 2022-12-02
fetch_date: 2025-10-04T00:16:57.714978
---

# SAP BN4L – Manage Dock Appointments: Enabling Role-Based Access

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* SAP BN4L – Manage Dock Appointments: Enabling Role...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4806&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BN4L – Manage Dock Appointments: Enabling Role-Based Access](/t5/supply-chain-management-blog-posts-by-members/sap-bn4l-manage-dock-appointments-enabling-role-based-access/ba-p/13563848)

![justyna](https://avatars.profile.sap.com/a/3/ida3bcf788248277cba1e90ef90a6be1000cbf9a6cc81caa5d8e8ff310ea7c2a8e_small.jpeg "justyna")

[justyna](https://community.sap.com/t5/user/viewprofilepage/user-id/42845)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4806)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4806)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563848)

‎2022 Dec 01
11:27 PM

[14
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4806/tab/all-users "Click here to see who gave kudos to this post.")

2,593

* SAP Managed Tags
* [SAP Business Network for Logistics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Logistics/pd-p/73554900100800001025)

* [SAP Business Network for Logistics

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BLogistics/pd-p/73554900100800001025)

View products (1)

# SAP Business Network for Logistics

## Feature for the Shipper: Enabling Role-Based Access of the Manage Dock Appointments app

#### **Business case:**

A Shipper created multiple Docking locations, and wants the warehouse operators to check appointments in Business Network for Logistics in the Manage Dock Appointment app.

A Shipper wants to avoid a situation when an operator of the first warehouse will manage appointments in the second warehouse.

![](/legacyfs/online/storage/blog_attachments/2022/12/5-3.png)

#### **Solution:**

Enable role-based access to the Manage Dock Appointments

##### **Step 1: Access SAP BTP Cockpit, and go to the created Shipper subaccount**

![](/legacyfs/online/storage/blog_attachments/2022/12/1-6.png)

##### **Step 2 Go to the Roles tab and filter by lbn-live**

Create role for AttributedLocationTemplate: Define your location id to filter docking locations in the Manage Docking Appointments app

![](/legacyfs/online/storage/blog_attachments/2022/12/2.png)

#####

##### **Step 3: Fill in needed information**

Example:

* Role name

![](/legacyfs/online/storage/blog_attachments/2022/12/3.png)

* Set the location\_idattribute as static and value as <Source System>:<External ID>

![](/legacyfs/online/storage/blog_attachments/2022/12/4-1.png)

Then press Enter to go next

![](/legacyfs/online/storage/blog_attachments/2022/12/2-3.png)

Source System:External ID you can find also in the created Docking location

* If there is already created a Role collection for users of a specific location you can assign just created Role, but if not, go next. Assigning Roles to Roles collections will be done in next step

![](/legacyfs/online/storage/blog_attachments/2022/12/6.png)

* Review the information and choose Finish

![](/legacyfs/online/storage/blog_attachments/2022/12/7.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/8.png)

The new role has been created

##### **Step 4 Go to Role collections and add new**

![](/legacyfs/online/storage/blog_attachments/2022/12/3-3.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/10.png)

An example of a Role collection’s name

The new Role collection is now created. To complete the settings, click the row:

![](/legacyfs/online/storage/blog_attachments/2022/12/11.png)

##### **Step 5 Edit Role collection**

![](/legacyfs/online/storage/blog_attachments/2022/12/12.png)

* Add users

![](/legacyfs/online/storage/blog_attachments/2022/12/15.png)

* Select the previously created role

![](/legacyfs/online/storage/blog_attachments/2022/12/13.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/14.png)

If users are not assigned to different Role collections that include Manage Appointment roles, add them to this Role collection

![](/legacyfs/online/storage/blog_attachments/2022/12/16.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/17.png)

Save changes

Now a user can see one Docking location as per setting:

![](/legacyfs/online/storage/blog_attachments/2022/12/4-4.png)

**Final remarks**:

The admin can create Role collections separately for each location and add users to more than one Role collections. Then the user will see multiple locations according to which he is assigned.

Or the administrator can create Role collection with multiple Roles, so there is more than one location in one Role collection. Note that all users will then see all locations from this Role collection.

Create a scenario which fits your organization, but my recommendation is to create Role collections for every location separately and assign users to many of them.

To see more information about SAP Business Network for Logistics Freight Collaboration I encourage you to visit: [SAP Logistics Business Network, freight collaboration option | SAP Help Portal](https://help.sap.com/docs/SAP_LBN_FC_OPTION)

I invite you to follow my profile to receive notifications about new blog posts.

Please share your opinion in the comments section.

* [Manage Dock Appointments](/t5/tag/Manage%20Dock%20Appointments/tg-p/board-id/scm-blog-members)

4 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-members%2Fsap-bn4l-manage-dock-appointments-enabling-role-based-access%2Fba-p%2F13563848%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Driving the Future of Utilities with SAP Intelligent Asset Management & Field Service](/t5/supply-chain-management-blog-posts-by-sap/driving-the-future-of-utilities-with-sap-intelligent-asset-management-amp/ba-p/14185187)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  2025 Aug 21
* [SAP Business Network for Logistics 2502 Release – What’s New?](/t5/supply-chain-management-blog-posts-by-sap/sap-business-network-for-logistics-2502-release-what-s-new/ba-p/14022289)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  2025 Feb 20
* [SAP Business Network for Logistics 2408 and 2409 Releases – What’s New?](/t5/supply-chain-management-blog-posts-by-sap/sap-business-network-for-logistics-2408-and-2409-releases-what-s-new/ba-p/13878448)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  2024 Sep 26
* [The Essential Role of Adverse Media Mo...