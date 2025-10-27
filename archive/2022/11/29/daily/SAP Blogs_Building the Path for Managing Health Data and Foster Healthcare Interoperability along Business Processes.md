---
title: Building the Path for Managing Health Data and Foster Healthcare Interoperability along Business Processes
url: https://blogs.sap.com/2022/11/28/building-the-path-for-managing-health-data-and-foster-healthcare-interoperability-along-business-processes/
source: SAP Blogs
date: 2022-11-29
fetch_date: 2025-10-03T23:58:46.593306
---

# Building the Path for Managing Health Data and Foster Healthcare Interoperability along Business Processes

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Industry Groups](/t5/industry-groups/ct-p/industries)
* [SAP for Healthcare](/t5/sap-for-healthcare/gh-p/healthcare)
* [Blog Posts](/t5/sap-for-healthcare-blog-posts/bg-p/healthcareblog-board)
* Building the Path for Managing Health Data and Fos...

SAP for Healthcare Blog Posts

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/healthcareblog-board/article-id/219&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

Read only

## [Building the Path for Managing Health Data and Foster Healthcare Interoperability along Business Processes](/t5/sap-for-healthcare-blog-posts/building-the-path-for-managing-health-data-and-foster-healthcare/ba-p/13557786)

![thorstenkampp](https://avatars.profile.sap.com/3/4/id340a580ca73944ff25b253860b6b88c4610398f66c9495b7553c5da39782a9ea_small.jpeg "thorstenkampp")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[thorstenkampp](https://community.sap.com/t5/user/viewprofilepage/user-id/44576)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=healthcareblog-board&message.id=219)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/healthcareblog-board/article-id/219)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557786)

‎2022 Nov 28
7:33 PM

[11
Kudos](/t5/kudos/messagepage/board-id/healthcareblog-board/message-id/219/tab/all-users "Click here to see who gave kudos to this post.")

2,307

* SAP Managed Tags
* [Healthcare](https://community.sap.com/t5/c-khhcw49343/Healthcare/pd-p/145882333770114278757787)
* [SAP Health](https://community.sap.com/t5/c-khhcw49343/SAP%2520Health/pd-p/73554900100700001094)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Healthcare

  Industry](/t5/c-khhcw49343/Healthcare/pd-p/145882333770114278757787)
* [SAP Health

  Software Product](/t5/c-khhcw49343/SAP%2BHealth/pd-p/73554900100700001094)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

In this blog post, I want to follow up on the [recent post](https://blogs.sap.com/2022/10/24/what-does-the-sap-health-product-strategy-update-to-support-hybrid-modular-healthcare-system-landscapes-mean-to-customers-and-partners-and-why-they-should-evaluate-and-adopt-now/) on the SAP Health Product Strategy and focus specifically on the updated plans in the context of healthcare-related services on the SAP Business Technology Platform (BTP).

Healthcare provider landscapes are traditionally heterogeneous and have always included highly specialized subsystems and modules. Even so, there is an ongoing and continuous modularization of these landscapes, including the hospital information system. Interoperability is the ability that ensures that these different information systems can “access, exchange, integrate, and cooperatively use data in a coordinated manner”[[1]](https://www.himss.org/resources/interoperability-healthcare). Often the integrations between these systems are built as custom interfaces in projects, are tailored and designed to their specific setting, and frequently require ongoing monitoring and maintenance, resulting in continuous effort and cost.

Several years of working on different healthcare solutions made it clear to me that interoperability has various dimensions and is much more than a technology problem at its core. It requires an alignment of standards, terminology, processes, and the motivation to work with each other. On the journey towards composable business processes, SAP has planned to address these dimensions step by step and engage the partner ecosystem along that way.

## Integration and Extensibility

The team I am working with wants to address two needs of our customers and partners. First, we want to support our partners and simplify hospital information system integration with SAP S/4HANA, analytics, and the broader SAP portfolio of solutions along end-to-end processes such as Patient-to-Reimbursement, Record-to-Report, Finance, and others. Hospital information system partners could position the integration between their solutions and the SAP Intelligent Suite enabling value-add and innovative use cases as a strong value proposition. Consequently, customers could benefit from an improved user experience through the integrated solution and an improved TCO. Second, we want to support customers and partners in developing healthcare cloud applications. We want to help customers to leverage SAP technology to create required extensions within their business process and allow partners to build software extensions and distribute them on the [SAP App Store](https://store.sap.com/dcp/en/industries/try-and-buy-healthcare-apps-and-software).

## FHIR on SAP Business Technology Platform

As an essential service to satisfy these needs to some extent and better support interoperability, we plan to leverage the [HL7® FHIR® standard](https://hl7.org/fhir/) on the [SAP Business Technology Platform (BTP)](https://www.sap.com/germany/products/technology-platform.html). SAP BTP is **the Choice** (please also see the highlights from [Jürgen Müller’s Keynote](https://www.youtube.com/watch?v=4TtkAe-oZv0) at SAP TechEd) to accelerate innovations. At the same time, FHIR is the leading candidate for an open and standard API ecosystem to connect with the broader healthcare ecosystem. Similarly, both SAP BTP and the HL7® FHIR® standard are designed to foster integration, extensibility, and scalability.

Hence, SAP plans to provide an HL7® FHIR® service on SAP BTP. If and when available, partners and customers can leverage this platform-as-a-service (PaaS) to support the design, implementation, and operation of a native cloud application or service relying on health-related data. Moreover, it is planned to support applications to satisfy their integration needs with SAP solutions and the SAP partner ecosystem. At its core, it is designed to represent an FHIR service for managing health data. The service is meant to provide a synchronous REST and asynchronous messaging-based API capable of supporting the necessary FHIR capabilities. Naturally, it is planned to use the in-memory database SAP HANA Cloud as persistence to be able to fulfill the needs for high-performance transactional applications.

In summary, the service intends to provide capabilities to address challenges faced by the healthcare industry, such as, e.g.,

* A reliable and secure environment to manage personal information and protected health information (PHI)

* Need for integration to different systems and applications in the landscape, within and across healthcare organizations, government authorities, and other industries such as life science and insurance

* Manage the varying complexities and regulations in the healthcare industry by providing flexible and customizable services, applications, and tools

When released, this service is planned to be the perfect starting point for customers and partners to build new healthcare cloud applications on SAP BTP and the necessary basis to address further integration needs with SAP solutions along end-to-end processes.

## What comes next?

Next month we will update the [Road Map Explorer](https://roadmaps.sap.com/business-views/000D3AAC9DD21EDC9684ABEF0D4E209D) with corresponding innovations. We plan to make a beta version of this service avai...