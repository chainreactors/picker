---
title: SAP PS project scheduling in complex ETO/CTO+ processes for mechanical & plant engineering / heavy industrial machinery
url: https://blogs.sap.com/2023/07/26/sap-ps-project-scheduling-in-complex-eto-cto-processes-for-mechanical-plant-engineering-heavy-industrial-machinery/
source: SAP Blogs
date: 2023-07-27
fetch_date: 2025-10-04T11:54:39.966377
---

# SAP PS project scheduling in complex ETO/CTO+ processes for mechanical & plant engineering / heavy industrial machinery

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP PS project scheduling in complex ETO/CTO+ proc...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68314&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP PS project scheduling in complex ETO/CTO+ processes for mechanical & plant engineering / heavy industrial machinery](/t5/enterprise-resource-planning-blog-posts-by-members/sap-ps-project-scheduling-in-complex-eto-cto-processes-for-mechanical-plant/ba-p/13566463)

![Serge_Driendl](https://avatars.profile.sap.com/9/2/id92bbc13fcce60707d44e19e3bc9b10424c5ba4ef875121a65f8067a541f18616_small.jpeg "Serge_Driendl")

[Serge\_Driendl](https://community.sap.com/t5/user/viewprofilepage/user-id/699456)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68314)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68314)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566463)

‎2023 Jul 27
12:11 AM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68314/tab/all-users "Click here to see who gave kudos to this post.")

3,506

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [PLM Project System (PS)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Project%2520System%2520%28PS%29/pd-p/653310048283475313268757797580946)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [PLM Project System (PS)

  Software Product Function](/t5/c-khhcw49343/PLM%2BProject%2BSystem%2B%252528PS%252529/pd-p/653310048283475313268757797580946)

View products (2)

Correct network and thus project scheduling is of paramount importance in SAP PS, especially for complex project schedules like they often occur in ETO/CTO+ scenarios, like e. g. in mechanical & plant engineering or heavy industrial machinery projects (of course this guide is valid for many more industries).

If we take projects from those industries as an example scenario, correct network scheduling in SAP PS plays a critical role in ensuring project success. It enables efficient resource utilization (workforce & material), timeline adherence, risk management, and cost control. By facilitating effective project monitoring and fostering collaboration among team members, it sets the foundation for a well-executed and successful project.

As all of you know, scheduling complex projects in SAP PS is one of the most complex activities possible and there are heavy misconceptions on how it is configured and executed properly.

### Configuration:

Especially in mechanical & plant engineering and heavy industrial machinery industries, the leading elements for scheduling are single network activities spread across different networks and sometimes even across several projects, that are scheduled strictly bottom up. That means that the duration of every single activity and their relationship to each other is determining scheduled dates on activity level. These dates are passed bottom up to the network headers and through the work breakdown structure up to the project definition, either with earliest or latest dates as the leading dates.

### Execution:

In SAP PS we have different possibilities on how to schedule one or more projects:

* Project Builder (CJ20N) – Project Definition + “Schedule”

* Project Planning Board

* CN24N (overall network scheduling with levels & subnetworks)

* CN24 (overall network scheduling)

* CJ29 (Project/WBS scheduling)

* others

And because of this multitude of possibilities, I experienced that users as well as consultants have a wrong understanding on how to properly (re)schedule complex projects with a multitude of networks connected to each other.

The usual way is to teach users and consultants to use either the project builder or the Project Planning Board functionalities. Especially for initial scheduling they work just fine and the calculated dates are always correct (at least I never experienced errors).

### Example Process

Please keep in mind, that the sequence of the displayed activities are highly simplified for demonstration purposes and do not represent an accurate picture of the real plant engineering business process.

Standard result from initial scheduling (three networks, each assigned to one level 2 WBSE, with three activities each):![](/legacyfs/online/storage/blog_attachments/2023/07/1-83.png)

Initial scheduling result

Now the duration of one activity is shortened e. g. due to adjustments in workload or available capacities.This requires the rescheduling of possibly the entire project, if you have end to end activity relationships.![](/legacyfs/online/storage/blog_attachments/2023/07/2-39.png)

Shortened activity duration

If you reschedule through CJ20N/Gantt the result is not what you would expect. The main problem is that in complex project plans, the wrong scheduling results might go unnoticed or noticed to late. That might have severe impacts on the project schedule from a logistical and also from a commercial point of view:![](/legacyfs/online/storage/blog_attachments/2023/07/3-36.png)

Wrong scheduling result with incorrect buffer (latest dates)

###

### Solution Design / Best Practice Process

In order to schedule the project correctly, you have to execute a two step process, that works as designed from SAP:

Step 1: Schedule the network activities resp. networks through CN24![](/legacyfs/online/storage/blog_attachments/2023/07/4-32.png)

Correct network scheduling but WBS is not scheduled yet (differences between WBSE and network activity dates are highlighted)

Step 2: Schedule the WBS through CJ29, Project Builder or Project Planning Board .The WBS resp. the Project Definition is scheduled correctly and the project (re)scheduling process is finished.![](/legacyfs/online/storage/blog_attachments/2023/07/5-30.png)

Correctly scheduled project

### Final thoughts & concluding words

The described solution scenario is neither generally valid for all industries and project scenarios nor it is required for every SAP PS scenario as projects might have a different structure and/or have service or plant maintenance orders integrated.

Therefore proper thoughts and/or consulting about the specific scenario and industry is required. Possibly I will add some insights to additional scenarios and functionalities in the future.

I hope this blog post was helpful for you!

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fsap-ps-project-scheduling-in-complex-eto-cto-processes-for-mechanical-plant%2Fba-p%2F13566463%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
...