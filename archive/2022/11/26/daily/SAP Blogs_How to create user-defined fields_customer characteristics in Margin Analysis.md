---
title: How to create user-defined fields/customer characteristics in Margin Analysis
url: https://blogs.sap.com/2022/11/25/how-to-create-user-defined-fields-customer-characteristics-in-margin-analysis/
source: SAP Blogs
date: 2022-11-26
fetch_date: 2025-10-03T23:48:45.869889
---

# How to create user-defined fields/customer characteristics in Margin Analysis

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to create user-defined fields/customer charact...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51631&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to create user-defined fields/customer characteristics in Margin Analysis](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-create-user-defined-fields-customer-characteristics-in-margin/ba-p/13558519)

![AlinaVranceanu](https://avatars.profile.sap.com/2/d/id2db34cadc4bf3d5ab51c017b13d03ddd674860bac8ed6cf93b0903e7f4dcda47_small.jpeg "AlinaVranceanu")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AlinaVranceanu](https://community.sap.com/t5/user/viewprofilepage/user-id/304573)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51631)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51631)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558519)

‎2022 Nov 25
6:38 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51631/tab/all-users "Click here to see who gave kudos to this post.")

17,862

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN Profitability Analysis](https://community.sap.com/t5/c-khhcw49343/FIN%2520Profitability%2520Analysis/pd-p/368252775582391257383490099411464)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN Profitability Analysis

  Software Product Function](/t5/c-khhcw49343/FIN%2BProfitability%2BAnalysis/pd-p/368252775582391257383490099411464)

View products (3)

If you wonder what are the options to create user-defined fields/customer characteristics in Margin Analysis and what are the pros and cons of each method, I will try to explain them in this article.

We have now 3 ways of creating COPA characteristics:

(1) Until SAP S/4HANA Release 2020, customer characteristics could be created only with the transaction "Maintain Characteristics" (KEA5) for Profitability Analysis. This is still available, but not recommended anymore. I will detail later the reasons we do not recommend the use of it anymore.

(2) As of SAP S/4HANA Release 2020, you can also create user-defined fields/customer characteristics (COPA characteristics) with the application "Custom Fields and Logic" for the business context "Accounting: Market Segment" for the Profitability Analysis component.

![](/legacyfs/online/storage/blog_attachments/2022/11/1-90.png)

From SAP S/4HANA Release 2021, “Custom Field and Logic” app it is deprecated, you can use “Custom Fields” and “Custom Logic” apps.

(3) A third possibility is to create an append in include INCL\_EEW\_MARKET\_SEGMENT\_PS via SE11 and add a custom field (created via SE11) with reference to an existing Data element or using an existing Check Table. Afterwards enable this new field for Business Context: Market Segment via transaction SCFD\_EUI, meaning the field will then be available for the "Custom Fields and Logic" app. Even if it looks more complex than option (2), this option may give big customers (using a high number of COPA characteristics) more flexibility than option (2).

Let’s analyze the three options and see what the differences, advantages and disadvantages between the three are.

* As mentioned at the beginning, KEA5 is still available in on-premise, but not recommended anymore. In cloud it is not available.

* Future developments for user-defined fields/customer characteristics will take place only on the basis of “Custom Fields and Logic app” (2) + (3). It is planned that, in time, this app will take over the previous functionalities of the transaction KEA5. Why is this important to know? **If you create the user-defined fields/customer characteristics using the old transaction KEA5 (1), these fields will not be available in the CDS views, API`s or SAP Fiori UI`s.** Moreover, there is no standard solution to make these fields available in CDS views, API`s or SAP Fiori UI`s for the time being.

* **Only user defined fields/customer characteristics created with the "Custom Fields and Logic" app (2) and the ones created via SE11+SCFD\_EUI (3) are automatically enabled for CDS views, SAP Fiori Ui`s or API`s.**

You might think now:” if I have a customer characteristic created via KEA5 why I would not use option (3) and to enable it for the "Custom Fields and Logic" app using SCFD\_EUI”?

* **It is not possible to transfer existing characteristics, which were created via transaction KEA5 to the application Custom Fields and Logic app**. Activities relating to the transaction "Enable Fields for Custom Field App" (SCFD\_EUI) are not available for the old characteristics. SAP strongly recommends that you do not migrate these characteristics to the applications "Custom Fields and Logic" in any way. This would result in data loss and system unusability.

* About the standard fields which can be used as COPA characteristics and are available for CDS views, SAP Fiori UI`s or API`s, well not every standard field is available. Only those documented in the following link: [APIs for General Ledger Accounting](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b978f98fc5884ff2aeb10c8fdeb8a43b/2c0ccd5780726264e10000000a4450e5.htm)

### (2) **How to create** **user-defined fields/customer characteristics with the Custom Fields and Logic app**

In the Custom Fields and Logic app, select the Business Context: “Accounting Market Segment”. Only fields created for Business Context: “Accounting Market Segment” can be assigned to an operating concern.

**There are 3 types of user-defined fields/customer characteristics**

![](/legacyfs/online/storage/blog_attachments/2022/11/2-52.png)

If you choose to use type Code List a Check Table will get generated automatically, you need to fill the length of the fields and you have the possibility to maintain the values or load them from csv file directly in the app.

![](/legacyfs/online/storage/blog_attachments/2022/11/3-46.png)

The check table cannot be maintained via SM30, the characteristics can be maintained only via the "Custom Fields and Logic" app, manually or via file upload. Once the user-defined field/customer characteristic is being created/changed/updated it needs to be published. This requires development rights.

![](/legacyfs/online/storage/blog_attachments/2022/11/1-92.png)

### Why option (3) is important as a variant of option (2)?

When you create the new custom field, with this option, you might use existing Data element or using an existing Check Table you have created, it doesn’t have to be the tables which are automatically generated as with the option (2). You can create your Check...