---
title: What’s New in Subscription Order Management 2022 FPS00
url: https://blogs.sap.com/2022/11/04/whats-new-in-subscription-order-management-2022-fps00/
source: SAP Blogs
date: 2022-11-05
fetch_date: 2025-10-03T21:44:56.818253
---

# What’s New in Subscription Order Management 2022 FPS00

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by SAP](/t5/financial-management-blog-posts-by-sap/bg-p/financial-management-blog-sap)
* What’s New in Subscription Order Management 2022 F...

Financial Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-sap/article-id/7944&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [What’s New in Subscription Order Management 2022 FPS00](/t5/financial-management-blog-posts-by-sap/what-s-new-in-subscription-order-management-2022-fps00/ba-p/13559855)

![AbhijeetDhar](https://avatars.profile.sap.com/c/4/idc47f081da8ceb69e0f3f6f41fe2e2120b02f1416a279e1db7a2904fd2dd71550_small.jpeg "AbhijeetDhar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[AbhijeetDhar](https://community.sap.com/t5/user/viewprofilepage/user-id/643514)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-sap&message.id=7944)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-sap/article-id/7944)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559855)

‎2022 Nov 04
7:11 PM

[5
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-sap/message-id/7944/tab/all-users "Click here to see who gave kudos to this post.")

3,138

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Billing and Revenue Innovation Management, subscription order management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Billing%2520and%2520Revenue%2520Innovation%2520Management%252C%2520subscription%2520order%2520management/pd-p/0f388a77-bf51-493a-8c31-13eb062332e7)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Billing and Revenue Innovation Management, subscription order management

  Software Product Function](/t5/c-khhcw49343/SAP%2BBilling%2Band%2BRevenue%2BInnovation%2BManagement%25252C%2Bsubscription%2Border%2Bmanagement/pd-p/0f388a77-bf51-493a-8c31-13eb062332e7)

View products (2)

New Release

PUBLIC

![](/legacyfs/online/storage/blog_attachments/2022/11/Header-Picture1.png)

**October 2022**

We’re delighted to announce the general availability of Subscription Order Management 2022 FPS00. With this release, we are introducing new features and apps that will enhance your user experience, integration capabilities, and system performance. This blog will highlight our new Fiori application **Subscription Contract Lifecycle Management**, Integration capabilities with Credit Management for credit check, and various other functional enhancements, as part of the [SAP Billing and Revenue Innovation Management (BRIM) suite](https://www.sap.com/products/billing-revenue-innovation-management.html).

---

# Manage Subscription Contract Lifecycle

Did you know that Subscription Order Management now has a new Fiori app to provide you with an end-to-end holistic overview of a specific contract and all the items within that contract?

Yes, you got it right! With this release, we introduce **Manage Subscription Contract Lifecycle**, which is loaded with tons of new features and provides the flexibility to navigate easily across contract objects. The app is designed to enable your sales representatives and back-office agents to negotiate more effectively with your end customers and respond to customer requests more efficiently.

The app provides you with a complete overview of the subscription contract and related contract phases. The 'Contract State' section provides you with a summary of your contract, including subitems, contract time slices, and other information. Whereas the ‘Contract State Sequence’ section provides you with a graphical representation of the evolution of the subscription contract, that is, from the initial state to the current active contract state and provides a view of the future planned phases in the contract.

You can also navigate directly to the **Subscription Contract Item Details** app from the individual line items in the ‘Contract States’ and ‘Contract State Sequence’ sections to view the item details, such as pricing, partners, dates, discounts and charges, technical resources, and equipment. You get the flexibility to trigger a change process and view the fulfillment status directly from the app.

![](/legacyfs/online/storage/blog_attachments/2022/11/Manage-Subscription-Contract-Lifecycle.png)

Contract view in the "Manage Subscription Contract Lifecycle" App

Listed below are some of the additional key features of this app:

* View a list of subscription contracts categorized by the current state of the items, that is, Current Items, Planned Items, and Expired Items

* Navigate easily to the **Monitor Master Data Distribution** app

* View the Fulfilment Status in the Distribution Monitor

* View the estimated contract value

You can find more details about this new feature from the [Manage Subscription Contract Lifecycle](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/95ad0cb1c441447888d695da7f3fd3d9/196a0ce5dda240f5a0712f857d59a702.html?version=2022.000) on the SAP Help Portal.

---

# Enabling Credit Check for Subscription Items in Subscription Orders and Solution Quotations

Ensuring the creditworthiness of your customer is always a key consideration before you take an order in the system. Understanding this market demand, we have now enabled the integration with the Credit Management functionality that is available in S/4HANA. This new feature enables subscription items in a solution quotation or subscription order to run automatic credit management functionalities, such as credit checks, credit exposure, and Documented Credit Decisions.

Here are a couple of key features that our customers can leverage using this integration:

* Execute automatic credit check in solution quotation/subscription order for subscription items to ensure the creditworthiness of your customer

* A failed credit check document is blocked for further processing and a Documented Credit Decision (DCD) is created

* Use Credit Management capabilities to manually release or recheck the DCD

* Transfer credit exposure from an order/quotation and to the contract once it is activated, thus reducing the exposure during billing/invoicing

![](/legacyfs/online/storage/blog_attachments/2022/11/Enabling-Credit-Check-.png)

Illustration of Credit Check Process

For more information about the enabling credit check functionality in Subscription Order Management, refer to [Enabling Credit Check on Subscription Items](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/95ad0cb1c441447888d695da7f3fd3d9/ad8911be57f04357bd771f573663bb4e.html?version=2022.000) on the SAP Help Portal.

---

# Rejecting Items in a Subscription Contracts

Your customer requests a change on an individual, future-dated (planned) subscription contract that is created from an accepted solution quotation. This enables users to trigger such a rejection directly from an individual subscription contract, either by clicking the reject button or by executing the respective change proc...