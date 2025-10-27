---
title: SAP Customer Checkout 2.0 FP16 for USA integrated with SAP BusinessOne – Part 2
url: https://blogs.sap.com/2023/05/03/sap-customer-checkout-2.0-fp16-for-usa-integrated-with-sap-businessone-part-2/
source: SAP Blogs
date: 2023-05-04
fetch_date: 2025-10-04T11:39:36.154039
---

# SAP Customer Checkout 2.0 FP16 for USA integrated with SAP BusinessOne – Part 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by SAP](/t5/crm-and-cx-blog-posts-by-sap/bg-p/crm-blog-sap)
* SAP Customer Checkout 2.0 FP16 for USA integrated ...

CRM and CX Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-sap/article-id/13079&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Customer Checkout 2.0 FP16 for USA integrated with SAP BusinessOne – Part 2](/t5/crm-and-cx-blog-posts-by-sap/sap-customer-checkout-2-0-fp16-for-usa-integrated-with-sap-businessone-part/ba-p/13558367)

![bikash_bansal](https://avatars.profile.sap.com/b/3/idb35cafc83758032f2e6cec7e6eb8dc243379361bda3dab3f008c43651ca0c57c_small.jpeg "bikash_bansal")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[bikash\_bansal](https://community.sap.com/t5/user/viewprofilepage/user-id/317354)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-sap&message.id=13079)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-sap/article-id/13079)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558367)

‎2023 May 03
10:46 PM

[3
Kudos](/t5/kudos/messagepage/board-id/crm-blog-sap/message-id/13079/tab/all-users "Click here to see who gave kudos to this post.")

1,271

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

This is 2nd part of the blog series regarding integration of SAP Customer Checkout 2.0 FP16 to SAP BusinessOne for USA localization. [The 1st blog can be read here](https://blogs.sap.com/2023/05/03/sap-customer-checkout-2.0-fp16-for-usa-integrated-with-sap-businessone-part-1/).

In the 2nd part, which is more aimed at implementation consultants, i explain step-by-step with screenshots how to configure SAP Customer Checkout specific for US localization integration of SAP Business One. In this blog, i do not discuss about how to install SAP Customer Checkout, or SAP Customer Checkout manager, or integrate out-of-the-box with SAP Business One using SAP Business One Integration Framework(B1if). It is assumed that the integration is set-up and 'check connection' is working. For beginners, this blog '[Getting started with SAP Customer Checkout and SAP Business One can help](https://blogs.sap.com/2021/04/18/sap-customer-checkout-and-sap-businessone-getting-started/)' can help.

In this current blog, we focus on US localization specific topics.

**Step-by-step configuration**
Let's start with SAP Business One as i assume this is familiar territory for SAP Business One consultant. I have created 2 sales tax code. 1st called NYC with 8.875% and  2nd called US0 with 0% tax. I created 2 articles.1 with tax liable flag set, and another with tax liable flag false.
I created 2 Customers, 1 is tax status Liable and 2nd one tax status exempt.
Below are the screenshots for reference.

Sales tax code with 8.875% tax
![](/legacyfs/online/storage/blog_attachments/2023/05/B1_Tax_Definition.jpg)

Sales tax code with 0.000% tax

![](/legacyfs/online/storage/blog_attachments/2023/05/B1_Tax_Definition_US0.jpg)
Article with tax liable flag set to true

![](/legacyfs/online/storage/blog_attachments/2023/05/Article_Tax.jpg)

Article with tax liable flag set to false

![](/legacyfs/online/storage/blog_attachments/2023/05/Article_No_Tax.jpg)

Customer with tax status liable

![](/legacyfs/online/storage/blog_attachments/2023/05/Customer_Tax.jpg)

Customer with tax status Exempt

![](/legacyfs/online/storage/blog_attachments/2023/05/B1_Customer_No_Tax.jpg)

Tax Code Determination maintained in SAP Business One is not used by SAP Customer Checkout.

![](/legacyfs/online/storage/blog_attachments/2023/05/B1_Tax_Jurisdiction.png)

Finally the account/PettyCash used by SAP Customer Checkout for cash transaction or card transaction needs to be extracted from the SAP Business One OACT table. This data we will see later where to maintain in SAP Customer Checkout.
![](/legacyfs/online/storage/blog_attachments/2023/05/B1_PettyCash.png)

Now lets start with SAP Customer Checkout. You select the country as US-United States and select a state. This ask for a confirmation as we will switch some configuration for you- which i will mention next.

![](/legacyfs/online/storage/blog_attachments/2023/04/1-23.jpg)

As a result of selection of United States as country,
we change the default currency to USD. screenshot below.
We maintain a field mapping USD=$. screenshot below.
We change the Taxation, Tax calculation mode, and Tax calculation trigger. screenshot below.

The currency is auto-selected to USD.

![](/legacyfs/online/storage/blog_attachments/2023/05/2_CCO_Default_Currency.png)

The field mapping is automatically maintained USD=$.
![](/legacyfs/online/storage/blog_attachments/2023/05/3_CCO_Field_mapping.png)

The tax calculation mode is automatically set.
![](/legacyfs/online/storage/blog_attachments/2023/05/4_CCO_Tax_calculation_Mode.png)

Now you need to maintain 3 very important data. Tax codes, Petty Cash and Default Tax rate. Attached screenshot to assist you.
Tax Codes
![](/legacyfs/online/storage/blog_attachments/2023/05/5_CCO_Tax_Config.png)

Petty Cash. This is the general ledger account to which cash transactions are posted. Same is true for different card payments. The data in Master Petty Cash ID, General Ledger Account needs to be filled with data from SAP Business One. You need to take this data from OACT table like you showed above.
![](/legacyfs/online/storage/blog_attachments/2023/05/6_CCO_PettyCash.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/6.jpg)

Default Tax Rate: This is the tax rate that will be applied to all items which are tax liable.

![](/legacyfs/online/storage/blog_attachments/2023/05/41_CCO_Tax_calcu.png)

Now that all configuration is done, you are re...