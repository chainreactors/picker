---
title: SAP BW Bridge: New Features in Q3 2022
url: https://blogs.sap.com/2022/10/27/sap-bw-bridge-new-features-in-q3-2022/
source: SAP Blogs
date: 2022-10-28
fetch_date: 2025-10-03T21:06:51.050813
---

# SAP BW Bridge: New Features in Q3 2022

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BW Bridge: New Features in Q3 2022

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159916&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BW Bridge: New Features in Q3 2022](/t5/technology-blog-posts-by-sap/sap-bw-bridge-new-features-in-q3-2022/ba-p/13556105)

![kurzdo93](https://avatars.profile.sap.com/f/0/idf0b109c03f870f5bbb5681f39362f028bdc0734954253c658d7ea427d96c2756_small.jpeg "kurzdo93")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[kurzdo93](https://community.sap.com/t5/user/viewprofilepage/user-id/41772)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159916)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159916)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556105)

‎2022 Oct 27
6:03 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159916/tab/all-users "Click here to see who gave kudos to this post.")

1,863

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

![](/legacyfs/online/storage/blog_attachments/2022/10/2022-Q3-2208-BWB-scaled.jpg)

The 2208 release of the *SAP Data Warehouse Cloud, SAP BW bridge* has been shipped with SAP BTP ABAP Environment.

**The new release contains the following main features:**

* Import hierarchies from the SAP BW bridge system

* Changing Technical Content InfoObjects

* Filtering by Attribute Name for CompositeProviders

 In addition, to the new features there is a [troubleshooting guide](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/ecce5bb08ae24ed089497fc00c2320d8/21ab1e7bfece4d22a3e58c296abd4340.html) available now in the online documentation. It explains how to identify and solve configuration issues in the connectivity of on-premise source systems to SAP BW bridge.

### Import hierarchies from the SAP BW bridge system

With SAP BW bridge 2208, you can now import hierarchies from the SAP BW bridge tenant into SAP Data Warehouse Cloud.

For every InfoObject with hierarchies, SAP BW bridge automatically creates the required views: the hierarchy directory view, the hierarchy directory text view, and the hierarchy view. These views are created when the InfoObject is activated. Note that InfoObjects which had been created and activated prior to release 2208 must once be activated manually to generate the hierarchy views.

You can import these views into SAP Data Warehouse Cloud as remote tables. In case you do not see the hierarchy views in the import dialog, you may simply activate the InfoObject and check again.

The hierarchy directory view shows all master data hierarchies with reference to an InfoObject, except for remote hierarchies or hierarchies that use link nodes.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture1-84.png)

More information about hierarchies on the SAP Help Portal:

* [New Features in Version 2022.19](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/5a2cf6cf78ee4f03bbd49714d79d8559/63279a7e47c74277bdf32852f2df88f2.html?locale=en-US)

* [Hierarchy (New)](https://help.sap.com/docs/SAP_BW_BRIDGE/b3701cd3826440618ef938d74dc93c51/0c4e19d245ce488fa1a9a06c4229fdd7.html?locale=en-US)

### Changing Technical Content InfoObjects

In SAP BW bridge, new objects like InfoObjects (either created manually, installed from Business Content, or transferred via shell or remote conversion) must be assigned to an ABAP development package. Assigning new objects to the local package $TMP is not possible in SAP BW bridge.

However, technical content InfoObjects, e.g., 0CALDAY, are automatically created and assigned to the local package $TMP when the BW bridge tenant is provisioned. Due to this assignment to $TMP, they cannot be changed.

To be able to enhance or change technical content InfoObjects, you can now assign them to one of your transportable packages in the BW modeling tools. To do this, call the InfoObject maintenance, go to the General screen area on the Properties tab page and press Change.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture2-61.png)

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture3-46.png)

Once the InfoObject is assigned to an ABAP development package and a transport request, you can modify the InfoObject. Note that the InfoObject then no longer receives any automatic changes from SAP.

More information about [Changing Technical Content InfoObjects](https://help.sap.com/docs/SAP_BW_BRIDGE/b3701cd3826440618ef938d74dc93c51/a5eb401f06524c0e8322925b8dd60106.html?locale=en-US) on the SAP Help Portal.

### Filtering by Attribute Name for CompositeProviders

Navigation attributes of InfoObjects can be selected in the Output tab of CompositeProviders. The usability of this dialog has been improved. You can now filter by attribute names when selecting navigation attributes.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture4-40.png)

More information about [Filtering by Attribute Name for CompositeProviders](https://help.sap.com/docs/SAP_BW_BRIDGE/b3701cd3826440618ef938d74dc93c51/d43fccab3c0745d9b30706c1e95652cd.html) on the SAP Help Portal.

### More information ![:backhand_index_pointing_down:](/html/@C4F818A309A90CCCB0A49E2B6A8FEF3E/emoticons/1f447.png ":backhand_index_pointing_down:")

You will find more information about what is new or changed with SAP BW bridge or SAP Data Warehouse Cloud in the sections on the SAP Help Portal:

* [What’s new in SAP Data Warehouse Cloud, SAP BW bridge](https://help.sap.com/docs/SAP_BW_BRIDGE/b3701cd3826440618ef938d74dc93c51/5955c30226eb4674b77ca2d04690b764.html?locale=en-US)

* [What's New in SAP Data Warehouse Cloud](https://help.sap.com/viewer/5a2cf6cf78ee4f03bbd49714d79d8559/cloud/en-US)

If you are interested in additional information, see our [SAP Data Warehouse Cloud Community](https://community.sap.com/topics/data-warehouse-cloud/). On our Community you will find further product information, various subpages with more detailed information about [Getting Started with SAP Data Warehouse Cloud](https://community.sap.com/topics/data-warehouse-cloud/getting-started), [Business Content](https://community.sap.com/topics/data-warehouse-cloud/business-content), as well as content for [Best Practices & Troubleshooting](https://community.sap.com/topics/data-warehouse-cloud/best-practices-troubleshooting) and more.

Labels

* [Product Updates](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap/label-name/product%20updates)

* [sap bw bridge](/t5/tag/sap%20bw%20bridge/tg-p/board-id/technology-blog-sap)
* [SAP Data Warehouse Cloud SAP BW Bridge](/t5/tag/SAP%20Data%20Warehouse%20Cloud%20SAP%20BW%20Bridge/tg-p/board-id/technology-blog-sap)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, regist...