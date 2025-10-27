---
title: Payment Differences and How to Deal with them in SAP S/4HANA Cloud
url: https://blogs.sap.com/2023/01/30/payment-differences-and-how-to-deal-with-them-in-sap-s-4hana-cloud/
source: SAP Blogs
date: 2023-01-31
fetch_date: 2025-10-04T05:13:48.638585
---

# Payment Differences and How to Deal with them in SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Payment Differences and How to Deal with them in S...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/53503&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Payment Differences and How to Deal with them in SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/payment-differences-and-how-to-deal-with-them-in-sap-s-4hana-cloud/ba-p/13571515)

![Angelika_Huber](https://avatars.profile.sap.com/d/4/idd4fb50795a33a62103c22a63d390308419c25107cb80a94c1d0c3db618ed9f37_small.jpeg "Angelika_Huber")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Angelika\_Huber](https://community.sap.com/t5/user/viewprofilepage/user-id/123878)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=53503)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/53503)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571515)

‎2023 Jan 30
9:17 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/53503/tab/all-users "Click here to see who gave kudos to this post.")

4,932

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Finance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

* [SAP S/4HANA Cloud Public Edition Finance

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BFinance/pd-p/66233466-fcd6-45d2-a9ae-2cba38c72e19)

View products (1)

Sometimes customers pay less than what they owe you. Does this sound familiar?
I bet it does, and you probably ask yourself how to deal with these payment differences. You‘ve heard all the buzz words - like *tolerance limits*, *partial payments*, *residual items, reason codes* - and your head is spinning. So, let’s take a closer look at how these features relate to each other.

### Tolerance Limits for Automatic Clearing

Tolerance limits define how big the difference between what you invoiced and what your customer actually pays is allowed to be. This means that if the payment difference is within the tolerance limit, it can still be posted and cleared automatically.
To learn more about tolerance limits, go to our Product Assistance for [Tolerance Limits](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/0d17fb1aeb984914a62f4fae57185f6f.html?version=latest).

### Partial Payments vs Residual Items

If the payment difference is outside the tolerance limits, you must post and clear the payment difference manually.

You can post partial payments and residual items in the *Clear Incoming Payments* app, the *Post Incoming Payments* app, and the *Reprocess Bank Statement Items* app.

* If you post a **partial payment**, both the invoice and the payment remain as open items until the outstanding payment is made.

* If you post a **residual item**, on the other hand, the invoice and the payment are cleared, and the system creates a new open item for the outstanding payment.

To learn more about partial payments and residual items, go to our Product Assistance for [Partial Payments versus Residual Items](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/279bad94d6414e05aab0cacf42eb3803.html?version=latest).

To learn more about the other options for manual clearing, go to our Product Assistance for [Payment Differences](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/a8d0f49995394451882809d7a0171f6a.html?version=latest).

### Reason Codes

You can use reason codes to document why you posted a payment difference. Reason codes can be used both for partial payments and residual items. You can also use them to write off payment differences via a separate G/L account.

To learn more about reason codes, go to our Product Assistance for [Reason Codes](https://help.sap.com/docs/SAP_S4HANA_CLOUD/918bca53037f408f91a2295d04ac16bc/1bbe9ae6af1a431aa8584f6edd919918.html?version=latest).

The following graphic sums up what you need to know about payment differences:

![](/legacyfs/online/storage/blog_attachments/2023/01/Payment-Differences-OverviewNewCut.png)

Overview of how to deal with payment differences

Thanks for reading this blog post. I hope it’s given you an insight into payment differences and how you can deal with them.

Feel free to leave any comments you may have below.

**See also:**

[Partial and Residual Payments in S/4HANA Cloud](https://blogs.sap.com/2019/07/02/partial-and-residual-payments-in-s-4hana-cloud/)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fpayment-differences-and-how-to-deal-with-them-in-sap-s-4hana-cloud%2Fba-p%2F13571515%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Int4 Suite Agents Empowers Functional Consultants To Test Integrated SAP S/4HANA Business Processes](/t5/enterprise-resource-planning-blog-posts-by-members/int4-suite-agents-empowers-functional-consultants-to-test-integrated-sap-s/ba-p/14234100)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  12 hours ago
* [Japan Bank Charges in Payment Lots](/t5/enterprise-resource-planning-blog-posts-by-sap/japan-bank-charges-in-payment-lots/ba-p/14231915)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [Digital payment add-on integration with Stripe PSP](/t5/enterprise-resource-planning-q-a/digital-payment-add-on-integration-with-stripe-psp/qaq-p/14212324)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  3 weeks ago
* [Regenerate DME where BCM is Activated in S4HANA](/t5/enterprise-resource-planning-q-a/regenerate-dme-where-bcm-is-activated-in-s4hana/qaq-p/14206146)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a month ago
* [Accounting Principles and SAP S/4HANA FI](/t5/enterprise-resource-planning-blog-posts-by-sap/accounting-principles-and-sap-s-4hana-fi/ba-p/14186371)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2025 Aug 21

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikima...