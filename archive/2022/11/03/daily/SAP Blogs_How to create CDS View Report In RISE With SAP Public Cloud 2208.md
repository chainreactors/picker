---
title: How to create CDS View Report In RISE With SAP Public Cloud 2208
url: https://blogs.sap.com/2022/11/02/how-to-create-cds-view-report-in-rise-with-sap-public-cloud-2208/
source: SAP Blogs
date: 2022-11-03
fetch_date: 2025-10-03T21:38:26.304477
---

# How to create CDS View Report In RISE With SAP Public Cloud 2208

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to create CDS View Report In RISE With SAP Pub...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67102&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to create CDS View Report In RISE With SAP Public Cloud 2208](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-create-cds-view-report-in-rise-with-sap-public-cloud-2208/ba-p/13551403)

![lakshminaraya95](https://avatars.profile.sap.com/a/f/idaf9c50b658a43a0f053919f0570fdd52525ae9ebe77344580d167b09ffbada20_small.jpeg "lakshminaraya95")

[lakshminaraya95](https://community.sap.com/t5/user/viewprofilepage/user-id/42399)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67102)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67102)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551403)

‎2022 Nov 02
7:06 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67102/tab/all-users "Click here to see who gave kudos to this post.")

11,412

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

View products (2)

### Hello All,

### In this Blog we are going to see How to create CDS view In Rise with SAP Public Cloud 2208

## Introduction- SAP Create Custom CDS View

SAP Create Custom CDS View can be used to generate the user’s own data access, in case they require access to data in the ERP system which is either not available in the standard apps or a report is needed to give more visibility to stakeholders or to create custom application that reads data from SAP.

Generally, the data of an application is spread across numerous database tables. SAP create custom CDS view that permits you to model the data access without altering underlying database tables. You can reorganize the table fields and define the metadata of the fields that fit into one object but then are set in different databases. Follow these steps when you are ready to create an app through the SAP create Custom CDS view.

Below is the summary of the steps we would be following

1. Creating CDS View

2. Specify Join condition

Check the logs and publish the CDS view which would be ready to use.

## ***“Core Data Services to build design-time data-persistence models”***

**STEP1:**

Move to the tile as “Custom CDS View”

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-1.png)

**STEP2:**

Click on Create and fill in the below detail. Note only when the Scenario is Analytical Dimension you can use the CDS view to create an analytical Query from it.

![](/legacyfs/online/storage/blog_attachments/2022/10/9-19.png)

Enter the detail name of which you want to customise the data source

* Label

* Name

* Scenario fields are mandatory then go to create option

![](/legacyfs/online/storage/blog_attachments/2022/10/9-18.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/2-34.png)

**STEP3:**

The screen will be display then Add the **Primary Data Source**

![](/legacyfs/online/storage/blog_attachments/2022/10/3-28.png)

**STEP4:**

Select the data Source

![](/legacyfs/online/storage/blog_attachments/2022/10/4-22.png)

Screen will be displayed like this after selecting the data source, Next move to **Associated Data Source.**

![](/legacyfs/online/storage/blog_attachments/2022/10/12-16.png)

Add Join Condition

![](/legacyfs/online/storage/blog_attachments/2022/10/13-12.png)

**STEP5:**

Add Join Condition

Select Cardinality and click on Add to choose the field for association in join condition

![](/legacyfs/online/storage/blog_attachments/2022/10/7-19.png)

**STEP6:**

Go to Tab Elements to select the field you require

![](/legacyfs/online/storage/blog_attachments/2022/10/11-13.png)

Select on the field you want from the 3 data sources

![](/legacyfs/online/storage/blog_attachments/2022/10/14-16.png)

Below are the selected field

![](/legacyfs/online/storage/blog_attachments/2022/10/16-14.png)

If you need some filter option as a then add the filter.

**STEP7:**

**All are done, then click the “Check” and” Preview” button**

![](/legacyfs/online/storage/blog_attachments/2022/10/17-13.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/19-10.png)

**STEP8:**

**After Preview you can Publish it.**

![](/legacyfs/online/storage/blog_attachments/2022/10/20-11.png)

## Conclusion – How To Create Custom CDS View

In this article, we talked about the steps used to create an app with the help of the Custom CDS View. Which in general, are intended to be consumed by a UI, analytics, or other systems.

### **Thanks for reading this blog…**

Hope this blog will be useful. If you enjoyed this blog post please give it a like! If you have questions,

feel free to comment.

If you would like to keep up on the latest updates regarding SAP S4/HANA cloud, Kindly follow me

**Thanks & Regards,**

**Lakshmi Narayanan K**

Kindly provide the feedback

**References:**

In this web site you can see the CDS view data

<https://api.sap.com/products/SAPS4HANACloud/cdsviews/cdsviews>

To learn more about ***SAP S/4HANA CDS views***

Check this blog post ABAP Core Data Services – Introduction (ABAP CDS view)

<https://blogs.sap.com/2017/09/09/abap-core-data-services-introduction-abap-cds-view/>

* [cdsviews](/t5/tag/cdsviews/tg-p/board-id/erp-blog-members)

8 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fhow-to-create-cds-view-report-in-rise-with-sap-public-cloud-2208%2Fba-p%2F13551403%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [How to trigger HU label print in S/4HANA Cloud Public Edition (API\_FORM\_PRINT\_SRV not available)](/t5/enterprise-resource-planning-q-a/how-to-trigger-hu-label-print-in-s-4hana-cloud-public-edition-api-form/qaq-p/14233989)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  7 hours ago
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Ent...