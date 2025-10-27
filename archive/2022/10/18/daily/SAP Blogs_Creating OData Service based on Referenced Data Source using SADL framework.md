---
title: Creating OData Service based on Referenced Data Source using SADL framework
url: https://blogs.sap.com/2022/10/17/creating-odata-service-based-on-referenced-data-source-using-sadl-framework/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:07:15.304175
---

# Creating OData Service based on Referenced Data Source using SADL framework

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Creating OData Service based on Referenced Data So...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/158462&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating OData Service based on Referenced Data Source using SADL framework](/t5/technology-blog-posts-by-members/creating-odata-service-based-on-referenced-data-source-using-sadl-framework/ba-p/13540084)

![KumarVishal](https://avatars.profile.sap.com/3/e/id3e689b55496617214f9b55948150fc513f65d651791bf91f2e07c28f4b93bdee_small.jpeg "KumarVishal")

[KumarVishal](https://community.sap.com/t5/user/viewprofilepage/user-id/493330)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=158462)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/158462)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13540084)

‎2022 Oct 17
8:47 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/158462/tab/all-users "Click here to see who gave kudos to this post.")

15,700

* SAP Managed Tags
* [API](https://community.sap.com/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)
* [ABAP Connectivity](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Connectivity/pd-p/266264953119842772207986043063520)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP Gateway](https://community.sap.com/t5/c-khhcw49343/SAP%2520Gateway/pd-p/01200615320800003185)
* [NW ABAP Gateway (OData)](https://community.sap.com/t5/c-khhcw49343/NW%2520ABAP%2520Gateway%2520%28OData%29/pd-p/181161894649260056016734803547327)

* [SAP Gateway

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BGateway/pd-p/01200615320800003185)
* [NW ABAP Gateway (OData)

  Software Product Function](/t5/c-khhcw49343/NW%2BABAP%2BGateway%2B%252528OData%252529/pd-p/181161894649260056016734803547327)
* [ABAP Connectivity

  Programming Tool](/t5/c-khhcw49343/ABAP%2BConnectivity/pd-p/266264953119842772207986043063520)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [API

  Programming Tool](/t5/c-khhcw49343/API/pd-p/b31da0dd-f79a-4a1e-988c-af0755c2d184)

View products (5)

This blog post will provide the steps to implement an OData service using SADL framework and how to reference an SAP ABAP CDS view in SEGW Gateway Builder.

### **Introduction**

As a developer, we are already familiar with the Gateway Service Builder (SEGW) tool, also we know the different ways to create and model an OData service.

Just to list down the different approaches to create and model an OData Service.

1. ABAP code-based service Implementation.

2. Service Adaptation Description Language (SADL) framework

   1. Mapping Editor

   2. Referenced Data Source

3. Annotation based approach

SADL framework - A model-driven approach using ABAP CDS Views to create OData service.

Enough of theory, lets jump into the system and see how this is created.

### **Steps**

\*\* For the purpose of demonstration, I will use a standard CDS view - ***A*****\_*BillingDocument***

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-5.jpg)

* #### Create Gateway Project in Gateway Service Builder (SEGW)

* + Project - ***ZSADL\_BILLINGDOCUMENT*** created.

* + To create the Data Model, we need to refer to Data Source. (CDS View in this case).

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-2.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-6.jpg)

* + In the next screen, we can see all the elements of CDS entity and corresponding Associations.

* + Select all the elements and proceed further. (We can select only the fields which are relevant for as per Business Need and we always have the option to edit that later)

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-8.jpg)

* + After completing this step all the Entity, Entity Sets, Association & corresponding Navigation is automatically generated in the Gateway Project.

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-9.jpg)

* + Now, generate the service.

* + After generating Register and Maintain the service. As like any OData service ![:slightly_smiling_face:](/html/@CB193FD929C1B3F628B5259D5B23C3AB/emoticons/1f642.png ":slightly_smiling_face:")

* #### Test in Gateway Client (/IWFND/GW\_CLIENT)

* + Once the service is maintained, it can be tested in the Gateway Client.

* + We can see all the Entity and corresponding Association in the Metadata Information.

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-10.jpg)

* + We can execute the service with different Entities to see the results.

![](/legacyfs/online/storage/blog_attachments/2022/10/blog-11.jpg)

### **Summary**

* The advantage of using the SADL framework with Referenced Data Source is that Mapping (Association & navigation) is derived automatically.

* With this approach change in the OData model is not supported but changes can be done in the SADL model and that reflects in the OData model.

* Also, field extensibility and custom code exits are possible.

So, using this approach OData service implementation can be optimized!

Please feel free to comment and let me know your feedback.

Happy Learning ….Together !! ![:slightly_smiling_face:](/html/@CB193FD929C1B3F628B5259D5B23C3AB/emoticons/1f642.png ":slightly_smiling_face:")

* [1 SAP\_Gateway](/t5/tag/1%20SAP_Gateway/tg-p/board-id/technology-blog-members)
* [ABAP+OData](/t5/tag/ABAP%2BOData/tg-p/board-id/technology-blog-members)
* [sadl](/t5/tag/sadl/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcreating-odata-service-based-on-referenced-data-source-using-sadl-framework%2Fba-p%2F13540084%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  14m ago
* [RAP Using Custom Entity with load multiple data using Pagination and Preview using UI annotations](/t5/technology-q-a/rap-using-custom-entity-with-load-multiple-data-using-pagination-and/qaq-p/14233901)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  8 hours ago
* [Build a Code-based Agent using SAP AI Core with Next.js and the Vercel AI SDK](/t5/technology-blog-posts-by-sap/build-a-code-based-agent-using-sap-ai-core-with-next-js-and-the-vercel-ai/ba-p/14230640)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/tech...