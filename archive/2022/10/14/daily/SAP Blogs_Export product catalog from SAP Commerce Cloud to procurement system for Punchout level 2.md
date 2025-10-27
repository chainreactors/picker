---
title: Export product catalog from SAP Commerce Cloud to procurement system for Punchout level 2
url: https://blogs.sap.com/2022/10/13/export-product-catalog-from-sap-commerce-cloud-to-procurement-system-for-punchout-level-2/
source: SAP Blogs
date: 2022-10-14
fetch_date: 2025-10-03T19:49:46.506574
---

# Export product catalog from SAP Commerce Cloud to procurement system for Punchout level 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by SAP](/t5/spend-management-blog-posts-by-sap/bg-p/spend-management-blog-sap)
* Export product catalog from SAP Commerce Cloud to ...

Spend Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-sap/article-id/1583&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Export product catalog from SAP Commerce Cloud to procurement system for Punchout level 2](/t5/spend-management-blog-posts-by-sap/export-product-catalog-from-sap-commerce-cloud-to-procurement-system-for/ba-p/13526924)

![scar](https://avatars.profile.sap.com/c/c/idcc24d0e62c0ed5d2a6addfb04e301cd1c4dd1b23f8678aa7911a4bad6ff509a3_small.jpeg "scar")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[scar](https://community.sap.com/t5/user/viewprofilepage/user-id/477568)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-sap&message.id=1583)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-sap/article-id/1583)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13526924)

‎2022 Oct 13
10:09 PM

[5
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-sap/message-id/1583/tab/all-users "Click here to see who gave kudos to this post.")

2,732

* SAP Managed Tags
* [SAP Ariba Catalog](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Catalog/pd-p/7ce99287-bea7-4831-ba0d-97be77b20574)
* [SAP Commerce](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)

* [SAP Commerce

  SAP Commerce](/t5/c-khhcw49343/SAP%2BCommerce/pd-p/67837800100800007216)
* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)
* [SAP Ariba Catalog

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BCatalog/pd-p/7ce99287-bea7-4831-ba0d-97be77b20574)

View products (3)

# Background

Hello All,

[SAP Commerce Cloud in the Public Cloud](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD?locale=en-US&state=PRODUCTION&version=v2205 "Product")(I'll use Commerce for short name in this article) will support [punchout level 2](https://help.sap.com/docs/ARIBA_NETWORK/11ee0faf55c74bf49379485c2ca588a9/415545f9d0a310149297e077d90665d7.html) with release 2211. As one of the prerequisites,  we have to upload product catalog information to procurement system. Below we provide a solution to automatically upload product catalog from Commerce to procurement system.

# **Prerequisites**

* You are the back office admin of Commerce

* You have right to deploy new iFlow in [SAP Cloud integration](https://help.sap.com/docs/CLOUD_INTEGRATION?locale=en-US&version=Cloud)

* You have admin right to import impex file in Commerce HAC(optional)

# Design

As commerce cloud has OOTB [Integrations and Data Management](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/bad9b0b66bac476f8a4a5c4a08e4ab6b/c8e7a9d3cd5f4240baae493804731155.html?version=v2011&locale=en-US) to export product info and changes to external terminal. We just tries to:

* Do some small configurations in [Integrations and Data Management](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/bad9b0b66bac476f8a4a5c4a08e4ab6b/c8e7a9d3cd5f4240baae493804731155.html?version=v2011&locale=en-US) side to export product info with some [virtual properties](https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/bad9b0b66bac476f8a4a5c4a08e4ab6b/de99ef65ca85473d92520c6eab4d30b7.html?locale=en-US&version=v2011&q=virtual%20property)

* Use [SAP Cloud Integration](https://www.sap.com/products/technology-platform/integration-suite.html) to create endpoints to receive the exported info and converted to target procurement system's format;

Below is a rough overall view of what's we have done

![](/legacyfs/online/storage/blog_attachments/2022/09/overall-view.jpg)

# Setup in Commerce cloud

In order to export product data from SAP Commerce Cloud to external system, firstly a new product integration object should be created, and then configure consumed destination and outbound sync.

## 1. Create the Product Integration Object

Create an Integration Object, for example, *PunchoutProduct*, that contains the code, name, catalogVersion and other required attributes. You can create the object using ImpEx.

1. In a web browser, navigate to the SAP Commerce Cloud Administration Console at <https://localhost:9002/> and log in.

2. Click Console > ImpEx Import

3. Paste the ImpEx into the Import Content field and click Import content, which will export product info with **virtualProductCode** as *product-<product-code>*
   Sample ImpEx:

   ```
   INSERT_UPDATE Script; code[unique = true]; content                           ; active[default = true, unique = true]

                       ; virtualProductCode        ; "import de.hybris.platform.core.model.product.ProductModel;

   ProductModel product = (ProductModel)itemModel;

   return ""product-""+product.code" ; true

   # Configure Integration Object

   INSERT_UPDATE IntegrationObject; code[unique = true]; integrationType(code)

                                  ; PunchoutProduct    ; INBOUND

   INSERT_UPDATE IntegrationObjectItem; integrationObject(code)[unique = true]; code[unique = true]; type(code)     ; root[default = false]; itemTypeMatch(code)

                                      ; PunchoutProduct                       ; Product            ; Product        ; true                 ; ALL_SUB_AND_SUPER_TYPES ;

                                      ; PunchoutProduct                       ; PriceRow           ; PriceRow       ;                      ; ALL_SUB_AND_SUPER_TYPES ;

                                      ; PunchoutProduct                       ; Currency           ; Currency       ;                      ; ALL_SUB_AND_SUPER_TYPES ;

                                      ; PunchoutProduct                       ; Catalog            ; Catalog        ;                      ; ALL_SUB_AND_SUPER_TYPES ;

                                      ; PunchoutProduct                       ; CatalogVersion     ; CatalogVersion ;                      ; ALL_SUB_AND_SUPER_TYPES ;

   INSERT_UPDATE IntegrationObjectItemAttribute; integrationObjectItem(integrationObject(code), code)[unique = true]; attributeName[unique = true]; attributeDescriptor(enclosingType(code), qualifier); returnIntegrationObjectItem(integrationObject(code), code); unique[default = false]; autoCreate[default = false]

                                               ; PunchoutProduct:Product                                            ; catalogVersion              ; Product:catalogVersion                             ; PunchoutProduct:CatalogVersion                            ; true                   ;

                                               ; PunchoutProduct:Product                                            ; manufacturerAID             ; Product:manufacturerAID                            ;                                                      ...