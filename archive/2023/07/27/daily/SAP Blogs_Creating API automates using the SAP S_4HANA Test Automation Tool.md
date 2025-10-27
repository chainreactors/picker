---
title: Creating API automates using the SAP S/4HANA Test Automation Tool
url: https://blogs.sap.com/2023/07/26/creating-api-automates-using-the-sap-s-4hana-test-automation-tool/
source: SAP Blogs
date: 2023-07-27
fetch_date: 2025-10-04T11:54:44.846575
---

# Creating API automates using the SAP S/4HANA Test Automation Tool

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Creating API automates using the SAP S/4HANA Test ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53014&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating API automates using the SAP S/4HANA Test Automation Tool](/t5/enterprise-resource-planning-blog-posts-by-sap/creating-api-automates-using-the-sap-s-4hana-test-automation-tool/ba-p/13567356)

![Aparna_Vohra](https://avatars.profile.sap.com/4/0/id40ddb9efea8d8a2345734c03d1851c1641d39c92a898ce3436bb0cc87a45de11_small.jpeg "Aparna_Vohra")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Aparna\_Vohra](https://community.sap.com/t5/user/viewprofilepage/user-id/131756)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53014)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53014)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567356)

‎2023 Jul 27
12:03 AM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53014/tab/all-users "Click here to see who gave kudos to this post.")

2,835

* SAP Managed Tags
* [test automation tool for SAP S/4HANA Cloud](https://community.sap.com/t5/c-khhcw49343/test%2520automation%2520tool%2520for%2520SAP%2520S%252F4HANA%2520Cloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [test automation tool for SAP S/4HANA Cloud

  Software Product Function](/t5/c-khhcw49343/test%2Bautomation%2Btool%2Bfor%2BSAP%2BS%25252F4HANA%2BCloud/pd-p/3b727198-80b8-459f-b8ec-5bcf6f9578d5)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (3)

The SAP S/4HANA Cloud Test Automation Tool helps in accelerating business process testing and regression tests. The tool supports standard UI Automation as a way of creating automates and with release CE2105 it was further extended to support API test automation to cater to the needs of our S/4HANA Cloud customers having many options for configurability and extensions.

The primary use-case of integrating the API framework with the Test Automation Tool is to support the automation of SAP S/4HANA Cloud public APIs. We can also achieve seamless integration with the current UI test automation framework where you can create process steps with UI automation and chain it with API automates together into one end to end process. The API framework enables the creation of multiple UI variations in a single automate hence reducing the number of test artefacts created. Support is mainly offered for the automation of both SOAP inbound as well as OData V2 and V4 APIs. As of today the framework supports offered to 459 OData and 123 SOAP APIs.

# Benefits of the API framework

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture1-36.png)

Considering that UI automates might be impacted by changes in underlying application as part of the regular software upgrades, API based execution brings out the following advantages:

* **Robustness** – Since API automates are not UI dependent and are completely based on SAP S/4HANA Public Cloud APIs delivered, it makes the framework consistent and robust until there is a change in the API itself

* **Smart payload generation** – An extremely simple way to generate payloads without knowing how to work with APIs is a unique ability of this framework. Business/functional experts and technical experts can equally work towards generation of payloads

* **Performance** – It takes minimal amount of time to execute an API test automate as there is a single action present for each process step with quick execution in the background.

* **Extensions** – API automates enable an end user to extend API payloads with multiple line items. This can simply be achieved using Copy-Paste functionality in the smart payload tree structure.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture2-27.png)

The API framework ensures efficient, rapid, and reliable solution for easy and quick API automation with a no-code approach. We can easily build automation scenarios which could contain the chaining of both UI and API process steps. The API Framework is based on public APIs that are available on the Business accelerator Hub and supports both ODATA APIs and SOAP APIs (inbound) and allows an end user to create an automated test case or process using a particular API. With the help of a user-friendly guided wizard, one can perform different CRUD operations (Create/Read/Update/Delete) on multiple entities present for that API.

# Working with API automates

For creation of an API automate, the end user is provided with a guided step-by-step wizard where one must select the API Type (ODATA/SOAP) and an S/4HANA Public API from the provided value help. These APIs are available on the SAP Business Accelerator Hub.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture3-22.png)

The Test Automation Tool is designed to support both Business users and more experienced technical users as well. The guided wizard simplifies the process of creating an API test process with ease. Once the desired API is selected, one needs to select Entity types, methods, Operation Types, Entity Operations based on the API type selected.

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture4-21.png)

In case where API requires an input payload, a payload structure will be provided to the end user for populating the payload values so that the test case can be generated. The Payload Structure can be viewed in two ways (as shown in below screenshots):

* **Smart View**: Payload will be visible in tree table format i.e hierarchical structure that would be easy to understand and manipulate for business users.

The following operations can be performed on the smart tree structure -

* **Copy and Paste** – Used to extend payload (e.g extending line items of an entity)

* **Delete** – Used to delete a certain payload property (if applicable)

* **Undo and Redo** – To undo and redo the changes

* **Expand All** – To expand the tree structure to the lowest level

* **Collapse All** – To collapse the tree structure

* **Code View**: Payload will be visible in technical format (json/xml) that would be useful for technical users.

### **Smart View:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture5-20.png)

### **Code View:**

![](/legacyfs/online/storage/blog_attachments/2023/07/Picture7-13.png)

As a user, you will have the provision to a...