---
title: Kazakhstan and Uzbekistan national track & trace digital systems. Compliance with SAP ATTP, S/4HANA and 3keys GmbH Add-on
url: https://blogs.sap.com/2023/02/28/kazakhstan-and-uzbekistan-national-track-trace-digital-systems.-compliance-with-sap-attp-s-hana-and-3keys-gmbh-add-on/
source: SAP Blogs
date: 2023-03-01
fetch_date: 2025-10-04T08:19:53.120142
---

# Kazakhstan and Uzbekistan national track & trace digital systems. Compliance with SAP ATTP, S/4HANA and 3keys GmbH Add-on

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Kazakhstan and Uzbekistan national track & trace d...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67835&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Kazakhstan and Uzbekistan national track & trace digital systems. Compliance with SAP ATTP, S/4HANA and 3keys GmbH Add-on](/t5/enterprise-resource-planning-blog-posts-by-members/kazakhstan-and-uzbekistan-national-track-trace-digital-systems-compliance/ba-p/13559945)

![gorbenkoteh](https://avatars.profile.sap.com/4/6/id46ee6e66e93c22dabdfa29c69de688bd03ae6636bed22ff4c9e0a1d8e92ee3c3_small.jpeg "gorbenkoteh")

[gorbenkoteh](https://community.sap.com/t5/user/viewprofilepage/user-id/594529)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67835)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67835)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559945)

‎2023 Feb 28
7:12 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67835/tab/all-users "Click here to see who gave kudos to this post.")

2,395

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

## 1.Intro

Kazakhstan and Uzbekistan are two large countries located in Central Asia with 19 and 36 million inhabitants respectively.

Like a many other countries, Kazakhstan and Uzbekistan have launched a government  serialization program to fight counterfeit and illegal medicines.

In 2023, in both of these countries, this program entered the final phase. All manufacturers and distributors must adapt their information systems to new government requirements.

For companies with SAP Landscape, using SAP ATTP with Add-ons for this purpose is a coherent step. This blog-posts consists from two parts - part I about  compliance in Uzbekistan, part II about compliance in Kazakhstan.

## 2.Compliance deadline

Uzbekistan:

* Phase 1: May, 2022: Initial preparation for complying with the regulation

* Phase 2: July, 2022: Focusing on serialization readiness

* Phase 3: Sep, 2022: Serialization with crypto codes to be mandatory

* Phase 4: May 2023: Aggregation and aggregation reporting to be mandatory

## 3.GS1 Standards

Government serialization in Uzbekistan based on GS1 Standards

Small overview:

**3.1. GS1 Identification Standards: GTIN, SSCC, GLN, GCP [1]**

**GTIN:**

GTIN is an identifier for trade items. Such identifiers are used to look up product information in a database (often by entering the number through a barcode scanner pointed at an actual product) which may belong to a retailer, manufacturer, collector, researcher, or other entity. The uniqueness and universality of the identifier is useful in establishing which product in one database corresponds to which product in another database, especially across organizational boundaries

**SSCC (Serial shipping container code):**

The Serial Shipping Container Code (SSCC) is an 18-digit number used to identify logistics units. In order to automate the reading process, the SSCC is often encoded in a barcode, generally GS1-128, and can also be encoded in an RFID tag. It is used in electronic commerce transactions. The SSCC comprises an extension digit, a GS1 company prefix, a serial reference, and a check digit. It is all numeric. It is applicable to the tertiary level of packing.

**GLN (The Global Location Number):**

GLN is part of the GS1 systems of standards.

The GLN is used to identify physical locations or legal entities. The key comprises a GS1 Company Prefix, Location Reference, and Check Digit

When a company joins GS1 it is normally given a number called a Global Company Prefix (GCP). A GCP is a unique number that can then be used as a base by the company to generate unique identification numbers for products (GTIN), shipments (SSCC), locations (GLN) and more.

 **3.2. GS1 Data Capture Standards: GS1 Data Matrix**

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_1.png)

*On author's photo: Data Matrix on drug package.*

DataMatrix on drug packs for Uzbekistan market must consists:

GS1 Global Trade Item Number (GTIN) (14 digit) - AI (01)

Serial Number (13 digit) - AI (21)

Verification key (4 digit) - AI (91)

Verification code (44 digit) - AI (92)

On our example:

(01)04750232014417(21)02007SNTW8V50(91)EE07(92)/wocCK9s/NSRAxQh/3zPPfLEVVTub+ogphCLW4N30M=

GTIN:  04750232014417

Serial number: 02007SNTW8V50

Crypto-Code (Verification key + Verification Code): )EE07 + /wocCK9s/NSRAxQh/3zPPfLEVVTub+ogphCLW4N30M=

## 4. Asl Belgisi. National Track & Trace Digital System

Asl Belgisi is the national system of labeling and trace ability of goods, which is largely used by participants in the commodities turnover [2]

A key part of the National T&T Digital System: web-site and mobile app [2]

Registration and receiving of E-imzo [8] digital signature a mandatory.

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_2.png)

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_3.jpg)

## 5.Uzbekistan Connector. SAP ATTP Add-on from 3keys GMBH

Right now SAP ATTP don't have country specific settings for Uzbekistаn and Kazakhstan

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_4.png)

Specific Add-on's for this Central Asian countries offered by 3-rd party SAP partners

One of them  - Germany based software company 3keys GMBH

Add-ons by this company  available in SAP Store for clients all over the world [3]

## 6.Uzbekistan Connector for ATTP in details. Installation.

**6.1.  Prerequisite.**

SAP Advanced Track and Trace for Pharmaceuticals 3.0 (STTP300) with support package 01 (on Feb,2023 - support package 02 also available) [4]

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_5.png)

**6.2.Installation**

Transaction - SAINT in 000 client.

Installation of:

3Keys Uzbekistan Add-On 3.1:SAPK-301COINK3TUZ

3Keys Uzbekistan OMS Add-On 3.1: SAPK-301COINK3TUZ1

**6.4. BC Sets activation**

Transaction - SCPR20

Activation of: /K3TUZ/CUST\_OMS\_3\_1

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_6.png)

##

## 7.Uzbekistan Connector for ATTP in details. Configuration.

**7.1. Basis configuration. Prerequisite**

The DigiCert Global Root CA certificate should be added to the SSL client (Anonymous) in the transaction STRUST.  You can download it from attachments of Note #2631190 [5]

![](/legacyfs/online/storage/blog_attachments/2023/02/kaz_uzb_7.png)

Parameter icm/HTTPS/client\_sni\_enabled with value TRUE shall be set in transaction RZ10 [6]

The corporate firewall, proxy, gateway, etc. should allow outbound HTTPS connection from ATTP to the Uzbekistan OMS.

Route from SAP ATTP server to  <https://omscloud.stage.aslbelgisi.uz (port>: 443) for QAS and DEV systems

from SAP ATTP server to <https://omscloud.aslbelgisi.uz (port>: 443) for

PROD system.

*...