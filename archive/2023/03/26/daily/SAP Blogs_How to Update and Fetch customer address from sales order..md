---
title: How to Update and Fetch customer address from sales order.
url: https://blogs.sap.com/2023/03/25/how-to-update-and-fetch-customer-address-from-sales-order./
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:54.252902
---

# How to Update and Fetch customer address from sales order.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to Update and Fetch customer address from sale...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67747&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Update and Fetch customer address from sales order.](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-update-and-fetch-customer-address-from-sales-order/ba-p/13559141)

![Shrikant_Metkar](https://avatars.profile.sap.com/1/4/id148eed1a49577511e6c78a989cdb6103d5e68c0c90a9812a6103a8e3a27d4887_small.jpeg "Shrikant_Metkar")

[Shrikant\_Metkar](https://community.sap.com/t5/user/viewprofilepage/user-id/4496)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67747)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67747)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559141)

‎2023 Mar 25
5:15 AM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67747/tab/all-users "Click here to see who gave kudos to this post.")

6,311

* SAP Managed Tags
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)

* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)

View products (1)

Customer address we used in many scenarios in O2C flows we use customer addresses to print on the smart form (Output). send it through idoc etc.

I am bringing this topic to you based on my experience in the implementation project \_

Some of you already know how to change a customer address in a Sales order and how to put logic to fetch details for the same however some are not still aware that we can change a customer address and we can fetch the address of the customer at sales order level as well\_

So let's begin... I will cover the below points\_

1. Fetching the customer address from the customer master.

2. How to change the Customer address in the sales order?

3. Fetching the customer address from the Sales order.

4. Workaround proposal for the customer address if it's fetched from the order level.

**1. Fetching address from customer master:**

Many consultants follow this approach to fetch data from the KNA1 table and use it in output,

the report, idoc etc.

the logic to fetch the customer address from KNA1 is\_

Pass KUNNR field into a table KNA1 and get ADRNR field

Pass ADRNR field as ADDRNUMBER into a table ADRC and get customer address

(NAME, STRRET, House Number, City, Pin code)

**2. How to change the customer address in the Sales Order?**

go to sales document (VA01/VA02) Header - Partners tab and double click on the

partner function for which you want to change the address details\_

![](/legacyfs/online/storage/blog_attachments/2023/03/Tes01.jpg)

and after completing changes save the order.

So before changing the customer address in the sales order the address number at sales order

VBPA and KNA1 table level will be same\_

![](/legacyfs/online/storage/blog_attachments/2023/03/KNA1-VBPA-1.jpg)

After changing address of customer in sales order your sales order level address number get

change and new address number will contain address from your sales order.

![](/legacyfs/online/storage/blog_attachments/2023/03/VBPA-Change.jpg)

**3. Fetching the customer address from the Sales order.**

Pass VBELN field into a table VBPA and get ADRNR field

Pass ADRNR field as ADDRNUMBER into a table ADRC and get customer address

(NAME, STRRET, House Number, City, Pin code)

**4. Workaround proposal for the customer address if it's fetched from the order level.**

In implementation project we have seen some scenario where customer address is not correctly updated into a system and user want to issue invoice, delivery, order to customer with correct address details so we can advice user to change it in the order itself and system will fetch expected details and user need not to wait till there master data get corrected.

**Conclusion:**

You can change the customer address only in sales order and delivery. when you update customer address in order or delivery it will automatically reflect in both place. however SAP have not given this functionality for invoice.

Change in customer address can be done in sales order even after the subsequent document are created.

Customer address change will be applicable only for particular Order and subsequent delivery.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fhow-to-update-and-fetch-customer-address-from-sales-order%2Fba-p%2F13559141%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [SAP Enterprise Support Academy Newsletter October 2025](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-enterprise-support-academy-newsletter-october-2025/ba-p/14232476)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [SII tip for Spain #5B: SII Adjustments for Canary Islands October 2025 - Enabling AIEM](/t5/enterprise-resource-planning-blog-posts-by-sap/sii-tip-for-spain-5b-sii-adjustments-for-canary-islands-october-2025/ba-p/14231940)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [Sales\_Q&A - Bulgaria EUR Transition for S/4HANA Cloud Public Cloud Live Customers](/t5/enterprise-resource-planning-blog-posts-by-sap/sales-q-amp-a-bulgaria-eur-transition-for-s-4hana-cloud-public-cloud-live/ba-p/14230125)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofil...