---
title: Implement Delta mechanism in SAP BODS – Summary
url: https://blogs.sap.com/2022/12/31/implement-delta-mechanism-in-sap-bods-summary/
source: SAP Blogs
date: 2023-01-01
fetch_date: 2025-10-04T02:50:45.781510
---

# Implement Delta mechanism in SAP BODS – Summary

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Implement Delta mechanism in SAP BODS - Summary - ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161434&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Implement Delta mechanism in SAP BODS - Summary - SCD1, SCD2 and SCD3](/t5/technology-blog-posts-by-members/implement-delta-mechanism-in-sap-bods-summary-scd1-scd2-and-scd3/ba-p/13558392)

![pallab_haldar](https://avatars.profile.sap.com/4/2/id42d0a352096e2fd071fe39e7ec5b73f1f20abf1d7ce6542aa72c8246918879b7_small.jpeg "pallab_haldar")

[pallab\_haldar](https://community.sap.com/t5/user/viewprofilepage/user-id/594699)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161434)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161434)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558392)

‎2022 Dec 31
5:33 AM

[1
Kudo](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161434/tab/all-users "Click here to see who gave kudos to this post.")

7,407

* SAP Managed Tags
* [SAP Data Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Services/pd-p/01200314690800000395)

* [SAP Data Services

  SAP Data Services](/t5/c-khhcw49343/SAP%2BData%2BServices/pd-p/01200314690800000395)

View products (1)

In this session I am going to discuss about the implementation of delta mechanism in **SAP BODS**. But before that we will go through few Transformations which is required for implement Delta Mechanism both for master data and transaction data flow. These major transformations  are given below -

**1. Table Comparison :** Used to compare data between Source and Target Table/Flat files. Others and  return opcode for Insert or update based on the expected changed column you defined in the transformation. It is not mandatory but good practice to use Query transform before table comparison to project/select the specific data. Key Generation is not mandatory or map function is not mandatory with Table comparison but in different scenario where insert required for update operation i.e. historical preservation needed they Key Generation and map Operation is useful.

![](/legacyfs/online/storage/blog_attachments/2022/12/Table-comparison-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Table-comparison.png)

**2. Map\_Operation :**  Modify **Opcodes (I/U/D)** operations. Allows conversion between opcodes provided as a input from previous transformation. After map operation use can only use transformation that understand opcode or a permanent table. Query transformation is optional to use.
The ‘Map\_Operation’ transform changes the operation codes on the input data sets.

![](/legacyfs/online/storage/blog_attachments/2022/12/MAP1.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/MAP2.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/MAP3.jpg)

3. **History Preservation :**  This transformation is used to keep historical data which is updated as a separate row and set the flag to 'N' and for new data row, set the flag to 'Y'. With Key\_Generation transform history preservation transform gives better result. When source table row has operation code of **Insert/Update** then it **insert** a new record in the target table.

The below 4 field is preferable in Target Table structure to for History Preservation -

* **S-key** (surrogate key) will act as the primary key as you will get duplicate records

* **STRT\_DATE** - have the valid from date

* **END\_DATE** - have the change date

* **Flag** Indicating  the current record or the old record.

Also preferable to have start and end date in the source column as well. Using History preservation transform with Table comparison and Key generation is preferable.

![](/legacyfs/online/storage/blog_attachments/2022/12/History-Preservation-4.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/History-Preservation3.png)

**4. Key Generation :** This transformation generate and extra key in incremental order to identify the old and new record inserted.

Using History preservation transform with Table comparison and Key generation is preferable.

![](/legacyfs/online/storage/blog_attachments/2022/12/Key-Generation.png)

Now we will discuss different delta mechanism implementation in BODS using those above transformation.

Most common and popular types of delta mechanism are SCD Types and CDC types (source and Target Based) which we are going to discuss.

**A. SCD (Slow Changing Dimension) Types :**

**1. SCD1 :**  In this techniques, we not save any historical data. If there is any changes on source data or row then  it override the old data with new data in the  target table row. No Opcodes(I/U/D) conversion performed.

This scenario is needed when organization do not requirement to keep historical data.

![](/legacyfs/online/storage/blog_attachments/2022/12/SCD1-T2.png)

Data flow will looks like below -

![](/legacyfs/online/storage/blog_attachments/2022/12/Table-comparison-2-1.png)

In a better way you can do the bellow flow also for **SCD1** -

![](/legacyfs/online/storage/blog_attachments/2022/12/SCD1_U.png)

**2. SCD2 Type :** Using SCD2 mechanism for each updated record a new row inserted and set flag to 'Y' and the Old record row set flag to 'N'.   we are keeping both the old and the new data using separate row. Using this technique we can keep unlimited old record i,e. history preservation.

Below mandatory  Opcodes(I/U/D) conversion performed -

U->I  i.e. UPDATE--> INSERT

I -> I  i.e. INSERT--> INSERT

![](/legacyfs/online/storage/blog_attachments/2022/12/SCD3.png)

**3. SCD Type 3 :**

In this type we store the last updated or modified record along with current record. An additional column added to capture the change column last change value. We only consider the current and the last changed value to be store as a column in the database.

For our case we changing EMAIL\_ID so in our case there will be an additional column  will be **OLD\_EMAIL\_ID.**

![](/legacyfs/online/storage/blog_attachments/2022/12/SCD3_fina.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/SCD3_diagram.png)

**Query Node :**

![](/legacyfs/online/storage/blog_attachments/2022/12/Query-node.png)

Inset Query Node  :

![](/legacyfs/online/storage/blog_attachments/2022/12/Insert-Query.png)

**Update Query node :**

![](/legacyfs/online/storage/blog_attachments/2022/12/Update3.png)

Map Operation :

![](/legacyfs/online/storage/blog_attachments/2022/12/MAP-Operation.png)

**3. SCD Type 4 :** Function wise SCD Type 4 is similar to SCD Type 2 but when changes made rapidly to the source data then volume increate and need to implement SCD Type where the change data store in another target table. This is not frequently use.

In my next blog I will discuss about the Source base CDC and Target Based CDC and Between CDC and SCD which we will use in which scenario.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment]...