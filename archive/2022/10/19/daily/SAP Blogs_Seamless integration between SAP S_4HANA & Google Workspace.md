---
title: Seamless integration between SAP S/4HANA & Google Workspace
url: https://blogs.sap.com/2022/10/18/seamless-integration-between-sap-s-4hana-google-workspace/
source: SAP Blogs
date: 2022-10-19
fetch_date: 2025-10-03T20:15:08.542352
---

# Seamless integration between SAP S/4HANA & Google Workspace

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Seamless integration between SAP S/4HANA & Google ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/47742&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Seamless integration between SAP S/4HANA & Google Workspace](/t5/enterprise-resource-planning-blog-posts-by-sap/seamless-integration-between-sap-s-4hana-google-workspace/ba-p/13535025)

![hoberhauser](https://avatars.profile.sap.com/6/e/id6e4d5ce8b1533067c6f8b719d5c2ce148c9e65351e9acd2161681812cfd82210_small.jpeg "hoberhauser")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[hoberhauser](https://community.sap.com/t5/user/viewprofilepage/user-id/39467)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=47742)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/47742)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13535025)

‎2022 Oct 18
4:58 PM

[15
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/47742/tab/all-users "Click here to see who gave kudos to this post.")

10,363

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Document Management service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Document%2520Management%2520service/pd-p/73555000100800002121)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Document Management service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BDocument%2BManagement%2Bservice/pd-p/73555000100800002121)

View products (4)

In May 2022 SAP and Google Cloud announced their partnership to expand native integration between Google Workspace and SAP S/4HANA in this [press release](https://news.sap.com/sea/2022/05/google-cloud-and-sap-expand-partnership-to-enable-native-integration-between-google-workspace-and-sap-s-4hana-cloud/).  “It’s all about collaboration” is a widely used and commonly agreed statement these days and with the partnership we want to foster collaboration based on Google Workspace integrated into SAP S/4HANA.

Many of our customers at SAP are moving to Google Workspace and are struggling with exporting data in a Google format, conversion of files, importing data from Google Sheets into SAP etc. To avoid all those manual steps and translation errors a seamless integration between SAP S/4HANA and Google Workspace is being implemented.

Connecting SAP software processes with the powerful collaborative capabilities of Google Workspace will innovate how work gets done across the enterprise.

![](/legacyfs/online/storage/blog_attachments/2022/10/1-42.png)

High Level Architecture

The customer benefits are clear:

* The efficiency of ready integration, enabling customers to adopt the solution quickly

* The ability to export and import data between SAP software and Google Docs and Google Sheets for instant access to real-time editing and simultaneous collaborative engagements on these documents and spreadsheets

* The confidence of having a clean data source due to the one-step integration, which enables version control and removes layers of potential translation when sharing application data and documents

We are happy to report that the first steps in our integration journey have become reality.

The initial set of features is already available with SAP S/4HANA Cloud, public edition 2208, SAP S/4HANA Cloud, private edition 2022 and SAP S/4HANA 2022, leveraging an SAP Business Technology Platform service for a tight integration and a consistent user experience (additional license required: SAP Document Management Service, integration option).

![](/legacyfs/online/storage/blog_attachments/2022/10/3-10.png)

Integration between SAP Tables and Google Sheets

## Common integration architecture

First let’s take a look at the integration architecture and the prerequisites to enable the integration features described later on.

![](/legacyfs/online/storage/blog_attachments/2022/10/archtiecture.png)

Architecture

* The Google Workspace account is customer owned and customer managed.

* The SAP Document Management Service, integration option, running on a customer owned tenant of the Business Technology Platform is a core piece of the integration between SAP S/4HANA and Google Workspace.

After subscribing to the service, the integration between the SAP Document Management Service and Google Workspace needs to be configured.

* On S/4HANA side the integration towards the SAP Document Management Service is set up via the communication scenario SAP\_COM\_0190 and the authentication is based on oAuth2SAMLBearerAssertion flow.

* Users must be maintained in all 3 systems with the same e-mail address and according authorizations to be able to use the integration.

* The UI integration is based on URL navigation, the user will need to log on to Google Workspace to access the Google Workspace applications.

* Single Sign On is supported by connecting SAP S/4HANA and Google Workspace to the central IdP infrastructure

The details for the mentioned configuration steps can be found in this [help.sap.com](https://help.sap.com/docs/DOCUMENT_MANAGEMENT/f6e70dd4bffa4b65965b43feed4c9429/594bf95dbab64358aef97a73296b6054.html) section.

## Features delivered with SAP S/4HANA Cloud 2208 and OnPremise S/4HANA 2022

After the configuration of the common integration architecture, both features are available immediately.

### Export to native Google Sheets

For all important UI tables the standard table export has been enhanced so that the table data can be exported to Google Sheets.  A ‘File Browser’ dialogue is available to browse the Google repository and decide on the preferred location for the table export.  After the export the Google Sheets is opened directly for further processing.

With this Google native integration for the broadly performed task of exporting table data, we hope to majorly improve the UX for Google Workspace users already with the first delivery.

### Import data from Google Sheets into SAP S/4HANA Upload General Journal Entries application

To upload General Journal Entries from Google Workspace to SAP S/4HANA, a template is exported from the SAP S/4HANA General Journal Entries application to Google Sheets where it is directly opened.  Once the user entered all relevant data, the Google Sheets can be uploaded and poste...