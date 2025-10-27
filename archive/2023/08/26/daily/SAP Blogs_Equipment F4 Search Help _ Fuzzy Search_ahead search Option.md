---
title: Equipment F4 Search Help / Fuzzy Search/ahead search Option
url: https://blogs.sap.com/2023/08/25/equipment-f4-search-help-fuzzy-search-ahead-search-option/
source: SAP Blogs
date: 2023-08-26
fetch_date: 2025-10-04T12:00:10.849896
---

# Equipment F4 Search Help / Fuzzy Search/ahead search Option

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Equipment F4 Search Help / Fuzzy Search/ahead sear...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/69210&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Equipment F4 Search Help / Fuzzy Search/ahead search Option](/t5/enterprise-resource-planning-blog-posts-by-members/equipment-f4-search-help-fuzzy-search-ahead-search-option/ba-p/13581441)

![vinoth_kumar47](https://avatars.profile.sap.com/9/2/id926cd46bb45b84b25f1fff6d94ecedab9c195706610c9f47fc6fcbf2a01a4bb2_small.jpeg "vinoth_kumar47")

[vinoth\_kumar47](https://community.sap.com/t5/user/viewprofilepage/user-id/262706)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=69210)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/69210)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13581441)

‎2023 Aug 25
9:05 PM

[3
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/69210/tab/all-users "Click here to see who gave kudos to this post.")

4,366

* SAP Managed Tags
* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)](https://community.sap.com/t5/c-khhcw49343/PLM%2520Enterprise%2520Asset%2520Management%2520%28EAM%29%252FPlant%2520Maintenance%2520%28PM%29/pd-p/430019464658497915145476514330950)

* [PLM Enterprise Asset Management (EAM)/Plant Maintenance (PM)

  Software Product Function](/t5/c-khhcw49343/PLM%2BEnterprise%2BAsset%2BManagement%2B%252528EAM%252529%25252FPlant%2BMaintenance%2B%252528PM%252529/pd-p/430019464658497915145476514330950)

View products (1)

Dear Friends,

**In this blog we can see how to enable the F4 search help/ fuzzy search/ ahead search option for the Equipment field.**

If we know only Equipment number then will directly pass the Equipment number in any transaction like IW28, IH08, IW38,ect to get the Equipment Details.

Some times we only know the Equipment Description, at that time we pass the Equipment Description in the Equipment field. It should display the Equipment number with Equipment Description.

In our case we can take **IH08** transaction, If we know Equipment number we can directly insert into the Equipment field.

![](/legacyfs/online/storage/blog_attachments/2023/08/Equipment-wo-F4-1.png)

Below Example we can see the material stock **MMBE** transaction. If we type Material description in the material fields it's showing the material number along with the material description in the dropdown. Here I have entered the description

![](/legacyfs/online/storage/blog_attachments/2023/08/Material.png)

Example of MMBE transaction

If we know only the Equipment description, when we typing the description in the Equipment field it should be display the Equipment number with Equipment Description. Like the above example of the **MMBE**transaction.

![](/legacyfs/online/storage/blog_attachments/2023/08/Equipment-Desc-2.png)

# Steps

Follow the below steps to enable the F4 search help/Fuzzy search/ahead search

**Step 1:-**

Open the "SAP logon" , click icon menu and click the "Options"

![](/legacyfs/online/storage/blog_attachments/2023/08/Icon-2.png)

Option Menu

**Step 2:-**

Expend the folder "Interaction Design", Click "Visualization 2",  choose "Show Enhanced Search automatically"

![](/legacyfs/online/storage/blog_attachments/2023/08/Icon-3.png)

Click "Apply" and "Ok"

**Step 3:-**

Check if the flag "'**Use proposal search for input fields"** is set in transaction **SDSH\_CONFIG**

![](/legacyfs/online/storage/blog_attachments/2023/08/Se11-1-2.png)

**Step 4:-**

Open the search help in **SE11** tcode, check the following 2 options in the tab "Definition" > "Enhanced Options"

* **Proposal Search for Input Fields**

* **Multi-Column Full Text Search (database-dependent) / Full Text Fuzzy Search (database-dependent) {Depends upon the version the description will change}**

For Equipment the Search Value is "**EQUIR**"

For Equipment Description Value is "**EQUIT**"

![](/legacyfs/online/storage/blog_attachments/2023/08/se11.png)

SE11

![](/legacyfs/online/storage/blog_attachments/2023/08/Se11-1.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/EQui.png)

In our case the Both options are disabled for the **EQUIR** and **EQUIT** , so we are not getting the Equipment details when passing the Equipment description in the Equipment filed in the **IH08** transaction.

So, we need to enable this Both options. With the help of Development Team we need to enable this check box.

Once it's enabled you will get the Equipment number with description when passing the description in the Equipment field in any transaction.

Thank you,

***VINOTHKUMAR POWNRAJ***

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fequipment-f4-search-help-fuzzy-search-ahead-search-option%2Fba-p%2F13581441%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  yesterday
* [Mass creation of RFQ in S/4 hana system](/t5/enterprise-resource-planning-q-a/mass-creation-of-rfq-in-s-4-hana-system/qaq-p/14234508)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Thursday
* [Requirement to Disable/Hide ‘Post Goods Issue’ in ME2ON output screen.](/t5/enterprise-resource-planning-q-a/requirement-to-disable-hide-post-goods-issue-in-me2on-output-screen/qaq-p/14233282)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Thursday
* [Issue with Cost Center linked to incorrect Profit Center in SAP S/4HANA Public Cloud (3SL, CBC)](/t5/enterprise-resource-planning-q-a/issue-with-cost-center-linked-to-incorrect-profit-center-in-sap-s-4hana/qaq-p/14232720)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKra...