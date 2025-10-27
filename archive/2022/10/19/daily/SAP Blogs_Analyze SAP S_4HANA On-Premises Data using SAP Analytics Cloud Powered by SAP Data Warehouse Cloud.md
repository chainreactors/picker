---
title: Analyze SAP S/4HANA On-Premises Data using SAP Analytics Cloud Powered by SAP Data Warehouse Cloud
url: https://blogs.sap.com/2022/10/18/analyze-sap-s-4hana-on-premises-data-using-sap-analytics-cloud-powered-by-sap-data-warehouse-cloud/
source: SAP Blogs
date: 2022-10-19
fetch_date: 2025-10-03T20:14:57.845584
---

# Analyze SAP S/4HANA On-Premises Data using SAP Analytics Cloud Powered by SAP Data Warehouse Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Analyze SAP S/4HANA On-Premises Data using SAP Ana...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/155714&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Analyze SAP S/4HANA On-Premises Data using SAP Analytics Cloud Powered by SAP Data Warehouse Cloud](/t5/technology-blog-posts-by-sap/analyze-sap-s-4hana-on-premises-data-using-sap-analytics-cloud-powered-by/ba-p/13544050)

![VenkatPS](https://avatars.profile.sap.com/7/5/id7513885092a6f441b0fe3446bd9d49c9271433eb95502f5a2e9b081647786dd9_small.jpeg "VenkatPS")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[VenkatPS](https://community.sap.com/t5/user/viewprofilepage/user-id/14765)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=155714)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/155714)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13544050)

‎2022 Oct 18
5:07 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/155714/tab/all-users "Click here to see who gave kudos to this post.")

6,396

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA smart data integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520smart%2520data%2520integration/pd-p/73554900100800000033)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA smart data integration

  SAP HANA](/t5/c-khhcw49343/SAP%2BHANA%2Bsmart%2Bdata%2Bintegration/pd-p/73554900100800000033)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (7)

This simple blog post helps you get an understanding of how data from an SAP S/4HANA on-premises system can be Analysed using SAP Analytics Cloud which is connected using Data Warehouse Cloud in SAP Business Technology Platform (BTP).

This blog post covers –

* Connectivity of SAP S/4HANA On-premise system to SAP Data Warehouse Cloud.

* Creation of a View using SAP Data Warehouse Cloud Data Builder.

* Consume the View in SAP Analytics Cloud and create a story.

**SAP Data Warehouse Cloud**

SAP Data Warehouse Cloud is an end-to-end data management and decision-making cloud solution designed for business and enterprise-grade experiences. It is an integrated, fully managed service, and persona-driven Data Warehouse as a Service solution, suitable for SAP and non-SAP customers offering reduced deployment complexity, flexible pricing with integration to SAP Intelligent Enterprise Suite solutions, SAP Analytics Cloud, SAP BTP services, Partner solutions and open-source technologies.

**SAP Analytics Cloud**

SAP Analytics Cloud is an all-in-one cloud product offered as software as a service (SaaS) for business intelligence (BI), planning, and predictive analytics. Built natively on SAP BTP, it provides a unified and secure public cloud experience to maximize data-driven decision making.

The scenario we are covering in the blog is given below:

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture1-5.jpg)

Let’s get started…

Go to Software Downloads on the SAP ONE Support Portal, search for Smart Data Integration. Download SAP HANA Smart Data Integration Package.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture2-3.jpg)

Extract the downloaded file, run the hdbsetup.exe file.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture3-3.jpg)

Go to the list of services running in your system, you should see that the below service. Ensure that the service is started.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture4-2.jpg)

After Installing the Data Provisioning (DP) Agent, Issue the below command in the command prompt

agentcli.bat --configAgent

This will start the initialization of DPAgent Configuration Tool.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture5-2.jpg)

After initialization, the DPAgent Configuration Tool will present the below options.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture6.jpg)

Select option 7 to start SAP HANA Connection.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture7-1.jpg)

Multiple options will be displayed for SAP HANA Connection.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture8-1.jpg)

Select option 2 to Connect to SAP Data Warehouse Cloud via JDBC.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture9-1.jpg)

SAP Data Warehouse Cloud Connectivity using JDBC will require details of the HANA Server, Messaging user etc. Obtain the details form SAP Data Warehouse cloud.

Go to your SAP Data Warehouse Cloud tenant, select main menu, choose configuration then click on the + tile in the Data Integration tab.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture10.jpg)

The following window will pop up.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture11.jpg)

Specify a name to the agent, and then click on create button. I have specified the name as dpagent.

This will show the settings needed by the agent configuration tool running in the command line. Keep the window open until all the details are provided in the command prompt.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture12-1.jpg)

Provide the selected details in the command line for SAP HANA Connection to SAP Data Warehouse Cloud using JDBC

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture13-1.jpg)

We need to stop and start the agent in order to bring the new settings to effect.

Go back to the previous menu option and select option 2 to stop and start the agent.

From the menu select option 2 again to stop the agent.

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture14.jpg)

Then select option 1 to start the agent

![](/legacyfs/online/storage/blog_attachments/2022/10/Picture15.jpg)

Go back to the main menu a...