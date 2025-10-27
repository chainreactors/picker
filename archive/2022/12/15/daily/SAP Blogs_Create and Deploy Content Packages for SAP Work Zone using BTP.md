---
title: Create and Deploy Content Packages for SAP Work Zone using BTP
url: https://blogs.sap.com/2022/12/14/create-and-deploy-content-packages-for-sap-work-zone/
source: SAP Blogs
date: 2022-12-15
fetch_date: 2025-10-04T01:32:21.426074
---

# Create and Deploy Content Packages for SAP Work Zone using BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Create and Deploy Content Packages for SAP Build W...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158285&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create and Deploy Content Packages for SAP Build Work Zone Advanced Edition using BTP](/t5/technology-blog-posts-by-sap/create-and-deploy-content-packages-for-sap-build-work-zone-advanced-edition/ba-p/13551511)

![former_member582997](https://avatars.profile.sap.com/former_member_small.jpeg "former_member582997")

[former\_member582997](https://community.sap.com/t5/user/viewprofilepage/user-id/582997)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158285)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158285)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551511)

‎2022 Dec 14
6:22 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158285/tab/all-users "Click here to see who gave kudos to this post.")

3,619

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Build Work Zone, advanced edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Work%2520Zone%252C%2520advanced%2520edition/pd-p/73555000100800002781)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Build Work Zone, advanced edition

  Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BWork%2BZone%25252C%2Badvanced%2Bedition/pd-p/73555000100800002781)

View products (3)

## Introduction

Content Packages are collection of content items like cards, workspace templates, workflows and workspaces that are bundled in a ZIP file that can be easily uploaded and installed in sub account.

For more details on the Content packages, refer the sap help link - [Content Packages](https://help.sap.com/docs/WZ/b03c84105ff74f809631e494bd612e83/da203f9d1ab143f084d75688f1e9e032.html)

Today I will be illustrating the creation of Local Content Packages which contains UI Integration Cards.

## Steps to setup Local Content Package

First step is to create a content package in Business Application Studio.

#### Prerequisite:

Make sure you have created a dev space with Development Tools for SAP Build Work Zone extension.

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-1.png)

In the Dev Space created, choose New Project from Template. Select Content Package and click on Start.

In the details. fill the name, title and set Include Content Samples field to true if you need a sample included. The workspace opens with your project.

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-2.png)

We will add a custom UI card into the Content Repository today. First, keep the zip file for the UI card ready.

Click on File->Import Project and upload the zip file for the card. Once the project is imported, you would see that there are two folders within the project. Delete the second folder. But before deleting, move the contents within the second folder to main folder. (Refer below image)

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-3.png)

Next, create a folder '.card' within the imported project. This is not necessary if the card is created in the same BAS.

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-4.png)

Next, right click on the manifest of the imported project. And select 'UI Integration Card: Package' and create a zip file.

Next, go to our content package project created first. Right click on content.json file and click 'Content Package: Content Edit'. Click on Add artifact. Enter the Name and fill the below details.

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-5.png)

Copy the path of the imported project by right clicking on the project. Enter the path in the from field as shown above. Enter the zip package name of the imported project created in the package field, as done in the previous step. Once done, save it.

**P.S. You can also select the mode as Git and use the github path too.**

Next, right click on the manifest.json file in Content Package project and choose 'Content Package: Package'. This will create a zip package. This package is used to upload into Work Zone to extract the cards.

**P.S. You can also deploy it directly to Work Zone by right clicking and selecting 'Content Package: Deploy to SAP Build Work Zone'.**

To manually deploy it, go to Administrator console in your Work Zone Tenant, and Select Content Packages under UI Integration. Click on Upload Content Package and choose your zip file. Once Uploaded, install the content package.

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-7.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-8.png)

Enable the card, and you can use the card in workspaces.

![](/legacyfs/online/storage/blog_attachments/2022/12/Capture-9.png)

## Conclusion

Above example explains how to create content packages to move cards, workflows or workspaces between various work zone tenants.

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fcreate-and-deploy-content-packages-for-sap-build-work-zone-advanced-edition%2Fba-p%2F13551511%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  4 hours ago
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  6 hours ago
* [Document Grounding: A (hidden) gem in SAP Business AI’s portfolio for smaller companies.](/t5/technology-blog-posts-by-sap/document-grounding-a-hidden-gem-in-sap-business-ai-s-portfolio-for-smaller/ba-p/14232864)
  in [Technology Blog Posts by SAP](/t5/technology-blog...