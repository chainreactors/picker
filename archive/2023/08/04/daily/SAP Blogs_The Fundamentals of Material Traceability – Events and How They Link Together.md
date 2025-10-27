---
title: The Fundamentals of Material Traceability – Events and How They Link Together
url: https://blogs.sap.com/2023/08/03/the-fundamentals-of-material-traceability-events-and-how-they-link-together/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:34.070292
---

# The Fundamentals of Material Traceability – Events and How They Link Together

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* The Fundamentals of Material Traceability – Events...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/5217&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [The Fundamentals of Material Traceability – Events and How They Link Together](/t5/supply-chain-management-blog-posts-by-sap/the-fundamentals-of-material-traceability-events-and-how-they-link-together/ba-p/13573930)

![ReemaJones](https://avatars.profile.sap.com/7/4/id7494659016ad866bd4b2506faa488ee2f459690c892f98ff345e07a1b97000c5_small.jpeg "ReemaJones")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ReemaJones](https://community.sap.com/t5/user/viewprofilepage/user-id/154641)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=5217)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/5217)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13573930)

‎2023 Aug 03
7:39 PM

[7
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/5217/tab/all-users "Click here to see who gave kudos to this post.")

1,763

* SAP Managed Tags
* [SAP Business Network for Logistics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Logistics/pd-p/73554900100800001025)

* [SAP Business Network for Logistics

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BLogistics/pd-p/73554900100800001025)

View products (1)

*This is the first of a series of blog posts explaining the fundamentals of SAP Business Network Material Traceability. If you'd first like a brief introduction to our solution, read [What is Material Traceability?](https://blogs.sap.com/2023/07/11/what-is-material-traceability/) by Mark Averskog.*

In this post, I will describe what “events” are in Material Traceability, how they are the building blocks of our digital supply chains, and how they are linked together. Basically, I'll summarize the ideas in these two videos:

<https://sapvideoa35699dc5.hana.ondemand.com/?entry_id=1_tyere0y2>

[Link](https://help.sap.com/docs/business-network-material-traceability/administration-guide-for-material-traceability/available-attributes) mentioned in video.

### An Introduction Stating the Obvious...

Supply chains are growing increasingly complex, posing significant challenges for companies to ensure transparency, traceability, safety, and sustainability. Consumers are more aware and demanding, wanting to know where their products come from and how they are made.

So, what’s the solution? Let’s look at how the SAP Business Network Material Traceability solution uses events to create a digital representation of supply chains with clarity, simplicity, and reliability.

### Receive, Produce, and Deliver Events in Material Traceability

In Material Traceability, we talk about “events” a lot. But what does that mean? Events refer to real-world activities that have a tangible impact on a product’s traceability. Of course, there are loads of different kinds of these activities. But if you think about it, any enterprise – whether it’s simple or complex, manufacturing or services, B2B or B2C, large or small – any enterprise operation, at its heart, boils down to three things: taking inputs, transforming them, and then selling the outcomes in a way that improves people’s lives. In other words: buy, do, and sell. In Material Traceability we call these three fundamental activities of any enterprise: receive, produce, and deliver *events*.

Since Material Traceability supports both batch-managed and serialized products, there are two of each of the three event types – one for batches and one for serialized products.

A receive event might involve recording the receipt of a batch of raw material from a supplier. When that raw material is processed to create a new batch, that would get recorded as a produce event. And then the deliver event is created to record the new batch being shipped off to another factory. At this point, we are usually looking at the delivery of goods between one company and another. So, we are dealing with the IT systems of two different companies and need to figure out a way for the two companies – and, indeed, all the companies involved in that supply chain – to collaborate to maintain a reliable digital system for tracing every ingredient, raw material, or subcomponent that went into making a finished product.

When all the receive, produce, and deliver events are recorded in Material Traceability, it serves as a digital mirror that reflects the real-world supply chain. A product’s genealogy can be traced as far upstream and downstream as the companies have contributed data. Information from related documents can be abstracted into the events. For example, a receive event can include the details of a purchase order.

### Attributes: Key Attributes and Customization

Attributes are characteristics of a product and are associated with each Material Traceability event. These attributes can be customized to suit the unique needs of each company and its business partners. Importantly, attributes can be consolidated over a supply chain to measure something, such as a product's total carbon footprint.

Key attributes are used to uniquely identify each event, and so are mandatory. The key attributes of an external event (that is, one that happened in another company) are extracted from related documents, such as goods receipts or delivery documents. Material Traceability recognizes when the key attributes match and links the events together.

And this is how Material Traceability balances the need for flexibility and privacy. Just enough information is shared to unequivocally establish a link between unique events, allowing for accurate and targeted recalls, if required. By enhancing the default set of attributes to suit your needs, you can go as deep into a complex bill-of-material for a product as the data contributions that the companies in the supply chain chose to input and share with each other, facilitating closer and more effective collaboration.

### Want to know more?

Check out [this page](https://www.sap.com/products/business-network/material-traceability.html) and read our [solution brief](https://www.sap.com/documents/2022/12/1c39d4ef-537e-0010-bca6-c68f7e60039b.html).

And... stay tuned for more posts.

Labels

* [Product Updates](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap/label-name/product%20updates)

* [batch traceability](/t5/tag/batch%20traceability/tg-p/board-id/scm-blog-sap)
* [digital supply chain](/t5/tag/digital%20supply%20chain/tg-p/board-id/scm-blog-sap)
* [Material Traceability](/t5/tag/Material%20Traceability/tg-p/board-id/scm-blog-sap)
* [materialtraceability](/t5/tag/materialtraceability/tg-p/board-id/scm-blog-sap)
* [sustainablelogistics](/t5/tag/sustainablelogistics/tg-p/board-id/scm-blog-sap)
* [sustainablesupplychain](/t5/tag/sustainablesupplychain/tg-p/board-id/scm-blog-sap)

You must be a registered...