---
title: SAP Data Migration Cockpit – Nutshell
url: https://blogs.sap.com/2023/02/19/sap-data-migration-cockpit-nutshell/
source: SAP Blogs
date: 2023-02-20
fetch_date: 2025-10-04T07:32:45.089824
---

# SAP Data Migration Cockpit – Nutshell

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP Data Migration Cockpit - Nutshell

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68529&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Data Migration Cockpit - Nutshell](/t5/enterprise-resource-planning-blog-posts-by-members/sap-data-migration-cockpit-nutshell/ba-p/13569981)

![ashishpinjwani](https://avatars.profile.sap.com/7/6/id76b2b81b71aaa3f47a7e436cad34a38e695d2e5b31e62602db2f7d226828ccaa_small.jpeg "ashishpinjwani")

[ashishpinjwani](https://community.sap.com/t5/user/viewprofilepage/user-id/685096)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68529)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68529)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569981)

‎2023 Feb 19
7:45 PM

[19
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68529/tab/all-users "Click here to see who gave kudos to this post.")

28,737

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Data Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Services/pd-p/01200314690800000395)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP Information Steward](https://community.sap.com/t5/c-khhcw49343/SAP%2520Information%2520Steward/pd-p/01200314690800001657)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)

* [SAP Data Services

  SAP Data Services](/t5/c-khhcw49343/SAP%2BData%2BServices/pd-p/01200314690800000395)
* [SAP Information Steward

  SAP Information Steward](/t5/c-khhcw49343/SAP%2BInformation%2BSteward/pd-p/01200314690800001657)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)

View products (6)

Hello Learners,

Hope you all are doing Great!

Welcome back to my data migration blog series.

**Purpose of this Blog :**

With introduction of S4 HANA, SAP has introduced us to many new tools built in the system. Today we will talk about one such tool used for data migration in S4 HANA, **SAP Migration Cockpit.**

I will try to cover the details which I have got over the period by working on this tool.

**What’s in it for you?**

The blog will explain the different pieces of migration cockpit which will give you the very good start and understanding of tool.

Let’s get into the blog!

**Overview -**

Migration cockpit is SAP provided tool in S4 Hana for data migration purpose. This tool has different approaches for migrating data from SAP or Non SAP system through files, tables or direct transfer. Tool comes with built in content/objects for data migration like products, business partners etc.

**Tool Access -**

Tool is available to be accessed in GUI through tcode as well as FIORI app in recent S4 versions.There have been significant changes in features between both the options but the end to end process is same.

*Tcode Way-*

LTMC (Legacy Transfer Migration Cockpit) is the tcode to access the tool in SAP GUI, user interface will open up in interner explorer browser. (see screenshot) Using this interface you can work with projects you created or you can create new projects also.

![](/legacyfs/online/storage/blog_attachments/2023/02/LTMC.png)

LTMC Tcode

*Fiori Way -*

You can access the fiori GUI using tcode (/n/ui2/flp) or through direct link. Once the fiori is up and running you can look for app called "Migrate Your Data" to access migration cockpit.

![](/legacyfs/online/storage/blog_attachments/2023/02/Fiori-Project.png)

Migration Cockpit main screen- Fiori

**What to use from above?**

Old versions including S4 hana 2020 and prior will allow you to use LTMC in full mode. SAP introduced fiori app from 2020 version. So 2020 version you will have both options available to you for using migration cockpit but versions released after 2020 will only allow fiori app method to access migration cockpit and LTMC will only be available as read only option.

*Note : There is one more important tcode associated with migration cockpit which is LTMOM used for customization purposes, will have more details in the later section of blog.*

**Data Migration Approaches -**

There are widely 3 migration approaches in migration cockpit-

1. *File Based Approach* -

   * In this approach, SAP provides in built templates for the data migration for various sap data objects.

   * This is suitable when you have less complex data migration requirements and volume is not huge.

   * This supports migration from NON SAP/SAP to S4 Hana

2. *Staging Tables based Approach* -

   * In this approach, staging tables are created in HANA DB for data objects which can be populated using ETL tool.

   * This is suitable for any complex data migration requirements and for high volumes of data.

   * This supports migration from NON SAP/SAP to S4 Hana

3. *Direct Transfer Approach*

   * In this approach, direct connection is created between SAP system to S4 Hana system for data transfer

Based on data migration requirement for business suitable approach is selected.

To use any approach you would need to create project first and set it up correctly based on approach requirements. select the data objects as per scope and make sure dependecies are also taken care.

**Data Migration Process -**

4 step guided migration process is built in migration cockpit for carrying out the data migration.

**Step 1- Validate Data -** This step validates the data from templates or tables and throws any errors encountered in configs etc

**Step 2 - Convert Values-**

* This step is used for performing value mapping for fields from source to target. You can view, edit any source to target value mappings for fields in use.

* Correct mapping of all values is must in this step

* You can export import value mappings when you have larget set of source to target values. LTMC generates semi colon separated csv file while exporting and it expects same format for import whereas fiori has predefined xml template for value mappings also which could be used.

**Step 3 - Simulation of Data -** Migration cockpit does data simulation before actual load to see if there any more data validation issues before the the final import of data

**Step 4- Import Data -**

* This is the step where actually the data is migrated to system, you may see some errors on this step also

* if any errors encontered in this step, those record...