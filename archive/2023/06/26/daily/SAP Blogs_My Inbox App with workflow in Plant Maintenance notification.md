---
title: My Inbox App with workflow in Plant Maintenance notification
url: https://blogs.sap.com/2023/06/25/my-inbox-app-with-workflow-in-plant-maintenance-notification/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:16.252462
---

# My Inbox App with workflow in Plant Maintenance notification

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* My Inbox App with workflow in Plant Maintenance no...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67853&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [My Inbox App with workflow in Plant Maintenance notification](/t5/enterprise-resource-planning-blog-posts-by-members/my-inbox-app-with-workflow-in-plant-maintenance-notification/ba-p/13560051)

![swapson](https://avatars.profile.sap.com/4/d/id4dbebffc434939571ef543fab3f2227655761fe350f4a8616b5d914319494b33_small.jpeg "swapson")

[swapson](https://community.sap.com/t5/user/viewprofilepage/user-id/5565)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67853)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67853)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560051)

‎2023 Jun 25
11:55 AM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67853/tab/all-users "Click here to see who gave kudos to this post.")

12,726

* SAP Managed Tags
* [SAP Alert Notification service for SAP BTP](https://community.sap.com/t5/c-khhcw49343/SAP%2520Alert%2520Notification%2520service%2520for%2520SAP%2520BTP/pd-p/73555000100800001401)
* [SAP Asset Strategy and Performance Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Asset%2520Strategy%2520and%2520Performance%2520Management/pd-p/73555000100800001111)
* [SAP EAM Work Order](https://community.sap.com/t5/c-khhcw49343/SAP%2520EAM%2520Work%2520Order/pd-p/01200615320800003602)
* [SAP Enhanced Maintenance and Service Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Enhanced%2520Maintenance%2520and%2520Service%2520Planning/pd-p/67837800100800007301)
* [SAP Maintenance Assistant](https://community.sap.com/t5/c-khhcw49343/SAP%2520Maintenance%2520Assistant/pd-p/73555000100800003272)
* [SAP Predictive Asset Insights](https://community.sap.com/t5/c-khhcw49343/SAP%2520Predictive%2520Asset%2520Insights/pd-p/73555000100800000891)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [SAP EAM Work Order

  SAP EAM Work Order](/t5/c-khhcw49343/SAP%2BEAM%2BWork%2BOrder/pd-p/01200615320800003602)
* [SAP Enhanced Maintenance and Service Planning

  SAP Enhanced Maintenance and Service Planning](/t5/c-khhcw49343/SAP%2BEnhanced%2BMaintenance%2Band%2BService%2BPlanning/pd-p/67837800100800007301)
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)
* [SAP Asset Strategy and Performance Management

  Software Product](/t5/c-khhcw49343/SAP%2BAsset%2BStrategy%2Band%2BPerformance%2BManagement/pd-p/73555000100800001111)
* [SAP Alert Notification service for SAP BTP

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BAlert%2BNotification%2Bservice%2Bfor%2BSAP%2BBTP/pd-p/73555000100800001401)
* [SAP Predictive Asset Insights

  Software Product](/t5/c-khhcw49343/SAP%2BPredictive%2BAsset%2BInsights/pd-p/73555000100800000891)
* [SAP Maintenance Assistant

  SAP Maintenance Assistant](/t5/c-khhcw49343/SAP%2BMaintenance%2BAssistant/pd-p/73555000100800003272)

View products (7)

Hi All SAP Consultants.

Welcome to the detailed blog to configure the **My Inbox** application in the Fiori Launchpad for SAP Plant Maintenance notification.

**\*\*\* This blog post was was originally posted on eursap.com \*\*\***

# SAP Tips: Processing Maintenance notifications through My Inbox Fiori App

Link - [https://eursap.eu/2021/08/05/eursaps-tip-of-the-week-processing-maintenance-notifications-through-my...](https://eursap.eu/2021/08/05/eursaps-tip-of-the-week-processing-maintenance-notifications-through-my-inbox-fiori-app/)

**Application**- Standard workflow can be configured to assign the task to the person responsible. The maintenance supervisor can assign task to the maintenance technician. The user responsible will be notified for the assigned task by getting the work item in the My Inbox application. So that the respective maintenance technician can act accordingly as per the task assigned by the supervisor. Also the maintenance supervisor will get the notification that the assigned task is completed in the same My Inbox Application.

**Lets begin!!!!**

**Step 1 - Workflow Activation**

**T-code: SPRO**

Select **Set Workflow for Maintenance Notifications** activate the workflow                                .

```
![](/legacyfs/online/storage/blog_attachments/2023/06/Picture1-31.png)
```

SPRO-> Plant Maintenance and Customer Service -> Maintenance and Service Processing -> Maintenance and Service Notifications -> Notification Processing -> Set Workflow for Maintenance Notifications.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture2-22.png)

Select **Assign Agents**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture3-25.png)

Select the task and click on Attributes to set the task as a general task which can be processed by any user.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture4-19.png)

Select the General task

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture5-12.png)

Click on transfer to set the general task.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture6-15.png)

Repeat till all the tasks are general tasks.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture7-14.png)

Click on **Activate** **Event Linking** to activate the event of workflow. This will trigger the email after creation of maintenance notification

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture8-14.png)

Click on ‘WS 20000317’ workflow and click on ![](/legacyfs/online/storage/blog_attachments/2023/06/Picture9-12.png)symbol to activate the event linking of the business object.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture10-10.png)

Select **Event Linkage activated** and click on save to activate the workflow and save the changes in the transport request.

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture11-9.png)

**Similarly, activate the event linking of INPROCESSAGAIN.**

**So, the notification will appear in the My Inbox app of the user responsible mentioned in the maintenance notification.**

**Step 2-** **Activating My Inbox App in Fiori Launchpad**

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture12-7.png)

Refer above details of My Inbox app in Fiori app Library

<https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2953')/S20OP>

![](/legacyfs/online/storage/blog_attachments/2023/06/Picture13-8.png)

Activate above services in T-code ‘/O/IWFND/MAINT\_SERVICE’

Assign the role ‘SAP\_BR\_MAINTENANCE\_PLANNER’ to your SAP user ID.

![](/legacyfs/online/storage/blog_attac...