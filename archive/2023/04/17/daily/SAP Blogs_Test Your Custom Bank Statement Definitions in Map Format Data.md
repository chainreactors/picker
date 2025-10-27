---
title: Test Your Custom Bank Statement Definitions in Map Format Data
url: https://blogs.sap.com/2023/04/16/test-your-custom-bank-statement-definitions-in-map-format-data/
source: SAP Blogs
date: 2023-04-17
fetch_date: 2025-10-04T11:32:00.555964
---

# Test Your Custom Bank Statement Definitions in Map Format Data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Test Your Custom Bank Statement Definitions in Map...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50903&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Test Your Custom Bank Statement Definitions in Map Format Data](/t5/enterprise-resource-planning-blog-posts-by-sap/test-your-custom-bank-statement-definitions-in-map-format-data/ba-p/13553827)

![RichardKuba](https://avatars.profile.sap.com/9/e/id9e0b7e5824a5f8f709ccbecccc27a1ae6c8ba3f83acb3c469c6dbd033e2c3c9e_small.jpeg "RichardKuba")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[RichardKuba](https://community.sap.com/t5/user/viewprofilepage/user-id/179617)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50903)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50903)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553827)

‎2023 Apr 16
3:58 PM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50903/tab/all-users "Click here to see who gave kudos to this post.")

4,618

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Localization](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Localization/pd-p/326d1e75-a83c-482d-bcf5-f5f6ac1c8d31)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Localization](https://community.sap.com/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

* [SAP S/4HANA Cloud Public Edition Localization

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BLocalization/pd-p/326d1e75-a83c-482d-bcf5-f5f6ac1c8d31)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Localization

  Topic](/t5/c-khhcw49343/Localization/pd-p/bfcb11f4-d6d5-4b4a-a2ce-2eafb48827a6)

View products (4)

With the release of SAP S/4HANA Cloud 2302 users of Map Format Data can use a new application called ****Test Incoming Format Mappings****. With this tool, it’s easier to define a Format Mapping in **Incoming direction**, for example, custom specifications of MT940, CAMT.053/4, MT300, MT320, etc.

You can now continuously check while defining whether the definition of your format behaves according to given requirements. If it sounds too complicated now, don’t worry. In this blog, we’ll go through the entire process using a simple example from “the world” of bank statements.

Even though we decided to use bank statement and Map Format Data for Incoming Files from Banks, the described process will be the same for **incoming** format mappings defined in other Map Format Data integrations e.g.: Map Format Data for Treasury Correspondence and Map Format Data for Advanced Payment Management.

In this article, I'll refer to various resources such as demo files and XML export of Format Mapping. All these resources can be found as an attachment of SAP Note [3309184 - Test Data to Learn to use Map Format Data (incoming format mappings)](https://launchpad.support.sap.com/#/notes/3309184)****.****

More information about Test Incoming Format Mappings can be found on [SAP Help Portal](https://help.sap.com/docs/SAP_S4HANA_CLOUD/441e7af2267a420996f92fca6131ffab/969f170d5ddf4fc3ba56ac87c0e2294a.html?locale=en-US).

# **Requirements of the Bank Statement**

If your bank requests you to receive an end-of-day bank statement, you have two options. Either use one of the standard formats, which are available within the Manage Incoming Payment Files app, or alternatively, if some customization is required, you can define a completely new mapping format in the Map Format Data for Incoming Files from Banks.

Within this demo we'll show you the process on how to create such customized format mapping in the application emphasizing the testing possibilities of such mapping. Refer to SAP Note’s attachment “**requirement.pdf”, which** represents a simple demo bank requirement, which will be used further on in this document as a base for defining custom flat-file format mapping.

In general, the bank requirements, as well as the format mapping, can be divided into three logical parts – ****header**** (yellow), ****items**** (green), and ****closing/footer**** (purple).

![](/legacyfs/online/storage/blog_attachments/2023/04/000-Requirements.png)*requirement.pdf from SAP Note 3309184*

In the next steps, we'll create the format first, and continue with defining all the logical parts one by one, starting with the header of the statement. For this demo, we'll always test our (even partial) definition in the Test Incoming Format Mappings after defining each part of the format mapping.

# **Format Creation**

Let’s start with the creation of a new flat-file format mapping.

![](/legacyfs/online/storage/blog_attachments/2023/04/001-Click-Create-1.png)

*Go to the Map Format Data and click the Create button above the table.*

![](/legacyfs/online/storage/blog_attachments/2023/04/002-Create-Dialog.png)

*Access the newly created Format Mapping with the arrow at the right end of the row.*

# **Defining a Header**

**If you wish to skip the manual configuration, you can upload “demo\_blog\_header.xml” from the SAP Note [3309184 - Test Data to Learn to use Map Format Data (incoming format mappings)](https://launchpad.support.sap.com/#/notes/3309184). The same step-by-step configuration is explained in the following text.**

According to our demo requirements, the header shall consist of three lines: “Account Information”, “Statement Identification” and “Opening Balance”.

First, we need to define a node of a type “Record Group”. This node type is used to manage relations between records. For example, if a record (or a group of records) is expected to repeat more times, we need to encapsulate it in a record group with a defined number of expected occurrences. Similarly, if only one from a set of records is to be present, the records must be encapsulated in a record group.

As per the demo requirements, we need to include multiple lines (multiple records) in the format mapping definition, therefore we need to define a record group first. We'll name it Start of Format. This record group defines, that we expect only one end-of-day bank statement per file, therefore in the Input Specification of this node we've to set the “Group Repetition” to one.

![](/legacyfs/online/storage/blog_attachments/2023/04/004-Start-of-Format.png)

*Define the node Start of Format.*

As a next step, we'll define the Account Information a...