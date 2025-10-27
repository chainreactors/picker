---
title: Prevent Receipt elements generation for BOM components with specific Products
url: https://blogs.sap.com/2023/07/04/prevent-receipt-elements-generation-for-bom-components-with-specific-products/
source: SAP Blogs
date: 2023-07-05
fetch_date: 2025-10-04T11:53:20.632788
---

# Prevent Receipt elements generation for BOM components with specific Products

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Prevent Receipt elements generation for BOM compon...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67156&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Prevent Receipt elements generation for BOM components with specific Products](/t5/enterprise-resource-planning-blog-posts-by-members/prevent-receipt-elements-generation-for-bom-components-with-specific/ba-p/13551750)

![former_member227350](https://avatars.profile.sap.com/former_member_small.jpeg "former_member227350")

[former\_member227350](https://community.sap.com/t5/user/viewprofilepage/user-id/227350)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67156)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67156)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551750)

‎2023 Jul 04
9:11 PM

0
Kudos

1,727

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)

View products (1)

**Introduction :**

In some cases Especially in pharmaceutical industry customer required to insert Product samples  quantity in FG plan  but not reflect in the main Semi-finished product (Bulk Material ) because it’s already created in batches fixed /round  lot size  in other words sometime we got business requirements  about not to create receipt elements (Planned order /PR ) for Dependent requirements for some BOM components with specific products and treat it with other products normally ( generate Planned order  / PR  )

# **The issue:**

IN MTS Environment customer require prevent creation of  Receipt element( Planned order / PR) for dependent requirements for one or more BOM component with specific product and treat it with other products normally (generate Receipt element)

we will use MRP area and BOM item detail data to run the solution

# **An Example :**

-Create MRP Area For storage location

![](/legacyfs/online/storage/blog_attachments/2023/07/image_2023-07-03_192456557.png)

2-Assign MRP to the SF material master using ND as Planning Type

![](/legacyfs/online/storage/blog_attachments/2023/07/2-2.png)

3-Assign Component in two different products BOM

![](/legacyfs/online/storage/blog_attachments/2023/07/3-2.png)

4-In the BOM  of  the product that we wouldn’t  dependent requirements to be generated we will assign the MRP storage location in the component item details

![](/legacyfs/online/storage/blog_attachments/2023/07/4-1.png)

5- Maintain PIR for the two Products  and Run MRP

![](/legacyfs/online/storage/blog_attachments/2023/07/5-2.png)

![](/legacyfs/online/storage/blog_attachments/2023/07/6-1.png)

6- Check Dependent requirements of BOM component  (MD04)

![](/legacyfs/online/storage/blog_attachments/2023/07/7-1.png)

-Planed order created for the first product  dependent requirements (note i maintained round value in SF material master 1500)

![](/legacyfs/online/storage/blog_attachments/2023/07/7_1.png)

-No receipt element created for second product  dependent requirements

![](/legacyfs/online/storage/blog_attachments/2023/07/8-2.png)

7- Convert Planned order to production order and confirm it

8- after the GI of the semi-finished product to the second FG this how MD04 will look like

![](/legacyfs/online/storage/blog_attachments/2023/07/9-1.png)

# The conclusion:

By applying this solution you will be able to appear to prevent the system of creating Receipt elements for some BOM components with specific product and let the system to create it with other products normally.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fprevent-receipt-elements-generation-for-bom-components-with-specific%2Fba-p%2F13551750%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP Sustainability Footprint Management: Q3-25 Updates & Highlights](/t5/enterprise-resource-planning-blog-posts-by-sap/sap-sustainability-footprint-management-q3-25-updates-amp-highlights/ba-p/14230327)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Wednesday
* [Next Generation Just-In-Time, Supply to Customer](/t5/enterprise-resource-planning-blog-posts-by-sap/next-generation-just-in-time-supply-to-customer/ba-p/14230304)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday
* [Mass download of pdf's and emails generated in Production which have been issued to customers](/t5/enterprise-resource-planning-q-a/mass-download-of-pdf-s-and-emails-generated-in-production-which-have-been/qaq-p/14224713)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  2 weeks ago
* [Export of CDS View generates two lines for one Product](/t5/enterprise-resource-planning-q-a/export-of-cds-view-generates-two-lines-for-one-product/qaq-p/14217333)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  3 weeks ago
* [Supply Chain Management in SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/supply-chain-management-in-sap-s-4hana-cloud-public-edition-2508/ba-p/14214877)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  3 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8232_small.jpeg "arghadipkar3013")  arghadipkar3013](/t5/user/viewprofilepage/user-id/686417) | 2 |
| [![vianshu](https://avatars.profile.sap.com/7/3/id73f851dd2d6...