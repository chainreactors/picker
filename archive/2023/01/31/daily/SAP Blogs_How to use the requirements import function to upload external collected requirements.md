---
title: How to use the requirements import function to upload external collected requirements
url: https://blogs.sap.com/2023/01/30/how-to-use-the-requirements-import-function-to-upload-external-collected-requirements/
source: SAP Blogs
date: 2023-01-31
fetch_date: 2025-10-04T05:13:56.493160
---

# How to use the requirements import function to upload external collected requirements

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* How to use the requirements import function to upl...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158144&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to use the requirements import function to upload external collected requirements](/t5/technology-blog-posts-by-sap/how-to-use-the-requirements-import-function-to-upload-external-collected/ba-p/13551140)

![anna_gemeiner](https://avatars.profile.sap.com/0/8/id08acb8ae27abef589a76093b5c4683309d2ef4c9059613a9b45a7e9e8cfa1559_small.jpeg "anna_gemeiner")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[anna\_gemeiner](https://community.sap.com/t5/user/viewprofilepage/user-id/122035)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158144)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158144)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551140)

‎2023 Jan 30
8:20 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158144/tab/all-users "Click here to see who gave kudos to this post.")

1,381

* SAP Managed Tags
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

View products (1)

I would like to show you, how external collected requirements can be uploaded into SAP Focused Build by using the requirements import function.

This function was designed to bring requirements from one system into another. How this use case works you can find in this blogpost: [Requirement Import in Focused Build for SAP Solution Manager](https://blogs.sap.com/2020/06/11/requirement-import-in-focused-build-for-sap-solution-manager/)

But sometimes we face the situation, that especially in the beginning of projects, a lot of tasks need to run in parallel to meet the expected timelines. So it can happen that the system set up and the collection of the requirements need to run in parallel.
And therefore a opportunity to upload a bunch of requirements into the SAP Solution Manager Focused Build is needed. This can be realised by the requirements import function, but there are some guidelines to follow.

First of all the mandatory SAP Focused Build set up is done. A solution is created and the process documentation is also entered into solution documentation.

Let's assume the following scenario: We got provided by the customer with an excel sheet that contain their requirements. One per line with the following columns:

* Titel

* Description

* Name of the owner

* Process Name

* Priority

* Classification (Fit, Gap, WRICEF, Non-Functional)

So first of all starting with the structure and input data.

### 1.) Downloading the excel with the requirements structure

In the Requirements Management App via the function "export to spreadsheet" an excel file can be downloaded even if there are no requirements. Within this excel you will receive the structure you need for the upload and don't worry - it is not necessary to fill every column!

![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.08.24.png)

### 2.) Download the solution documentation structure (optional)

Prerequisite for this step is an existing solution documentation with at least processes. Within the upload SAP Solution Manager is not able to map the requirement to the respective process just by the process name. Therefore the technical ID is needed.

1. Open Solution Documentation

2. Change to List view
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.11.38.png)

3. Ensure that the whole Solution is shown in the list and download the .txt file
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.15.30.png)

4. Open the .txt
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.19.16.png)

5. Copy the header into your excel file in a new spread
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.19.16-copy.png)
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.21.53.png)

6. Copy the data into the excel table
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.22.43.png)
   ![](/legacyfs/online/storage/blog_attachments/2023/01/Screenshot-2023-01-24-at-14.24.06.png)

### 3.) Download Business Partner numbers

Prerequisite for this step are existing users including corresponding business partner numbers in the SAP Solution Manger. All fields like owner or business process expert referencing in the backend to business partner numbers and not names. Therefore you need the business partner number for the upload for the fields like owner or business process expert.

The whole list of names and their business partner numbers can be downloaded from transaction BP.

With these 3 steps the structure and input data is set.

The final steps are bringing all together.

### 4.) Fill in the column Title and column Description based on the customer provided data

Title and description are normally easy to fill into the upload structure. It is important to check, if there tab stops or line breaks especially in the description text because they will cause failure when uploading. One line will be translated into one requirement in the system.

### 5.) Fill the column Priority

This column is filled out with numeric values from 1 to 4 to reflect the priority.

### 6.) Fill the column Owner with the name

Based on the name in this column, I use excel formulas to map the corresponding business partner number in the column "Owner BP Number" based on the input data we dowloaded earlier.

### 7.) Fill the column Branch

The branch the requirements should be imported to, is the Design branch. The value to enter for all requirements is "Design".

### 8.) Fill the column Solution

In this column the name of your solution needs to be entered.

### 9.) Fill the column Element ID

For this column I use also a formula that maps the process name given by the customer to the input data downloaded from the solution documentation. You need to find the downloaded solution documentation list the line item for the process the requirement is related to. From this line item the value of the column "OCC\_ID" needs to be entered into the upload excel structure in the column "Element ID".
This will create the process reference of the requirement when uploading.

### 10.) Fill column Owner BP Number

I look up the BP number based on the name in the downloaded business partner list and transferring the value to this column.

### 11.) Fill the column Priority ID

These are the same numeric values than in the column Priority.

### 12.) Fill the last three columns ClassifAttributes - Compo...