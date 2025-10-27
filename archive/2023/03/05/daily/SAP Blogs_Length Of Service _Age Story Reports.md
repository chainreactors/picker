---
title: Length Of Service /Age Story Reports
url: https://blogs.sap.com/2023/03/04/length-of-service-age-story-reports/
source: SAP Blogs
date: 2023-03-05
fetch_date: 2025-10-04T08:43:45.897237
---

# Length Of Service /Age Story Reports

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by Members](/t5/human-capital-management-blog-posts-by-members/bg-p/hcm-blog-members)
* Length Of Service /Age Story Reports

Human Capital Management Blog Posts by Members

Explore blogs from customers or SAP partners to gain best practices and fresh insights to succeed.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-members/article-id/5081&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Length Of Service /Age Story Reports](/t5/human-capital-management-blog-posts-by-members/length-of-service-age-story-reports/ba-p/13562921)

![former_member543465](https://avatars.profile.sap.com/former_member_small.jpeg "former_member543465")

[former\_member543465](https://community.sap.com/t5/user/viewprofilepage/user-id/543465)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-members&message.id=5081)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-members/article-id/5081)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562921)

‎2023 Mar 04
7:52 AM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-members/message-id/5081/tab/all-users "Click here to see who gave kudos to this post.")

6,918

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP SuccessFactors HCM Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520HCM%2520Suite/pd-p/67838200100800004730)
* [SAP SuccessFactors People Analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520People%2520Analytics/pd-p/73554900100800002745)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP SuccessFactors HCM Suite

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BHCM%2BSuite/pd-p/67838200100800004730)
* [SAP SuccessFactors People Analytics

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPeople%2BAnalytics/pd-p/73554900100800002745)

View products (3)

Story Reports are being the frequent word hearing from the SAP SuccessFactors HXM Suite.

The **Story** type of report in **Report Centre** is part of the People Analytics solution, and it's based on the integration of **SAP SuccessFactors HXM Suite** with **SAP Analytics Cloud**. After you create a story, you can add and edit pages, sections, and elements. You can share your story with others to enable them to use the report you've created. It is a presentation-style report that uses charts, visualizations, text, images, and pictograms to describe data. A story mainly involves building a query, and using the query to create the report.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture1-4.png)

This blog is going to take you through the complete story report creation.

**Requirement:** Story Report on Employee Length of Service & Age should be created

1.Navigate to Report Centre and Select New

2.Choose Story from the available options and click on select.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-4.png)

3.Select a connection here. There are 2 types of connection

1. **SAP SuccessFactors Learning**

2. **SAP SuccessFactors Reporting**

Choose SAP SuccessFactors LMS for LMS related reports and SAP SuccessFactors Reporting for all the other modules data.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-4.png)

4.Now a Query Designer page will be loaded as below.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture4-2.png)

5.Choose the entities as per the requirement.

1. As we have to calculate age of employee, drag and drop **Personal Information ---->Biographical Information** entity from Available data

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-4.png)

  2.As we have to calculate Length of Service for employee, drag and drop **Employment --->Job           Information** entity from Available data.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-3.png)

6.Select the fields which has to be shown on the story report by click on the **Add Columns**

As per the above select columns option in **Biographical Information** and select **Date of Birth & Person ID**. In similar way select columns in **Job Information** **Date of Joining /Start Date.**

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-2.png)

7.Select **Preview Query** to see the selected columns for the story report.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-2.png)

System will request for the variables like As of Date for which data has to be reported.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-2.png)

Preview Query looks as below.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-1.png)

Now create a **calculated column** for Length of service and Age.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-2.png)

Select **Calculated Column** and Provide an ID and description. Now enter the condition as below for Length of Service.

***IF (***

***ISNULL ([Employment#Job Information#Last Working Date]),***

***(DAYS\_BETWEEN ([Employment#Job Information#Joining Date],CURRENTDATE())/365) ,***

***(DAYS\_BETWEEN ([Employment#Job Information#Joining Date],[Employment#Job Information#Last Working Date])/365) )***

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture12-2.png)

Again, Select Calculated Column and Provide an ID and description. Now enter the condition as below for Age.

***DAYS\_BETWEEN([Person#Biographical Information#Date of Birth],CURRENTDATE())/365***

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture13-2.png)

*Now Click OK and Finish.*

Give a name to the Data Source and set the **As of Date** as per your requirement to report the data.

Now Select which object you wanted to report the story on.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture14-1.png)

As per the requirement here we are choosing **Table**. And we have to add the columns on to the design.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture15-2.png)

Selected columns will appear on the story report as per the calculation.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture16-1.png)

Now Click on **SAVE**. Story Report Successfully created.

**Current Limitations for Stories in People Analytics**

* The schemas for Recruiting Marketing, Recruiting Posting, and Onboarding 1.0 aren't supported. However, the schema for Onboarding, which replaces Onboarding 1.0, is supported.

* Currently, the Recruiting schema for Stories in People Analytics doesn't support the Status Audit Trail table for Application Status.

* The option to configure timestamps in the time zone of the user running a Story isn't available.

* The JDM (Job Description Manager) schema isn't available.

* Objects (other than Employee Central and Benefits) that include custom fields configured as generic objects or foundation objects (type of reference object under DataType) aren't currently supported. Employee Central and Benefits objects support custom fields configured as generic objects or foundation objects.

* Quickcard isn't suppor...