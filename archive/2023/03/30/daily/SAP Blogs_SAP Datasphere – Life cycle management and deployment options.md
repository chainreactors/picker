---
title: SAP Datasphere – Life cycle management and deployment options
url: https://blogs.sap.com/2023/03/29/sap-datasphere-life-cycle-management-and-deployment-options/
source: SAP Blogs
date: 2023-03-30
fetch_date: 2025-10-04T11:06:33.519699
---

# SAP Datasphere – Life cycle management and deployment options

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Datasphere - Life cycle management and deploym...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160115&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere - Life cycle management and deployment options](/t5/technology-blog-posts-by-sap/sap-datasphere-life-cycle-management-and-deployment-options/ba-p/13556681)

![prasanthi_k](https://avatars.profile.sap.com/8/d/id8df5ad3afa8cda9305d446cc71e3b1b6460a56628bdf8cd8b6858ddf7a607f94_small.jpeg "prasanthi_k")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[prasanthi\_k](https://community.sap.com/t5/user/viewprofilepage/user-id/190878)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160115)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160115)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556681)

‎2023 Mar 30
12:32 AM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160115/tab/all-users "Click here to see who gave kudos to this post.")

10,702

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

**Introduction**

Transporting of Content. aka. Lifecycle management in SAP Datasphere is a bit different than in traditional on-premises systems because SAP is responsible for software, hardware, and infrastructure update.

# **Deployment Options**

**Single Tenant**

A landscape with a single system is appropriate for very small deployments, or for the initial phase of your SAP Datasphere. This landscape is not supported for reliable lifecycle management.

However, you can store test and production content in different spaces.

Memory and DP Agent consumption and configuration are to be high observant aspects from a performance view.

**Multiple Tenants**

Add at least two SAP Datasphere tenants to your landscape. You can use one to develop and test the content, and other as production environment as source of truth.

Here are some of the advantages of such a scenario:

The test content is fully separate from the production data and content.

Improved performance, as there is no need to use production data sources for testing and development tasks. One may want to add more non-productive systems so that the SAP Datasphere landscape matches the structure of the source systems.

Lifecycle management is easier. One can use Import and Export features to promote content, and the production system contains fully tested content.

# **Use Case scenarios for content transports**

## **1. Transport within Single Tenant**

### **a. Same Space but with a different connection**

Export the content to a CSN file which has connection pointing to development connection (example: ECD\_ABAP).

**![](/legacyfs/online/storage/blog_attachments/2023/03/Connection.png)**

Connection pointing to development system

1. After exporting the JSON file, change the connectionID to ECC\_ABAP(connection pointing to Quality)

**![](/legacyfs/online/storage/blog_attachments/2023/03/Picture2-33.png)**

Connection name change

Import the JSON file, connection name will be changed in the Dataflow.

### **b.  Different Space with different connection**

Follow the steps of scenario (a) and import the CSN file to a different space of the same tenant.

### **c. Different Space with same connection**

It is a recommended practice to maintain the same connection name across to have smoother transition of the content to forward landscapes or tenants

**Step 1:** select to open an object that needs to be exported from the source  space -> Data Builder option to the target space. For example, Data Flow –

**![](/legacyfs/online/storage/blog_attachments/2023/03/Picture3-26.png)**

Export CSN/JSON option

The file will be exported to the downloads of the local desktop as CSN/JSON format provided there are no issues with the object.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture4-20.png)

**Step 2**: Import the file into the target space as below -

Select the space -> Data Builder section or menu where the object needs to be imported

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture5-22.png)

Select the option to import the CSN/JSON file and select from the downloads folder

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture6-20.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture7-21.png)

The file gets imported and as next step open the object and deploy for the successful transport.

Note – Always look for the existence of the dependencies as active or deployed  while doing so.

### **d. Share the Content between the Spaces/Cross Space Sharing**

This allows us to use data from another spaces (Functional areas or teams) without replicating the data physically in both spaces. To show this functionality is working we are going to use an example of sales data.

Step1: Select and open the object from the data builder or business builder and click share icon as highlighted below

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture8-18.png)

Select or choose the target the space name

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture9-15.png)

Go To the target space -> data builder and looks for the section shared objects

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture10-11.png)

Now this can be consumed into any view or dataset to consume for further actions.

## **2. Transport across the Tenants (Multiple)**

### **a. Content with the same connection**

When moving the content across the tenants use the SAP Datasphere option of Export and Import for the Content management along the different landscapes

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture11-14.png)

Create a package and choose the objects that needs to be exported to the target tenant.  Post selection of the objects the below will be the dialogue window that appears.

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture14-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture13-10.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture15-8.png)

Go to the target tenant and Import the package

![](/legacyfs/online/storage/blog_attachments/2023/03/Picture16-7.png)

### **b. Content with Different Connection**

It is recommended to always have the same connection as source in the target to avoid any disrupts to content working and functionality therefore avoid corruption.

As any in a case of this as 1%, may be an option of CSN/JSON file format with connection string changes could be foreseen as a workaround. But this should be tried and tested further based of use case.

###### \*\* *Content provided based on real time project experience.*

**Summary**

There are multiples ways to Transport Datasphere Objects and Connection, w...