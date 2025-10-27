---
title: Revenue Recognition for Project Sales(Time and Material) in SAP Business ByDesign
url: https://blogs.sap.com/2022/11/04/revenue-recognition-for-project-salestime-and-material-in-sap-business-bydesign/
source: SAP Blogs
date: 2022-11-05
fetch_date: 2025-10-03T21:45:02.510041
---

# Revenue Recognition for Project Sales(Time and Material) in SAP Business ByDesign

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Revenue Recognition for Project Sales(Time and Mat...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67979&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Revenue Recognition for Project Sales(Time and Material) in SAP Business ByDesign](/t5/enterprise-resource-planning-blog-posts-by-members/revenue-recognition-for-project-sales-time-and-material-in-sap-business/ba-p/13561830)

![former_member821424](https://avatars.profile.sap.com/former_member_small.jpeg "former_member821424")

[former\_member821424](https://community.sap.com/t5/user/viewprofilepage/user-id/821424)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67979)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67979)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561830)

‎2022 Nov 04
5:51 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67979/tab/all-users "Click here to see who gave kudos to this post.")

1,872

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)
* [SAP Financial Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Financial%2520Supply%2520Chain%2520Management/pd-p/01200615320800000553)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)
* [SAP Financial Supply Chain Management

  SAP Financial Supply Chain Management](/t5/c-khhcw49343/SAP%2BFinancial%2BSupply%2BChain%2BManagement/pd-p/01200615320800000553)

View products (2)

In this blog post I have explained how the Revenue is Recognized for the Revenue type **‘Project Sales(Time and Material)'** when the accrual method is **“Recognize at the point of delivery”.**

Project sales include the sale of project-based services and Material but it does not includes the sale of standardized material and services.

**Prerequisites**

Navigate to Business Configuration > Choose the First Implementation > Click on Edit Project Scope > Under third Step Scoping Make sure that Sell Project-Based Products and Services is in Scope

![](/legacyfs/online/storage/blog_attachments/2022/11/1-11.png)

Figure1:Scoping

Under Fourth step Questions > Enable the question “Do you want to use Solution-Supported Revenue Recognition for sales orders?”.

![](/legacyfs/online/storage/blog_attachments/2022/11/6-7.png)

Figure2:Enable the question

Navigate to Business Configuration > Select the First Implementation > Click on Open Activity list > Search for Accrual Method Determination Activity > Assign the accrual method for the Revenue type Project sales(time and Material) .

![](/legacyfs/online/storage/blog_attachments/2022/11/7-10.png)

Figure3:Accrual method Determination

**Process flow**

Navigate to Sales order Workcenter > Create a new sales order by entering all the mandatory details . Under items tab add the Project Based Material and Services and click on Save.

![](/legacyfs/online/storage/blog_attachments/2022/11/8-11.png)

Figure4:Create Sales Order

Create a Project from the sales order and ‘Create Project’ field will be enabled only if we add the Project-Based Material and Services in the sales order.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-8.png)

Figure5:Create Project

Enter all the mandatory details and click on ok

![](/legacyfs/online/storage/blog_attachments/2022/11/9-9.png)

Figure6:Enter mandatory details

Project is Created and it is linked to the Sales Order

![](/legacyfs/online/storage/blog_attachments/2022/11/9-10.png)

Figure7:Project is linked to the sales order

Release the Sales Order

![](/legacyfs/online/storage/blog_attachments/2022/11/9-11.png)

Figure8:Release the sales order

Navigate to Project Management workcenter > Open the Created Project > Add the team member and Edit Period Plans for the Service under Work tab.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-12.png)

Figure9:Added team member

Enabled 'From Stock' indicator as I'm going to consume it from own stock for the Material under Materials tab.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-13.png)

Figure10:Enabled From Stock indicator

Released the project task

![](/legacyfs/online/storage/blog_attachments/2022/11/9-14.png)

Figure11: Release the Project Task

Created project stock order for the Material under Products tab.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-15.png)

Figure12:Create Project Stock Order

Choose the Ship From Location and click on finish

![](/legacyfs/online/storage/blog_attachments/2022/11/9-16.png)

Figure13:Choose ship from location

Navigate to Outbound Logistics control Workcenter > Search for Created Project Stock Order > Release the Project Stock Order demand

![](/legacyfs/online/storage/blog_attachments/2022/11/9-17.png)

Figure14:Release the Project Stock order Demand

Navigate to Outbound Logistics Workcenter > Delivery Proposal > Search for Project Stock Order > Allocated Material to the Project by clicking on Allocate button.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-18.png)

Figure15: Allocate material to the project

Choose the Source Logistics area and click on Save

![](/legacyfs/online/storage/blog_attachments/2022/11/9-20.png)

Figure16:Choose the Source Logistics area

Navigate to the Project Management Workcenter > Open the created Project >Click on Consume in order to Consume the material to the project![](/legacyfs/online/storage/blog_attachments/2022/11/Untitled-11.png)

Figure17: Consume the material to the Project

By logging into the Employee user, Edit and release the timesheet for the employee

![](/legacyfs/online/storage/blog_attachments/2022/11/9-21.png)

Figure18:Edit and release the timesheet for the employee

Actual quantity for the material and Service is updated in the Project .

![](/legacyfs/online/storage/blog_attachments/2022/11/Untitled-10.png)

Figure19:Actual quantity for the Material and Service

We can see the Journal entry posted for Internal Service Confirmation and Goods Issue for consumption where Cost of sales of Material and Services are posted to the Deferred Costs account. This account is a balance sheet account, which means that the costs are not yet recognized.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-22.png)

Figure20:Goods issue for consumption

![](/legacyfs/online/storage/blog_attachments/2022/11/Untitled-9.png)

Figure21:Internal Service Confirmation

Navigate to Cost and Revenue Work Center > Search for Sales Order > Execute Revenue Recognition for sales order before doing Customer Invoice and click on ok

![](/legacyfs/online/storage/blog_attachments/2022/11/9-23.png)

Figure22:Execute Revenue Recognition

Enter all the Mandatory Details and click on Ok

![](/legacyfs/online/storage/blog_attachments/2022/11/9-24.png)

Figure23:Enter the Mandatory details

Here we can see the Journal entry, the run posts recognized r...