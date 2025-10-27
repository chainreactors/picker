---
title: ABAP RAP(RESTful Application Programming) Model, Part- 1 –> Managed scenario
url: https://blogs.sap.com/2023/01/04/abap-raprestful-application-programming-model-part-1-managed-scenario/
source: SAP Blogs
date: 2023-01-05
fetch_date: 2025-10-04T03:04:02.354351
---

# ABAP RAP(RESTful Application Programming) Model, Part- 1 –> Managed scenario

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* ABAP RAP(RESTful Application Programming) Model, P...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67933&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [ABAP RAP(RESTful Application Programming) Model, Part- 1 --> Managed scenario](/t5/enterprise-resource-planning-blog-posts-by-members/abap-rap-restful-application-programming-model-part-1-gt-managed-scenario/ba-p/13560740)

![rajat_verma3](https://avatars.profile.sap.com/e/d/ideda624db180df74d8c4a0fdd2e0aaab52599c65b5fad017fefa3a462c4b1219b_small.jpeg "rajat_verma3")

[rajat\_verma3](https://community.sap.com/t5/user/viewprofilepage/user-id/545641)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67933)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67933)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560740)

‎2023 Jan 04
7:36 PM

[21
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67933/tab/all-users "Click here to see who gave kudos to this post.")

100,593

* SAP Managed Tags
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [ABAP RESTful Application Programming Model](https://community.sap.com/t5/c-khhcw49343/ABAP%2520RESTful%2520Application%2520Programming%2520Model/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP RESTful Application Programming Model

  Software Product Function](/t5/c-khhcw49343/ABAP%2BRESTful%2BApplication%2BProgramming%2BModel/pd-p/7e44126e-7b27-471d-a379-df205a12b1ff)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

In this blog, you will learn how to create a simple RAP model. In this example, we will create a table, CDS view entity, Metadata extension, Behavior definition, Service definition, Service Binding.

We will create below application for creation of Driver detail with the help of FIORI element.

![](/legacyfs/online/storage/blog_attachments/2022/12/Image1-10.png)

**Step 1 -->** Create table - ZRV\_RAP\_DRIVER

Right click on the package --> New --> Other ABAP Repository Object --> Select Database Table and enter the the name of the table.

![](/legacyfs/online/storage/blog_attachments/2022/12/Image2-10.png)

Here is the code snippet.

![](/legacyfs/online/storage/blog_attachments/2022/12/Image3-10.png)

**Step 2 -->** Create Root CDS Entity ZI\_RAP\_DRIVER

Right click on the package --> New --> Other ABAP Repository Object --> Select Data Definition and enter the the name of Root CDS Entity --> Select Define Root View Entity.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture4-24.png)

Here is the code snippet.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture5-19.png)

**Step 3 -->** Create a Metadata Extension

Right click on root view entity --> Select New Metadata Extension --> Enter the the name of Metadata Extension.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture6-17.png)

Here we annotate the CDS Entity and fields we add screen position, set selection field etc.

Here is the code snippet.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture7-17.png)

**Step 4 -->** Create a Behavior Definition

Right click on root view entity --> Select New Behavior Definition.

All detail will be already filled, just click next.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture8-17.png)

Here is the code snippet,

**Note -->** For managed scenario we don’t need a class. Create, Delete, Update functionality will work as a standard(It is required to handle for non-standard action, features, determination, validations and so on that will be covered in coming Part-2)

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture9-13.png)

**Step 5 -->** Create a Service Definition

Right click on root view entity --> Select New Service Definition

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture10-12.png)

Here is the code snippet.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture11-13.png)

**Step 6 -->** Create Service Binding

Right click on service definition --> Select New Service Binding.

Here we need to choose Binding type OData V2-UI or OData V4-UI, for now we have chosen V2-UI.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture12-12.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture13-9.png)

Now publish the Service by clicking on Publish button.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture14-10.png)

Our RAP model is completed, now test the application.

**Test Application -->**

Select Service and click on preview button.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture15-7.png)

**Click on Go -->** To see the data, if already available in system.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture16-8.png)

**Click on CREATE -->** Here we can create new driver.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture17-8.png)

**UPDATE / DELETE -->** To update or delete the record.

Select the entry from the list.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture18-6.png)

These buttons appear on the top right corner.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture19-6.png)

**Conclusion -->** After reading this blog you will be able to create simple RAP model application.

Give it a try and let me know in the comments if you need any help/support.

Please feel free to suggest if any correction is needed ![:slightly_smiling_face:](/html/@5D2D4274E851E17FD6B6AA8F470AA6B3/emoticons/1f642.png ":slightly_smiling_face:")

* [abaponhana](/t5/tag/abaponhana/tg-p/board-id/erp-blog-members)
* [RAP](/t5/tag/RAP/tg-p/board-id/erp-blog-members)
* [RAPMODEL](/t5/tag/RAPMODEL/tg-p/board-id/erp-blog-members)
* [S4HANA](/t5/tag/S4HANA/tg-p/board-id/erp-blog-members)
* [SAPRAP](/t5/tag/SAPRAP/tg-p/board-id/erp-blog-members)

10 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fabap-rap-restful-application-programming-model-part-1-gt-managed-scenario%2Fba-p%2F13560740%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-...