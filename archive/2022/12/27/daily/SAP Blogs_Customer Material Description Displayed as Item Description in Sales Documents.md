---
title: Customer Material Description Displayed as Item Description in Sales Documents
url: https://blogs.sap.com/2022/12/26/customer-material-description-displayed-as-item-description-in-sales-documents/
source: SAP Blogs
date: 2022-12-27
fetch_date: 2025-10-04T02:32:57.306082
---

# Customer Material Description Displayed as Item Description in Sales Documents

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Customer Material Description Displayed as Item De...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51641&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customer Material Description Displayed as Item Description in Sales Documents](/t5/enterprise-resource-planning-blog-posts-by-sap/customer-material-description-displayed-as-item-description-in-sales/ba-p/13558546)

![StevenLiu21](https://avatars.profile.sap.com/4/e/id4e29fe8f42550ff727f5fd227c0d1cf5ef9d9e5f69a68b0a8e56f2fe7c62b4b4_small.jpeg "StevenLiu21")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[StevenLiu21](https://community.sap.com/t5/user/viewprofilepage/user-id/12914)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51641)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51641)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13558546)

‎2022 Dec 26
10:02 AM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51641/tab/all-users "Click here to see who gave kudos to this post.")

2,640

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sales](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

* [SAP S/4HANA Cloud Public Edition Sales

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

View products (1)

In SAP S/4HANA and SAP S/4HANA Cloud, when you create a sales document, an item description may be derived from customer material master data and filled with customer material description.

For example, as the screenshots below show, the customer material description (**CUS\_US\_TG11**) overrides the material description in product master data (**Trad. Good 11, PD, Reg. Trading**).

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture1-50.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture2-28.png)

This is because when both customer material description and product description exist for a product, the system preferentially uses the customer material description as item description in sales documents.

However, if you don't want the customer material description to override the product description from product master data, please leave the customer material description empty in the *Manage Customer Materials* app.

You can complete the following steps to remove customer material description:

1. Go to Fiori app *Manage Customer Materials*.

2. Select the corresponding entry considering customer, customer material, product, sales organization, and distribution channel.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture3-24.png)

3. Click *Edit* and clear the field **Customer Material Description**.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture5-15.png)

4. Save the record.

Now when you create a new sales document, the item description is picked from the product master data.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture4-20.png)

You can also find a knowledge base article (KBA) about this:

[3228018 - Customer Material Description displayed as Item Description in Sales Document - SAP ONE Su...](https://launchpad.support.sap.com/#/notes/0003228018)

**For more information on SAP S/4HANA Cloud, check out the following links:**

Follow SAP S/4HANA Cloud for Sales environment Topic page: <https://community.sap.com/topics/s4hana-cloud-sales>

Post and answer questions: [All Questions in SAP S/4HANA Cloud for Sales | SAP Community](https://answers.sap.com/tags/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

Read other posts on the topic: [SAP S/4HANA Cloud for Sales | SAP | SAP Blogs](https://blogs.sap.com/tags/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0/)

Please feel free to share feedback or thoughts in a comment and follow my profile for more content.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fcustomer-material-description-displayed-as-item-description-in-sales%2Fba-p%2F13558546%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Urgent Purchasing with Purchase Requisition Workflow in SAP S/4HANA Public Cloud-1](/t5/enterprise-resource-planning-blog-posts-by-members/urgent-purchasing-with-purchase-requisition-workflow-in-sap-s-4hana-public/ba-p/14234546)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  14m ago
* [The description of the cost center are not displayed.](/t5/enterprise-resource-planning-q-a/the-description-of-the-cost-center-are-not-displayed/qaq-p/14232153)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Wednesday
* [2508 Maintenance Act/Plan app - (WO) descriptions](/t5/enterprise-resource-planning-q-a/2508-maintenance-act-plan-app-wo-descriptions/qaq-p/14231680)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Tuesday
* [ENGINEERING CHANGE MANAGEMENT(ECM)](/t5/enterprise-resource-planning-blog-posts-by-members/engineering-change-management-ecm/ba-p/14163252)
  in [Enterprise Resource Planning Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)  Monday
* [Account Assignment Q (Project Stock) - possible for Services and for Orders without Material Number?](/t5/enterprise-resource-planning-q-a/account-assignment-q-project-stock-possible-for-services-and-for-orders/qaq-p/14227735)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993bbd8c3abd793e64af5050b65e9a4b850c04ce6bbb7_small.jpeg "Andrew_Ford")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") Andrew\_Ford](/t5/user/viewprofilepage/user-id/98013) | 8 |
| [![DianaMala](https://avatars.profile.sap.com/6/...