---
title: Financial Accounting for SAP Subscription Billing with Sales Billing in S/4HANA Cloud
url: https://blogs.sap.com/2023/08/03/financial-accounting-for-sap-subscription-billing-with-sales-billing-in-s-4hana-cloud/
source: SAP Blogs
date: 2023-08-04
fetch_date: 2025-10-04T12:01:29.507694
---

# Financial Accounting for SAP Subscription Billing with Sales Billing in S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Financial Accounting for SAP Subscription Billing ...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/52177&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Financial Accounting for SAP Subscription Billing with Sales Billing in S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/financial-accounting-for-sap-subscription-billing-with-sales-billing-in-s/ba-p/13562594)

![volkmar_zahn](https://avatars.profile.sap.com/f/5/idf5a29b40977409c9dcb297526d07ae01fcc24a135380b6acb969addd469a2c7e_small.jpeg "volkmar_zahn")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[volkmar\_zahn](https://community.sap.com/t5/user/viewprofilepage/user-id/286333)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=52177)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/52177)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562594)

‎2023 Aug 03
8:24 PM

[20
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/52177/tab/all-users "Click here to see who gave kudos to this post.")

5,845

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Subscription Billing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Subscription%2520Billing/pd-p/73555000100800000472)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [SAP Subscription Billing

  SAP Billing and Revenue Innovation Management](/t5/c-khhcw49343/SAP%2BSubscription%2BBilling/pd-p/73555000100800000472)

View products (3)

Subscriptions and recurring revenue patterns have become a hot topic for many customers and across all industries. The scenarios range from the sales of digital assets such as the right to use software to the sales of physical goods such as consumables.

Subscription models offer benefits to both the provider of the subscription and the end customer: The provider can set up a steady, predictable revenue flow, and the end customer can spread an upfront investment over time, allowing for a predictable budgeting and flexibility to adapt the right level of service and features over time.

The integration of SAP Subscription Billing with S/4HANA Cloud, public edition (in the following referred to as S/4HANA Cloud) enables you to support subscription-based business models linked to a powerful Finance solution. In this blog, we'll take a deep dive into the integration with a special focus on the aspects of revenue recognition and margin analysis.

SAP Subscription Billing offers numerous capabilities which are well described in many blogs or in the user assistance. For instance, you can find a great set of resources [here](https://blogs.sap.com/tag/sap-subscription-billing-how-to/). Subscription Billing has been designed as a set of microservices that can be integrated also with non-SAP solutions. The real power, however, comes with the integration into S/4HANA Cloud, which we want to explore here.

The integration is based on two integration scenarios: Integration with Sales Billing and the integration with Contract Accounting and Invoicing in S/4HANA Cloud.

![](/legacyfs/online/storage/blog_attachments/2023/07/Fig-1-Solution-Options-in-S4HANA-Cloud-1.png)

In this blog we want to focus on the **integration with Sales Billing** with the special focus on Finance. Well, in fact it's even more than that as we'll talk about the full end-to-end scenario starting with the integration into the solution order on one side and controlling and accounting at the other end of the spectrum. If your business requires a bundling of subscriptions with other sales types, such as projects, service documents and sales orders, the solution order is a perfect fit. And the tight integration into accounting and controlling allows you to do a combined margin analysis of revenues and costs on the aggregated level of the solution order.

Interested? OK, then let’s get started. Before we get into a little system-based scenario, some fundamental aspects first.

SAP Subscription Billing is based on **SAP’s Business Technology Platform**. Integration with S/4HANA Cloud is done via services, enabling the applications to run decoupled from one other.

Each subscription in Subscription Billing is replicated to a **provider contract** in S/4HANA, which represents the accounting view. This means the provider contract holds additional attributes that are relevant for the follow-on processes in Finance. For example, it holds the revenue recognition key for event-based revenue recognition, or the profit center. The provider contract becomes part of the market segment and the Universal Journal and, simply speaking, is the basis for profitability reporting in S/4HANA Cloud when it comes to subscriptions.

We must also explore the underlying data model a bit further. Firstly, the **products** defined in Subscription Billing are synchronized with the materials in S/4HANA Cloud. The subscription product holds a rate plan with rate elements, which could represent, for example, a one-time fee or a recurring charge based on usages or number of licenses. Essentially a product entered in a subscription item could be broken down into 1 to n rate elements. In this setup, not only is the top-level product mapped into a material in S/4HANA but also the underlying rate elements refer to materials. Usually, you want to understand how well a product sells. Consequently, in Finance the top-level product is mapped into the product sold, while the sub level materials are passed through as “consumption” materials.

![](/legacyfs/online/storage/blog_attachments/2023/07/Fig-2-Subscription-and-Provider-Contract-3.png)

Another important element in the data model is the **billing forecast** and **billing plan**. A common requirement, especially in subscription scenarios, is to recognize revenue independently from billing – which is a fundamental requirement of the revenue accounting standard IFRS 15. For this purpose, the billing forecast in Subscription Billing provides estimates of expected billing amounts for a given time frame. The billing forecast is mapped to the billing plan in Convergent Invoicing in S/4HANA. While the billing plan is a standalone business object (in contrast to the billing plan in service contracts, for example), here it can be seen as an attachment to the provider contract, which is used by event-based revenue recognition to accrue revenue independently of the actual invoice amount and dates.

To complete the picture, we need to talk about **billing**. Subscription Billing is responsible for the rating and pre-billing of subscri...