---
title: Steps to Generate SAP Readiness Check Report for SAP Cloud ALM
url: https://blogs.sap.com/2023/05/17/steps-to-generate-sap-readiness-check-report-for-sap-cloud-alm/
source: SAP Blogs
date: 2023-05-18
fetch_date: 2025-10-04T11:39:44.066712
---

# Steps to Generate SAP Readiness Check Report for SAP Cloud ALM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Steps to Generate SAP Readiness Check Report for S...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160654&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Steps to Generate SAP Readiness Check Report for SAP Cloud ALM](/t5/technology-blog-posts-by-members/steps-to-generate-sap-readiness-check-report-for-sap-cloud-alm/ba-p/13553632)

![ksandeep1525](https://avatars.profile.sap.com/b/4/idb46e641618024baee75e938dfa8ed432d7bf3ac758009b8615b5ce465bccd2e5_small.jpeg "ksandeep1525")

[ksandeep1525](https://community.sap.com/t5/user/viewprofilepage/user-id/141605)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160654)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160654)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553632)

‎2023 May 17
10:49 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160654/tab/all-users "Click here to see who gave kudos to this post.")

7,836

* SAP Managed Tags
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)

* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (1)

SAP Readiness Check for SAP Cloud ALM, SAP provides a self-service tool to analyze an existing SAP Solution Manager system in preparation for a transition to SAP Cloud ALM. SAP Readiness Check for SAP Cloud ALM provides visibility to the application lifecycle management capabilities used in an SAP Solution Manager system. This new SAP Readiness Check scenario also offers details regarding the availability and information on equivalent capabilities in SAP Cloud ALM or other SAP products to be considered when planning the move from SAP Solution Manager to SAP Cloud ALM.

SAP Readiness Check for SAP Cloud ALM helps customers to better understand the usage of their SAP Solution Manager system, and to plan and scope the transition of application lifecycle management capabilities to SAP Cloud ALM. This transition can be performed either completely or by taking a capability-by-capability approach. The new tool provides a mapping of equivalent capabilities between SAP Solution Manager and SAP Cloud ALM, while also showing the availability status of capabilities in SAP Cloud ALM. It also helps customers to engage with partners and SAP to discuss options for the most appropriate transition plan.

**Usage in SAP Solution Manager**: This check provides an overview of the application lifecycle management capabilities that are used in the analyzed SAP Solution Manager system and scopes these capabilities based on their relevance for the transition.

**Availability of Relevant Capabilitie**s: This check displays all SAP Solution Manager capabilities set to relevant in the Usage in SAP Solution Manager check, their mapping to equivalent capabilities in SAP Cloud ALM, and the availability status of these capabilities.

**SAP Cloud ALM Capabilities**: This check contains a complete list of currently available capabilities in SAP Cloud ALM per functional area (implementation and operations). In addition, the check shows which of these capabilities have an equivalent capability that is used in the analyzed SAP Solution Manager system, and which capabilities are only available in SAP Cloud ALM.

**Here are the steps we followed to generate Readiness Report for cloud ALM**

**Prerequisites:**

To run SAP Readiness Check for SAP Cloud ALM, data collectors are required to gather master and transactional data, as well as important customizing settings and application-relevant KPIs. However, only statistical data and no transactional data is exported.

To install the data collection framework and the associated collectors, implement this SAP Note in your SAP Solution Manager system or update the ST-PI component to Support Package 21 or higher. We recommend implementing or updating this Note in your system before executing a new analysis to always run with the latest updates.

Please note that the collector program /SDF/RC\_ALM\_COLLECT\_DATA will only run in an SAP Solution Manager 7.2 system.

**Execution Steps**:

1. **Execution of the Data Collectors**

* Execute the program /SDF/RC\_ALM\_COLLECT\_DATA via transaction SA38 in the productive client of the production system to schedule and download the data archive by performing the following three steps

Choose Schedule Analysis to schedule the master job to collect data.

![](/legacyfs/online/storage/blog_attachments/2023/05/2-26.png)

Once the data collection jobs finish, choose the Download Analysis Data option from within the program /SDF/RC\_ALM\_COLLECT\_DATA.

If analysis data has been already collected and you want to trigger a new collection, choose Delete Buffered Analysis Data before scheduling a new analysis.

* Optional: At this point, feel free to review the content of the archive file. The data is presented in a human-readable format.

![](/legacyfs/online/storage/blog_attachments/2023/05/3-29.png)

2. **Upload the Collected Data**

**To upload the collected data, take the following steps:**

* Launch the landing page for the SAP Readiness Check cloud application. <https://me.sap.com/readinesscheck>

* Choose Start New Analysis.

![](/legacyfs/online/storage/blog_attachments/2023/05/4-21.png)

* Provide a name for the analysis, locate the data archive file that was generated from the program /SDF/RC\_ALM\_COLLECT\_DATA, review and acknowledge the Terms of Use and Disclaimer, and then choose Create.

![](/legacyfs/online/storage/blog_attachments/2023/05/5-21.png)

* After a short period of time, usually less than 5 minutes, the status of the analysis will change from In Preparation to Available. You will need to refresh your browser or choose the Refresh icon on the page to get the updated status.![](/legacyfs/online/storage/blog_attachments/2023/05/6-18.png)

* Once the analysis is Available, you can open the analysis to find an interactive dashboard where you can explore the results of the analysis. The Learn More side panel and the embedded help capabilities can assist you as you explore and start to capture the next steps.

* Download the file for further analysis.

![](/legacyfs/online/storage/blog_attachments/2023/05/7-15.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/8-16.png)

**Note:**

The program /SDF/RC\_ALM\_COLLECT\_DATA will trigger a background job. You can check the background job log to ensure that the data was collected properly. To open the job log, select the Display Analysis Log option.

The same user that triggers the collection analysis with the program /SDF/RC\_ALM\_COLLECT\_DATA is set in the background job. Therefore, this user needs to have sufficient authorizations to read the analyzed data. Attached to this note is a template role with the required authorizations. You can upload this role via transaction PFCG and copy it into your system to assign it to the user executing the analysis.

References :

...