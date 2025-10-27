---
title: Installation Eclipse and  configuration ADT tool
url: https://blogs.sap.com/2022/11/04/installation-eclipse-and-configuration-adt-tool/
source: SAP Blogs
date: 2022-11-05
fetch_date: 2025-10-03T21:45:04.834732
---

# Installation Eclipse and  configuration ADT tool

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Installation Eclipse and configuration ADT tool

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161868&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Installation Eclipse and configuration ADT tool](/t5/technology-blog-posts-by-members/installation-eclipse-and-configuration-adt-tool/ba-p/13560273)

![Dhanasekhar](https://avatars.profile.sap.com/a/f/idaf9984ddd26d7b72a957357004481e17ff4c8c5376669189f319f5ec91ceefb7_small.jpeg "Dhanasekhar")

[Dhanasekhar](https://community.sap.com/t5/user/viewprofilepage/user-id/175534)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161868)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161868)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560273)

‎2022 Nov 04
5:42 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161868/tab/all-users "Click here to see who gave kudos to this post.")

75,699

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (2)

**Introduction**

Before Driving deep into Technical details . let me give some brief about why we need to do this ABAP Development Tool (ADT) is an Eclipse  based tool provided by SAP, You will need ADT if you have to work on the ABAP CDS views. Even though,CDS views are emdedded into the ABAP Dictionary, there are some Difference in the features available between the Eclipse and the Data Dictionary environments.

Detail example  how to **Connect to S/4HANA 1809 SAP Server from Eclipse** explained in this Blog.

Follow below steps to install Eclipse and set up GUI ADT

**Install Eclipse**

Download Eclipse using this link - <https://www.eclipse.org/downloads/>

![](/legacyfs/online/storage/blog_attachments/2022/11/image001.png)

Double Click the Eclipse Installation file which is downloaded above.

![](/legacyfs/online/storage/blog_attachments/2022/11/image002.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/image003.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/image004.png)

We have selected Eclipse IDE for Enterprise Java Developers. You may choose the first one too i.e. Eclipse IDE for Java Developers.

![](/legacyfs/online/storage/blog_attachments/2022/11/image005.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/image006.png)

Accept the Terms and Conditions

![](/legacyfs/online/storage/blog_attachments/2022/11/image007.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/image008.png)

Once the Installation is complete, Launch the Eclipse

![](/legacyfs/online/storage/blog_attachments/2022/11/22.png)

This is how the Eclipse should look once the Launch is complete.

![](/legacyfs/online/storage/blog_attachments/2022/11/21.png)

If you want to check the version of your Eclipse, you may go the Help -> About.

![](/legacyfs/online/storage/blog_attachments/2022/11/20.png)

Ours is 2020-03 version

![](/legacyfs/online/storage/blog_attachments/2022/11/19.png)

**Install ADT (ABAP Development Tool) in Eclipse**

![](/legacyfs/online/storage/blog_attachments/2022/11/18.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/17-1.png)

Get the latest ADT tools from below link.

<https://tools.eu1.hana.ondemand.com/#abap>

![](/legacyfs/online/storage/blog_attachments/2022/11/16-2.png)

Enter below URL if you installed the latest Eclipse 2020-03 like us :

<https://tools.hana.ondemand.com/latest>

![](/legacyfs/online/storage/blog_attachments/2022/11/15-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/14-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/13-4.png)

Hit Finish and check the progress at the bottom right corner.

![](/legacyfs/online/storage/blog_attachments/2022/11/13-3.png)

Once it is complete, it will as ask to Restart Eclipse. Not Computer.

![](/legacyfs/online/storage/blog_attachments/2022/11/12-4.png)

Wait for Eclipse to start again.

**Open ABAP Perspective in Eclipse ADT**

![](/legacyfs/online/storage/blog_attachments/2022/11/11-4.png)

Choose ABAP in Others Perspective.

![](/legacyfs/online/storage/blog_attachments/2022/11/11-3.png)

Top Left corner, ABAP perspective is visible.

![](/legacyfs/online/storage/blog_attachments/2022/11/9-5.png)

**Connect to S/4HANA 1809 SAP Server from Eclipse**

Click on Create ABAP Project

![](/legacyfs/online/storage/blog_attachments/2022/11/8-7.png)

It will show the SAP System from the Local GUI. You need to have the GUI installed and the S/4HANA Server details added to it.

![](/legacyfs/online/storage/blog_attachments/2022/11/6-4.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/7-7.png)

Provide the SAP User Id and Password provided to you. If you have not received the id and password yet, please ignore this step.

![](/legacyfs/online/storage/blog_attachments/2022/11/5-6.png)

Hit Finish Button

![](/legacyfs/online/storage/blog_attachments/2022/11/4-7.png)

Add Your Favourite Package to Project

Add Favourite Package and Hit Finish or Add Package later by right clicking and Add Package.

![](/legacyfs/online/storage/blog_attachments/2022/11/3-8.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/2-5.png)

To find anything in Eclipse, you may use short cut - SHIFT + CNTRL + A

![](/legacyfs/online/storage/blog_attachments/2022/11/last-1.png)

I hope this blog made it easier for you to troubleshoot all the issues while installing Eclipse for ADT. Please leave any comments or suggestions you might have.

6 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Finstallation-eclipse-and-configuration-adt-tool%2Fba-p%2F13560273%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Everyday issues: SAP HANA database parameters (recommended by SAP) not configured properly.](/t5/technology-blog-posts-by-sap/everyday-issues-sap-hana-database-parameters-recommended-by-sap-not/ba-p/14230055)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [SAP IQ to SAP HANA Cloud, Data Lake Migration Overview](/t5/technology-blog-posts-by-sap/sap-iq-to-sap-hana-cloud-data-lake-migration-overview/ba-p/14228663)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Wednesday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 ...