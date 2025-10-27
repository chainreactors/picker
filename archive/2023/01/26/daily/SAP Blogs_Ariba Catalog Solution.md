---
title: Ariba Catalog Solution
url: https://blogs.sap.com/2023/01/25/ariba-catalog-solution/
source: SAP Blogs
date: 2023-01-26
fetch_date: 2025-10-04T04:52:00.048312
---

# Ariba Catalog Solution

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Spend Management](/t5/spend-management/ct-p/spend-management)
* [Spend Management Blog Posts by Members](/t5/spend-management-blog-posts-by-members/bg-p/spend-management-blog-members)
* Ariba Catalog Solution

Spend Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/spend-management-blog-members/article-id/1822&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Ariba Catalog Solution](/t5/spend-management-blog-posts-by-members/ariba-catalog-solution/ba-p/13549568)

![Chhetan1](https://avatars.profile.sap.com/d/3/idd35a10cb1334547512e63e16f648267bf6ed163abca1e3b31a32e8fb0ee05204_small.jpeg "Chhetan1")

[Chhetan1](https://community.sap.com/t5/user/viewprofilepage/user-id/46979)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=spend-management-blog-members&message.id=1822)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/spend-management-blog-members/article-id/1822)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549568)

‎2023 Jan 25
6:35 PM

[13
Kudos](/t5/kudos/messagepage/board-id/spend-management-blog-members/message-id/1822/tab/all-users "Click here to see who gave kudos to this post.")

17,264

* SAP Managed Tags
* [SAP Ariba Catalog](https://community.sap.com/t5/c-khhcw49343/SAP%2520Ariba%2520Catalog/pd-p/7ce99287-bea7-4831-ba0d-97be77b20574)

* [SAP Ariba Catalog

  Software Product](/t5/c-khhcw49343/SAP%2BAriba%2BCatalog/pd-p/7ce99287-bea7-4831-ba0d-97be77b20574)

View products (1)

**Hello, welcome to my blog post!** I’m Chetan Jadhav. I’m an SAP Ariba consultant. This is my brand-new blog on Ariba catalog solution. It’s a complete guide for Ariba consultants and administrators who configures catalog, approval flow and master data in Ariba.

**Introduction**

Catalog is a list of sourced items maintained systematically with image, specification, part number, price, unit of measure, commodity code, parametric attributes, lead time and supplier in Ariba.

Catalogs are generally maintained for categories such as MRO, IT hardware, R&D equipment, software licenses, office supplies, contracted cleaning and security services.

Catalogs would help customers to reduce their tail spend made through ad hoc purchases, reduce procurement risks and tackle poor performance of suppliers.

There are two types of catalogs maintained in Ariba and they are technically called as buyer hosted catalog and supplier hosted catalog. **Buyer hosted catalog:** The content team of customer builds a catalog based on the rate sheet shared by supplier and imports it to Ariba. **Supplier hosted catalog:** Seller creates a list of items based on contracted terms, uploads it to their Ariba account and Ariba network shares it with customer. In some cases, supplier can also host their web-based catalog upon agreed terms.![](/legacyfs/online/storage/blog_attachments/2023/01/S10-3.png)

**Note:**

Product and service catalog, non-standard catalog, partial catalog, tier-Pricing catalog and parametric catalog are example of static catalogs and can be managed by either buyer or supplier

Punchout catalog is a web-based catalog which is managed by supplier as it requires frequent updates on price, description and content.

**How to build Catalog using Excel template?**

Excel template has four sheets, an instruction sheet, a header sheet, an items sheet and a sample formats sheet. **Instruction sheet** contains the details of how to use the catalog template. **Header sheet** has fields such as Load mode, supplier ID domain, code format, UNUOM, currency and comments**. Items sheet** has fields related to unique ID’s, codes, descriptions, price, images, attachments, components, parametric attributes, search words, restrictions etc. catalog administrator updates content of items in it based on rate sheet. **Sample formats sheet** contains the details of how to update data in fields such as Images, commodity code, price configuration. User can remove Instructions and Sample Format sheets from the template.

**Below are the instructions to fill the catalog template:**

**Header Sheet:**![](/legacyfs/online/storage/blog_attachments/2023/01/S2-2.png)

***LoadMode:*** Set value “F” in the field while loading a new catalog or value “I” while modifying, adding or deleting any items to the activated catalog.

***Supplierid\_Domain:*** NetworkID, buyersystmID or SAP ID values can be updated in this field

***UNUOM:*** This filed should always be updated as TRUE

***Currency:*** Update the currency used for the pricing of items in rate sheet

***Comments:*** Use this field to update any comments related to catalog

**Note:**

* Ensure all the cells are formatted in Excel as “Text” to retain any leading or trailing zeros

* Template fields are color coded:

* RED Fields -> Required, do not leave these fields blank, cannot be deleted

* Yellow Fields -> Optional but wanted, can leave blank, can be deleted

* Green Fields -> Optional, can leave blank, can be deleted, can add customized fields

* Remove Instructions and Sample Formats sheets from template

**Items Sheet:**![](/legacyfs/online/storage/blog_attachments/2023/01/S3-2.png)

***Supplier ID:*** Enter BuyersystemID, SAP Vendor ID or Supplier’s AN ID

Example:

* BuyersystemID: ACM\_12345678 -> Supplier’s Ariba profile ID

* SAP Vendor ID: 778866 -> SAP partition vendor ID

* Ariba Network ID: Test –> AN123456789-t and Production –>AN123456789

***Supplier Part ID:*** The supplier part ID should be unique for each line item in catalog. It is generally mentioned in the rate sheet which is shared by supplier.

Note: If supplier part ID is not mentioned in the rate sheet, then create an ID of your choice or follow the best practices set in your procurement operation

***Item Description:*** Update complete product or service description in 276 characters based on the rate sheet and do not include any special characters in it

**Note:** Create a separate custom field for Item description or specification, if there are more than 276 characters in it. Ariba can create a custom field to input characters up to 1000 in the template.

***Unit Price:*** Update the price without currency symbol based on the rate sheet

***Unit of measure****:* Update UOM based on rate sheet and ensure that it should be updated in Ariba and ERP

***Short Name:*** A short description of an item in 50 characters. Do not use abbreviations. It should provide brief information of product and service items.

***Classification Codes:*** Classification of the product or services based on UNSPSC or customized taxonomies

* Domain: should be UNSPSC or Custom -> if customer uses taxonomy codes to track spend

* Value: update valid commodity codes by referring to the list of UNSPSC or taxonomy

![](/legacyfs/online/storage/blog_attachments/2023/01/S4-2.png)

***Image:*** The image size should be 250\*250 pixels. Update image extension or URL in thumbnail, normal and detailed fields

***Lead Time:*** Number of business days required to deliver goods or services once the order is received by the supplier

***Currency:*** Update the currency used for the pricing of items in rate sheet

***Supplier Part Auxiliary ID:*** A unique ID combined with Supplier ID and Supplier part number

***Supplier URL:*** Web address ...