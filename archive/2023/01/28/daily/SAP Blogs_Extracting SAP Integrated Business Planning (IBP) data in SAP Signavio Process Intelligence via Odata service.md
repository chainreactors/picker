---
title: Extracting SAP Integrated Business Planning (IBP) data in SAP Signavio Process Intelligence via Odata service
url: https://blogs.sap.com/2023/01/27/extracting-sap-integrated-business-planning-ibp-data-in-sap-signavio-process-intelligence-via-odata-service/
source: SAP Blogs
date: 2023-01-28
fetch_date: 2025-10-04T05:03:26.342260
---

# Extracting SAP Integrated Business Planning (IBP) data in SAP Signavio Process Intelligence via Odata service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Extracting SAP Integrated Business Planning (IBP) ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/167849&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extracting SAP Integrated Business Planning (IBP) data in SAP Signavio Process Intelligence via Odata service](/t5/technology-blog-posts-by-sap/extracting-sap-integrated-business-planning-ibp-data-in-sap-signavio/ba-p/13579941)

![abhisekdutta](https://avatars.profile.sap.com/d/5/idd531c52ace1f5bcea91807f54ea5f8d53a3ded1b20e4bc0d348d6cf7c3069f66_small.jpeg "abhisekdutta")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[abhisekdutta](https://community.sap.com/t5/user/viewprofilepage/user-id/122631)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=167849)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/167849)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13579941)

‎2023 Dec 21
9:30 AM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/167849/tab/all-users "Click here to see who gave kudos to this post.")

2,325

* SAP Managed Tags
* [SAP Signavio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Signavio/pd-p/088166be-6441-4660-9e5b-1a046de322bf)
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)

* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP Signavio

  Additional Software Product](/t5/c-khhcw49343/SAP%2BSignavio/pd-p/088166be-6441-4660-9e5b-1a046de322bf)

View products (2)

Hello SAP-community,

In this post, we will see how to establish a connection to SAP Integrated Business Planning (IBP) in SAP Signavio using Odata service /odata/IBP/MASTER\_DATA\_API\_SRV. And as test case, we will extract IBP location master data from one planning area and view it in SAP Signavio.

**IBP Prerequisites:**

Below steps should be executed by IBP Consultant with admin role.

1-Choose Communication Management from IBP homepage and click on **Maintain Communication Users** app.

*Maintain Communication Users (a)*

2-Select **NEW** user setup and enter below details

**User Name:** IBP\_COM\_USER

**Description:** IBP\_COM\_USER

**Password** can be generated automatically by clicking **Propose Password** or else manually give any password.

*Maintain Communication Users (b)*

3-Select **Communication Systems** app and click **New**.

*Communication Systems (a)*

4-Enter the system ID and name for the communication system. Then in the General heading in the Technical Data section, checklist Inbound Only. Under Users for Inbound Communication, add the communication user previously created and select the authentication method below.

Choose Save.

**System ID:** SIGNAVIO

**System Name:** SIGNAVIO

**User ID and Password:** IBP\_COM\_USER

*Communication Systems (b)*

5- Select the **Communication Arrangements** app and click **New**.

*Communication Arrangements (a)*

6-Fill the communication scenario as **SAP\_COM\_0720**, enter a name for the communication arrangement, and select the communication system that was previously created.

Also maintain the business user under Additional Properties section.

**Arrangement Name:** SAP\_COM\_0720

**Communication System:** SIGNAVIO

**Corresponding Business User:** CBXXXXXXX

*Communication Arrangements (b)*

7-In order to expose which planning area and master data to be used, we have to enter required planning areas and master data in **Global Configuration app** in IBP.

*Global Configuration (a)*

8-Odata - /IBP/PLANNING\_DATA\_API\_SRV service is used to add planning areas, hence select **FLEXQUERY  PLANNINGAREA**.

Odata -  /IBP/MASTER\_DATA\_API\_SRV service is used to define master data types, hence select **FLEXQUERY  RELEVANT\_MDT\_FOR\_MD\_API**.

*Global Configuration (b)*

**Signavio Prerequisites:**

Below steps should be executed by Signavio Consultant-

1-Login to **SAP Signavio homepage > Process Intelligence > Manage Data > Connections**.

Select Create and enter below details.

**Connection name:** IBP-TEST

**Connection type:** Open Data Protocol

*Connections (a)*

2-Fill Credentials details from IBP communication user and enter the Configuration URL from IBP communication system.

*Connections (b)*

**Configure Data extraction:**

Here in this step, we will extract Location master data from IBP planning area **SAPIBP1**.

1-Create test data in Location master data staging table **INTLOCATION** under planning area **SAPIBP1**.

*Manage Master Data - INTLOCATION*

2-Create new **source data named** - IBP-UWE-Test and select **connection type** – Open Data Protocol.

*Signavio - source data (a)*

3-Click **Next** and select the connection created before. Then click **Create**.

*Signavio - source data (b)*

4-Now the setup is complete.

*Signavio - source data (c)*

5-Click **Add table** option and select the table which needs to extract. Here we are selecting the location master staging table. Click **Next**.

*Signavio - source data (d)*

6-Here we need to select which fields needs to extract for location staging table. Click **Next**.

*Signavio - source data (e)*

7-Now location table can be seen in list of tables here.

*Signavio - source data (f)*

**Final Data extraction:**

1-Click on the **action menu** on right side of tables.

2-Select **Extract** from the list.

3-Extraction process starts, and it can be checked in **Logs** tab.

4-Once job completes – click on the record to show extraction logs.

5-For viewing the data click on **Preview** from **action menu.**

6-IBP test data is visible here.

**Summary:**

After reading this blog, you will be able to integrate IBP data to SAP Signavio using Odata service and this data will be used in Signavio Process data pipelines. Below are the steps covered:

1-IBP configuration

2-Signavio configuration

3-Master data transfer from IBP to Signavio

Like what you’ve read? Please share your thoughts, questions and feedback. Feel free to share on Facebook, Twitter, or LinkedIn using the super-easy share buttons at the bottom! And don’t forget to follow [SAP Signavio @ SAP Community](https://community.sap.com/topics/signavio) & [SAP IBP @ SAP Community](https://community.sap.com/topics/integrated-business-planning) for more content like this.

Thank You...!!

Labels

* [Technology Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/technology%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-sap%2Fextracting-sap-integrated-business-planning-ibp-data-in-sap-signavio%2Fba-p%...