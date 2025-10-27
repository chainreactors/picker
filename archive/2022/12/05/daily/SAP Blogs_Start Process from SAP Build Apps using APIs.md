---
title: Start Process from SAP Build Apps using APIs
url: https://blogs.sap.com/2022/12/04/start-process-from-sap-build-apps-using-apis/
source: SAP Blogs
date: 2022-12-05
fetch_date: 2025-10-04T00:30:56.009803
---

# Start Process from SAP Build Apps using APIs

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Start Process from SAP Build Apps using APIs

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163038&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Start Process from SAP Build Apps using APIs](/t5/technology-blog-posts-by-sap/start-process-from-sap-build-apps-using-apis/ba-p/13565862)

![Archana](https://avatars.profile.sap.com/7/a/id7a4ae4db2971de6ec725bc554a1d48cb58072198309a59073a2843abdcd6dd39_small.jpeg "Archana")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Archana](https://community.sap.com/t5/user/viewprofilepage/user-id/15812)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163038)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163038)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565862)

‎2022 Dec 04
7:28 AM

[22
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163038/tab/all-users "Click here to see who gave kudos to this post.")

15,641

* SAP Managed Tags
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Build Process Automation](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Process%2520Automation/pd-p/73554900100800003832)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)
* [SAP Build Process Automation

  SAP Build](/t5/c-khhcw49343/SAP%2BBuild%2BProcess%2BAutomation/pd-p/73554900100800003832)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (4)

[SAP Build](https://www.sap.com/products/technology-platform/low-code.html) combines Apps, Process Automation and Workzone to empower users, both professional and citizens developers, to build applications, automate processes and design customised dashboards with simple drag-and-drop options, integrate smoothy with SAP and non-SAP systems and collaborate effectively between business and developers.

With SAP Build Apps gaining popularity among the community as an intuitive no-code development tool to design beautiful user interfaces, I have been often asked on how to start the processes from SAP Build Apps, that are built and deployed via new SAP Build Process Automation studio.

In this blog, I will explain you how you can execute a process from custom application using the latest features of:

* API Trigger, Workflow Public APIs in SAP Build Process Automation

* SAP BTP Destination to connect to SAP in SAP Build Apps

Assumptions:

* You already have an application built in SAP Build Apps

* You already have a process designed in SAP Build Process Automation

### **Add API Trigger in process**

API trigger is a new feature in Process Automation through which you can start or trigger the process using public REST APIs from anywhere – be it custom application, integration flows, CAP applications and from any SAP and non-SAP systems where there is provision to call APIs.

You can add API trigger to any existing process (where you might have used Form earlier) or you can create trigger to be added in new process. As there can be only one-way to start the process – form or API trigger – you will have to delete the start form first to be able to add API trigger.

![](/legacyfs/online/storage/blog_attachments/2022/12/image1-2.png)

Now, let us add an API trigger to a new process

![](/legacyfs/online/storage/blog_attachments/2022/12/image2-1.png)

You can give any name to the API trigger.

* Once the API trigger is created, you can click on “empty” canvas and you will see **Inputs** tab from where you can **Configure** the input fields that will be used to start the process.

* When you will create the API trigger an input structure will for formed with the name of the API trigger

![](/legacyfs/online/storage/blog_attachments/2022/12/image3-2.png)

In the configuration dialog, you can choose the input field name of your choice. The type could be some standard type like String, Number etc. Or an already available datatype. If you choose the datatype, then all the fields of the data types will automatically be part of the input fields.

![](/legacyfs/online/storage/blog_attachments/2022/12/image4-1.png)

* You can also choose a List as input if you want to pass multiple input or collection to the process like Sales Order Items etc.

* You can also choose input fields based on your requirements like combination of datatypes or standard fields. For example: in screenshot below I have used *salesOrder* type and then added two more inputs of standard types (*customerName* > String, *orderStatus* > String)![](/legacyfs/online/storage/blog_attachments/2022/12/image5.png)

### **Model the process**

While modelling the process, you can use the fields from the start process context to map the subsequent fields of the process activities.

*Note: the fields from the API trigger will appear under **Process Start Inputs** node*

![](/legacyfs/online/storage/blog_attachments/2022/12/image6.png)

####

### **Update API Trigger**

You can edit, deactivate, or delete the API trigger properties from **Triggers** tab in the respective process builder overview. *Deactivate* means that while the trigger exists in design-time, but you can consume it in runtime. *Delete* will permanently delete the trigger from design-time but for already deployed process the trigger will still exist at runtime. In general, any changes in the trigger will be affective only when the process is released and deployed.

note: All the API triggers that are created in that project will be shown.

![](/legacyfs/online/storage/blog_attachments/2022/12/image7.png)

####

###

### **Release and deploy the process with API trigger**

Once you have finished designing your process, you have to release and deploy the process so that it can consumed via APIs.

* If you go into the deployed view of the process, you can see the API details of how you can call the API Trigger.

  + The API triggers can be called via the public REST API

  + The API are available in [API Business Hub](https://api.sap.com/api/SPA_Workflow_Runtime/resource)

  + The URL shown in screenshot below is the complete API URL where:

    - <https://spa-api-gateway-bpi-eu-prod.cfapps.sap.hana.ondemand.com> : is the host URL and will change depending upon the system you have deployed the process

    - **/workflow/rest/v1/workflow-instances**: is the relative URL to start the workflow and remains static.

  + Method: POST

  + The payload in the screenshot is t...