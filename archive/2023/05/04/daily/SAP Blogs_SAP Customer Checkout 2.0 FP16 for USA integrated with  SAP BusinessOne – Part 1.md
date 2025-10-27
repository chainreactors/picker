---
title: SAP Customer Checkout 2.0 FP16 for USA integrated with  SAP BusinessOne – Part 1
url: https://blogs.sap.com/2023/05/03/sap-customer-checkout-2.0-fp16-for-usa-integrated-with-sap-businessone-part-1/
source: SAP Blogs
date: 2023-05-04
fetch_date: 2025-10-04T11:39:34.024877
---

# SAP Customer Checkout 2.0 FP16 for USA integrated with  SAP BusinessOne – Part 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* SAP Customer Checkout 2.0 FP16 for USA integrated ...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/13040&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Customer Checkout 2.0 FP16 for USA integrated with SAP BusinessOne - Part 1](/t5/crm-and-cx-blog-posts-by-sap/sap-customer-checkout-2-0-fp16-for-usa-integrated-with-sap-businessone-part/ba-p/13556488)

![bikash_bansal](https://avatars.profile.sap.com/b/3/idb35cafc83758032f2e6cec7e6eb8dc243379361bda3dab3f008c43651ca0c57c_small.jpeg "bikash_bansal")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[bikash\_bansal](https://community.sap.com/t5/user/viewprofilepage/user-id/317354)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=13040)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/13040)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556488)

‎2023 May 03
10:48 PM

[4
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/13040/tab/all-users "Click here to see who gave kudos to this post.")

879

* SAP Managed Tags
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004775)
* [SAP Customer Checkout](https://community.sap.com/t5/c-khhcw49343/SAP%2520Customer%2520Checkout/pd-p/67838200100800006251)
* [SAP Point-of-Sale](https://community.sap.com/t5/c-khhcw49343/SAP%2520Point-of-Sale/pd-p/01200615320800000725)

* [SAP Customer Checkout

  SAP Customer Checkout](/t5/c-khhcw49343/SAP%2BCustomer%2BCheckout/pd-p/67838200100800006251)
* [SAP Point-of-Sale

  SAP Point-of-Sale](/t5/c-khhcw49343/SAP%2BPoint-of-Sale/pd-p/01200615320800000725)
* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004775)

View products (4)

This blog details a topic which is planned for delivery with a future release FP16 of SAP Customer Checkout 2.0 (scheduled for end of Q2,2023). The functionality are all subject to change and may be changed by SAP at any time for any reason without notice. The information in this
blog is not a commitment, promise or legal obligation to deliver any material, code or functionality.

Hello Everyone,

This blog post informs you about integration of SAP Customer Checkout 2.0 FP16 to SAP BusinessOne for USA localization. In this integration no external third party system for tax calculation is used by SAP Customer Checkout. However SAP Customer Checkout in standalone mode also supports integration to Avalara for tax calculation which is not part of this blog.

In this 1st blog, i explain the concepts, what is supported and what is not supported.
In the [2nd blog](https://blogs.sap.com/2023/05/03/sap-customer-checkout-2.0-fp16-for-usa-integrated-with-sap-businessone-part-2/), which is more aimed at implementation consultants, i explained step-by-step with screenshots how to configure SAP Customer Checkout specific for US localization integration of SAP Business One.

**Understand the basis**

SAP BusinessOne integration for US localization is supported from SAP Customer Checkout 2.0 FP16. It is not really dependant on a specific SAP Business One version or version of SAP Customer Checkout B1if scenarios for SAP Business One integration.  For USA localization, when integrated with SAP Business One, SAP Customer Checkout calculates the tax locally and does not call an external third party system for tax calculation. Lets understand how it works.
SAP Customer Checkout requires a default tax-rate and a zero-tax-rate for non-tax article(also called tax-exempt article or Tax Liable = false). Let's assume a default tax-rate called 'NYC' which is 8.875% and tax-rate called 'US0' which is 0.0%.

When articles in SAP Business One are tax liable then we apply the default tax-rate called 'NYC' for tax-calculation, and when articles in SAP Business One are not tax liable then we apply the zero-tax-rate called 'US0' for tax-calculation.
If a customer is tax liable, then articles data is used to decide whether the article is taxed or not, and if a customer is not tax liable, then for all articles zero-tax-rate called 'US0' is used for tax-calculation.

It is possible that during the sales process, you can switch from the default tax rate example 'NYC' to zero-tax-rate example 'US0' for specific article or the whole transactions.If other tax rates are maintained locally, it is also possible to switch between different tax codes.

When a sales transaction is finished in SAP Customer Checkout, then in real time the transaction with tax information is posted to SAP Business One. SAP Business One then breaks down the tax into different components like City Tax(4.5%), State Tax(4%) and Metropolitan Commuter Transportation District surcharge(0.375%) and stores it.

**What is not supported (in integration with SAP BusinessOne)**1) SAP Customer Checkout does not know the break-of default tax-rate example 'NYC' into different components like New York City local sales and use tax rate of 4.5 percent, New York State sales and use tax rate of 4.0 percent, and Metropolitan Commuter Transportation District surcharge of 0.375 percent. It does not store this break-up and it cannot print this break-up. This information is available in your SAP Business One system as the transaction reaches to SAP Business One system in real time.

2) SAP Customer Checkout does not store multiple shipment address of customer or the tax code assigned to the shipment address of the customer. It just knows if the customer is tax liable or not tax liable and reacts based on this flag.

3) It does not know the different tax jurisdiction or tax determination. So if you have 1 tax code for Article Group A, and another tax code for Article Group B. SAP Customer Checkout does not fetch this information from SAP Business One. SAP Customer Checkout either applies the default tax rate or the zero-tax-rate.

**Step-by-step configuration**If you are interested in a step-by-step configuration, kindly proceed with the 2nd part of this blog where i explain this with screenshots.

In this blog, you have learnt about SAP Customer Checkout and SAP Business One focusing on out-of-the-box integration for USA.

Hope you enjoyed the blog. Best of luck with your SAP Customer Checkout journey.

**Feel free to comment and give feedback about the blog.**

**About me:**
**My name is Bikash Bansal. I work for SAP SE, Germany. My current role is of Product Owner for SAP Customer Checkout.**
You can find more blogs from me about SAP Customer Checkout [here](https://blogs.sap.com/author/bikash.bansal/).

Labels

* [Product Updates](/t5/crm...