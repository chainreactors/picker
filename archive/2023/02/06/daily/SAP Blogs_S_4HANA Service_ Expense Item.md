---
title: S/4HANA Service: Expense Item
url: https://blogs.sap.com/2023/02/05/s-4hana-service-expense-item/
source: SAP Blogs
date: 2023-02-06
fetch_date: 2025-10-04T05:47:22.943807
---

# S/4HANA Service: Expense Item

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* S/4HANA Service: Expense Item

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68022&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4HANA Service: Expense Item](/t5/enterprise-resource-planning-blog-posts-by-members/s-4hana-service-expense-item/ba-p/13562489)

![zenithltd1](https://avatars.profile.sap.com/5/c/id5c8d06609ee480ce553ee9d69211be59058b2e94f86c76de3aba7ba3bb2e627c_small.jpeg "zenithltd1")

[zenithltd1](https://community.sap.com/t5/user/viewprofilepage/user-id/591353)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68022)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68022)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13562489)

‎2023 Feb 05
3:19 PM

0
Kudos

3,200

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Service](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Service/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [C4C Service](https://community.sap.com/t5/c-khhcw49343/C4C%2520Service/pd-p/569449780209093647095570245113309)
* [CRM Service](https://community.sap.com/t5/c-khhcw49343/CRM%2520Service/pd-p/336839465795980684603250734763165)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [CRM Service

  Software Product Function](/t5/c-khhcw49343/CRM%2BService/pd-p/336839465795980684603250734763165)
* [C4C Service

  Software Product Function](/t5/c-khhcw49343/C4C%2BService/pd-p/569449780209093647095570245113309)
* [SAP S/4HANA Cloud Public Edition Service

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BService/pd-p/378e2958-7587-4f1b-9653-ed06c8fcc107)

View products (4)

In S/4HANA Service Service Order, there are many types of postings possible

* Material

* Labor

* Expense Item

This blog is about how expense items are created and posted in a Service Order. Typically expense items are unplanned - travel expense, flight, car rental, etc. In various industries they capture different expenses. In Automotive third party subcontractor costs are expensed and is referred to as "Sublet".

![](/legacyfs/online/storage/blog_attachments/2023/02/MATERIAL-1.png)

                                  SERV material set up

In S/4HANA Service as material and labor, expense item is a set up material with material type SERV. It has to be set up first before it can be used in a Service Order.

**Entry in Service Order**

Expense item is entered in the items section.

![](/legacyfs/online/storage/blog_attachments/2023/02/Service-Order-2-1.png)

Service Order

**Pricing**

When you create the Service Order, manual condition is used to enter the value of the expense item if the value is dynamic in nature. If you are creating static you can use VK11 to derive the pricing.

Click the pencil, pricing totals and Add to enter pricing. In standard system PMP0 is set up as a manual price condition. Enter value of your expense item.

![](/legacyfs/online/storage/blog_attachments/2023/02/pricingpng-2.png)

Manual Pricing of Expense item

Save the Service Order and release. On release, system will create an internal order. This is old "OP 2020". In this release Internal Order is the cost collector. In newer Cloud and C4 releases, Service Order itself is the cost object.

**Service Confirmation**

The next step is create a follow up Service Confirmation from Service Order.

Here the expense item is copied into confirmation.

![](/legacyfs/online/storage/blog_attachments/2023/02/Service-confirmation-2.png)

Service Confirmation view of Expense Item

On completion of Service Confirmation expenses will be posted in the internal order.

I**nternal Order posting of Expense Item**

![](/legacyfs/online/storage/blog_attachments/2023/02/internal-order-2.png)

Internal Order posting

**Billing**

There is no difference with EBDR or billing process. Billing is not discussed here.

**Configuration CE/GL account**

Here expense item is assigned to Cost Element (GL account)

![](/legacyfs/online/storage/blog_attachments/2023/02/CE-config-2.png)

Expense Item to Cost Element

**GL Account/CE**

The CE category should be 1,

![](/legacyfs/online/storage/blog_attachments/2023/02/GL-CE-categorypng-2.png)

CE category

* [Expense Item](/t5/tag/Expense%20Item/tg-p/board-id/erp-blog-members)
* [s4crm](/t5/tag/s4crm/tg-p/board-id/erp-blog-members)
* [S4HANA Customer Management](/t5/tag/S4HANA%20Customer%20Management/tg-p/board-id/erp-blog-members)
* [SAP S4HANA Service](/t5/tag/SAP%20S4HANA%20Service/tg-p/board-id/erp-blog-members)
* [Sublet](/t5/tag/Sublet/tg-p/board-id/erp-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fs-4hana-service-expense-item%2Fba-p%2F13562489%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [My Learning Journal on BTP (5) - Build A Small Finance Agent: CAP + Generative AI Hub + LangChain](/t5/enterprise-resource-planning-blog-posts-by-sap/my-learning-journal-on-btp-5-build-a-small-finance-agent-cap-generative-ai/ba-p/14222295)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  2 weeks ago
* [Finance Part1 - Bulgaria EUR Transition for S/4HANA Cloud Public Cloud Live Customers](/t5/enterprise-resource-planning-blog-posts-by-sap/finance-part1-bulgaria-eur-transition-for-s-4hana-cloud-public-cloud-live/ba-p/14206962)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  a month ago
* [Service Entry Sheet Accruals - Posting and Configurations for SAP S/4HANA 2023](/t5/enterprise-resource-planning-blog-posts-by-members/service-entry-sheet-accruals-posting-and-configurations-for-sap-s-4hana/ba-p/14189510)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  2025 Sep 02
* [Public Sector highlights of the SAP Cloud ERP 2508 release](/t5/enterprise-resource-planning-blog-posts-by-sap/public-sector-highlights-of-the-sap-cloud-erp-2508-release/ba-p/14191660)
  in [Enterprise Resource Planning ...