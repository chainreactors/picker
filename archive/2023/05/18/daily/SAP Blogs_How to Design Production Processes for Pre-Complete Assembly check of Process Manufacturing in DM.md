---
title: How to Design Production Processes for Pre-Complete Assembly check of Process Manufacturing in DM
url: https://blogs.sap.com/2023/05/17/how-to-design-production-processes-for-pre-complete-assembly-check-of-process-manufacturing-in-dm/
source: SAP Blogs
date: 2023-05-18
fetch_date: 2025-10-04T11:39:51.187654
---

# How to Design Production Processes for Pre-Complete Assembly check of Process Manufacturing in DM

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* How to Design Production Processes for Pre-Complet...

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1435&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Design Production Processes for Pre-Complete Assembly check of Process Manufacturing in DM](/t5/product-lifecycle-management-blog-posts-by-members/how-to-design-production-processes-for-pre-complete-assembly-check-of/ba-p/13554108)

![former_member532862](https://avatars.profile.sap.com/former_member_small.jpeg "former_member532862")

[former\_member532862](https://community.sap.com/t5/user/viewprofilepage/user-id/532862)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1435)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1435)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554108)

‎2023 May 17
10:43 PM

[1
Kudo](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1435/tab/all-users "Click here to see who gave kudos to this post.")

3,843

* SAP Managed Tags
* [SAP Digital Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing/pd-p/73555000100800001492)
* [SAP Digital Manufacturing Insights](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing%2520Insights/pd-p/73554900100800000751)

* [SAP Digital Manufacturing Insights

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing%2BInsights/pd-p/73554900100800000751)
* [SAP Digital Manufacturing

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing/pd-p/73555000100800001492)

View products (2)

**How to Design Production Processes for Pre-Complete Assembly Check of Process Manufacturing in SAP DM**

**Design Production Processes**

To design production processes without any coding skills DMC delivers the app Design Production Processes. The app helps to model various production processes using a graphical design tool. The production processes define the interaction between machines or define rules, actions, and workflows that control the execution on the shop floor. The custom-made business process extension can be consumed and used like a standard business service within the Design Production Process app.

**Objective:** Define the production process for per-complete SFC check. Hence the process should be by clicking on the Complete button production process will be triggered and check if the user assembled or not. If the components are assembled, then the system allow to complete the SFC otherwise the system doesn’t allow to complete the SFC.

**Step:1 Create Production Process**

Need to go Design Production Processes app (Path->Manufacturing Automation->Design Production Processes), now able to create a production process. Here, we will learn how to create a production process design for a pre-complete assembly check (Process Manufacturing). Need to put the Production process name and description and create the process.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture1-6.jpg)

Need to put Name, ID, Description, and Runtime Type to create production process, now process variable session is enabled to declare production process. Now go to the editor and design the production process as per the requirement.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture2-34.png)

**Step:2 Production Process flow**

At 1st take the start controls and need to add the Inputs parameters as per the requirement by clicking on the manage parameters button. After that need to add Check Component services and map the input parameter as per the requirement.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture3-31.png)

As we know for process manufacturing GI is being confirmed against phase. Hence, need to map the Operation as Phase

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture4-31.png)

Now, need to add the Complete SFC service and map the Body parameter as per the requirement.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture5-23.png)

Now, need to end the production process. Hence to need the End controls.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture6-21.png)

**Step:3 Test the Production Process**

Need to save the Production Process by clicking on the Save All button, click on the Quick Deploy to deploy the created production process, and run the process standalone.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture7-20.png)

Click on the Run button to execute the Production process standalone. Then put the required input and again click on the Run button.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture8-19.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture9-16.png)

**Step:4 Add the Production Process into the Complete Button**

Need to go to the POD designer (Path->Manufacturing Configuration->POD Designer), and open the custom POD (Process Order).

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture10-15.png)

Now, need to configure the Complete button. Go to assign action and add the created production process. Also, need to map the variable with parameters.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture11-14.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture12-13.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture13-12.png)

Now, it has been working through the POD.

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture14-12.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/Picture15-11.png)

Thanks,

Rajat

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fproduct-lifecycle-management-blog-posts-by-members%2Fhow-to-design-production-processes-for-pre-complete-assembly-check-of%2Fba-p%2F13554108%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Why is BOM Header Not Transferred to Project in Auto BOM Transfer (VC / PS Integration)?](/t5/product-lifecycle-management-q-a/why-is-bom-header-not-transferred-to-project-in-auto-bom-transfer-vc-ps/qaq-p/14233783)
  in [Product Lifecycle Management Q&A](/t5/product-lifecycle-management-q-a/qa-p/plm-questions)  Thursday
* [Day 1 EHS & Product Compliance InfoDays](/t5/product-lifecycle-management-blog-posts-by-sap/day-1-ehs-amp-product-compliance-infodays/ba-p/14231803)
  in [Product Lifecycle Management Blog Posts by SAP](/t5/product-lifecycle-management-blog-posts-by-sap/bg-p/plm-blog-sap)  Tuesday
* [Customized BOM generator to use S4/HANA PLM module for EBOM & MBOM generation](/t5/product-lifecycle-management-q-a/customized-bom-generator-to-use-s4-hana-plm-module-for-ebom-amp-mbom/qaq-p/1423...