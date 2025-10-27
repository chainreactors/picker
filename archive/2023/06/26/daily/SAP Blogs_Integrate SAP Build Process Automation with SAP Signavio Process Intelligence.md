---
title: Integrate SAP Build Process Automation with SAP Signavio Process Intelligence
url: https://blogs.sap.com/2023/06/25/integrate-sap-build-process-automation-with-sap-signavio-process-intelligence/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:10.357245
---

# Integrate SAP Build Process Automation with SAP Signavio Process Intelligence

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Integrate SAP Build Process Automation with SAP Si...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162162&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrate SAP Build Process Automation with SAP Signavio Process Intelligence](/t5/technology-blog-posts-by-members/integrate-sap-build-process-automation-with-sap-signavio-process/ba-p/13561825)

![KazuhikoTakata](https://avatars.profile.sap.com/1/8/id1889cf49a29cb509d7526ad74839f1ef100438707b1dfe1b052916512cac4a6b_small.jpeg "KazuhikoTakata")

[KazuhikoTakata](https://community.sap.com/t5/user/viewprofilepage/user-id/38010)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162162)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162162)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561825)

‎2023 Jun 25
1:35 PM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162162/tab/all-users "Click here to see who gave kudos to this post.")

5,236

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Workflow Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management/pd-p/73554900100800003239)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Signavio Process Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Signavio%2520Process%2520Intelligence/pd-p/73554900100800003814)
* [SAP Workflow Management, process visibility capability](https://community.sap.com/t5/c-khhcw49343/SAP%2520Workflow%2520Management%252C%2520process%2520visibility%2520capability/pd-p/73555000100800001452)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Workflow Management

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement/pd-p/73554900100800003239)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Workflow Management, process visibility capability

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BWorkflow%2BManagement%25252C%2Bprocess%2Bvisibility%2Bcapability/pd-p/73555000100800001452)
* [SAP Signavio Process Intelligence

  business process transformation](/t5/c-khhcw49343/SAP%2BSignavio%2BProcess%2BIntelligence/pd-p/73554900100800003814)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (6)

This article is successor of [Use SAP Build Process Automation data for process mining](https://blogs.sap.com/2022/12/14/use-sap-build-process-automation-data-for-process-mining/).

## Introduction

Last time I posted my thought of Signavio Process Intelligence use case against workflow process developed by SAP Build Process Automation. That was generic idea to reduce initial setup effort of process mining project, and I thought it can be automated by something integration solution.

After some time, I have chance to develop this solution by myself. It was one week hackathon event and I completed implementing program by SAP BTP Integration Suite (like below architecture). Even my team was not awarded at that event, now I would like to share this solution for you to help your future process mining projects. Also, this activity was helpful for me to catch up SAP BTP Integration Suite capability.

From now on I will explain about my solution, but you may directly go to [my GitHub repository](https://github.com/kaztakata/sap-build-process-automation-integration-with-sap-signavio-process-intelligence/tree/main) to use my artifact.

![](/legacyfs/online/storage/blog_attachments/2023/06/Architecture-3.png)

Figure 1: Solution Architecture (Click to enlarge if applicable).

## Preparation

Before starting integration, we will prepare the source and target applications.

### Process Automation setup

As discussed in my previous post, any kind of Process (workflow) is available. This time I used Change and Innovation Approval sample process.

Please do not forget to add Visibility Scenario. This time I setup visibility attributes (e.g. Line of Business) for detailed analysis purpose.

After deployment, enter few data is helpful for testing integration.

![](/legacyfs/online/storage/blog_attachments/2023/06/VisibilityAttributes-1.png)

Figure 2: Visibility Attributes in Process Details (Click to enlarge if applicable)

### Signavio Process data pipeline setup

This is standard operation to create new Process data pipeline. Select Ingestion API as connection type, then follow instruction to complete wizard.

After that click connection (first) box in the pipeline, then you can see API information. This information is required at integration setup later.

![](/legacyfs/online/storage/blog_attachments/2023/06/SignavioApiCredentials.png)

Figure 3: Signavio API Credentials in Ingestion API connection (Click to enlarge if applicable)

## Integration overview

I would like to explain overview of this integration developed by SAP BTP Integration Suite.

### Required tables

"events" table storing event log is mandatory for process mining. This data is enough for minimum process mining, but normally we would like to do detailed analysis using attribute of workflow instance.

This is possible by "cases" table. It have case ID as primary key and arbitrary attribute columns. Then connect to "events" table by case ID, and provide attributes to each event log.

Finally, I need one more "tasks" table to decorate event description.

### Source API endpoints

Based on the table requirements above, I mapped Process Automation API endpoints and target tables.

1. [GET /v1/task-instances](https://api.sap.com/api/SPA_Workflow_Runtime/path/get_v1_task_instances) -> events table (completed events per workflow box)

2. [GET /v1/workflow-instances/{workflowInstanceId}](https://api.sap.com/api/SPA_Workflow_Runtime/path/get_v1_workflow_instances__workflowInstanceId_) -> cases table (workflow started event)

3. [GET /v1/workflow-instances/{workflowInstanceId}/attributes](https://api.sap.com/api/SPA_Workflow_Runtime/path/get_v1_workflow_instances__workflowInstanceId__attributes) -> cases table (visibility attributes)

4. [GET /v1/task-definitions](https://api.sap.com/api/SPA_Workflow_Runtime/path/get_v1_task_definitions) -> tasks table (event name)

You may feel "cases" table came from two sources. It is just technical matter to minimize Signavio Ingestion API call.

### Implementation key points

As discussed, I need to call four types of API to get data. I united these API call to single integration flow then call it from main program via ProcessDirect. API endpoint is parameter from main program....