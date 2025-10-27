---
title: Asset transfer between the company codes (Intercompany Asset Transfer)
url: https://blogs.sap.com/2022/11/16/asset-transfer-between-the-company-codes-intercompany-asset-transfer/
source: SAP Blogs
date: 2022-11-17
fetch_date: 2025-10-03T23:00:17.553006
---

# Asset transfer between the company codes (Intercompany Asset Transfer)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Asset transfer between the company codes (Intercom...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68486&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Asset transfer between the company codes (Intercompany Asset Transfer)](/t5/enterprise-resource-planning-blog-posts-by-members/asset-transfer-between-the-company-codes-intercompany-asset-transfer/ba-p/13569713)

![thaider110](https://avatars.profile.sap.com/e/d/idedc54c4a46b387261185083b85e69968218c8f6cd8ee50f2266ad5c72a5c7f88_small.jpeg "thaider110")

[thaider110](https://community.sap.com/t5/user/viewprofilepage/user-id/43116)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68486)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68486)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13569713)

‎2022 Nov 16
3:03 PM

[7
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68486/tab/all-users "Click here to see who gave kudos to this post.")

49,943

* SAP Managed Tags
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [FIN Asset Accounting](https://community.sap.com/t5/c-khhcw49343/FIN%2520Asset%2520Accounting/pd-p/253758978139952938680563247610563)

* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [FIN Asset Accounting

  Software Product Function](/t5/c-khhcw49343/FIN%2BAsset%2BAccounting/pd-p/253758978139952938680563247610563)

View products (2)

***Hello everyone!!***

***This is my first blog I am contributing to the SAP world. Since I started my SAP career, I believe SAP community has given everyone vast space to learn and explore new things in the SAP world. My sincere thanks to those who contribute and share their experience and knowledge to make others' life easy and help them to learn and grow in their jobs.***

***So now I decided to write something where I got some good exposure and understanding. As this is my first blog, I request all the audience to give me their valuable feedback so the next time I can write a blog considering the feedback I will receive on this blog***

***In this blog, I tried to give an overview of Intercompany Asset transfer, but my main purpose is to explain the cross-system depreciation area and its use. But, to understand that first we need to understand the intracompany asset transfer process.***

***Intercompany asset*** ***transfers:*** *Intercompany transfer means the transfer of assets from the books of one company code to another company code.* For the companies involved in the intercompany transfer, an intercompany transfer represents a retirement for the sender company and an acquisition for the receiver company. It is typically representing a transfer that balances to zero in the asset history sheet for the sender company and shows asset acquisition in the asset history sheet of the receiver company.

An Intercompany asset transfer may be required for one of the following reasons:

* The organizational structure of the corporate group has changed, requiring reassigning the asset to another company code

* The physical location of the asset has changed, making it essential to assign the asset to a new company.

If you want to transfer an asset from one company to another, it is not possible to change the organizational assignment of the asset by changing the master records. To transfer an asset, we need to have an asset master record created in receiving the company code.

As an asset, intercompany transfer represents the retirement of one asset in sending the company code and the acquisition of another asset in receiving the company code. Hence, different sets of transaction types are required for acquisitions and retirements that will be used during the transfer process.

SAP has provided all relevant transaction types, but we can configure custom transaction types based on the requirement. Best practice, if you want to configure or change transaction types, never modify the standard transaction types instead, copy the standard transaction type that most closely meets your needs and create a new transaction type in the custom name range, starting with Z or Y.

Now we have got a basic understanding of Intercompany asset transfer now let’s see, what are the possible ways to transfer assets from one company code to another.

Basically, there are 2 ways to do the intercompany asset transfer.

**Automatic Intercompany Transfer (ABT1N):** With the use of this transaction code, asset get retired in the sender company code and acquisition get posted in the receiver company code in one step. The prerequisite asset master record must exist in the receiver company code to post the transaction. However, in the transaction code, ABT1N SAP has given the option to create an asset master record in receiving the company code during the posting intercompany transaction itself.

**Manual Intercompany Asset Transfer:** In this process, 2 steps need to be performed, the retirement of an asset in the sender company code and acquiring an asset in receiving company code. SAP has provided different transaction types which identify the transactions performed. Transaction types relevant to intercompany transfer can be used while posting the retirement of an asset in the sender company code and acquisition in the receiver company code.

**Step 1:   Retirement of an Asset in the sender company code:** The asset needs to be retired in the sender company code by using standard transaction code ABAON, while posting the retirement of an asset, we need to ensure the trading partner field must be updated with receiver company code information. By populating the trading partner in the retirement transaction, it will call the relevant transaction type and the trading partner will be updated in the retirement posted document.

**Step 2:   Acquisition of an Asset in the receiving company code**: The asset needs to be acquired in receiving company code using standard transaction code ABZP, while posting an acquisition using the ABZP transaction code we need to ensure the trading partner field must be populated with sender company code information. By populating trading partner in an acquisition transaction, it will allow using transaction type of acquisition from affiliated company code. ABZP is specifically defined for acquisition from affiliated company code.

There are 2 ways to transfer asset values from the sender company code to the receiver company code, depending on the reason for the transfer and the association between the company codes, acquisition of the transferred asset can be posted either gross (with its historical APC and value adjustments which include accumulated depreciation, if any) or net (with its net book value, no accumulated depreciation). Therefore there is a special indicator defined in the transaction types. This indicator indicates ...