---
title: Identity and Access Management / Authorization Assignment (Part 3.2)
url: https://blogs.sap.com/2023/02/07/identity-and-access-management-authorization-assignment-part-3.2/
source: SAP Blogs
date: 2023-02-08
fetch_date: 2025-10-04T05:58:12.418184
---

# Identity and Access Management / Authorization Assignment (Part 3.2)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Identity and Access Management / Authorization Ass...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52648&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Identity and Access Management / Authorization Assignment (Part 3.2)](/t5/enterprise-resource-planning-blog-posts-by-sap/identity-and-access-management-authorization-assignment-part-3-2/ba-p/13564974)

![bjoern_brencher](https://avatars.profile.sap.com/8/c/id8c3473c3a9787d366cd104da8d2f24c357afeca9337322b3564270b389addd6a_small.jpeg "bjoern_brencher")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[bjoern\_brencher](https://community.sap.com/t5/user/viewprofilepage/user-id/194082)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52648)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52648)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564974)

‎2023 Feb 07
10:36 PM

[11
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52648/tab/all-users "Click here to see who gave kudos to this post.")

2,315

* SAP Managed Tags
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (2)

**Risk**

Users have access privileges beyond those necessary to perform their assigned duties, which may create improper segregation of duties.

**Control Description**

Dedicate approvers approve the nature and extent of user-access privileges for new and modified user access, including standard application business catalogues / business roles, critical financial reporting transactions, and segregation of duties.

**Background**

Assigning the correct authorizations to the right user is a key element in the segregation of duties – and therefore a cornerstone in the auditing process.

In S/4 HANA Cloud, authorizations are collected in so-called ‘Business Catalogue IDs” which are assigned to ‘Business roles” which can be assigned to users. These business roles give access to underlying applications. The access to company codes and within company codes can be restricted in roles.

**How to obtain the populations***(Please remember that the process might change with later releases)*

##### User created during the audit period (former USR02)

To obtain the population of users created during the audit period navigate to ‘Identity & Access Management’ > ‘Maintain Business Users’ > ‘Display Changes’, select the date range and check the selection box ‘Created Users’.

Note 1: By clicking on the user, it is possible to receive the following information:

* User validity (prior table USR02)
* User Lock indicator (prior table USR02)
* Role assignments (prior report RSUSR002)

Note 2: By clicking on the Business Role ID, you can identify the authorizations from the role as well as the Business Catalogues assigned to the role.

##### Business roles assignment changes during audited period (former RSUSR100N):

To obtain the population of users with Business roles assignment changes during the audit period navigate to ‘Identity & Access Management’ > ‘Maintain Business Users’ > ‘Display Changes’, select the date range and check selection box ‘Business Roles Changed’.

Note 3: Entries with "Authorizations have been reorganized/optimized due to technical reasons" can be ignored as these indicate SAP system internal reorganizations and do not necessarily indicate authorization changes.

Note 4: Business users require creation of an employee, but not all employees need to have a business user.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-05_20-49-26.png)

##### Role changes during audited period (role change documents)

To obtain a listing of changes made to roles during the testing period navigate to ‘Identity & Access Management’ > ‘Maintain Business Roles’ -> 'Display Changes'.

![](/legacyfs/online/storage/blog_attachments/2023/02/2023-02-05_21-00-11.png)

**Engage with us**

To read all upcoming posts in this series, please follow the [S4HANACloud audit](https://community.sap.com/t5/tag/S4HANACloud%20audit/tg-p/board-id/erp-blog-sap) tag we’ve created for this purpose.”

Or contact us on LinkedIn.

Labels

* [Technology Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/technology%20updates)

* [S4HANACloud audit](/t5/tag/S4HANACloud%20audit/tg-p/board-id/erp-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fidentity-and-access-management-authorization-assignment-part-3-2%2Fba-p%2F13564974%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [Authorization control to display data for Manage Supplier Line Items using BP authorization group](/t5/enterprise-resource-planning-blog-posts-by-sap/authorization-control-to-display-data-for-manage-supplier-line-items-using/ba-p/14231135)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [VIM Foundation & Invoice Solution Configuration Overview](/t5/enterprise-resource-planning-blog-posts-by-sap/vim-foundation-amp-invoice-solution-configuration-overview/ba-p/14229743)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Sunday
* [How to Create and Manage Blanket or Framework Purchase Orders in SAP S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-create-and-manage-blanket-or-framework-purchase-orders-in-sap-s/ba-p/14226571)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  a week ago
* [Issue with Activating Advanced Shipping and Receiving (ASR) in Integrated TM in S/4HANA 2022](/t5/enterprise-resource-planning-q-a/issu...