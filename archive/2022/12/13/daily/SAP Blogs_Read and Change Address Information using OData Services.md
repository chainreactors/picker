---
title: Read and Change Address Information using OData Services
url: https://blogs.sap.com/2022/12/12/read-and-change-address-information-using-odata-services/
source: SAP Blogs
date: 2022-12-13
fetch_date: 2025-10-04T01:18:10.481480
---

# Read and Change Address Information using OData Services

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Read and Change Address Information using OData Se...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/50379&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Read and Change Address Information using OData Services](/t5/enterprise-resource-planning-blog-posts-by-sap/read-and-change-address-information-using-odata-services/ba-p/13549923)

![knutheusermann](https://avatars.profile.sap.com/b/7/idb7fb30c49002d854c7e85e06a5b6918a428f7110a27aba746cec5be3200811d3_small.jpeg "knutheusermann")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[knutheusermann](https://community.sap.com/t5/user/viewprofilepage/user-id/4457)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=50379)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/50379)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549923)

‎2022 Dec 12
5:09 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/50379/tab/all-users "Click here to see who gave kudos to this post.")

3,092

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

*SAP Business ByDesign* (ByD) uses unified data model components and UI components for address information in master data objects and business documents. This blog post describes how to read and write address information using OData services.

You find all examples mentioned in this blog post in the GitHub repository [SAP Business ByDesign - API Samples](https://github.com/SAP-samples/byd-api-samples) including the ByD custom OData services *khsalesorder* and *khaddresssnapshot* and the Postman collection *Master Data*, folder *Address Snapshot*.

### Address Snapshot - Change Address Data in Business Documents

Let me start with some explanations about the handling of address information and the role of the business object "*AddressSnapshot*" in ByD:

**Business partner master data:**

When you edit the address of a business partner, the system creates a new address snapshot. In general the address snapshot business object has no public write access and behaves as a read-only business object after it has been saved. In result the history of business partner address changes is stored as a stack of address snapshots, whereas only the latest address snapshot is displayed on the master data UI.

**Business transactional documents:**

When you create a business document, the system refers to the latest address snapshot from the respective business partner master data record.

*Example: You create a sales order with the ship-to party “Silverstar Wholesale Corp”. In result the latest address snapshot of the business partner “Silverstar Wholesale Corp” is used as default and displayed as ship-to party address in the sales order.*

By changing the address data in the business partner master data record, the address of the sales order ship-to party remains unchanged, because the sales order keeps a stable reference to the address snapshot instance that was assigned originally (even if it is no longer the latest address state from a master data point of view). By this approach we ensure stable address data in transactional documents and avoid implicit/accidental changes of transactional documents by master data changes.

Along business process chains the reference to the same address snapshot is handed over from business document to business document (for example from the sales order to the customer invoice). Hence, by default all business documents along a process chain refer to the same address snapshot instance, unless you edit the address information of some business document in the process chain.

If you change the address information of a business transaction document, then the system creates a new address snapshot instance which occurs as document specific address information.

On the ByD UI this address snapshot exchange is processed automatically by the system.
However, if you want to change the address in a business document via OData services, you need to realize the address snapshot exchange in a sequence of OData requests.

### **Flow of sample OData request**

Example scenario: Create a sales order and change the address information of the ship-to party.

**Step 1: Create sales order**

*POST /sap/byd/odata/cust/v1/khsalesorder/SalesOrderCollection*

Request payload:

```
{

	"ExternalReference": "{{A_SalesOrderExternalReference}}",

	"Name": "Sales order for address change",

	"DataOriginTypeCode": "1",

	"SalesUnitParty":

		{

			"PartyID": "{{A_SalesUnitID}}"

		},

	"BuyerParty":

		{

			"PartyID": "{{A_CustomerID}}"

		},

	"PricingTerms":

		{

			"CurrencyCode": "EUR",

			"GrossAmountIndicator": false

		},

	"Item":

		[

			{

				"ID": "10",

				"ProcessingTypeCode": "TAN",

				"ItemProduct":

					{

						"ProductID": "{{A_MaterialID_stock}}"

					},

				"ItemScheduleLine":

					[

						{

							"Quantity": "2",

							"unitCode": "EA"

						}

					]

			}

		]

}
```

In result the ship-to address is defaulted with address information from the business partner master data record

**Step 2: Get sales order with ship-to party address data**(business object node: SalesOrder.ProductRecipientParty.AddressSnapshot)

*GET /sap/byd/odata/cust/v1/khsalesorder/SalesOrderCollection?$format=json&$expand=ProductRecipientParty/ProductRecipientPartyDetails/ProductRecipientPartyName,ProductRecipientParty/ProductRecipientPartyDetails/ProductRecipientPartyFormattedAddress,ProductRecipientParty/ProductRecipientPartyDetails/ProductRecipientPartyPostalAddress&$filter=ID eq '4214'&$select=ObjectID,UUID,ID,Name,ExternalReference,ProductRecipientParty,ProductRecipientParty/ProductRecipientPartyDetails,ProductRecipientParty/ProductRecipientPartyDetails/ProductRecipientPartyName,ProductRecipientParty/ProductRecipientPartyDetails/ProductRecipientPartyFormattedAddress,ProductRecipientParty/ProductRecipientPartyDetails/ProductRecipientPartyPostalAddress&$inlinecount=allpages&sap-language=en*

Response:

```
{

    "d": {

        "__count": "1",

        "results": [

            {

                "ObjectID": "91C8E1EA590F1EED9EC7B422F39F9941",

                "UUID": "91C8E1EA-590F-1EED-9EC7-B422F39F9941",

                "ID": "4214",

                "Name": "Sales order for address change",

                "ExternalReference": "KH-2022-12-12T16:54",

                "ProductRecipientParty": {

                    "ObjectID": "91C8E1EA590F1EED9EC7B422F39F9941                                    4",

                    "ParentObjectID": "91C8E1EA590F1EED9EC7B422F39F9941",

                    "PartyID": "CP100110",

                    "DeterminationMethodCode": "5",

                    "DeterminationMe...