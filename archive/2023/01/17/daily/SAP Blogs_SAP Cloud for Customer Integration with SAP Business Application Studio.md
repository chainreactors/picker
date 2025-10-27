---
title: SAP Cloud for Customer Integration with SAP Business Application Studio
url: https://blogs.sap.com/2023/01/16/sap-cloud-for-customer-integration-with-sap-business-application-studio/
source: SAP Blogs
date: 2023-01-17
fetch_date: 2025-10-04T04:02:50.377351
---

# SAP Cloud for Customer Integration with SAP Business Application Studio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Cloud for Customer Integration with SAP Busine...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/160850&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud for Customer Integration with SAP Business Application Studio](/t5/technology-blog-posts-by-sap/sap-cloud-for-customer-integration-with-sap-business-application-studio/ba-p/13558760)

![yuval_morad](https://avatars.profile.sap.com/3/a/id3a4becc097f6141fc9ca08930cbb8e84f7b8e092d41aa24ad7f102f9bce65553_small.jpeg "yuval_morad")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[yuval\_morad](https://community.sap.com/t5/user/viewprofilepage/user-id/205212)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=160850)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/160850)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558760)

‎2023 Jan 16
11:57 AM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/160850/tab/all-users "Click here to see who gave kudos to this post.")

4,629

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Cloud for Customer core applications](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520for%2520Customer%2520core%2520applications/pd-p/67837800100800004276)
* [C4C Extensibility](https://community.sap.com/t5/c-khhcw49343/C4C%2520Extensibility/pd-p/522899869556788325823974243317861)
* [C4C Service](https://community.sap.com/t5/c-khhcw49343/C4C%2520Service/pd-p/569449780209093647095570245113309)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [C4C Service

  Software Product Function](/t5/c-khhcw49343/C4C%2BService/pd-p/569449780209093647095570245113309)
* [C4C Extensibility

  Software Product Function](/t5/c-khhcw49343/C4C%2BExtensibility/pd-p/522899869556788325823974243317861)
* [SAP Cloud for Customer core applications

  SAP Cloud for Customer](/t5/c-khhcw49343/SAP%2BCloud%2Bfor%2BCustomer%2Bcore%2Bapplications/pd-p/67837800100800004276)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (6)

### Overview

[SAP Cloud for Customer](https://help.sap.com/docs/SAP_CLOUD_FOR_CUSTOMER?locale=en-US) (C4C) is an SAP cloud solution which helps you manage day-to-day sales and service interactions efficiently by sending and receiving signals between front and back-office solutions and providing a single view of the customer.

[SAP Business Application Studio](https://help.sap.com/docs/SAP%20Business%20Application%20Studio?locale=en-US) (BAS) is an SAP cloud IDE which offers a modular development environment tailored for efficient development of business applications for the SAP Intelligent Enterprise.

With the new offering, you can now easily explore your live C4C services and create SAP business applications, such as SAP Fiori, HTML5, or SAP BTP full-stack extensions.

**In this blog post,** we develop an SAP BTP frontend application consuming data from C4C, using the Service Center view in BAS.

The development in BAS includes 4 steps:

* Create an SAP System (destination) pointing to a live C4C system

* Explore in services of the live C4C system

* Develop an SAP Fiori or an HTML5 application from a C4C service

* Optional: Compare the live C4C services to the C4C services located in the SAP API Business Hub in the Service Center

The formal documentation can be found [here.](https://help.sap.com/docs/SAP%20Business%20Application%20Studio/9d1db9835307451daa8c930fbd9ab264/892114ce078b4e17a9ff7e751e6330cc.html)

**Prerequisites**

You have access to a live C4C system.

You subscribed to BAS and have assigned yourself the developer and administrator role.

**Create an SAP System (Destination) Pointing to a Live C4C System**

* Click **Service Center** from the left-side activity bar.
  ![](/legacyfs/online/storage/blog_attachments/2022/12/service_center.png)
  ![](/legacyfs/online/storage/blog_attachments/2022/12/service_center_icon-1.png)

* Expand the **SAP SYSTEM** section and click **“+” (Add System)**.

* An editor for adding a new SAP System in SAP BTP opens.

* Choose the **Cloud for Customer Catalog** system type, fill the required fields, and press **Add**.![](/legacyfs/online/storage/blog_attachments/2022/12/add_system-1.png)

**Explore Services of the Live C4C System**

* The new live C4C system is available under the SAP system section.

* The C4C catalog exposes all the C4C services available in the SAP API Business Hub, and also additional SAP services and custom services.

  ![](/legacyfs/online/storage/blog_attachments/2023/01/c4csys.png)

**Develop an SAP Fiori or an HTML5 Application from a C4C Service**

* Select a service that you want to use as a data source in your application, then explore its entities and live data.

![](/legacyfs/online/storage/blog_attachments/2023/01/servicec4c-1.png)

* Create an SAP Fiori project or an HTML5 project from the service![](/legacyfs/online/storage/blog_attachments/2022/12/createproject-1.png)

* [Preview](https://help.sap.com/docs/SAP_FIORI_tools/17d50220bcd848aa854c9c182d65b699/05f2a9ef5e27402382d1ac9cfb98537f.html?locale=en-US) the application from the **Run Configurations** view.

* [Build and deploy](https://help.sap.com/docs/SAP_FIORI_tools/17d50220bcd848aa854c9c182d65b699/1b7a3be8d99c45aead90528ef472af37.html?locale=en-US) the application to Cloud Foundry.

**Compare the Live C4C Services to the C4C Services in SAP API Business Hub**

* Expand the **SAP API BUSINESS HUB** section in the Service Center view.

* You must log in to the SAP API Business Hub one time per session to see the service entities.

* Select the **SAP Customer Experience>SAP Cloud for Customer,** and see the list of services which are delivered by C4C.![](/legacyfs/online/storage/blog_attachments/2022/12/apihubc4c.png)

* Select the service that you used as a data source in your application.

* Compare the list of services from the live C4C system to the services in the SAP API Business Hub.

### **Conclusion**

You created a SAP Cloud for Customer system, then explored a service from the new system.

You created an application from the service, previewed it and deployed it to SAP BTP.

You compared the services in the live C4C system to the services of the SAP Cloud for Customer
package in the SAP API Business Hub from the Service Center view....