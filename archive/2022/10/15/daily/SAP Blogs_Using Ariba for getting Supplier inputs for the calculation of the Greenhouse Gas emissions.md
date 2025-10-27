---
title: Using Ariba for getting Supplier inputs for the calculation of the Greenhouse Gas emissions
url: https://blogs.sap.com/2022/10/14/using-ariba-for-getting-supplier-inputs-for-the-calculation-of-the-greenhouse-gas-emissions/
source: SAP Blogs
date: 2022-10-15
fetch_date: 2025-10-03T19:56:41.988674
---

# Using Ariba for getting Supplier inputs for the calculation of the Greenhouse Gas emissions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Using Ariba for getting Supplier inputs for the ca...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/157414&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using Ariba for getting Supplier inputs for the calculation of the Greenhouse Gas emissions](/t5/technology-blog-posts-by-members/using-ariba-for-getting-supplier-inputs-for-the-calculation-of-the/ba-p/13532869)

![stevang](https://avatars.profile.sap.com/f/c/idfced6a2c78544706495f6bfa2d992f63b191b332f455b7b5131be97f1bce95b8_small.jpeg "stevang")

[stevang](https://community.sap.com/t5/user/viewprofilepage/user-id/7643)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=157414)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/157414)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13532869)

‎2022 Oct 14
6:45 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/157414/tab/all-users "Click here to see who gave kudos to this post.")

3,160

* SAP Managed Tags
* [SAP Ariba Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Procurement/pd-p/73554900100700001921)
* [SAP Ariba Supplier Lifecycle and Performance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Supplier%2520Lifecycle%2520and%2520Performance/pd-p/9566c2c2-c688-4939-ac50-30732b383e53)
* [SAP Supplier Lifecycle Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Supplier%2520Lifecycle%2520Management/pd-p/01200314690800002016)
* [Sustainability](https://community.sap.com/t5/c-khhcw49343/Sustainability/pd-p/140502597117949649788634441139048)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Supplier Lifecycle Management

  SAP Supplier Lifecycle Management](/t5/c-khhcw49343/SAP%2BSupplier%2BLifecycle%2BManagement/pd-p/01200314690800002016)
* [Sustainability

  Topic](/t5/c-khhcw49343/Sustainability/pd-p/140502597117949649788634441139048)
* [SAP Ariba Procurement

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BProcurement/pd-p/73554900100700001921)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)
* [SAP Ariba Supplier Lifecycle and Performance

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BSupplier%2BLifecycle%2Band%2BPerformance/pd-p/9566c2c2-c688-4939-ac50-30732b383e53)

View products (5)

# **Introduction**

In this article, I am presenting a Solution Concept – how to use Ariba to support Sustainability topics. I am addressing some of the common problems related with acquiring Suppliers’ specific inputs, necessary for the calculation of the Greenhouse Gas (GHG) emissions. I will present some Solution Concept(s) how Ariba Procurement and/or Ariba Supplier Lifecycle Management (SLP) products can join “force” with SAP Business Technology Platform (BTP) in resolving these problems.

This article is not about Solution itself, but more about Architectural Thinking – reviewing Problem Context, and ideating on possible Solution Concept(s).

# **Problem Statement**

Let’s start with explaining the greenhouse gas “problem”…

When talking about Sustainability and Sustainability reporting, under greenhouse gas emissions, we are basically referring to gasses which are causing the, so-called, greenhouse effect. Now, greenhouse gasses are not something new. They were always present in the atmosphere, but in much lower concentrations. Human activities since the beginning of the industrial revolution have caused an increase of over 50% of the atmospheric concentration of carbon dioxide [1], which is the principal contributor to the greenhouse effect. Most carbon dioxide emissions come from combustion of fossil fuels; principally coal, petroleum (including oil) and natural gas. All this is used in various operations; like production of electricity which is then used in many other operations; or production of the raw materials or (semi-)finish goods; or it is used in transport and logistics; etc.

Of course, it is not only carbon dioxide (CO2) which causes the greenhouse effect. Other gasses are contributors as well like methane (CH4), nitrous oxide (N2O) etc. To simplify the calculation, the potential of each greenhouse gas to cause global warming is expressed in carbon dioxide equivalent (CO2e), so in general when saying “carbon emissions” we actually mean “carbon dioxide equivalent emissions” [2].

But why is all this important?

As stated above, greenhouse gas emissions are causing the greenhouse effect. The greenhouse effect is a process that occurs when energy from the Sun goes through Earth's atmosphere and heats the  surface, but greenhouse gasses in the atmosphere prevent some of the heat from returning directly to space, resulting in a warmer planet [3]. At current greenhouse gas emissions rates, temperatures could increase by 2 C in the next thirty years, which the United Nations Intergovernmental Panel on Climate Change (IPCC) marked as an upper limit to avoid "dangerous" levels [4]. As per Paris Agreement [5] the goal is “to limit global warming to well-below 2°C above pre-industrial levels and pursue efforts to limit warming to 1.5°C”.

And how do we measure greenhouse gas emissions?

To be able to control greenhouse gas emissions rates, we are implementing protocols to measure CO2e emissions, like Greenhouse Gas Protocol [6]. As per Greenhouse Gas Protocol, depending on the operations, we recognize three scopes of the emissions:

* Scope 1: all carbon emissions from own operations, like factories and intra logistics.

* Scope 2: all carbon emissions related to purchased energy

* Scope 3: all external emissions:

Furthermore, operations may be upstream or downstream:

* Upstream: emissions related to all procured goods and services

* Downstream: emissions related to lifecycle emissions of finished products

This article will address, as examples, carbon emission from the consumed electricity (Scope 2, but also relevant for Scope 3 – e.g. operations of leased outlets) and carbon emission from the raw materials (Scope 3).

# **Problem Context**

While for many activities (or operations in general) it is quite possible to calculate carbon emission from internally acquired data e.g. purchased goods and services, for some key operations and/or production activities, we must rely on Supplier provided data e.g.

1. % renewable electricity (out of overall consumed/acquired electricity)

2. % recycled content of the raw material (in packaging)

While carbon emission from consumed electricity can be fairly easily calculated (by applying specific emission factors from the Country, Region or Supplier), all renewable energy should be subtracted from that formula, since carbon emission of the renewable energy is set to zero. Obviously consumed electricity (as a non-stock item) is acquired either through invoicing from the Suppliers or based on (self-)meteri...