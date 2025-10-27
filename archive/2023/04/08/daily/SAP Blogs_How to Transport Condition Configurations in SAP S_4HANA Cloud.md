---
title: How to Transport Condition Configurations in SAP S/4HANA Cloud
url: https://blogs.sap.com/2023/04/07/how-to-transport-condition-configurations-in-sap-s-4hana-cloud/
source: SAP Blogs
date: 2023-04-08
fetch_date: 2025-10-04T11:30:02.979272
---

# How to Transport Condition Configurations in SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* How to Transport Condition Configurations in SAP S...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51101&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Transport Condition Configurations in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-transport-condition-configurations-in-sap-s-4hana-cloud/ba-p/13555464)

![scqllw](https://avatars.profile.sap.com/2/2/id2235b706493af47d45d1af601b2b22868cb62db529b701c6199f6d642b1ffcd1_small.jpeg "scqllw")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[scqllw](https://community.sap.com/t5/user/viewprofilepage/user-id/681260)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51101)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51101)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555464)

‎2023 Apr 07
10:35 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51101/tab/all-users "Click here to see who gave kudos to this post.")

3,518

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (1)

There are two types of configurations related to conditions. One is client specific, such as Condition Type, we call it customizing item. The other one is cross-client, such as Access Sequence, Condition Table, etc., we call it extension item. The relations/dependencies among these configurations are illustrated below.

![](/legacyfs/online/storage/blog_attachments/2023/04/Condition_configurations_categories_and_relations.jpg)

A Condition Type might reference to an Access Sequence. An Access Sequence is referencing to one or more Condition Tables. A Condition Table is referencing to one or more Field Catalogs. While transporting these configurations, to avoid data inconsistency in P-system, the referenced item needs to be transported first, or together with the referencing item.

However, different tools/apps are used for transporting different types of configurations. If the items are of different types, they can not be transported together. For example, Condition Type (customizing item) and Access Sequence (extension item) could not be transported together. In this case, we need to transport the Access Sequence to P-system first separately.

But what tools/apps are used for transporting different types of configurations? That is depending on the system landscape and configuration environment of your SAP S/4HANA Cloud installation. For your quick reference, this has been summarized in the tables below.

### Export Operation

![](/legacyfs/online/storage/blog_attachments/2023/04/Export_apps_v2.jpg)

### Import Operation

![](/legacyfs/online/storage/blog_attachments/2023/04/Import_apps_v2.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/03/Legend.jpg)

Below are some useful links for reference.

**System Landscapes in SAP S/4HANA Cloud**: [https://help.sap.com/docs/SAP\_S4HANA\_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/aa60b129af7b4ce8ae052618...](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/aa60b129af7b4ce8ae052618c8315d29.html)

**3SL and Transport Management:** [https://help.sap.com/docs/SAP\_S4HANA\_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e022623ec1fc4d61abb398e4...](https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/e022623ec1fc4d61abb398e411670200.html)

**Q to P Transport Process:** [https://help.sap.com/docs/SAP\_S4HANA\_CLOUD/b17ac6f2e3e34629a5b205a5b2c8ea11/f2032855a2014d6f98d5faee...](https://help.sap.com/docs/SAP_S4HANA_CLOUD/b17ac6f2e3e34629a5b205a5b2c8ea11/f2032855a2014d6f98d5faeef5bdc151.html)

**Export Software Collection:** [https://help.sap.com/docs/SAP\_S4HANA\_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/6896de5f70c54753ac028f44...](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/6896de5f70c54753ac028f444eafa16f.html)

**Import Collection:** [https://help.sap.com/docs/SAP\_S4HANA\_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/cf87e503ddfd4a60a402a444...](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0f69f8fb28ac4bf48d2b57b9637e81fa/cf87e503ddfd4a60a402a44453c90c04.html)

## FAQ

**Q1**: Our SAP S/4HANA Cloud installation is based on 2-System Landscape. While attempting to release the business change project(BCP) in Q-system, it gets blocked by external checks. The error message indicates to transport the access sequence ZZZZ for condition type YYYY (see screenshot below). What should I do?

![](/legacyfs/online/storage/blog_attachments/2023/03/03.a_BCP_external_check_error-1.jpg)

**A**: Perform below two steps to transport the referenced access sequence ZZZZ to P-system first. These two steps need to be performed by key user Administrator.

1. In Q-system, add the access sequence ZZZZ into a software collection and export the software collection using app 'Export Software Collection'.

2. In P-system, import the software collection using app 'Import Collection'.

After that, you can try to release the BCP again.

Similarly, if the error message indicates to transport the extension item (like condition table, field catalog, etc.) to P-system first, or the extension item not exist in P-system, you can do the same to transport the referenced extension item to P-system first.

**Q2**: I have created a new Access Sequnce (e.g. ZMR6), how to add it to a software collection?

**A**: Assuming that you have created the software collection, follow below steps to add the target Access Sequence ZMR6 to the software collection.

1. Login to the customizing tenant (either Q-system in 2SL or D-system in 3SL) as key user Administrator.

2. Launch app 'Export Software Collection'.

3. Select the software collection to which you want to add the Access Sequence.

4. Under tab 'Content', click button 'Add Items'.![](/legacyfs/online/storage/blog_attachments/2023/04/Add_AS_to_SW_Collection_01.jpg)

5. Select Type 'Access Sequence of Condition Technique (CT\_ACC\_SEQ)', and click button 'Go'.![](/legacyfs/online/storage/blog_attachments/2023/04/Add_AS_to_SW_Collection_02.jpg)

6. Select the target Access Sequence ZMR6, then click button 'OK'.![](/legacyfs/online/storage/blog_attachments/2023/04/Add_AS_to_SW_Collection_03.jpg)Note that, Access Sequence technical name ZMR6 has been prefixed with 'YY1\_AV ' here, together they form the identifier of this Access Sequence. 'YY1\_' is the namespace for extension items created in customizing tenant, 'A' means it's for usage Sales, 'V' means it's for application Pricing.

After above steps, you will see the extension item 'YY1\_AV ZMR6' got successfully added to the software collection.![](/legacyfs/online/storage/blog_attachments/2023/04/Add_AS_to_SW_Collect...