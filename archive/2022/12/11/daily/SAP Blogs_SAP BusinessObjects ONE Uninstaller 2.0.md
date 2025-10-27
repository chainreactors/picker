---
title: SAP BusinessObjects ONE Uninstaller 2.0
url: https://blogs.sap.com/2022/12/10/sap-businessobjects-one-uninstaller-2.0/
source: SAP Blogs
date: 2022-12-11
fetch_date: 2025-10-04T01:12:23.469011
---

# SAP BusinessObjects ONE Uninstaller 2.0

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BusinessObjects ONE Uninstaller 2.0

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/164178&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BusinessObjects ONE Uninstaller 2.0](/t5/technology-blog-posts-by-sap/sap-businessobjects-one-uninstaller-2-0/ba-p/13569443)

![VenkateswaraGupthaY](https://avatars.profile.sap.com/f/2/idf2c216d278f7b2940cf8a8fd8abf13c3d9176986813276318a46e1af71e3ea52_small.jpeg "VenkateswaraGupthaY")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[VenkateswaraGupthaY](https://community.sap.com/t5/user/viewprofilepage/user-id/484)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=164178)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/164178)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569443)

‎2022 Dec 10
2:55 AM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/164178/tab/all-users "Click here to see who gave kudos to this post.")

4,238

* SAP Managed Tags
* [SAP BusinessObjects Business Intelligence platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520Business%2520Intelligence%2520platform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Platform Administration](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Platform%2520Administration/pd-p/493706448058243238508632186627562)
* [SAP BusinessObjects - Platform Infrastructure](https://community.sap.com/t5/c-khhcw49343/SAP%2520BusinessObjects%2520-%2520Platform%2520Infrastructure/pd-p/908268185089197093202840551891078)

* [SAP BusinessObjects Business Intelligence platform

  SAP BusinessObjects Business Intelligence](/t5/c-khhcw49343/SAP%2BBusinessObjects%2BBusiness%2BIntelligence%2Bplatform/pd-p/01200314690800000337)
* [SAP BusinessObjects - Platform Administration

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BPlatform%2BAdministration/pd-p/493706448058243238508632186627562)
* [SAP BusinessObjects - Platform Infrastructure

  Software Product Function](/t5/c-khhcw49343/SAP%2BBusinessObjects%2B-%2BPlatform%2BInfrastructure/pd-p/908268185089197093202840551891078)

View products (3)

SAP BusinessObjects ONE Uninstaller was introduced back in 2020 to ease in addressing the challenges faced by IT Administrators managing the BI Systems with respect to ever growing footprint (disk space) due to multiple Service Pack and patch updates of different BI Suite of products. To optimize footprint of BI Suite of products with the traditional uninstallation is not an easy task or sometimes impossible due to challenges related to getting maintenance window. As you know, in traditional method of uninstallation it is last in first should be the approach, in that way, one has to uninstall the lastest version(s) updated (like n, (n-1)), and then uninstall the intermediate versions (which you believe are no more required) one after another, and once all the intermediate versions are uninstalled, then you need to update the system back with last/latest versions previously uninstall to bring the system back to the level where it was, before staring this process. This way if more number of intermediate versions are there, then it will take accordingly longer time to finish this task.

To address this challenge and ease the job for IT Administrators **SAP BusinessObjects ONE Uninstaller** tool was introduced. This tool, with its ability to calculate analyze and calculate the obsolete intermediate BI versions and offer them to delete all the selected versions of all the BI Suite of product's cache in one shot is winning the hearts of IT/BI Administrators. Like in Jenga Game.. you should know which block is safe to remove... without disturbing the tower.. this is what tool will do it for you automatically..

![](/legacyfs/online/storage/blog_attachments/2022/12/Jenga.png)

Now your favorite Uninstaller tool, has got more power, gives more flexibility for IT/BI Administrators looking to optimize large number remote BI Servers or BI Client machines of their end users.  **Introducing** **Silent Execution** **/** **Remote Execution** of the **SAP BusinessObjects ONE Uninstaller** tool is the major breakthrough feature ever since its inception. And along with this major feature one another useful feature is also got introduced in this **ONE Uninstaller release v2.0,** that is to know the install history information of a remote BI Server / BI Client machine.

#### **Points related to Tool delivery and execution :**

1. Delivery of this release **v2.0** is also done through the same SAP Note **[2846512](https://launchpad.support.sap.com/#/notes/2846512)****.**

2. Also the future releases of this tool will also be done via the same SAP Note **[2846512](https://launchpad.support.sap.com/#/notes/2846512)****.**

3. SAP will not maintain the previous versions of this tool with the Note, having said that, you will find only the latest version released for this tool in the Note.

4. You need to keep the backup of this tool when you plan to start using the latest version of this tool in your BI systems, in case of any unexpected results or blockers with the latest version, you can use previous version of the tool from your backup, until the issue is fixed in the future release.

5. Tool will fail to execute and will exit, if the value for the Installation directory path and Log directory path has trailing slash.

   * For example: if the installation directory path as following "C:\Program Files (x86)\SAP BusinessObjects\" then tool will fail to execute properly, hence the correct input for the path for this example will be as follows: "C:\Program Files (x86)\SAP BusinessObjects"

**So, let us see what are these, and how these features together will help BI Administrators / IT Administrators managing the BI Landscapes, and their BI End user systems.**

## **Gathering information remotely(-i![:disappointed_face:](/html/@298C2BB6A146EEB751358995E97C787E/emoticons/1f61e.png ":disappointed_face:")**

IT Administrator / BI Administrator planning to optimize Install footprint on their BI systems (BI Server / BI Client) can now **fetch the BI Suite Install footprint information** **remotely**.

With this option in place, Administrators can gather the information about BI Suite Installation history into a file to know which obsolete versions can be deleted. In fact you can get the same information displayed when you run the ONE Uninstaller tool on the command prompt, but for that you need login (directly / remotely) into the machine and run the following command interactively:

```
java -jar OneUninstaller.jar -InstallDir <BO_Install_Dir> [-LogDir <Directory_Path_for_Writing_Logs>]
```

Then on the command prompt it will display the information as following (For example):

![](/legacyfs/online/storage/blog_attachments/2022/12/ONEUninstaller.png)

In the above example screenshot, you can only see purely vers...