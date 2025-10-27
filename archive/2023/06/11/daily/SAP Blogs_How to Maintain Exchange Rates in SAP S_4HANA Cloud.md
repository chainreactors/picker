---
title: How to Maintain Exchange Rates in SAP S/4HANA Cloud
url: https://blogs.sap.com/2023/06/10/how-to-maintain-exchange-rates-in-sap-s-4hana-cloud-2/
source: SAP Blogs
date: 2023-06-11
fetch_date: 2025-10-04T11:45:15.637652
---

# How to Maintain Exchange Rates in SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to Maintain Exchange Rates in SAP S/4HANA Clou...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161159&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Maintain Exchange Rates in SAP S/4HANA Cloud](/t5/technology-blog-posts-by-members/how-to-maintain-exchange-rates-in-sap-s-4hana-cloud/ba-p/13556656)

![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")

[mickaelquesnot](https://community.sap.com/t5/user/viewprofilepage/user-id/150004)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161159)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161159)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556656)

‎2023 Jun 10
9:10 AM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161159/tab/all-users "Click here to see who gave kudos to this post.")

12,530

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

View products (4)

You would always need exchange rates in a financial system.
SAP S/4HANA Cloud offers four ways to update your exchange rates in the system going from 100% manual to 100% automation.
• Manual maintenance of exchange rates in the Currency Exchange Rates app
• Upload exchange rates from file via the Import Foreign Exchange Rates app
• Import exchange rates via API using the SAP Market Rate Management Service
• Import exchange rates directly from external data provider using the SAP Market Rate Management Service
Manual Maintenance
The simplest way to enter exchange rates is through manual entry. You do this in the Currency Exchange Rates app.

Here you can maintain each pair individually. You can either enter the data from an empty screen or copy an existing rate and update the date and exchange rate.

There is no mass maintenance, so if you have many rates you would want to use the file upload.

Upload from File
If you want to upload the exchange rates from file, you first have to download a template which you find here in the app where you would also upload the file. So, go to Import Foreign Exchange Rates.

Via this template you can also upload interest rates, credit spreads, FX volatilities, and other data needed for the treasury management, but here we just want to look at the exchange rates.

How to fill in the template is described
A detailed description on the generic template of the Import Foreign Exchange Rates app.
For templates in a single generic file, the fields have different meanings, depending on the market data category that you select. You can follow the descriptions below:

Market Data Category From To ERTy Value Date Exchange Rate From Factor To Factor Price Quotation
Exchange Rates Enter the Category Number 01 for this column. Enter the From Currency for this column. Enter the To Currency for this column. Enter the Exchange Rate Type for this column. Enter the Effective Date for this column.
Only the format YYYYMMDD is supported currently. Enter the Exchange Rate for this column. Enter theFrom Ratio for this column. Enter theTo Ratio for this column. Enter thePrice Quotation for this column.
You need to enter X for indirect quotation, and leave empty for direct quotation.
The system shows the message of data validation after you upload this file.

Here’s how it could look like:

When you then upload it, the system will give you a log showing you whether the upload was successful.
It is easy to set up but requires that you have a manual process to upload the exchange rate table daily. Apart from that it requires manual work daily to keep the exchange rates up-to-date, auditors could have issues with the file interfaces that could potentially be manipulated by other users.
It’s therefore recommended to use the API for exchange rates which is part of the SAP Market Rate Management Services.
Upload via API
If you already have the exchange rates stored centrally inside your company and now want to automatically update S/4HANA Cloud with these rates daily, you should do it via an API.
There is no API directly in SAP S/4HANA Cloud to upload exchange rates, but you can use the SAP Market Rate Management Services, which is integrated with SAP S/4HANA via an SAP managed communication scenario.
This service can receive exchange rates from two types of sources:
• Bring your own data API
• Market data feed from external source
The “Bring your own data API” is used to upload the data from your intel source. The rates will be stored in this app and several other apps and platforms and then read the data from here.
This is part of the concept for the SAP Market Rate Management Services. It works as a central hub for distributing FX rates to other systems within the organization not just to SAP S/4HANA Cloud.
<https://www.sap.com/products/market-rates-management.html>

You can then set up a daily job within SAP S/4HANA Cloud to read the exchange rates from the SAP Market Rate Management Services and automatically fill the exchange rate table without any manual intervention.
However, this depends on whether you have an internal source for the exchange rates. Most rates would come from an external provider, like Refinitiv (previously known as Thompson Reuters) or Bloomberg.
Upload FX Rates Directly from Data Provider
With the SAP Market Rate Management Services, you can also load data directly from the market rate provider and truly use this SAP Cloud Platform app as a central platform for distributing FX rates in a compliant and easy way.
This is the easiest and most secure way to get FX data provided directly to SAP S/4HANA Cloud. All you need to do is to configure the required rates and set up a daily job to import the FX rates from the SCP portal.
Currently we offer two sources: Refinitiv and the European Central Bank (ECB). There might be more options in the future. Please note, however, that you can currently use the ECB rates only for testing purposes but not in your production system.
You don’t need a licen...