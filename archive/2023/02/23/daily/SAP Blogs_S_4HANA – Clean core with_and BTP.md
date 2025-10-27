---
title: S/4HANA – Clean core with/and BTP
url: https://blogs.sap.com/2023/02/22/s-4hana-clean-core-with-and-btp/
source: SAP Blogs
date: 2023-02-23
fetch_date: 2025-10-04T07:50:46.162168
---

# S/4HANA – Clean core with/and BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* SAP S/4HANA – Clean core with/and SAP BTP

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50959&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4HANA – Clean core with/and SAP BTP](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-clean-core-with-and-sap-btp/ba-p/13554328)

![Louenas](https://avatars.profile.sap.com/0/3/id03910ea804d671d62a34763617760b173ee6977feae88ebfe4bb4f35c812f5fc_small.jpeg "Louenas")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Louenas](https://community.sap.com/t5/user/viewprofilepage/user-id/3372)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50959)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50959)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554328)

‎2023 Feb 22
11:54 PM

[38
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50959/tab/all-users "Click here to see who gave kudos to this post.")

37,402

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud Public Edition Extensibility](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Extensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [SAP S/4HANA Cloud ABAP Environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520ABAP%2520Environment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP S/4HANA Cloud Public Edition Extensibility

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BExtensibility/pd-p/270c4f37-c335-46e1-bfad-a256637d5e26)
* [SAP S/4HANA Cloud ABAP Environment

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BABAP%2BEnvironment/pd-p/60907aa9-99e9-4d5d-9103-8b970e9bc0a4)

View products (4)

```
Last updated on August 1st, 2023
```

### Target audience:

Partners, CIOs, CTOs, Digital transformation officers, Practice leads, Innovation directors and any managers interested in learning about clean core and how to achieve it.

# Introduction:

In today's fast-paced business landscape, digital transformation has become a critical component of success. To stay competitive, companies must embark on this journey, whether by starting from scratch or building on their existing investments. However, a key consideration in future-proofing an organization is ensuring a clean core. SAP recognizes this, and it is a crucial element of their strategy. At the recent [SAP Global Partner Success Kickoff](https://blogs.sap.com/2023/02/13/7-takeaways-from-saps-global-partner-success-kickoff/), Scott Russell, SAP's Executive Board Member, and Karl, SAP's Chief Partner Officer, emphasized that partners should lead with RISE with SAP, a Business Transformation as a Service solution that has proven effective in helping customers establish and scale a clean core platform.

A clean core, in the context of an ERP system, is essential for ensuring stable and reliable operations while being agile and innovative. By maintaining a clean core, businesses can future-proof themselves and remain competitive in an ever-evolving business landscape.

In this blog, we will explore different extensibility options available with SAP S/4HANA and how they can help businesses achieve their clean core objectives.

# Why keeping a clean core is important:

An ERP system is the central system responsible for running an organization's day-to-day operations. Keeping this system clean core compliant is essential in ensuring that the organization remains future-proof. According to a [report by McKinsey](https://blogs.sap.com/www.mckinsey.com/capabilities/mckinsey-digital/our-insights/tech-debt-reclaiming-tech-equity), between 10 and 20 percent of the technology budget dedicated to new products is often diverted to resolving issues related to technical debt. This debt accumulates over the years due to numerous modifications to the core ERP system, resulting in significant maintenance and testing efforts during patches and software upgrades. This constant technical debt can leave companies frozen in the past by delaying upgrades and patches, and can make them slow to innovate while being exposed to unforeseen risks.

By prioritizing a clean core and implementing extensibility options that minimize modifications to the core ERP system, companies can avoid incurring technical debt and ensure that their technology budget is being spent on innovation and new product development. This approach can help businesses to stay ahead of the curve, remain competitive, and maintain the agility needed to thrive in today's ever-changing business landscape.

Unclean core could manifest itself in different forms:

**Release management**

* Too old ERP release

* Too old partner solution releases

**Code**

* Modifications to standard code

* Redundant enhancements to standard functionality

**Data**

* Database tables abused

* Data structures and fields used for the unintended purposes

**Processes**

* Unnecessary use of custom processes

* Disregard to SAP-recommended Best Practices

**Extensions/Integration**

* Use of non-approved add-ons

* Extensions built on non-upgrade-stable interfaces

* Integrations built using non-standard approaches

**Operations**

* luck of data cleaning discipline

* luck of housekeeping on security and user/authorizations

For its flagship SAP S/4HANA and line of business (LoB) cloud solutions, SAP offers different approaches for partners and customers to extend the digital core depending on the use case at hand. In this blog, I will focus only on SAP S/4HANA extensibility.

# Extensibility of SAP S/4HANA:

Extensibility for SAP S/4HANA can be categorized into three sections: key user extensibility, on-stack developer extensibility and finally side-by-side extensibility on the SAP Business Technology Platform. For more detailed and up-to-date information on ABAP Cloud and ABAP Extensibility, please refer to the [SAP S/4HANA extensibility guide](https://www.sap.com/documents/2022/10/52e0cd9b-497e-0010-bca6-c68f7e60039b.html) and go to the two following communities: [ABAP Development community](https://community.sap.com/topics/abap) and [ABAP Extensibility community](http://ABAP Extensibility)

**![](/legacyfs/online/storage/blog_...