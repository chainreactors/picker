---
title: Cloud Integration – Poll-Enrich with SFTP Adapter for multiple file polling
url: https://blogs.sap.com/2022/10/31/cloud-integration-poll-enrich-with-sftp-adapter-for-multiple-file-polling/
source: SAP Blogs
date: 2022-11-01
fetch_date: 2025-10-03T21:25:30.874282
---

# Cloud Integration – Poll-Enrich with SFTP Adapter for multiple file polling

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Cloud Integration – Poll-Enrich with SFTP Adapter ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160834&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cloud Integration – Poll-Enrich with SFTP Adapter for multiple file polling](/t5/technology-blog-posts-by-members/cloud-integration-poll-enrich-with-sftp-adapter-for-multiple-file-polling/ba-p/13554848)

![fellipe_mendes](https://avatars.profile.sap.com/a/2/ida2ac67441d82d5d5ea2eb112b2a2f99258d2ae3dc3837ce5d59b47a8d4efe508_small.jpeg "fellipe_mendes")

[fellipe\_mendes](https://community.sap.com/t5/user/viewprofilepage/user-id/380351)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160834)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160834)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554848)

‎2022 Oct 31
8:26 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160834/tab/all-users "Click here to see who gave kudos to this post.")

13,247

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (3)

This blog describes a way to configure the Poll Enrich pattern in combination with the SFTP adapter to transfer files from SAP S/4HANA AL11 (DIR\_SAPUSERS) to an external SFTP.

#### **Background Information**

While working on a SAP S/4HANA implementation project, there was a requirement to transfer files generated on the SAP S/4HANA AL11 (DIR\_SAPUSERS) to an external SFTP.
There are some processes that create these files and that need to be transferred to an external SFTP.

#### **Systems and Platforms**

SAP S/4HANA FOUNDATION 2020
SAP BTP Integration Suite -> Cloud Integration -> Cloud Foundry 6.30.17
External SFTP – SSH File Transfer Protocol

#### **Business Requirement**

Periodically check the SAP S/4HANA folders for new files. When a file is available, it needs to be transferred to the external SFTP server through Cloud Integration and then the file is moved to the archive folder.

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog-Diagram.jpg)

High-level process overview

#### **The Challenge with this Integration**

With the latest SAP Cloud Integration features, the new Poll Enrich pattern in combination with the SFTP adapter was made available with the main possibilities as mentioned in this blog:

*(*<https://blogs.sap.com/2021/05/12/cloud-integration-use-poll-enrich-with-sftp-adapter/>*)*

- Enrich the message payload with additional data retrieved from a file on the SFTP server
- Poll from a SFTP server triggered by an external trigger, for example triggered via HTTPS call
- Poll from a SFTP server but want to define the configuration in the SFTP adapter dynamically, for example from a partner directory

With this, it is possible to execute a call to an SFTP retrieving a file in the middle of the iFlow, which was previously only possible at the beginning of the iFlow (using the Sender channel).

The challenge begins when Poll-Enrich always polls only one file. If you need to poll multiple files you need to do this Poll-Enrich call in a loop.

However, when you trigger the Poll-Enrich call in a loop, for the first time the file is read (SAP\_PollEnrichMessageFound = true); but in the second time, the file is not read  (SAP\_PollEnrichMessageFound = false).

The issue is with the SFTP poll-enrich feature and the post-processing in a loop.

To avoid this, the recommendation is to implement the loop in one integration flow and from the loop process call another integration flow via ProcessDirect adapter. The second flow then contains the poll-enrich with SFTP, in this way:

*Main Flow -> Loop Process Call -> ProcessDirect Adapter -> Second Flow with PollEnrich with SFTP*

#### **Solution Implemented**

Two iFLows were created for this solution:

* First iFlow to orchestrate the pooling

* Second iFlow to execute the pooling

##### **First IFlow to orchestrate the pooling**

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog-iFlow-1.jpg)

First IFlow to orchestrate the pooling

1. The possibility to trigger the integration scenario on-demand by HTTPS call

2. The possibility to trigger the integration scenario periodically using a Start Timer

3. The main integration process to:

* + Receive the calls (from block 1 or 2)

  + Set general properties to control the log level

  + Set the SFTP address by external parameters

  + A Groovy script to get the directories to be accessed from a value mapping:![](/legacyfs/online/storage/blog_attachments/2022/10/Blog-VM.jpg)

  + A router to evaluate if has directories or not

  + A value to start the loop

  + Call the process that executes the loop

  + Get the final payload that was combined for each file transferred

  + Log the final payload (execution log) as an attachment in the message (if configured)

      4. A local integration process to transfer all files containing:

* + Get the directory of the current loop stage

  + A router to check if there is directory or not

  + Set the SFTP information like Environment, Folder Source and Folder Destination

  + Define the SFTP environment based on the environment configured

  + Log the beginning of the process

  + Set the loop condition to true

  + Call the process inside the loop

  + Log the ending of the process

      5. A local integration process to call the next iFlow that pool the file

* + Set the payload that will be transferred to the next iFlow

  + Request Reply to call the next iFlow

  + Get the results of the next iFLow

  + A router to evaluate if a file was found or not

  + Log the result of process (If a file was found or not)

##### **Second IFlow to execute the pooling**

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog-iFlow-2.jpg)

Second IFlow to execute the pooling

1. The main integration process to:

* + Explore the payload received from the previously iFlow with the SFTP informations

  + A Poll Enrich to fetch the file

  + A SFTP Sender adapter to fetch the file (any file \*)

  + A router to evaluate if a file was found or not

  + If found, send to the External SFTP

  + Fill the body with the results of the execution

#### **Execution log**

At the end of the process, an execution log will be presented, as following:

![](/legacyfs/online/storage/blog_attachments/2022/10/Blog-Log.jpg)

Execution log

#### **Benefits/Advantages ...