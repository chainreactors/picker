---
title: Migrate / Upload Open Production Order in SAP Cloud 2208
url: https://blogs.sap.com/2022/10/19/migrate-upload-open-production-order-in-sap-cloud-2208/
source: SAP Blogs
date: 2022-10-20
fetch_date: 2025-10-03T20:22:48.257607
---

# Migrate / Upload Open Production Order in SAP Cloud 2208

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Migrate / Upload Open Production Order in SAP Clou...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66158&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Migrate / Upload Open Production Order in SAP Cloud 2208](/t5/enterprise-resource-planning-blog-posts-by-members/migrate-upload-open-production-order-in-sap-cloud-2208/ba-p/13539814)

![aravind_rr](https://avatars.profile.sap.com/8/b/id8b5d869b21962a68dec33f06165db7912422f4fc62f05be811c39abef176e93c_small.jpeg "aravind_rr")

[aravind\_rr](https://community.sap.com/t5/user/viewprofilepage/user-id/40037)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66158)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66158)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13539814)

‎2022 Oct 19
8:47 PM

[16
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/66158/tab/all-users "Click here to see who gave kudos to this post.")

5,297

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Data Migration](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Data%2520Migration/pd-p/be32fdc2-968e-4717-97e2-1be5fb65bf99)
* [SAP S/4HANA Cloud Public Edition Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Manufacturing/pd-p/2b555401-a867-4c2d-9d12-e709d78d635f)
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [SAP S/4HANA migration cockpit](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520migration%2520cockpit/pd-p/791935194581077217831679640306539)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [SAP S/4HANA migration cockpit

  Software Product Function](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2Bmigration%2Bcockpit/pd-p/791935194581077217831679640306539)
* [SAP S/4HANA Cloud Public Edition Manufacturing

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BManufacturing/pd-p/2b555401-a867-4c2d-9d12-e709d78d635f)
* [SAP S/4HANA Cloud Public Edition Data Migration

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BData%2BMigration/pd-p/be32fdc2-968e-4717-97e2-1be5fb65bf99)

View products (4)

Hi all,

**Introduction:**

* I am SAP S/4 Hana Production Planning consultant. Due to some internal reason, My client is asking Open Production Order creation by upload method in SAP system

* **Previously we don’t have any SAP Standard facility to upload the Open Production orders in SAP system.**

* But in “Rise with SAP” Public Cloud 2208, SAP given the Proficiency to upload Open Production Order in “Migrate Your Data”.

* People who follow manual Production Order creation method & want to create them into Upload mode, then this blog is for you.

* This blog provides an overview of how to Upload Open Production Order in SAP S/4HANA Cloud 2208.

* Here we can able to create multiple number of Open Production Orders in a Single upload.

* This Production Order Upload is applicable for both “**Internal and External Number ranges**” of Different Production Order types.

After migration, all Production orders will show the status Only as **Created.**

**Scope Item:**

* Data Migration to SAP S/4HANA from Staging (‏2Q2‏), kindly check you have activate this Scope ID.

Let’s see how to upload the Open Production order with Internal Number range by step by steps in detail.

Steps,

1. Project creation

2. Download Template

3. Upload

4. Prepare

5. Mapping Task

6. Simulate

7. Migrate

**Step 1:**

Open your “Migration Cockpit” tile,

![](/legacyfs/online/storage/blog_attachments/2022/10/1-60.png)

Create New Migration “Project” for upload ,

![](/legacyfs/online/storage/blog_attachments/2022/10/2-23.png)

In Migration objects search “Production Order” , you can found object same as below.

![](/legacyfs/online/storage/blog_attachments/2022/10/3-17.png)

Then select & move the Object from Available Migration Objects to Selected Migration Objects.

Click ‘Review’. No need to add additional Objects.

Finally, Project Created.

**Step 2:**

Download **XML** template file from your Project,

![](/legacyfs/online/storage/blog_attachments/2022/10/4-14.png)

**Template Preparation:**

After download XML template file, we can see the Mandatory fields, that need to be maintained inside the excel template.

Based on the date that you plan for Production, select the scheduling type accordingly (forward scheduling, backward scheduling, etc.)

![](/legacyfs/online/storage/blog_attachments/2022/10/5-16.png)

Maintain the mandatory fields along with your required fields,

![](/legacyfs/online/storage/blog_attachments/2022/10/6-20.png)

Suppose if your Production Order Number range is Maintained with **Internal number range**,

Then give random number as like “1” given below, system automatically convert your default Number range inside SAP system.

![](/legacyfs/online/storage/blog_attachments/2022/10/7-11.png)

**Note:** Same Production Order number should not be repeat for the any other Production Order Number. And for External Number range give the Production Order number accordingly.

Upload template is ready !

**Step 3:**

Now select “Upload File” on your project,

![](/legacyfs/online/storage/blog_attachments/2022/10/8-8.png)

Then choose “Upload” and select the **XML** file from your desktop,

![](/legacyfs/online/storage/blog_attachments/2022/10/9-8.png)

System will validate the file and give successful message.

![](/legacyfs/online/storage/blog_attachments/2022/10/10-3.png)

**Step 4:**

Then go for "Prepare",

![](/legacyfs/online/storage/blog_attachments/2022/10/11-3.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/12-4.png)

Select the “Prepare Staging Tables”, it will go and prepare the tables to upload.

![](/legacyfs/online/storage/blog_attachments/2022/10/13-4.png)

**Step 5:**

Then go for "Mapping Tasks",

Need to Complete the Open task before going to Next step,

Below displayed five Tasks need to be confirmed one by one. It is done by manually,

![](/legacyfs/online/storage/blog_attachments/2022/10/14-3.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/15-3.png)

Once confirming all five Task system gives green signal,

![](/legacyfs/online/storage/blog_attachments/2022/10/16-3.png)

**Step 6:**

Then go for "Simulate",

![](/legacyfs/online/storage/blog_attachments/2022/10/17-4.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/18-3.png)

Simulate “All instances”

In this simulation stage, if values are maintaining with any errors system will intimate. Again solving the errors complete the simulation step.

**Step 7:**

Then go for "Migrate",

![](/legacyfs/online/storage/blog_...