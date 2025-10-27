---
title: Reset a variable in CVS in B2 cluster using a custom function to stop CVS overflow dump
url: https://blogs.sap.com/2023/01/03/reset-a-variable-in-cvs-in-b2-cluster-using-a-custom-function-to-stop-cvs-overflow-dump/
source: SAP Blogs
date: 2023-01-04
fetch_date: 2025-10-04T02:59:18.300411
---

# Reset a variable in CVS in B2 cluster using a custom function to stop CVS overflow dump

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Reset a variable in CVS in B2 cluster using a cust...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67956&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Reset a variable in CVS in B2 cluster using a custom function to stop CVS overflow dump](/t5/enterprise-resource-planning-blog-posts-by-members/reset-a-variable-in-cvs-in-b2-cluster-using-a-custom-function-to-stop-cvs/ba-p/13560953)

![jeet_bhattacharjee](https://avatars.profile.sap.com/0/2/id021c46648353d2df5a44a22f348221ce9ccda9832d4373207121c8a8d68e182c_small.jpeg "jeet_bhattacharjee")

[jeet\_bhattacharjee](https://community.sap.com/t5/user/viewprofilepage/user-id/610252)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67956)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67956)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560953)

‎2023 Jan 03
8:27 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67956/tab/all-users "Click here to see who gave kudos to this post.")

1,500

* SAP Managed Tags
* [SAP Payroll and Time Change Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Payroll%2520and%2520Time%2520Change%2520Management/pd-p/01200615320800000695)
* [HCM Time Management](https://community.sap.com/t5/c-khhcw49343/HCM%2520Time%2520Management/pd-p/666118459887932219928019980895838)

* [SAP Payroll and Time Change Management

  SAP Payroll and Time Change Management](/t5/c-khhcw49343/SAP%2BPayroll%2Band%2BTime%2BChange%2BManagement/pd-p/01200615320800000695)
* [HCM Time Management

  Software Product Function](/t5/c-khhcw49343/HCM%2BTime%2BManagement/pd-p/666118459887932219928019980895838)

View products (2)

**Introduction**

With more and more customers opting for cloud based solutions like SuccessFactors, customization skills on Time Evaluation engine (RPTIME00) in SAP on-premise solution is unfortunately becoming a dying art. But still there are few, who are not yet ready to move out of the on-premise solution. It could be because of number of factors due to which these organizations feel its in their best interest to continue with the on-premise solution rather than spending on migrating to a new HCM solution. I personally believe that the time evaluation driver built by SAP for its on-premise solution is still one of the most robust and configurable time management solution in the ERP domain. But, due to the latest shift in technology and customer focus towards cloud based solutions, it has brought us to a situation, where the consultants supporting customers still continuing with on-premise solution, may come across new or something out of the ordinary requirement, where they may not get enough support from the SCN discussions or other SAP content repositories or forums.

In my small career of working extensively with SAP on-premise time management solution for more than 4 years now, I have come across situations such as above and thought of documenting the solutions I implemented, so it can help another fellow consultant in getting the solution but only much faster than me.

I am going to start with something, which recently had me scampering through SAP forums. I wanted to see if any standard solution was available but ultimately had to resort to building a custom time function to solve this.

**Target****audiences**

This blog can be helpful for SAP HCM and time management functional consultants, who are facing the same error which is described below in details. Also this blog has been written based on assumption that reader is versed with writing custom functions in SAP HCM and this should not be treated as a tutorial for the same.

**Business Requirement**

To setup auto progression (payscale reclassification) based upon duration (time worked in payscale) and service hours (hours worked in payscale). For  employees in an award/agreement (identified by Payscale type and Payscale Area by my customer) Full time employees are eligible to get auto progression once they complete 12 months on a payscale, whereas Part time and casual employees need to complete YYYY hours worked along with completing 12 months on payscale to be eligible.

**High level Solution details**

I am going to write a separate blog on how this requirement was configured as I found the SAP help documentation on service hours based progression is not detailed enough for me to be able to adopt it into a configuration solution. The grouping configuration (ESG for CAP) for my customer did not differentiate based on employee being Full Time, Part Time or Casual.

The solution implemented on a high level is as follows:

Update the variable ITIG in table VS with hours worked in payscale (from the date employee first moved to this payscale classification, because that is how the standard payscale reclassification works) for Part time and Casual employees, once they had completed 12 months on payscale. For Full time employees once they complete 12 months on payscale update ITIG as YYYY each day till reclassification happens.

**Technical Issue**

It was key for above solution that each day VS table is updated with hours worked in payscale (or hard coded hours for Full time) after employee completed 12 months on payscale. In cases, where reclassification is not done for a significant period of time after employee is eligible, the VS variable ITIG keeps on cumulating each day into CVS and would extrapolate into a large value ultimately leading to system dump 'COLLECT\_OVERFLOW\_TYPE\_P' when running time evaluation.

![](/legacyfs/online/storage/blog_attachments/2023/01/CVS-OVERFLOW-3.jpg)

CVS Overflow System Dump

We needed the service hour progression in VS table and not in CVS table, but CUMBT being a standard function always cumulates VS variable into CVS.

**Reset CVS using custom function**

I could not find any standard delivered function or operation to reset CVS. ADDVS with a negative offset is not an option, as we needed to retain the service hours in payscale day-wise value in VS. So, I created a custom function with code below to reset CVS-ITIG once it crosses YYYY hrs. Since our reclassification configuration would trigger for anything equal to or above YYYY hours, resetting CVS-ITIG to YYYY did not impact our solution and stopped the overflow system dump.

**Custom Function Z\_ABC**

Create Function Z\_ABC like time management function (eligible for all country assignment), with no input / output parameters, from transaction PE04.

![](/legacyfs/online/storage/blog_attachments/2023/01/Function-Z_ABC-3.jpg)

Modify RPTMOZ00 include to insert subroutine FUZ\_ABC (mapped to custom function) from transaction SE38.

![](/legacyfs/online/storage/blog_attachments/2023/01/FUZ_ABC-routine.jpg)

Insert newly created custom function in time management schema, just after function CUMBT is called.

![](/legacyfs/online/storage/blog_attachments/2023/01/Call-Z_ABC-in-Time-schema-after-CUMBT-1.jpg)

You may encapsulate the custom f...