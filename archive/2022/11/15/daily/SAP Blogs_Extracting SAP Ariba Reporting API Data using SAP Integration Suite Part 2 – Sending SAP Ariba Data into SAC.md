---
title: Extracting SAP Ariba Reporting API Data using SAP Integration Suite Part 2 – Sending SAP Ariba Data into SAC
url: https://blogs.sap.com/2022/11/14/extracting-sap-ariba-reporting-api-data-using-sap-integration-suite-part-2-sending-sap-ariba-data-into-sac/
source: SAP Blogs
date: 2022-11-15
fetch_date: 2025-10-03T22:45:18.641150
---

# Extracting SAP Ariba Reporting API Data using SAP Integration Suite Part 2 – Sending SAP Ariba Data into SAC

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)
* Extracting SAP Ariba Reporting API Data using SAP ...

Spend Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-sap/article-id/1833&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Extracting SAP Ariba Reporting API Data using SAP Integration Suite Part 2 - Sending SAP Ariba Data into SAC](/t5/spend-management-blog-posts-by-sap/extracting-sap-ariba-reporting-api-data-using-sap-integration-suite-part-2/ba-p/13564858)

![MacMoylan](https://avatars.profile.sap.com/f/6/idf6f708f17e9e973162a9a011c15df08fe222ae465612ab124fd68ab4cf22c191_small.jpeg "MacMoylan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[MacMoylan](https://community.sap.com/t5/user/viewprofilepage/user-id/64140)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-sap&message.id=1833)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-sap/article-id/1833)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564858)

‎2022 Nov 14
9:40 PM

[12
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-sap/message-id/1833/tab/all-users "Click here to see who gave kudos to this post.")

7,904

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Ariba Extensibility](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Extensibility/pd-p/ff06b2d6-8e62-4ba2-b1a8-9d4867d0a62f)
* [SAP Ariba Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Procurement/pd-p/73554900100700001921)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Ariba Procurement

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BProcurement/pd-p/73554900100700001921)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP Ariba Extensibility

  Software Product Function](/t5/c-khhcw49343/SAP%2BAriba%2BExtensibility/pd-p/ff06b2d6-8e62-4ba2-b1a8-9d4867d0a62f)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (5)

Earlier this year I was able to show you how to to extract SAP Ariba Analytical Reporting API Data using SAP Integration Suite (CPI). Here is a link for the first part -

[https://blogs.sap.com/2022/06/01/extracting-sap-ariba-reporting-api-data-using-sap-integration-suite...](https://blogs.sap.com/2022/06/01/extracting-sap-ariba-reporting-api-data-using-sap-integration-suite/)

By now, we've managed to create an end to end process that can fully automate the extraction of SAP Ariba Analytical Reporting data using CPI and sending it to SAP Data Warehouse Cloud (DWC) to create dashboards with SAP Analytics Cloud (SAC) on Top. This leverages a variety of capabilities that live within the SAP Business Technology Platform (BTP). We are using the flexibility of CPI, and the data warehousing and analytics capabilities to store and visualize data.

The purpose of this blog is provide a high level overview of the components involved.

Here is a video of what the end product looks like with Spend Analytics -

<https://www.youtube.com/watch?v=_QoZ0orFY5c>

**Architecture**

What we've done is make this full process available from end to end with SAP products, without the need for using a 3rd party. We can leverage the prebuilt content and stories on SAC to easily create dashboards. Currently, we've used the Spend Visibility offering facts and dimensions to send the data into SAC via CPI and DWC -

![](/legacyfs/online/storage/blog_attachments/2022/11/2022-07-27_12-18-02.png)

However, we have successfully configured the iFlow to work with any of the out of the box Analytical Reporting API fact tables. This can unlock further potential with feeding other SAP Ariba reporting API's into SAC via DWC. You can be flexible and establish this connection with a HANA DB as well.

**Enablement**

You can enable this by following the steps in mentioned in Part 1 of this blog. We will have a live SAP Discovery Center Mission published soon that will have a step by step implementation guide, along with a public Git Repository that will allow you to access the iFlows we built and modify them to access the data tables you want from the Analytical Reporting API.

The licenses needed to make this work is CPI, DWC , and SAC alongside with SAP Ariba to get access to the reporting data. If you have a CPEA BTP license, you can use CPI and SAP DWC on free tier mode to test out business process.

We chose to use DWC because it integrates nicely withSAC, and currently there is not a native connection between SAP Ariba and SAC. The data from SAP Ariba needs a data store to flow into, and DWC is was the choice since users can leverage the pre built business content that is available on SAC.

For more information on how to connect SAC with DWC, please refer to this blog -

<https://blogs.sap.com/2020/05/19/how-to-connect-sap-analytics-cloud-and-sap-data-warehouse-cloud/>

### SAP Data Warehouse Cloud Space creation

## SAP Data Warehouse Cloud Spaces

Before you can import any SAP or partner content package, the space into which the content will imported, needs to be created. SAP content is currently imported into space SAP\_CONTENT.

Therefore, create a space with the technical name “SAP\_CONTENT” once before you import any content package. Use the description “SAP Content”. In addition, assign the user that is to import the content to space SAP\_CONTENT.

You need the Administrator role to create a space.

* For more information on the steps to create a space in DWC, go to

* Assign a user to the space in the ‘Member Assignment’ section. You need this use to test the final content package in SAP Analytics Cloud. For more instructions, go to [Assign Members to Your Space](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/be5967d099974c69b77f4549425ca4c0/9d59fe511ae644d98384897443054c16.html)

* Create a database user in the Database Users section. You need this user to access the SAP HANA Cloud layer and run the SQL Table Creation scripts (needed for the Inbound Layer objects for the content). For more instructions, go to [Create a Database User](https://help.sap.com/docs/SAP_DATA_WAREHOUSE_CLOUD/be5967d099974c69b77f4549425ca4c0/798e3fd6707940c3bd2219b2d1ebaac2.html)

Take note of the database user name and password. You need this information when you connect the SAP Integration Suite integration flow with DWC. Verify that you can open the Database Explorer with this user.

![](/legacyfs/online/storage/blog_attachments/2022/11/Picture9-9.png)

### SAP Data Warehouse Cloud content download

Navigate to the Cont...