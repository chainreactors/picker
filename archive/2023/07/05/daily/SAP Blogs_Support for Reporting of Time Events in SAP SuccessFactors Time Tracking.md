---
title: Support for Reporting of Time Events in SAP SuccessFactors Time Tracking
url: https://blogs.sap.com/2023/07/04/support-for-reporting-of-time-events-in-sap-successfactors-time-tracking/
source: SAP Blogs
date: 2023-07-05
fetch_date: 2025-10-04T11:53:37.680207
---

# Support for Reporting of Time Events in SAP SuccessFactors Time Tracking

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Support for Reporting of Time Events in SAP Succes...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50600&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Support for Reporting of Time Events in SAP SuccessFactors Time Tracking](/t5/enterprise-resource-planning-blog-posts-by-sap/support-for-reporting-of-time-events-in-sap-successfactors-time-tracking/ba-p/13551259)

![neethadevaraj](https://avatars.profile.sap.com/0/0/id0047f4487cdf87f671009a84137a655bf82a083b093c70107b967ec13a92dfca_small.jpeg "neethadevaraj")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[neethadevaraj](https://community.sap.com/t5/user/viewprofilepage/user-id/34955)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50600)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50600)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551259)

‎2023 Jul 04
3:26 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50600/tab/all-users "Click here to see who gave kudos to this post.")

7,938

* SAP Managed Tags
* [SAP SuccessFactors Time Tracking](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Time%2520Tracking/pd-p/73555000100800002827)
* [HCM Time Management](https://community.sap.com/t5/c-khhcw49343/HCM%2520Time%2520Management/pd-p/666118459887932219928019980895838)

* [HCM Time Management

  Software Product Function](/t5/c-khhcw49343/HCM%2BTime%2BManagement/pd-p/666118459887932219928019980895838)
* [SAP SuccessFactors Time Tracking

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BTime%2BTracking/pd-p/73555000100800002827)

View products (2)

Hello Time Community,

We are happy to announce that Time Events (punches) are now reportable with 1H 2023 release of SAP SuccessFactors Time Tracking.

The Time Events fields are available and can be created via Story Reporting. Generally, there are additional information like and many more details required to generate the report. The reports will help admins to generate Time Events for the employees with the following filters:

* Date range – daily, bi- weekly, weekly, monthly or quarterly

* Specific country, location, department, cost center, etc.

* Punched in a specific region when location capture is enabled.

* Percentage of employees who punch using terminal, web or mobile (pie chart or bar graph)

Below are some simple steps for creating the report. It uses the basic filter of date range for a month. If you follow the steps mentioned below, you can see the report as shown in the screenshot.

![](/legacyfs/online/storage/blog_attachments/2023/07/Reporting-example.png)

**Steps to create a Time Event Report:**

*Pre-requisites:* Ensure you have access to Report center along with permission to create the new Story.

* Click on the New Button and select the report you want to create as “Story”.

* This takes you to the next section where you can decide to create any kind of report. I selected a Table to get the above report.

* Once you land on the Query Designer that looks the following way

![](/legacyfs/online/storage/blog_attachments/2023/07/Reporting-Center-for-Story.png)

* You will now see Clock In Clock Out object displayed under Available Data section.

* Expand the Clock In Clock Out object to see Time Events. Drag the Time Events to the Query Designer screen. You will see the other entities associated with Time Events.

![](/legacyfs/online/storage/blog_attachments/2023/07/Query-Designer-with-Time-Event.png)

* Clicking on Time Event in the Query Designer will show related tables, columns to be selected, adding filters and delete.

![](/legacyfs/online/storage/blog_attachments/2023/07/Query-Designer-with-options.png)

* Click on the “show related tables” to show three entities – Geo Location, Time Event Type and Basic User Information.

![](/legacyfs/online/storage/blog_attachments/2023/07/Query-Designer-with-three-options-to-add.png)

* Click on the “+” icon on the top of every entity to add the table to extract data for the report.

* I added the “Time Event Type” as this contains the Time Event Type Name like the Clock In for the P10 and Clock Out for say P20.

* Now, click on the select column option to enable columns required for the report.

![](/legacyfs/online/storage/blog_attachments/2023/07/Query-Designer-and-options-to-select-columns.png)

* I enabled the Time Event Type Name columns to display the Clock In and Clock Out.

* Similarly, I also added the Basic User Information and selected columns like Display Name, Manager and Location.

![](/legacyfs/online/storage/blog_attachments/2023/07/Basic-User-Information-with-column-Options.png)

* Basic User Information also has the related tables with Job Information which you can add as well to add details like Supervisor/Manager’s Display Name, Department, Division information.

![](/legacyfs/online/storage/blog_attachments/2023/07/Job-Information-column-options.png)

* Geo Location is also another entity associated with Time Event which contains information of employee’s location of punch details like latitude, longitude, address.

![](/legacyfs/online/storage/blog_attachments/2023/07/Geo-Location-column-options.png)

* The columns related to Time Events are also selected.

![](/legacyfs/online/storage/blog_attachments/2023/07/Time-Event-columns.png)

* Once selected, the structure will look as below and you could try to check the preview by clicking on the “Preview Query”

![](/legacyfs/online/storage/blog_attachments/2023/07/Query-Designer-after-column-selection.png)

* Once you are able to generate the preview, you can click the “Finish” button.

* A prompt to select the Data Source appears which is already filled with “Time Event”. Click on “OK” button.

* It prompts another popup with setting variable of “As of Date for Job Information”. You could decide to set to the current date or a prior date as well. Click on the “OK” button.

* You are now taken to select the object for the story canvas. I have selected “Table” as I require a table layout. Click on the “Table”.

* You are now shown the table and the Builder to make modifications to column headers, the layout on how the table should be displayed, etc.

![](/legacyfs/online/storage/blog_attachments/2023/07/Builder-for-Time-Event.png)

* Select the Cross-tab as the Table Structure to get the table I showed in the beginning. In the Column section, the count is the only column shown. You could delete this row and add the required row by clicking on Add Dimensions button. Select the required columns you want to show in the table. I have selected all except the Time Event Date. I will use this as a filter.

![](/legacyfs/online/storage/blog_attachments/2023/07/Dimension-Selection.png)

* Once, they are selected, the Builder will show with values as below. It is time now to arrange the columns in the necessary order by dragging them using th...