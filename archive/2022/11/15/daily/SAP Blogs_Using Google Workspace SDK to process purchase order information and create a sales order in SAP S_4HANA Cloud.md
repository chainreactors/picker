---
title: Using Google Workspace SDK to process purchase order information and create a sales order in SAP S/4HANA Cloud
url: https://blogs.sap.com/2022/11/14/using-google-workspace-sdk-to-process-purchase-order-information-and-create-a-sales-order-in-sap-s-4hana-cloud/
source: SAP Blogs
date: 2022-11-15
fetch_date: 2025-10-03T22:45:01.945788
---

# Using Google Workspace SDK to process purchase order information and create a sales order in SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Using Google Workspace SDK to process purchase ord...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163654&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Google Workspace SDK to process purchase order information and create a sales order in SAP S/4HANA Cloud](/t5/technology-blog-posts-by-sap/using-google-workspace-sdk-to-process-purchase-order-information-and-create/ba-p/13567627)

![sankalpmalhotra](https://avatars.profile.sap.com/e/3/ide3efccb9100b9acca13f5f55da4046964d9b07a9a2f3a603cc683bb7ee2a7ebd_small.jpeg "sankalpmalhotra")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[sankalpmalhotra](https://community.sap.com/t5/user/viewprofilepage/user-id/43469)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163654)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163654)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567627)

‎2022 Nov 14
10:32 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163654/tab/all-users "Click here to see who gave kudos to this post.")

1,763

* SAP Managed Tags
* [SAP Intelligent Robotic Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Intelligent%2520Robotic%2520Process%2520Automation/pd-p/73554900100800002142)
* [SAP Cloud Platform, industry edition, client libraries](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Platform%252C%2520industry%2520edition%252C%2520client%2520libraries/pd-p/73555000100800000218)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Cloud Platform, industry edition, client libraries

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BPlatform%25252C%2Bindustry%2Bedition%25252C%2Bclient%2Blibraries/pd-p/73555000100800000218)
* [SAP Intelligent Robotic Process Automation

  Software Product](/t5/c-khhcw49343/SAP%2BIntelligent%2BRobotic%2BProcess%2BAutomation/pd-p/73554900100800002142)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)

View products (5)

**Use Case: Using Google Workspace SDK to process purchase order information and create a sales order in SAP S/4HANA Cloud.**

**Prelude:**

SAP Build Process Automation enables automation of google workspace products such as Gmail, Google drive, Google calendar, Google sheet, Google slides, Google documents and Google cloud storage. In addition to that it has the capabilities to automate ML based services such as, Google document AI and vision AI. The below SDKs can be used in automations to automate Google services:

1. Google Authorization SDK

2. Google Workspace SDK

3. Google Cloud Storage SDK

4. Google Document AI SDK

5. Google Vision AI SDK

In this blog I will use Google Authorization SDK and Google Workspace SDK to talk about how you can automate google applications such as google drive, Gmail and google sheet. I am using Sales Order creation use case in SAP S/4HANA System to explain these features.

**Detailed Use case for our automation:**

* Uses Google Workspace SDK to Search GMAIL account for Purchase Order Emails

* Uses Google Workspace SDK to Read the email and download the attachments

* Use SAP DOX service to read PDF and create an output schema

* Uses Google Workspace SDK to Fill values from PDF into a pre-created Google Sheet

* Uses Google Workspace SDK to Read values from Google Sheets to create Sales Order

* Uses Pre-built SAP Sales Order Creation Bot to create Sales Order using the above values

* Uses Google Workspace SDK to Reply to the original email with the created Sales Order ID

**Recommended SDK's version:** 1.31.49

**Pre-requisites:**

* A Purchase Order in PDF Format

* An Email in a GMAIL Account containing a PO (Purchase Orders) in the above format

* A Sales Order Input template in Google Sheets

* Sales Order Creation Automation that takes input from the above template

I have a prebuilt sales order automation bot and I am using the same. The bot expects a Data structure as shown below and gives Standard Order id as an output.

![](/legacyfs/online/storage/blog_attachments/2022/11/1a-1.png)

Sample expected Input by the prebuilt Sales Order Automation

**Step – 1:** Create a new Document Template as shown in the figure below and define the schema for the same document template to be used in the subsequent activities

![](/legacyfs/online/storage/blog_attachments/2022/11/1b-2.png)

Sample Purchase Order document Template

**Step – 2:** I will use a pre-defined template, for which I am populating the data read from purchase order and upload this to Google Drive for the BOT to use.

![](/legacyfs/online/storage/blog_attachments/2022/11/1c-1.png)

Sample sales order input template

**Now, we are ready with the pre-requisite steps. Let us now start building our Automation.**

**Step – 3:** Create a new automation to read Purchase Order data from Google Products and Add Google Packages as dependencies in this Automation.

![](/legacyfs/online/storage/blog_attachments/2022/11/1e.png)

New Automation

Now Select Dependencies tab and click on Add Dependency, then click on Add a Business Process project Dependency and from the drop down, select Google Authorization SDK & Google Workspace SDK.

**Step – 4:** Add following steps into the automation to Search Purchase Order Email and extract data from the attached PDF.

Our automation will search for an email in the users GMAIL account based on query input and then read the email contents. It will download the attachments to a local File System and then extract Data from the PDF Attachment to fill into Sales Order Template.

Then, the Bot will use the data from the template to create Sales order using our pre-built Sales order Automation

* Add **Google Authorization** activity with proper scopes. For Google Sheets, the Google Drive scope is sufficient. [[click here to refer Authorization Blog for more details]](https://blogs.sap.com/2022/11/14/authorizing-sap-process-automation-to-automate-google-applications/)![](/legacyfs/online/storage/blog_attachments/2022/11/1f.png)

* Add **Search Email** activity to search for Purchase Order Email. This activity uses GMAIL API to search for emails based on the search filters as specified in the search query Parameters. You can optionally also specify if the search should include spam and trash folders or not. Output of this activity is a l...