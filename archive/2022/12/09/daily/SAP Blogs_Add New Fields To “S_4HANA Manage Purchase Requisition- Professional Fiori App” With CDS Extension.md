---
title: Add New Fields To “S/4HANA Manage Purchase Requisition- Professional Fiori App” With CDS Extension
url: https://blogs.sap.com/2022/12/08/add-new-fields-to-s-4hana-manage-purchase-requisition-professional-fiori-app-with-cds-extension/
source: SAP Blogs
date: 2022-12-09
fetch_date: 2025-10-04T00:59:46.334536
---

# Add New Fields To “S/4HANA Manage Purchase Requisition- Professional Fiori App” With CDS Extension

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Add New Fields To "S/4HANA Manage Purchase Requisi...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67939&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Add New Fields To "S/4HANA Manage Purchase Requisition- Professional Fiori App" With CDS Extension](/t5/enterprise-resource-planning-blog-posts-by-members/add-new-fields-to-quot-s-4hana-manage-purchase-requisition-professional/ba-p/13560779)

![umtyzc](https://avatars.profile.sap.com/3/1/id31e1e5cad9d6f35605d8ae50f6a4aa31a1215955591d8fe487447e83387860a5_small.jpeg "umtyzc")

[umtyzc](https://community.sap.com/t5/user/viewprofilepage/user-id/155264)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67939)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67939)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13560779)

‎2022 Dec 08
8:52 PM

[6
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67939/tab/all-users "Click here to see who gave kudos to this post.")

7,426

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)

View products (3)

**Summary**

This topic demonstrates how you can extend the original CDS view with a view extension to provide some additional fields.

**Problem:**

Our customer asked us to add some fields that are in the "EBAN" table but not in the Manage Purchase Requisition Professional Fiori application(F2229).

**Solution:**

I created this example to show how those who need to add fields to the S/4HANA Manage Purchase Requisition Professional Fiori App can do so via the CDS extension. We used it in our S/4 Hana(On-Premise) Greenfield Implementation project and we met our customer's need.

**What will you learn?**

In this example I will create “CDS Extension” for Purchase Order Professional App to add two fields in the EBAN table.

**You’ll learn**

* How to create custom CDS extension for Purchase Requisition Item Extensibility View-***E\_Purchaserequisitionitem*.**

* How to create custom CDS extension for standart CDS view ***C\_PurchaseReqnHeader***

* How to use E\_Purchaserequisitionitem in the C\_PurchaseReqnHeader .

**1**- First, we open our application package and **C\_PurchaseReqnHeader CDS view** on Eclipse.

![](/legacyfs/online/storage/blog_attachments/2022/11/pr1.png)

**2-** Go To *C\_PurchaseReqnHeader->T\_PurchaseReqn ->I\_PurchaseReqn->I\_PurchaseReqn->I\_Purchaserequisitionitem*

In the I\_Purchaserequisitionitem CDS View you can see standart extension view E\_Purchaserequisitionitem.

![](/legacyfs/online/storage/blog_attachments/2022/12/pr3.png)

**3-** This view is using the "EBAN" table. We will add the fields we want to get from the EBAN table by making a standard view extension to this view.

Right Click to **E\_Purchaserequisitionitem**.and **choose New Data Definition.**

![](/legacyfs/online/storage/blog_attachments/2022/12/Screenshot-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/pr7.png)

**4-** I add two new fields to this extension view then activate it.

***Created by- ERNAM***

***Request Date- BADAT***

![](/legacyfs/online/storage/blog_attachments/2022/12/pr9.png)

**5**- Now we can use these fields in the main *C\_PurchaseReqnHeader view.*

I create a extend view for *C\_PurchaseReqnHeader as in point **3**  and activate it.*

After all of these, you can see your new fields in "Manage Purchase Requisition Professional Fiori Application(F2229)."

![](/legacyfs/online/storage/blog_attachments/2022/12/pr10.png)

Please submit questions in the respective [Q&A area](https://developers.sap.com/tutorials/community-qa.html) in SAP Community.

**References**

<https://help.sap.com/docs/BTP/f859579898c7494dbe2449bb7f278dcc/cb7a12b0faf44b41b9fc62e57fec55c5.html>

* [abap](/t5/tag/abap/tg-p/board-id/erp-blog-members)
* [CDS](/t5/tag/CDS/tg-p/board-id/erp-blog-members)
* [Extension](/t5/tag/Extension/tg-p/board-id/erp-blog-members)
* [S4HANA](/t5/tag/S4HANA/tg-p/board-id/erp-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fadd-new-fields-to-quot-s-4hana-manage-purchase-requisition-professional%2Fba-p%2F13560779%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [MD01N Behavior: Issuing Storage Location Not Set in Stock Transport Requisitions](/t5/enterprise-resource-planning-q-a/md01n-behavior-issuing-storage-location-not-set-in-stock-transport/qaq-p/14234045)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  9 hours ago
* [Why asset doest not have material code in SAP ERP?](/t5/enterprise-resource-planning-q-a/why-asset-doest-not-have-material-code-in-sap-erp/qaq-p/14231693)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  Tuesday
* [How do I add international freight and insurance costs to a material's price in SAP?](/t5/enterprise-resource-planning-q-a/how-do-i-add-international-freight-and-insurance-costs-to-a-material-s/qaq-p/14227754)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [Account Assignment Q (Project Stock) - possible for Services and for Orders without Material Number?](/t5/enterprise-resource-planning-q-a/account-assignment-q-project-stock-possible-for-services-and-for-orders/qaq-p/14227735)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago
* [How to attach a file in a purchase requisition in sap public cloud](/t5/enterprise-resource-planning-q-a/how-to-attach-a-file-in-a-purchase-requisition-in-sap-public-cloud/qaq-p/14226856)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/vi...