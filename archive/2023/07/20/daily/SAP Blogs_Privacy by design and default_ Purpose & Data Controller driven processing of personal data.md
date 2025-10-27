---
title: Privacy by design and default: Purpose & Data Controller driven processing of personal data
url: https://blogs.sap.com/2023/07/19/privacy-by-design-and-default-purpose-data-controller-driven-processing-of-personal-data/
source: SAP Blogs
date: 2023-07-20
fetch_date: 2025-10-04T11:54:42.255940
---

# Privacy by design and default: Purpose & Data Controller driven processing of personal data

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Privacy by design and default: Purpose & Data Cont...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52540&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Privacy by design and default: Purpose & Data Controller driven processing of personal data](/t5/enterprise-resource-planning-blog-posts-by-sap/privacy-by-design-and-default-purpose-data-controller-driven-processing-of/ba-p/13564177)

![Volker-Lehnert](https://avatars.profile.sap.com/7/a/id7a42338488c01879ebe2b5e9a740c953d9e583682d2727dae54b898283c1cee9_small.jpeg "Volker-Lehnert")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[Volker-Lehnert](https://community.sap.com/t5/user/viewprofilepage/user-id/82367)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52540)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52540)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564177)

‎2023 Jul 19
9:22 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52540/tab/all-users "Click here to see who gave kudos to this post.")

2,447

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

View products (2)

## Abstract

Within SAP S/4HANA, a major change opportunity in the processing of personal data is planned. SAP plans to provide substantial functionality to adhere even more to the privacy by design and default principle. Purpose-based processing of personal data in S/4HANA shall be technically supported in future. Effectively this will change the possibilities to comply with data protection regulations across the globe dramatically.

With **Release 2308** we are providing in a first step the Data Controller attribute and related functionality.

## Regulatory Background

Guiding principles of Data Protection have been provided in 1980 by the OECD. These guiding principles have been overtaken in the legislation of various member states as well as in the EU. Already in 1996, the EU-Directive on Data Protection (EC95/46) defined the same requirements as basic principles of personal data processing in Europe. This has been overtaken in the EU-GDPR. These principles are:

* Collection Limitation Principle

* Data Quality Principle

* Purpose Specification Principle

* Use Limitation Principle

* Security Safeguards Principle

* Openness Principle

* Individual Participation Principle

* Accountability Principle

Most of the principles are subject to Art. 5 GDPR, only few of them in other Articles. Failing to adhere to these principles is punishable with the highest potential fines. Most of these principles are directly related with the purposes of the processing.

In the past, Data Protection requirements have been usually addressed by single features and measures – purpose driven processing is an holistic approach to solve the named generic and broad requirements of Data Protection. . No single feature in itself is capable to reach compliance with Data Protection but only for named requirements covering single aspects only. The reason is obvious – any measure and even more the combination of all measures taken must protect end to end personal data in relation to the purposes and risks – nothing less. For example: A company encrypting the database but providing non-restricted access to all personal data for all its employees will not achieve compliance.

Within this blog an overview on the aimed final opportunities of purpose-based processing is provided. The technical provision of software features to achieve this is in development.

The whole implementation (achieved, ongoing, planned) is based on several assumptions which are not necessarily identical with the policies established in your organization. SAP S/4HANA provides in this sense only a technical opportunity but no legal guidance on how to handle personal data. It remains the customer's responsibility to conclude the purposes and means of processing personal data.

SAP’s implementation starts with the strengthening of the data controller, followed by data categories and purpose attributes. Still we assume, that customers should be awareabout the full soludtion picture, even so this is potentially subject to change.

## Guiding assumptions and definitions for purpose-based processing

### First assumption

Privacy by design and default is based on the purposes of the processing of personal data. Only legitimate purposes justify the processing of personal data including the storage of personal data down to the level of single pieces of personal data.

### Second assumption

Any safeguards implemented are based on the processing purposes and the risk for the data subject.

### Third assumption

At any point in time, it must be possible to document for which purposes certain personal data is processed.

### Fourth assumption

Any purpose is linked to an identifiable data controller or – in case of joint controllership – to the data controllers responsible. A very basic implementation of purpose driven processing relies on the data controller, which grants basic data separability.

### Fifth assumption and basic definition of purpose

The (**primary**) **purpose** means the reason and the final goal for which a data controller processes personal data in an End-to-End (E2E) process.

In some cases, one purpose is not (specific) enough, obviously, there could be differences for data (categories) regarding

* Retention Periods,

* Access or

* Transfer of Data.

The E2E process may further be specified into more detailed ***complementary****, **inherent** or in other consequence **subsequent purposes***. Although they are inextricably linked to the primary purpose, these subsequent purposes enable a more differentiated application and use of data protection measures.

### Sixth assumption and basic definition of data categories

A **data category** is an entity, that includes a set of data fields (attributes of the data subject or a data subject's business object) with similar behavior in the sense of

* Usage,

* Meaning,

* Quality or

* Risk

in relation to a data subject. In addition, the data assigned to a dedicated data category are intended to be used in at least one processing step as a semantical unit.

From this principle deviating categories are categories provided by legal, international, or national standard or public administration definition.

## Concept

### Perspective in a Business process – transparency regarding the data controller

Most business processes dealing with personal data start with the creation of master data.. In SAP S/4HANA this is done for customers and suppliers using the business par...