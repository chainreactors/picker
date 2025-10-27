---
title: Get your organization in shape: Keep a Clean Core with SAP Business Technology Platform
url: https://blogs.sap.com/2023/02/06/get-your-organization-in-shape-keep-a-clean-core-with-sap-business-technology-platform/
source: SAP Blogs
date: 2023-02-07
fetch_date: 2025-10-04T05:51:02.395385
---

# Get your organization in shape: Keep a Clean Core with SAP Business Technology Platform

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Get your organization in shape: Keep a Clean Core ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161530&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Get your organization in shape: Keep a Clean Core with SAP Business Technology Platform](/t5/technology-blog-posts-by-sap/get-your-organization-in-shape-keep-a-clean-core-with-sap-business/ba-p/13561064)

![JohnClavijo](https://avatars.profile.sap.com/f/d/idfdad6cae86fef0ae46ada5ba6e6e6a4a8027a3c7bec067a74af011bf5d090908_small.jpeg "JohnClavijo")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[JohnClavijo](https://community.sap.com/t5/user/viewprofilepage/user-id/138628)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161530)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161530)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561064)

‎2023 Feb 06
9:15 PM

[60
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161530/tab/all-users "Click here to see who gave kudos to this post.")

27,186

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Build](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build/pd-p/73555000100700001491)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Build

  Software Product](/t5/c-khhcw49343/SAP%2BBuild/pd-p/73555000100700001491)

View products (3)

There is no question that the future is digital, So digital transformation is essential for any competitive business. Organizations must embark on a digital transformation journey that implies either a fresh start  or building on top of their existing investment.

This journey isn't  just about adopting new technology  but is  a quest to  provide differentiating value to customers while being highly available. To help organizations achieve these goals, SAP introduced its *clean core* strategy designed for those running  legacy ERP systems and envisioning a move to a  next-generation ERP like S/4HANA or for  those ready to adopt S/4HANA natively.

The strategy implies keeping the ERP system as close as possible to the standard, decoupling customizations, adopting inner extension methods and being aware of the customization footprint.

If you are wondering how to begin, follow these strategies to get a clean core:

1. Retire the code which is not being used.

2. Leverage SAP standard processes where possible by adhering to Fit-to-Standard.

3. Use APIs to leverage BTP application development and integration.

4. Document technical debt in case making clean core extension is not possible.

5. Leverage tools like the SAP custom code Migration App.

Do you want more details? If you are in IT Leadership check the [Custom Extensions in SAP S/4HANA Implementation](https://www.sap.com/documents/2020/03/ceeea71f-8a7d-0010-87a3-c30de2ffd8ff.html) guide, or if you are a project manager, key user or ABAP developer check the  [SAP S/4HANA extensibility guide.](https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html)

**Why keeping a clean core is important?**

Simply because keeping a clean core makes business future-proof. On the one hand, a clean core ensures operations are stable and reliable, while on the other hand, they remain agile and able to innovate at market speed.

Since Business Processes vary from one organization to another,  customers require ERP systems to cover their specific and unique scenarios through customization. This customization is defined as *Extensibility*.

SAP customers have followed a ***Classic Extensibility*** approach to implement Extensibility in the past. Classic Extensibility allowed developers to modify the SAP Core, which was reasonable for On-Premise Operation Models. However,  that is no longer a sustainable approach for Cloud Operation Models.  The main reason behind this is that this kind of  Extensibility adds too much complexity to the Core and prevents adopting agile practices. For example,  implementing new software versions  becomes too complex, too long, or too expensive.

To address this challenge, It was necessary to think about the evolution of Classic Extensibility and sustainably adapt to modern business models. A new evolution module proposes decoupling two components: one focused on *predictability* and the other on *exploration*. This evolution model is known as *Bimodal IT*, a concept that  Gartner first introduced. Understanding  this concept is paramount for organizations starting their digital transformation journey.

Following *Bimodal IT* and in line with the adoption of Cloud practices, SAP proposes instead ***In-App*** and ***Side-Side** Extensibility* to implement new standard functionalities without needing external tools.

![](/legacyfs/online/storage/blog_attachments/2023/02/bimodal.jpg)

Through *In-App Extensibility* the digital Core of SAP S/4HANA offers a set of tools covering diverse needs like modifying the UI, exposing data models, adding application logic and  running specific transactions, among others. Additionally, following a  'Fit-to-Standard’  approach, SAP constantly adopts new standard business process through the latest product releases. Hence, Industry best practices are applied to create a self-reliant solution for customers to operate effectively.

On the other hand, through Side-By-Side Extensibility SAP provides a decoupled way to innovate and implement new extensibility techniques. Side-by-side extensions open up the door to possibilities like mobile user experience, B2C and B2B integrations, Data Science, Business Intelligence, IoT  among many others.

Additionally, Side-By-Side Extensibility is supported by SAP Business Technology Platform through  integrations that provide seamless user experience, process connectivity, event management   and data replication.

![](/legacyfs/online/storage/blog_attachments/2023/02/Extensions.jpg)

**How to achieve a clean core with SAP** **Business T****echnology Platform?**

By leveraging  Side-By-Side Extensibility on SAP Business Technology Platform.

While predictability is offered by the S/4HANA Core and *In-App Extensibility,* exploration *and* innovation  are available through SAP Business Technology Platform Technology and  Side-By-Side Extensibility. Specifically, SAP Business Technology Platform  offers Cloud services that integrate seamlessly with the SAP Core and help the business get the differentiating value it requires. The Platform is a unified and open PaaS that combines several capabilities on one  public cloud platform where customers can deploy their extensions, minimizing the use ...