---
title: Why We Chose an Event-Based Architecture for Cell and Gene Therapy Orchestration
url: https://blogs.sap.com/2023/03/25/why-we-chose-an-event-based-architecture-for-cell-and-gene-therapy-orchestration/
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:43:01.819271
---

# Why We Chose an Event-Based Architecture for Cell and Gene Therapy Orchestration

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* Why We Chose an Event-Based Architecture for Cell ...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/4851&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Why We Chose an Event-Based Architecture for Cell and Gene Therapy Orchestration](/t5/supply-chain-management-blog-posts-by-sap/why-we-chose-an-event-based-architecture-for-cell-and-gene-therapy/ba-p/13555660)

![EduardH](https://avatars.profile.sap.com/2/8/id289b6fe44cb62dd80843b6bf41002a9d7f224e92c04671eb42621227688126ff_small.jpeg "EduardH")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[EduardH](https://community.sap.com/t5/user/viewprofilepage/user-id/170474)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=4851)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/4851)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555660)

‎2023 Mar 25
12:03 AM

[8
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/4851/tab/all-users "Click here to see who gave kudos to this post.")

2,149

* SAP Managed Tags
* [Life Sciences](https://community.sap.com/t5/c-khhcw49343/Life%2520Sciences/pd-p/95174915017257381839339)
* [SAP Event Mesh](https://community.sap.com/t5/c-khhcw49343/SAP%2520Event%2520Mesh/pd-p/73554900100800000765)
* [SAP Cell and Gene Therapy Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cell%2520and%2520Gene%2520Therapy%2520Orchestration/pd-p/73555000100700001599)

* [Life Sciences

  Industry](/t5/c-khhcw49343/Life%2BSciences/pd-p/95174915017257381839339)
* [SAP Event Mesh

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BEvent%2BMesh/pd-p/73554900100800000765)
* [SAP Cell and Gene Therapy Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BCell%2Band%2BGene%2BTherapy%2BOrchestration/pd-p/73555000100700001599)

View products (3)

## Introduction

Cell therapy, a promising and rapidly growing field, involves the production and delivery of living cells to treat or prevent diseases. The complex nature of these therapies requires precise coordination across multiple stages of the supply chain, from sourcing suitable cells from the patient to be treated in the autologous cell therapy approach or a donor in the allogeneic cell therapy approach as the starting materials to delivering the final product to patients. As such, we built [SAP Cell and Gene Therapy Orchestration](https://www.sapstore.com/solutions/76120/SAP-Cell-and-Gene-Therapy-Orchestration) (CGTO) as a software-as-a-service (SaaS) product that can effectively orchestrate these processes. We have chosen an event-based architecture for CGTO, an approach in which components communicate through events that has proven to be highly effective for building such Industry Cloud products. This chapter will explore the benefits of implementing event-based architecture in CGTO.

**Scalability and Flexibility**

The event-based architecture enables CGTO to scale easily as demand for cell therapies increases. In this approach, components are loosely coupled and can be independently scaled or modified without affecting other parts of the system. As new products are introduced in additional treatment centers and variation in cell therapy supply chains grows, new event sources or consumers can be added without disrupting existing functionality. This flexibility is essential for catering to the expanding and evolving landscape of cell therapy.

**Real-time Processing and Responsiveness**

In the cell therapy supply chain, real-time data processing and responsiveness are critical to ensure timely delivery and product efficacy. Event-based architecture supports real-time processing through the continuous flow of events between components. As events are generated, they can be immediately consumed and acted upon, facilitating rapid responses to changes in the supply chain. This real-time nature ensures that CGTO can effectively monitor and manage processes, such as shipments and processing activities, to maintain product quality and safety.

**Increased Visibility and Traceability**

Event-based architecture inherently promotes visibility and traceability across the entire supply chain. Each event represents a state change or action taken within the system, creating a detailed history of all activities. This comprehensive event log, the chain of identity and chain of custody, facilitates end-to-end tracking of cell therapies, ensuring compliance with regulatory requirements and enabling rapid identification of issues. Furthermore, this visibility allows stakeholders to make informed decisions and optimize their operations based on historical and real-time data.

**Enhanced Collaboration and Integration**

The loosely coupled nature of event-based architecture encourages collaboration and integration between different stakeholders in the cell therapy supply chain. Thus, CGTO can easily interface with external systems, such as patient onboarding systems, laboratory information management systems, inhouse manufacturing or contract manufacturing systems, and logistics service providers. By seamlessly connecting these various components, event-based architecture fosters a collaborative environment, streamlining processes, and improving overall efficiency.

**Improved Fault Tolerance and Resilience**

Event-based systems are inherently more fault-tolerant and resilient compared to traditional architectures. By decoupling components and processing events asynchronously, the system can continue to function even if one component fails or experiences delays. This fault tolerance is vital in the cell therapy supply chain, where any disruption could compromise the quality and efficacy of the final product. Event-based architecture ensures that CGTO can maintain orchestration capabilities even in the face of unforeseen challenges. E.g., the post-processing-framework can re-send messages to an external system that was unavailable for a period of time and messages were not received successfully.

**Adaptability to Emerging Technologies**

The cell therapy landscape is continually evolving, with new treatments and technologies emerging regularly. The event-based architecture allows CGTO to adapt and incorporate these advancements quickly. As new event sources are introduced, the system can accommodate them without extensive reconfiguration, ensuring that CGTO remains at the forefront of innovation.

## Conclusion

Event-based architecture offers numerous benefits for CGTO designed to orchestrate cell therapy supply chains. Its scalability, flexibility, real-time processing capabilities, visibility, traceability, and adaptability make it an ideal choice for managing the complex and dynamic nature of cell therapy production and delivery. By leveraging event-based architecture, CGTO is a robust and efficient solution that effectively supports the growing demands of this promising field.

Labels

* [Product Updates](/t5/supply-cha...