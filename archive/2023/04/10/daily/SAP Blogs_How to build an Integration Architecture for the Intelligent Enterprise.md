---
title: How to build an Integration Architecture for the Intelligent Enterprise
url: https://blogs.sap.com/2023/04/09/how-to-build-an-integration-architecture-for-the-intelligent-enterprise/
source: SAP Blogs
date: 2023-04-10
fetch_date: 2025-10-04T11:29:42.354997
---

# How to build an Integration Architecture for the Intelligent Enterprise

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to build an Integration Architecture for the I...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163606&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to build an Integration Architecture for the Intelligent Enterprise](/t5/technology-blog-posts-by-members/how-to-build-an-integration-architecture-for-the-intelligent-enterprise/ba-p/13571281)

![stevang](https://avatars.profile.sap.com/f/c/idfced6a2c78544706495f6bfa2d992f63b191b332f455b7b5131be97f1bce95b8_small.jpeg "stevang")

[stevang](https://community.sap.com/t5/user/viewprofilepage/user-id/7643)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163606)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163606)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571281)

‎2023 Apr 09
8:09 PM

[15
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163606/tab/all-users "Click here to see who gave kudos to this post.")

5,825

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Integration Strategy](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Strategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)
* [SAP Business Accelerator Hub](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Accelerator%2520Hub/pd-p/73555000100800001091)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Strategy

  Topic](/t5/c-khhcw49343/SAP%2BIntegration%2BStrategy/pd-p/e26e2f63-fcc1-42a7-af06-decec0762b90)
* [SAP Business Accelerator Hub

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BAccelerator%2BHub/pd-p/73555000100800001091)

View products (3)

![](/legacyfs/online/storage/blog_attachments/2023/04/denny-muller-JyRTi3LoQnc-unsplash.jpg)

How do we build an Integration Architecture for the Intelligent Enterprise?

Okay, let’s start with the usual disclaimers – we need to be pragmatic and use common sense (as always in the Architecture area). I have presented some views on Lean EA (Enterprise Architecture) in my article [Enterprise Architecture in the era of Agile…](https://groups.community.sap.com/t5/enterprise-architecture-blog/enterprise-architecture-in-the-era-of-agile/ba-p/224058)

Common sense, and no “worshiping” of any EA frameworks, fine – but we could still use some guidelines, right?

This article is providing a high-level overview – how to build Integration Architecture in the Organization. As usually, I am providing Solution Concept (an idea or working idea), not a Solution itself.

## Integration Guiding Principles

On the Enterprise Architecture level, I would define 2 main guiding principles:

1. Consumer driven integration – we build for business needs; APIs should not dictate the integration;

2. Events driven integration – no need to replicate and create multiple copies of the same “data” in the different Systems;

On the Solution Architecture level (when solutioning & designing integrations), I would define 2+1 main guiding principles:

1. Use standard –whenever possible;

2. Reuse existing – as much as possible;

3. Keep it well documented (this is "+1" as this is something we should commonly enforce in all domains);

## The Approach (or Methodology)

We do need to put some order in the Integration Architecture. And let us not reinvent the “hot water”…

I would start with SAP Integration Solution Advisory Methodology (ISA-M)[1]. No, it is not used only for SAP Eco space. ISA-M defines (among other things) **Integration Domains**, **Integration Styles** and **Use Cases Patterns** in a very agnostic way.

In this article, I will stay with the agnostic part of ISA-M, as I firmly believe Enterprise Architecture should not be vendor driven (at least on the high-level), just as I believe Integration Architecture should not be API driven[2].

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture1-24.png)

ISA-M proposes a very useful definition and split into main **Integration Styles** and accompanying **Use Cases Patterns**:

* **Process Integration** Style; and **Master Data Integration**, **A2A**, **B2B** associated Use Case Pattern;

* **Data Integration** Style; and **ETL**, **Data Orchestration** associated Use Case Pattern;

* **User Integration** Style; and **UI Integration**, **Chatbot Integration** associated Use Case Pattern

* Etc,

**Use Case Patters** can have many **Integration Services**

E.g. *Customer* (Business Object) **Integration Service** within **Process Integration** Style (as part of the business process of creating/updating of the *Customer/Account*) could be part of **Master Data Integration** Use Case Pattern; but *Customer* (Business Object) **Integration Service** within **Data Integration** Style (for DWH and reporting) could be part of **ETL** Use Case Pattern…

*Sales Order* (Business Object) **Integration Service** within **Process Integration** Style (as business process of Order Fulfillment) could be part of **A2A** Use Case Pattern…

*Service Ticker* (Business Object) within **User Integration** Style (as iFrame) could be part of **UI Integration** Use Case Pattern…

While each Organization has it’s one **Integration Services**, some common “major” services are usually built around key Business Object (or Data Object). Here as well, fortunately, there are many proposed “Best Practice” definitions. I find [LeanIX](https://www.leanix.net/en/)[3][4] approach very useful for building Integration Architecture (and Enterprise Architecture overall).

Now, let’s clearly understand one Business Object does not represent one Integration Service.

E.g. Business Object Sales Order is essentially part of several Integration Services like Sales Order Replicate, Sales Order Create/Update etc.

![](/legacyfs/online/storage/blog_attachments/2023/04/Picture2-18.png)

Also, one Integration Service may have more than one Interface – and this is not because of GET, POST, PUT etc. – this would still be one interface, but with different methods. Let’s take an example – we might be designing *Product Replicate* Integration Service from S/4HANA which consists of two interfaces – one is MATMAS IDoc for *Material*, and one is CLFMAS IDoc for (*Material) Classification*.

And, of course, each System may have more Integration Services, and versa-vise one Integration Services may be used to connect more than two Systems.

### A bit more on SAP ISA-M…

Of course, when building SAP specific Integration Architecture one can further benefit with various accelerators. For more details on ISA-M and how to start using it, pls visit the official page[5]. To learn more about current template versions (version 4 is the latest available, pls. check article [SAP Integration Solution Advisory Methodology: Template version 4.0 available now](https://blogs.sap.com/2022/08/25/sap-integration-solution-advisory-methodology-template-version-4.0-available-now...