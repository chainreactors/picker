---
title: Enhance user experience using SAP BTP Mobile Services Part 4
url: https://blogs.sap.com/2022/11/10/enhance-user-experience-using-sap-btp-mobile-services-part-4/
source: SAP Blogs
date: 2022-11-11
fetch_date: 2025-10-03T22:22:52.243577
---

# Enhance user experience using SAP BTP Mobile Services Part 4

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Enhance user experience using SAP BTP Mobile Servi...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163929&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enhance user experience using SAP BTP Mobile Services Part 4](/t5/technology-blog-posts-by-sap/enhance-user-experience-using-sap-btp-mobile-services-part-4/ba-p/13568455)

![nhatdoan](https://avatars.profile.sap.com/a/5/ida5490a07f5959f18b25154fff95782c659e3e1e1aab073083346d715149a0f6b_small.jpeg "nhatdoan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[nhatdoan](https://community.sap.com/t5/user/viewprofilepage/user-id/39493)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163929)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163929)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568455)

‎2022 Nov 10
7:36 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163929/tab/all-users "Click here to see who gave kudos to this post.")

768

* SAP Managed Tags
* [SAP Mobile Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Services/pd-p/668874921104038800958643358380369)

* [SAP Mobile Services

  Software Product Function](/t5/c-khhcw49343/SAP%2BMobile%2BServices/pd-p/668874921104038800958643358380369)

View products (1)

My name is Nhat Doan. I am currently in SAP Student Training and Rotation (STAR) Program. In my first rotation, I have a chance to join CoE Mobile & UX team. I have learned a lot of things especially about current developments in mobile technology. Today, smartphones become essential for daily life. Businesses are using mobile applications to serve their clients and they will see many benefits such as brand building, customer connection, and profit boosts. I would like to share some topics concerning mobile development.

1. [Build ProductCatalog application with AppGyver and Northwind OData service.](https://blogs.sap.com/2022/11/02/enhance-user-experience-using-sap-btp-mobile-services/)

2. [Build ProductCatalog application with SAP MDK and Northwind OData service.](https://blogs.sap.com/2022/11/07/enhance-user-experience-using-sap-btp-mobile-services-2/)

3. [How to style the MDK application.](https://blogs.sap.com/2022/11/08/enhance-user-experience-using-sap-btp-mobile-services-part-3/)

4. [How to run MDK application on virtual device and override resources.](https://blogs.sap.com/2022/11/10/enhance-user-experience-using-sap-btp-mobile-services-part-4/)

5. [How to reads log, traces issue, and measures performance for MDK application.](https://blogs.sap.com/2022/11/10/enhance-user-experience-using-sap-btp-mobile-services-part-5/)

**How to run MDK application on virtual device and override resources**

**Download Mobile development kit client**

Go to this page <https://developers.sap.com/trials-downloads.html?search=Mobile%20development%20kit> to download Mobile development kit client.

**Install MDK**

Copy the downloaded file to home folder. Extract the downloaded file. We will have these files like the picture below.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_1.png)

*Figure 1: The content of the downloaded file*

Extract **MDKDependenciesInstallerWindows.zip**. We will have a new folder **MDK Dependencies Installer-win32-ia32**. Go to this folder and double click **MDK\_Dependencies\_Installer.exe** to install MDK dependencies. The MDK Dependencies Installer will check all the dependencies that need to be installed in order to use Mobile development kit client.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_2.png)

*Figure 1: The content of the downloaded file*

Extract **MDKDependenciesInstallerWindows.zip**. We will have a new folder **MDK Dependencies Installer-win32-ia32**. Go to this folder and double click **MDK\_Dependencies\_Installer.exe** to install MDK dependencies. The MDK Dependencies Installer will check all the dependencies that need to be installed in order to use Mobile development kit client.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_3.png)

*Figure 3: create-client.cmd file after installing MDKClient\_SDK*

**Create an mdkproject folder**

Clone **template.mdkproject** to **ProductCatalog.mdkproject**. Open **ProductCatalog.mdkproject**. We will have these files below.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_4.png)

*Figure 4: The content of ProductCatalog.mdkproject*

**Config to run ProductCatalog on the virtual device**

Open **MDKProject.json**. Change **AppDisplayName** to “Product Catalog”. Change **AppName** to “ProductCatalog”. Change **BundleID** to “com.sap.mdk.productcatalog”. The **BundleID** is the ID of the application inside Mobile Services.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_5.png)

*Figure 5: The ID of the application can be found inside Mobile Service*

Here is the content of **MKDProject.json** after our modification.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_6.png)

*Figure 6: The content of MDKProject.json*

Open **BrandedSettings.json**. Set **ApplicationDisplayName** to “Product Catalog”. For the other field like: **AppId**, **ClientId**, **ServerUrl**, **AuthorizationEndpointUrl**, **RedirecUrl**, **TockenUrl**. We can find the information of these fields by opening the Product Catalog app in **Mobile Services** and click on **Mobile Settings Exchange**.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_7.png)

*Figure 7: Click on Mobile Settings Exchange to see all the information that need for BrandedSetting.json*

Click **Info** tab inside **Mobile Settings Exchange** to see the **Connection Settings** for **BrandedSettings.json**

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_8-1.png)

*Figure 8: The ConnectionSettings that can be used for BrandedSettings.json*

Beside that we can customize the value of **DetailLabelViewText** and **SigninButtonText** for the label and the Signin button of the application.

**Run create-client.cmd**

Open **Windows PowerShell**. Go to the folder that contents **create-client.cmd** file. Type the command ./create-client.cmd. And enter **ProductCatalog.mdkproject**. This is the folder that we have just cloned from **template.mdkproject**. We will have a new **ProductCatalog** folder.

**Run the application on virtual device**

Go to **ProductCatalog** using this command **cd ProductCatalog**. Use this command to run the application on virtual device **tns run android**. Now the application can run on the virtual device.

![](/legacyfs/online/storage/blog_attachments/2022/11/pic_4_9.png)

*Figure 9: The application is running on the virtual device*

**Override the resource of the application**

Currently, the color of the systems icons is black. These icons can be changed to white by overriding the styles.xml of the application. Go to **.mdkproject** folder and find folder **App\_Resources/Android** and create f...