---
title: SAP S/4HANA Extensibility Options For Clean Core Journey
url: https://blogs.sap.com/2023/05/01/sap-s-4hana-extensibility-options-for-clean-core-journey/
source: SAP Blogs
date: 2023-05-02
fetch_date: 2025-10-04T11:39:13.344235
---

# SAP S/4HANA Extensibility Options For Clean Core Journey

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA Extensibility Options For Clean Core J...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53197&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA Extensibility Options For Clean Core Journey](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992)

![jeet_kapase](https://avatars.profile.sap.com/0/0/id008b5bef5d6007221ab5d86367db67c9ec91895fa76b16aeddea0ed2fe268734_small.jpeg "jeet_kapase")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jeet\_kapase](https://community.sap.com/t5/user/viewprofilepage/user-id/16635)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53197)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53197)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568992)

‎2023 May 01
2:19 PM

[131
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53197/tab/all-users "Click here to see who gave kudos to this post.")

84,728

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud Public Edition Extensibility](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Extensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud Public Edition Extensibility

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BExtensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (7)

Experts, before getting into the topic, let's understand the motivation and purpose of the new modern extensibility options defined by the SAP for SAP S/4HANA Public, On-premise, and PCE editions.

## **Motivation**

A cloud-first approach is becoming the new normal powered by software-as-a-service (SaaS) applications with AI/ML, digital assistants, automating routine tasks, better user experience, flexible and agile operating model. SAP is bringing innovation into the core ERP business processes with frequent product release updates. SAP also provides freedom to go beyond standard ABAP language with a BTP side-by-side extensibility approach using BTP ABAP Cloud, Java, node.js, BYOL, etc. to build full-stack applications which will run in parallel with ERP which is challenging with the classic extension options. The extensibility option is a key capability of an ERP application that enables customers to customize their business processes with a competitive advantage in the industry and allows partners to enrich ERP with tailor-made solutions. The importance of extensibility has been confirmed by the legacy ERP flagship product SAP ECC and will remain valid for the current and future cloud ERP transformation.

SAP S/4HANA is a front-runner product providing intelligent ERP in the cloud and on-premise. The goal is to shift from the classic ABAP extensibility model to an SAP S/4HANA modern extensibility model that allows customers to consume SAP innovations, building future-proof extensions that are ready for the cloud ERP. For all, it is important to understand and know how*SAP is shifting away from a monolithic architecture (SAP ECC era) to a microservices architecture that is modular, flexible, continuous deployment, and agile (SAP S/4HANA era with BTP).*

There is chaos in the developer's community, how do we connect the dots for customers that are on traditional ABAP so they can take advantage of modern innovations? What is a new extension model? What is Embedded Steampunk, BTP ABAP environment? SAP CAP (Java, node.js) or RAP?  What is Side-by-side BTP Extension? How it is different from standard ABAP?  Where can we use SAP Build Apps with ERP?  And more questions.

**\*\*\*  Blog Last Updated on 04/22/2025 \*\*\***

## **Contents**

1. [Current customer situation](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#1)
2. [Challenges with the classic extensibility model](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#2)
3. [What are the extensions?](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#3)
4. [Why does SAP S/4HANA need extensibility?](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#4)
5. [What and why about the clean core concept?](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#5)
6. [What is the new extensibility model?](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#6)
7. [SAP S/4HANA Extensibility Options](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#7)
   1. [Key User (In-app) Extensibility](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/sap-s-4hana-extensibility-options-for-clean-core-journey/ba-p/13568992#7-1)
   2. [On-stack Developer Extensibility](https://community.sap.com/t5/enterprise-resource-...