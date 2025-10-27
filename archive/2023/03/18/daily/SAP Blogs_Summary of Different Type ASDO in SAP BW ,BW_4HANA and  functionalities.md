---
title: Summary of Different Type ASDO in SAP BW ,BW/4HANA and  functionalities
url: https://blogs.sap.com/2023/03/17/a-quick-summary-of-different-type-asdo-in-sap-bw-bw-4hana-and-their-functionality./
source: SAP Blogs
date: 2023-03-18
fetch_date: 2025-10-04T09:57:03.872424
---

# Summary of Different Type ASDO in SAP BW ,BW/4HANA and  functionalities

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Summary of Different Type ASDO in SAP BW ,BW/4HANA...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160108&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Summary of Different Type ASDO in SAP BW ,BW/4HANA and functionalities](/t5/technology-blog-posts-by-members/summary-of-different-type-asdo-in-sap-bw-bw-4hana-and-functionalities/ba-p/13550378)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160108)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160108)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550378)

‎2023 Mar 17
9:39 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160108/tab/all-users "Click here to see who gave kudos to this post.")

41,343

* SAP Managed Tags
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (1)

In this topic we will discuss about the main **ASDO's** and their functionality which will help to understand the basic BW project design in the next blog I am going to discuss about.

The below is very important . Common **ADSO's** available in **BW 7.5 on HANA**, **BW4/HANA 1.0 and** **BW/4HANA 2.0** -

![](/legacyfs/online/storage/blog_attachments/2023/03/ADSO-type.png)

**1. Data Mart ADSO :**

![](/legacyfs/online/storage/blog_attachments/2023/03/Data-Mart-1-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/Datamartdiagram.png)

**Memorable point :**

* Can be report on top of active data table and Inbound table either using AND or OR.

* When reading data using navigation the data will not change i.e stable.

* Data are ADDITIVE not OVERWRITE.

* All key form the Composite Key.

* Only in inbound table RequestID is the key like other ADSO.

* Change Log exists but not loaded.

**2. Standard ADSO :**

![](/legacyfs/online/storage/blog_attachments/2023/03/StandardADSO.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/STD-diagram.png)

**Memorable point :**

* Data store at document level .

* Can be report on top of active data table only.

* When reading data using navigation the data will change if load happen i.e non stable.

* Data are always OVERWRITE.

* All key form the Composite Key at Active table .

* Only in inbound table RequestID is the key like other ADSO.

* Change Log exists and  loaded from inbound queue during activation . Delta DTP takes data from change log table.

* Full Load DTP takes data from Active table.

Standard ADSO with Snapshot support always do Reverse image if you full load the data next time .

Suppose you have 10 record in load1 and if you have snapshot support and there are 9 records in second row. 1 row will be deleted from ADSO but without snapshot support if you load the roq will be 10.

**3. Staging ADSO or Write optimized DSO:**

![](/legacyfs/online/storage/blog_attachments/2023/03/staging.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/STAGING-Diagram.png)

**Memorable point :**

* Commonly used as PSA  at data entry layer . It act as a consistent base level data store.

* Field based modeling preferable for faster performance.

* Reporting not preferable.

* No key is Mandatory.

* Only in inbound table RequestID is the key like other ADSO.

* Change Log exists but not loaded from inbound queue.

* Full and delta Load DTP takes data from inbound table.

**4. Direct update ADSO :**

![](/legacyfs/online/storage/blog_attachments/2023/03/Direct-Update-ADSO.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/DUADSODIAGRAM.png)

**Memorable point :**

* Directly Active table updated.

* No need to Activation.

* Using request you can delete data.

* Using DTP or API data can be loaded.

* Supports only full load. After the data load the data is visible immediately from reporting.

5. **Inventory Type ADSO :** you can used standard and Data Mart ADSO as Inventory ADSO by enabling checkbox inventory enabled for inventory purpose use. This is not used frequently.

Note : ADSO can contain maximum 2 billion of record. For larger implementation do Symantec partitioning or Physical partitioning.

As per my recommendation :

1. Do tearing management of Hot, Warm and cold data based on the date range ( 1 year or two year)

2. if Tearing is not possible then go with Symantec partitioning.

3. if Symantec partitioning is not possible go with manual secondary partitioning of the ADSO at table level. because Primary level partitioning to all the table done automatically. You can only manually partition the Active table by range.

![](/legacyfs/online/storage/blog_attachments/2023/03/Partioning.png)

Hope this will help. In the next blog using this concept I will discuss about a standard,common  BW/BI architecture of a project a developer can adopt.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsummary-of-different-type-asdo-in-sap-bw-bw-4hana-and-functionalities%2Fba-p%2F13550378%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Top 10 SAP Cloud ALM News September 2025](/t5/technology-blog-posts-by-sap/top-10-sap-cloud-alm-news-september-2025/ba-p/14230396)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [🚀 Remember the pioneering days of SAP ECC?](/t5/technology-blog-posts-by-members/remember-the-pioneering-days-of-sap-ecc/ba-p/14229517)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [🚀 Mastering the Essentials: Your Journey into SAP S/4HANA Starts Here!](/t5/technology-blog-posts-by-members/mastering-the-essentials-your-journey-into-sap-s-4hana-starts-here/ba-p/14229489)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [The Ultimate Guide to SAP S/4HANA Master Data - Part 5](/t5/technology-blog-posts-by-members/the-ultimate-guide-to-sap-s-4hana-master-data-part-5/ba-p/14229426)
  in [Technology Blog Posts by ...