---
title: FM’s for Taxes
url: https://blogs.sap.com/2023/02/14/fms-for-taxes/
source: SAP Blogs
date: 2023-02-15
fetch_date: 2025-10-04T06:37:12.575283
---

# FM’s for Taxes

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* FM's for Taxes

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/66896&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [FM's for Taxes](/t5/enterprise-resource-planning-blog-posts-by-members/fm-s-for-taxes/ba-p/13548419)

![kasralikarpratik](https://avatars.profile.sap.com/5/b/id5bbff3f9d10f048202c0c0b73d56590b785951fa8fa4ac4a9c73a791b54d0cca_small.jpeg "kasralikarpratik")

[kasralikarpratik](https://community.sap.com/t5/user/viewprofilepage/user-id/541785)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=66896)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/66896)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548419)

‎2023 Feb 14
10:36 PM

0
Kudos

2,448

* SAP Managed Tags
* [ABAP Connectivity](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Connectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [ABAP Connectivity

  Programming Tool](/t5/c-khhcw49343/ABAP%2BConnectivity/pd-p/266264953119842772207986043063520)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)

View products (4)

There are many FM's to get tax details from external system. Few of them are below and what are details to pass to get exact tax details

* CALCULATE\_TAX\_FROM\_GROSSAMOUNT

Parameters to pass:

I\_BUKRS - Company Code
I\_MWSKZ - Tax Code
I\_TXJCD - Tax Jurisdiction Code
I\_WAERS - Currency
I\_WRBTR - Amount

* CALCULATE\_TAX\_FROM\_NET\_AMOUNT

Parameters to pass:

I\_BUKRS - Company Code
I\_MWSKZ - Tax Code
I\_TXJCD - Tax Jurisdiction Code
I\_WAERS - Currency
I\_WRBTR - Amount

* CALCULATE\_TAXES\_NET

Parameters to pass:

TAX\_ITEM\_IN-BUKRS - Company Code
TAX\_ITEM\_IN-MWSKZ - Tax Code
TAX\_ITEM\_IN-TXJCD - Tax Jurisdiction Code
TAX\_ITEM\_IN-WAERS - Currency
TAX\_ITEM\_IN-WRBTR - Amount

* DETERMINE\_TXJCD\_EXTERNALLY

This FM will be used to show in dialog mode as F4 help

Parameters to pass:

COUNTRY - Country
REGION - State
ZIPCODE - Postal Code

* RFC\_DETERMINE\_JURISDICTION

This FM needs to be called with RFC Destination. Most of the time you will find destinations in TTXD table

Parameters to pass:

LOCATION\_DATA-COUNTRY - Country
LOCATION\_DATA-REGION - State
LOCATION\_DATA-ZIPCODE - Postal Code

I will keep adding more FM's as soon as i come across but i think above 4 FM's mostly solve most of the requirements. Please share if you know any other FM's with parameters to pass.

This blog is not to conflict any other blogs, there are many but i just thought to have all these at one place because requirements are different at different places.

Thank you.

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Ffm-s-for-taxes%2Fba-p%2F13548419%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Tax statement item missing for tax code V0 in intercompany billing VF02](/t5/enterprise-resource-planning-q-a/tax-statement-item-missing-for-tax-code-v0-in-intercompany-billing-vf02/qaq-p/14234014)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  15 hours ago
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition 2508](/t5/enterprise-resource-planning-blog-posts-by-sap/grc-trade-and-tax-with-sap-s-4hana-cloud-public-edition-2508/ba-p/14229204)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  yesterday
* [Streamlining North American Tax Compliance with SAP Document and Reporting Compliance](/t5/enterprise-resource-planning-blog-posts-by-sap/streamlining-north-american-tax-compliance-with-sap-document-and-reporting/ba-p/14232011)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [SII tip for Spain #5B: SII Adjustments for Canary Islands October 2025 - Enabling AIEM](/t5/enterprise-resource-planning-blog-posts-by-sap/sii-tip-for-spain-5b-sii-adjustments-for-canary-islands-october-2025/ba-p/14231940)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Tuesday
* [SII tip for Spain #6: Invoices with zero amounts in SII due to full discounts](/t5/enterprise-resource-planning-blog-posts-by-sap/sii-tip-for-spain-6-invoices-with-zero-amounts-in-sii-due-to-full-discounts/ba-p/14228706)
  in [Enterprise Resource Planning Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)  Monday

Top kudoed authors

| User | Count |
| --- | --- |
| [![MichalKrawczyk](https://avatars.profile.sap.com/6/7/id677f624df4f67fa55aef9b803484fd38cfa389573f663b9623d9dc410597c931_small.jpeg "MichalKrawczyk")  MichalKrawczyk](/t5/user/viewprofilepage/user-id/45785) | 11 |
| [![Amin_Omidy](https://avatars.profile.sap.com/3/e/id3ec1fabb5feddc26ec180cef8c60f7c62692cc423031b6be3bab024c75e2c7d3_small.jpeg "Amin_Omidy")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") Amin\_Omidy](/t5/user/viewprofilepage/user-id/40654) | 3 |
| [![AhmetZ](https://avatars.profile.sap.com/9/b/id9bd18482b8f2b410b8d0206e72935dc3ca0fb940d648a21e9d1a809de3dd235c_small.jpeg "AhmetZ")  AhmetZ](/t5/user/viewprofilepage/user-id/1882423) | 2 |
| [![arghadipkar3013](https://avatars.profile.sap.com/5/1/id51c365bfbf414980aeb2ea0d09a62924387b63918439f3d24edf49314d3f8232_small.jpeg "arghadipkar3013")  arghadipkar3013](/t5/user/viewprofilepage/user-id/686417) | 2 |
| [![vianshu](https://avatars.profile.sap.com/7/3/id73f851dd2d601f9bd347d78ecfa46602245b7e89d831c26845276966f760a654_small.jpeg "vianshu")  vianshu](/t5/user/viewprofilepage/user-id/19840) | 2 |
| [![aamelin1](https://avatars.profile.sap.com/8/e/id8eacda0d2305d74a12c601ec075433bbe922d1383cf670a775c5368c0ec2b14e_small.jpeg "aamelin1")  aamelin1](/t5/user/viewprofilepage/user-id/157733) | 1 |
| [![Marssel700](https://avatars.profile.sap.com/7/d/id7d495a1938a224ad342ea99fd1c5eaf9f5c2c696859f31cee676461d418793d1_small.jpeg "Marssel700")  ![SAP Champion](/html/@B3DACAC616...