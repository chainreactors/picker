---
title: What happens next with SAP Business Connector?
url: https://blogs.sap.com/2022/11/07/what-happens-next-with-sap-business-connector/
source: SAP Blogs
date: 2022-11-08
fetch_date: 2025-10-03T21:56:05.446954
---

# What happens next with SAP Business Connector?

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* What happens next with SAP Business Connector?

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162124&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What happens next with SAP Business Connector?](/t5/technology-blog-posts-by-sap/what-happens-next-with-sap-business-connector/ba-p/13562706)

![Zilch](https://avatars.profile.sap.com/0/0/id004c81e57898dea34f80b75b5c3b644234a26399222853f7a24393574012f969_small.jpeg "Zilch")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Zilch](https://community.sap.com/t5/user/viewprofilepage/user-id/41110)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162124)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162124)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562706)

‎2022 Nov 07
7:01 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162124/tab/all-users "Click here to see who gave kudos to this post.")

10,014

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

Objective of this blog is to give some background information about SAP Business Connector and some guidance for replacing it with a more contemporary platform.

## What is SAP Business Connector?

SAP Business Connector (SBC) is a middleware or integration platform offered by SAP to connect SAP-systems to non-SAP partner systems.
SAP Business Connector was released in 1999 when an SAP-system was an ERP-system running on an ABAP-stack. There was none of the integration tools that later became essential part of the SAP Netweaver stack. SBC was released as the solution from SAP for integrating SAP-systems to 3rd-party-systems using the technologies that were considered state of the art for business-to-business communication at that time, such as XML, HTTP(S) or WebServices.

![](/legacyfs/online/storage/blog_attachments/2022/11/SBC_Architektur_EN.jpg)

SBC Architecture

However, with introducing SAP Web Application Server and SAP Exchange Infrastructure (shortly later renamed to SAP Process Integration, SAP PI, and better known under that name) a few years later, SAP Business Connector was no longer the recommended integration tool. Since that time SAP has stopped developing SBC any further but still supports it and offers it to customers for download.
Apart from customer-specific integration scenarios a typical use case for SAP Business Connector are SAP customers who are not using the integration solutions like Cloud Integration Suite or SAP PI and run ELSTER scenarios. ELSTER is a joint project of the German Federal Tax Administration and the tax administrations of the German Federal States that has made the electronic transmission of tax return data possible. Customers need a middleware to transfer their data to the financial authorities as part of these scenarios.
As technology and common design patterns have been constantly developing over the time, SAP Business Connector and its underlying architecture seems more and more outdated. As a result, many customers are looking for recommendations how to cope with that situation. End of maintenance for the current and final release 4.8 of SBC will be 2027. Customers still running SAP Business Connector will have to come up with a strategy how to continue thereafter.

## SAP Business Connector Architecture

SAP Business Connector is a Java application that uses SAP Java Connector (JCO) to connect with SAP-systems. Hence the communication between SBC and SAP ERP is based on the RFC protocol in the first place. SAP Business Connector supports various types of RFC-communication (synchronous, asynchronous, transactional) and comes with built-in support for IDoc-communication. For the communication towards the non-SAP partner systems SBC supports HTTP(S), FTP, Email (SMTP, IMAP, POP3), JDBC and WebService.
Apart from the transportation layer SAP Business Connector can also perform data processing, such as conversions and mappings. That can be done using a graphical mapping engine, with XSLT or by deploying own coding (Java or C++). The graphical mapping engine comes with a dedicated development environment called SAP Business Connector Developer.

![](/legacyfs/online/storage/blog_attachments/2022/11/SBC_graphical_mapping-1.png)

SBC Graphical Mapping

At first glance mappings in SAP Business Connector may look similar to data mappings in SAP PI, but in fact they are based on a different technology and cannot be exported or easily migrated to SAP PI, Cloud Integration Suite or any other SAP NetWeaver component.
SAP Business Connector is a pure Java application running on a JRE (Java Runtime Environment). The current version is shipped with the SAP own Java runtime, previous versions were shipped with Java runtimes from other vendors. SAP Business Connector is not part of the NetWeaver stack but uses proprietary technology. It has no ABAP stack and, despite being a Java server, is of completely different nature than SAP WebApplication server. It neither complies to any common standard such as J2EE or similar, it is rather a proprietary solution.

## Limitations

Because of its different nature, some common tools that are widely used in a typical SAP landscape are not available for SAP Business Connector. For example, it cannot be integrated in the SAP Central User Administration, it cannot be integrated in solutions like Change Request Management (ChaRM) or Focused Build to control development and transport processes throughout the landscape. There is no transport management system compatible with that for other SAP solutions.
Sound knowledge in SAP administration, maintenance, development, or error investigation won’t help much when it comes to SAP Business Connector. Customers often depend on service providers for these activities because they don’t have the required know-how and typically it is not worthwhile for them to build it up in their own team.
Due to the low level of standardization and market penetr...