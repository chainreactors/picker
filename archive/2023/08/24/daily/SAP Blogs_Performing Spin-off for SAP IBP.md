---
title: Performing Spin-off for SAP IBP
url: https://blogs.sap.com/2023/08/23/performing-spin-off-for-sap-ibp/
source: SAP Blogs
date: 2023-08-24
fetch_date: 2025-10-04T12:01:24.331557
---

# Performing Spin-off for SAP IBP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Performing Spin-off for SAP IBP

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/5125&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Performing Spin-off for SAP IBP](/t5/supply-chain-management-blog-posts-by-members/performing-spin-off-for-sap-ibp/ba-p/13580482)

![samir_ali](https://avatars.profile.sap.com/9/9/id99964f6066b17ccd2f6b68b359e298d93208cfc7ed88d0721007b2af7efe28ea_small.jpeg "samir_ali")

[samir\_ali](https://community.sap.com/t5/user/viewprofilepage/user-id/684406)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=5125)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/5125)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13580482)

‎2023 Aug 23
10:14 PM

[1
Kudo](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/5125/tab/all-users "Click here to see who gave kudos to this post.")

1,105

* SAP Managed Tags
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)
* [SAP Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Supply%2520Chain%2520Management/pd-p/01200615320800000492)

* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP Supply Chain Management

  SAP Supply Chain Management](/t5/c-khhcw49343/SAP%2BSupply%2BChain%2BManagement/pd-p/01200615320800000492)

View products (2)

Dear All,

Nowadays mergers, acquisitions and restructuring of organisations are common. These kind of projects are very different from a usual SAP IBP implementation project and have their own challenges on the IT side, so they need a different approach for successful execution.

There are several ways and options to tackle SAP Carve-Out / Spin-off projects.

You can perform it into two phases like:

![](/legacyfs/online/storage/blog_attachments/2023/08/Spin-off.jpg)

**SAP IBP Spin-Off**

Here, I have covered 1st phase for Supply Chain area and its logical separation. Segregation of data and access to End-users using authorization control.

In the IBP logical data segregation is achieved using permission filters, roles and user groups.

At the backend, the SAP IBP database (Planning Area) remains the same.

![](/legacyfs/online/storage/blog_attachments/2023/08/Access_Control.jpg)

**SAP IBP Spin-off Phase 1 - Using Authorization Control**

* New locations will be cloned into new entities in the ERP system.

* SAP product numbers will remain the same, and they will be extended to the new location.

* All data will flow co-mingled into IBP and will be segregated for the end users based on the permission filters and the role assigned for viewing or modifying the data.

* The permission filters will apply to all the planning and report templates for the end users, and they will be able to view only the permissible data as defined in the respective filters attached to their roles.

**High Level Key tasks:**

* Create Permission filters

* Create User Groups and assign users

* Create User roles

* Assign permission filters to User group

* Assign Users to User roles

* Modify User Global Configuration parameter

* Update Copy Operators

* Create / Modify Planning filters

* Update Interfaces

**Details of Key Tasks :**

* **Create Permission filters: -**

Create permission filter for each Company and its based-on attribute condition for the Product category and Locations

e.g.

![](/legacyfs/online/storage/blog_attachments/2023/08/Permission_filter.jpg)

Permission Filter

* Similarly created for Spin-off Company 2

* **Create New user groups and assign users:**

e.g. Company1 and Company 2

If you have multiple roles then you can create multiple user groups

Like Supply planner\_Comp1, Demand planner\_Comp1

        Supply planner\_Comp2, Demand planner\_Comp2

* Assign permission filters to user groups

* **Creation and assignment of User Roles :-** Create New user roles created with restrictions mainly based on e.g. subnetworks, Planning versions, planning view templates, Planning operators, etc.

* .Assign these roles to business users

* **Planning Filter** Changes or new creation: Create or modify planning filter and assign it to users / user groups

* **Global parameter changes :-** To propagate the attribute permission filter global parameter "PERMFILTER\_SIMPLE\_TO\_COMPOUND\_MD"  to be activated to "Yes"

* **Copy Operator’s profile Changes :-** In copy operator profile , Activate check box - "Consider Permission Filter (Write)" Option

* **IBP Application job template:-**

Batch job re-alignment is required.  Review each job and make necessary changes As we have same planning area, so common jobs can be run as it is but any specific scenario to new company then create new job template or modify existing.

* **CPI Interface modification:-** Relevant CPI interfaces updated ( Master data, Transactional data) – mainly review filters and update accordingly

**Note:** If few existing users moved to new spin-off company then re-assignment exercise need to be performed for following to their new user id

* Un assign from old user roles and user groups

* Review below Favourite types and act for re-assignment.

  + Alert Definition

  + Alert Subscription

  + Analytics Chart

  + Master Data Favourite

  + Planning Filter

  + Planning View (Web-Based)

  + Planning View Favourite

  + Scenario

  + Supply Chain Network Chart

I hope that you found this blog useful for your future spin off / carveout projects.

Thank you for reading!  All the best

* [SAP IBP Carveout](/t5/tag/SAP%20IBP%20Carveout/tg-p/board-id/scm-blog-members)
* [SAP IBP Spinoff](/t5/tag/SAP%20IBP%20Spinoff/tg-p/board-id/scm-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fsupply-chain-management-blog-posts-by-members%2Fperforming-spin-off-for-sap-ibp%2Fba-p%2F13580482%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Material & Quality Management in SAP S/4HANA](/t5/supply-chain-management-blog-posts-by-members/material-amp-quality-management-in-sap-s-4hana/ba-p/14234018)
  in [Supply Chain Management Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)  yesterday
* [What's New in SAP Asset Performance Management 2509](/t5/supply-chain-management-blog-posts-by-sap/what-s-new-in-sap-asset-performance-management-2509/ba-p/14229539)
  in [Supply Chain Management Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)  Tuesday
* [Means of Transport Ranking based on Transportation Duration - SNP Pla...