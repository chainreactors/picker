---
title: Taking process management in SAP Integrated Planning for Supply Chain (SAP IBP) to the next level with Microsoft Teams
url: https://blogs.sap.com/2023/02/10/taking-process-management-in-sap-integrated-planning-for-supply-chain-sap-ibp-to-the-next-level-with-microsoft-teams/
source: SAP Blogs
date: 2023-02-11
fetch_date: 2025-10-04T06:19:40.691723
---

# Taking process management in SAP Integrated Planning for Supply Chain (SAP IBP) to the next level with Microsoft Teams

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* Taking process management in SAP Integrated Planni...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5050&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Taking process management in SAP Integrated Planning for Supply Chain (SAP IBP) to the next level with Microsoft Teams](/t5/supply-chain-management-blog-posts-by-sap/taking-process-management-in-sap-integrated-planning-for-supply-chain-sap/ba-p/13566410)

![ZoltanMBiro](https://avatars.profile.sap.com/c/9/idc94a8f16e7574c925e37c7bbafe42dcc17f6e3a67cb59972777f35ee9e1da1ef_small.jpeg "ZoltanMBiro")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ZoltanMBiro](https://community.sap.com/t5/user/viewprofilepage/user-id/123548)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5050)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5050)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566410)

‎2023 Feb 10
8:01 PM

[6
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/5050/tab/all-users "Click here to see who gave kudos to this post.")

3,264

* SAP Managed Tags
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)
* [SAP Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Supply%2520Chain%2520Management/pd-p/01200615320800000492)

* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP Supply Chain Management

  SAP Supply Chain Management](/t5/c-khhcw49343/SAP%2BSupply%2BChain%2BManagement/pd-p/01200615320800000492)

View products (2)

As of the February 2023 release for SAP Integrated Business Planning for Supply Chain (SAP IBP), you can replicate planning tasks from process management in SAP IBP to Microsoft Teams. Please see our short [product video](https://youtu.be/aPcNK8YQW14) on this.

In the [previous blog post](https://blogs.sap.com/2023/02/06/design-considerations-when-integrating-ibp-tasks-into-microsoft-teams/) about the integration topic, we reviewed the advantages and disadvantages of the different modelling options that large enterprises could use for supporting process participants who are organized into different communities and where teams are spread over different locations.

In this article, we will explore how an organization could use Microsoft Teams to take their process management to the next level.

It’s important to understand the basic flow that’s involved when you use the additional automation capabilities of Microsoft Teams by leveraging Microsoft Power Automate to build an automatic flow that augments the process modelled within SAP IBP. In SAP IBP, the supply chain planning processes are modelled in process templates that break down the processes into process steps and then tasks. When SAP IBP is integrated with Microsoft Teams, these tasks are also generated on the Microsoft Teams side as the SAP IBP system is making various Microsoft Graph API calls. It is important to highlight that in such an integrated scenario, the process orchestration and, very importantly, the creation of tasks and the process are still driven by the process automation capability of SAP IBP. The tasks of one process step are created only when the process reaches that step and the step status is manually or automatically set to “In Progress”. The tasks are first created in SAP IBP. Immediately after this, a Microsoft Graph API is called to create their identical twins in Microsoft Teams. The process management backend ensures that changes made to tasks in Microsoft Teams or SAP IBP are synchronized. This applies to most changes like updating the task name or description, assignees, priority, and most importantly, the status (or rather the **Percent Complete** property). However, there are certain task properties or entities that are valid only within Microsoft Teams, such as attachments, comments, or lists; these are not synchronized back to SAP IBP. Similarly, there is information stored in SAP IBP that connects the tasks to a process instance and step that is not visible in Microsoft Teams when you’re looking at the task (unless it’s reflected by the bucket names).

So, when we use Microsoft Power Automate, we can extend the process automation and orchestration capabilities by using event triggers related to tasks, for example, when a task is created or completed.

Let’s look at two simple examples that can extend the interaction and process management capabilities by leveraging the Microsoft Teams environment:

**Example 1:** We would like to notify the planning community through a channel message that a task was completed.
For this we would go through a step-by-step description on how to create this in Microsoft Power Automate.

If you recall from the previous blog post, we can model the planning communities as teams and the processes within SAP IBP in different ways if they’re located in multiple countries. Let’s use option 2A where the planning community is modelled as one large team:

![](/legacyfs/online/storage/blog_attachments/2023/02/Blog2_Fig1.jpg)

This setup option could be enriched in Microsoft Teams by having dedicated private channels, one channel for the European supply chain planning community and one channel for the planners in the Americas region:

![](/legacyfs/online/storage/blog_attachments/2023/02/Blog2_Fig2.jpg)

When we start Microsoft Power Automate from within Microsoft Teams and create a new flow, we can use a template. We will search for the word “tasks” and select the template “Notify a team when Planner tasks change status”.

![](/legacyfs/online/storage/blog_attachments/2023/02/Blog2_Fig3.jpg)

At this point we give our flow a name and click **Next:**

![](/legacyfs/online/storage/blog_attachments/2023/02/Blog2_Fig4.jpg)

We will select which plan will be monitored for completing the tasks. Previously we added the **Tasks by Planner and To Do** app as a new tab to the **General** channel so that all community members can have a look at the tasks. At the same time, we created a new plan called “SAP IBP Planning Tasks”.
This is the plan that we will be selecting now in the flow for our unified team called “All Demand Planners”. Then we select who we want to notify, for example, the whole team and we select the **General** channel for this example, so that everyone sees this message:

![](/legacyfs/online/storage/blog_attachments/2023/02/Blog2_Fig5.jpg)

When you create a flow, default content is generated. To edit your flow, you can select it from the **Home** tab and edit it there.

At this point we see that the default flow that was created is based on the template with a standard three steps: the trigger condition at the top is that the task is completed, we then read the user profile of the task creator, and then we post an...