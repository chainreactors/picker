---
title: Implement authorization concept for the Fiori apps to display in the SAP build work Zone based on the roles configured in BTP
url: https://blogs.sap.com/2023/02/12/implement-authorization-concept-for-the-fiori-apps-to-display-in-the-sap-build-work-zone-based-on-the-roles-configured-in-btp/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:28:01.831485
---

# Implement authorization concept for the Fiori apps to display in the SAP build work Zone based on the roles configured in BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Implement authorization concept for the Fiori apps...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162676&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Implement authorization concept for the Fiori apps to display in the SAP Build Work Zone based on the roles configured in BTP](/t5/technology-blog-posts-by-members/implement-authorization-concept-for-the-fiori-apps-to-display-in-the-sap/ba-p/13565249)

![amalakar46](https://avatars.profile.sap.com/d/9/idd9260b919d36dddb3ac9a86444fc911e6acfcbceb05dfd8a73e1a8be7900355a_small.jpeg "amalakar46")

[amalakar46](https://community.sap.com/t5/user/viewprofilepage/user-id/122984)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162676)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162676)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565249)

‎2023 Feb 12
8:12 AM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162676/tab/all-users "Click here to see who gave kudos to this post.")

5,712

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

View products (1)

In this Blog I will explain the steps how to Implement authorization concept for the Fiori apps to display in the SAP Build Work Zone, standard edition based on the roles/catalog/groups configured in BTP content.

We can control the Fiori apps to display in the SAP build work zone. We will configure the roles for the Fiori apps deployed in cloud foundry in BTP / HTML5 Application Repository and SAP build work zone should show based on the role assigned to user.

**Please note:** -SAP Launchpad service is now changed SAP Build Work Zone, Standard Edition.

To achieve this scenario, we will use a use case, we will create 2 HTML5 freestyle Fiori apps in BAS using the Northwind odata service and deploy in cloud foundry.

1. **Customer app**

2. **Order app**

These apps should be visible to users based on the Role assigned to them.

**Configuration Steps:-**

Step 1: - Login to BTP cockpit ( Trial account in this scenario) Subscribe to the SAP Build Work Zone, standard edition.

Step 2: - Create a north wind destination.

Step 3: - Create two freestyle Fiori app in Business application studio using the Northwind odata service.

Step 4: - Deploy these two Fiori apps to cloud foundry.

Step 5: - Create respective role in build work zone (launchpad service) and assign the deployed apps.

Step 6: - Assign the role to user and open the launchpad URL to view the app.

**Step 1: - Subscribe to the SAP Build Work Zone, standard****edition.**

1. In Subaccount of BTP go to **Service****Marketplace on** the left.

2. Search for the **SAP Build work zone Service** tile and choose **Create**.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_2.png)

    3. Keep the default settings for **Service** and **Plan** and choose **Create**.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_3.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_4.png)

       4. **Assign Role Collection** and assign the role: - **Launchpad\_Admin** collection to your user.

5. Navigate to the Site Directory and create a new site.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_5.png)

      6. Give your site a name and click “Create”, it will not display anywhere on your final site, it is just reference.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_6.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_7.png)

**Step 2: - Create a north wind destination.**

Destinations are key building blocks in SAP BTP and are used to define connections for outbound communication from your application to remote systems. These remote systems can be on-premises or in the cloud.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_8.png)

A destination has a name, a URL, authentication details, and some other configuration details.

The destination you will define here is for the set of [OData](http://www.odata.org/) services known as the “Northwind” services, which are publicly available.

The Northwind OData services comes in several versions. We will use version V2 in our case.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_9.png)

**Step 3: - Create a freestyle Fiori app in Business application studio using the Northwind odata service.**

1. We will develop a Fiori App using the SAP Business Application Studio to create a freestyle app in BAS using a wizard that creates a multi-target application (MTA) project that is configured to use Managed Application Router. An MTA is required to create the deployment artifact for SAP BTP, Cloud Foundry environment.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_10.png)

When end-users access an app in the Cloud Foundry environment, they actually access the Application Router first. The application router is used to serve static content, authenticate users, rewrite URLs, and forward or proxy requests to other micro services while propagating user information.

The managed application router is the HTML5 Applications Runtime capability provided by SAP Build Work Zone, standard edition, to which you must be subscribed.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_11.png)

  2. The Application Route Generator Wizard opens up and following parameters need to be provided:

* Application router project path

* MTA ID and description

* Add Route Module

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_12.png)

   3.Wait until the creation of project is completed. A notification that “The files has been generated” appears at the bottom right of the screen.

![](/legacyfs/online/storage/blog_attachments/2023/02/4PIC_13.png)

   4. Open the project's folder. select the created project within the **projects** folder, and click **OK**

![](/legacyfs/online/storage/blog_attachments/2023/02/4PIC_13-3.png)

  5.SAP Business Application Studio reloads with the project open in its workspace. In the Explorer view you can see the project, its folder structure, and files.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_14.png)

  6. Generate an app based on SAPUI5 Application template The easiest way to develop an SAPUI5 freestyle app from scratch is to create it from a template.

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_15.png)

   7.For Template Selection, select the following, and click Next.

|
 **Step** |
 **Parameter** |
 **Value** |

|
 A |
 Application type |
 SAPUI5 freestyle |

|
 B |
 Which template do you want to use? |
 SAP Fiori List – Detail Application |

![](/legacyfs/online/storage/blog_attachments/2023/02/PIC_16.png)

   8. For Data Source and Service Selection, select the following, and click Next.

|
 **Step** |
 **Parameter** |
 **Value*...