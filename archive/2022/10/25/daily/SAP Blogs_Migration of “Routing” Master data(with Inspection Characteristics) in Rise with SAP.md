---
title: Migration of “Routing” Master data(with Inspection Characteristics) in Rise with SAP
url: https://blogs.sap.com/2022/10/24/migration-of-routing-master-datawith-inspection-characteristics-in-rise-with-sap/
source: SAP Blogs
date: 2022-10-25
fetch_date: 2025-10-03T20:46:44.502310
---

# Migration of “Routing” Master data(with Inspection Characteristics) in Rise with SAP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Migration of "Routing" Master data(with Inspection...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66256&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migration of "Routing" Master data(with Inspection Characteristics) in Rise with SAP](/t5/enterprise-resource-planning-blog-posts-by-members/migration-of-quot-routing-quot-master-data-with-inspection-characteristics/ba-p/13541471)

![arunsubu15](https://avatars.profile.sap.com/2/d/id2dac98fcb337e8df630a4e9781350a3b94605a84a35828b3b6a174f37468e950_small.jpeg "arunsubu15")

[arunsubu15](https://community.sap.com/t5/user/viewprofilepage/user-id/40390)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66256)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66256)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13541471)

‎2022 Oct 24
7:22 PM

[9
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66256/tab/all-users "Click here to see who gave kudos to this post.")

7,043

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Data Migration](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Data%2520Migration/pd-p/be32fdc2-968e-4717-97e2-1be5fb65bf99)

* [SAP S/4HANA Cloud Public Edition Data Migration

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BData%2BMigration/pd-p/be32fdc2-968e-4717-97e2-1be5fb65bf99)

View products (1)

Hi Friends...

### **Introduction:**

This blog will guide you with the steps required for migrating “**Routing**” master data (with inspection

characteristics assigned in each operation)into the ***SAP* S/4HANA *Cloud 2208*.**

First, we will see the basic overview of **"Routing" and "SAP S/4 HANA Cloud migration cockpit"**

and its functionalities:-

***Routing:***

**Routing** defines a sequence of activities performed at the work center. Routing plays an

important role in calculating production cost, machine time and labor time.

The routing operation will contain the inspection characteristics which are needed to be inspected

during the in-process checks

***SAP S/4 HANA Cloud Data Migration:***

**SAP S/4HANA Cloud migration cockpit** **is** a tool designed **for customers who have just**

**installed SAP S/4HANA** cloud (Rise with SAP) and want *to transfer* their *business data from*

*SAP or non-SAP software systems*.

**Migration in Sap S/4 HANA Cloud** involves the following steps:-

![](/legacyfs/online/storage/blog_attachments/2022/10/1-59.png)![](/legacyfs/online/storage/blog_attachments/2022/10/2-14.jpg)

*System Setup SAP S/4HANA Cloud Local Database Schema*

### **General Procedure for Transferring Data to SAP S/4HANA Cloud Using Staging Tables**

**Prerequisites:**

For routing migration, we will use the **work center ,master inspection characteristics & sampling**

**procedure** which are already created in the  system. Similarly, the number range for routing can be

external or internal. In our case, we use internal number range.

**Required Roles**

##### ***For SAP S/4HANA Cloud:***

* ##### SAP\_BR\_CONFIG\_EXPERT\_DATA\_MIG

### **Steps for Migration of "Routing" Master data in Cloud System**

**STEP 1:**

Select "**Migrate Your Data Migration Cockpit tile".**

**![](/legacyfs/online/storage/blog_attachments/2022/10/1123-1.png)**

First step is to create a project. In order to create a project, Click “**Create**” icon.

![](/legacyfs/online/storage/blog_attachments/2022/10/4-13.png)

In the initial screen,

1) Enter the project name (Example :-**Production Planning),**

**2) Mass transfer ID & Data retention time**(When a new project is created in the system, a Mass Transfer ID is automatically generated for that project files. To distinguish between projects across systems, this ID is used.) and

3) Ensure that "**Local SAP S/4 hana database schema**" is enabled.

Then, click **Step 2** in order to proceed further.

![](/legacyfs/online/storage/blog_attachments/2022/10/5-15.png)

In this screen, we will be adding the migration objects which are required for our project. In our case, we need to add the objects which are relevant to Production Planning.

Enter the object name “**Routing**” and click search icon.

System will populate the relevant objects. Select the required object and select “**Move to Selected** **Migration Objects***”*  icon to include it to our project. The system moves the object to the Selected Migration Objects area.

![](/legacyfs/online/storage/blog_attachments/2022/10/6-19.png)

Similarly, add all the objects required for Production Planning and click **“Review”.**

**Note:** To remove objects from the **Selected Migration Objects** area, select the migration objects you want to remove and choose the button "**Move"** to Available Migration Objects.

![](/legacyfs/online/storage/blog_attachments/2022/10/7-10.png)

Now, the system will suggest the Predecessor objects which are existing for our selection. Depending upon the requirement, select the options. In our case, we will proceed by Clicking **“Add”** button.

![](/legacyfs/online/storage/blog_attachments/2022/10/8-12.png)

Now Click **“Create project”.**

![](/legacyfs/online/storage/blog_attachments/2022/10/9-7.png)

Our Project “**Production Planning**“ is created.

![](/legacyfs/online/storage/blog_attachments/2022/10/10-9.png)

On the **Migration Project screen**, we can view the migration objects which were previously selected.

![](/legacyfs/online/storage/blog_attachments/2022/10/11-2.png)

To get detailed information about a migration object, choose the migration object name” **Routing”** in the Migration Object column.

![](/legacyfs/online/storage/blog_attachments/2022/10/12-3.png)

The system displays the **Migration Object screen**, where you can view information about the **table** **structure, views, history, technical information** and the **migration object´s documentation** and dependencies.

![](/legacyfs/online/storage/blog_attachments/2022/10/13-2.png)

**STEP 2:**

Next step is to download the required migration Template.  To download the data template for migration object , select the relevant object and click **Download** **Template.**

![](/legacyfs/online/storage/blog_attachments/2022/10/14-10.png)

By default, system will suggest **XML** and **CSV** file format. Select the required file format and click **ok**.

![](/legacyfs/online/storage/blog_attachments/2022/10/15-6.png)

An Excel XML. file for the source data of the migration object opens.

In the **Introduction sheet** we can see the overview about the migration template. For each migration template, you need to specify data for the mandatory sheets, and for the optional sheets that are relevant for your project:

* **Mandatory sheets (orange)**-Mandatory sheets represent the minimum set of data you must provide for data migration. Fill in all mandatory fields.

* **Optional sheets (blue)**

![](/legacyfs/online/storage/bl...