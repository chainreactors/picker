---
title: A Technical Guide to Uploading Events Using Spreadsheet Templates in SAP Business Network Material Traceability Solution
url: https://blogs.sap.com/2023/04/20/a-technical-guide-to-uploading-events-using-spreadsheet-templates-in-sap-business-network-material-traceability-solution/
source: SAP Blogs
date: 2023-04-21
fetch_date: 2025-10-04T11:34:40.334757
---

# A Technical Guide to Uploading Events Using Spreadsheet Templates in SAP Business Network Material Traceability Solution

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by SAP](/t5/supply-chain-management-blog-posts-by-sap/bg-p/scm-blog-sap)
* A Technical Guide to Uploading Events Using Spread...

Supply Chain Management Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-sap/article-id/4827&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [A Technical Guide to Uploading Events Using Spreadsheet Templates in SAP Business Network Material Traceability Solution](/t5/supply-chain-management-blog-posts-by-sap/a-technical-guide-to-uploading-events-using-spreadsheet-templates-in-sap/ba-p/13554475)

![jinesh_krishnan](https://avatars.profile.sap.com/5/7/id57e9d45d0b1327da19ee57dd213b6e40a24b2fbf24937c069b14d21a07e2f071_small.jpeg "jinesh_krishnan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[jinesh\_krishnan](https://community.sap.com/t5/user/viewprofilepage/user-id/281072)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-sap&message.id=4827)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-sap/article-id/4827)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554475)

‎2023 Apr 20
8:54 PM

[6
Kudos](/t5/kudos/messagepage/board-id/scm-blog-sap/message-id/4827/tab/all-users "Click here to see who gave kudos to this post.")

1,646

* SAP Managed Tags
* [SAP Business Network for Logistics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Network%2520for%2520Logistics/pd-p/73554900100800001025)

* [SAP Business Network for Logistics

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BNetwork%2Bfor%2BLogistics/pd-p/73554900100800001025)

View products (1)

SAP Business Network Material Traceability solution has introduced a new application that enables users to upload events via a templated spreadsheet. This additional feature provides SAP Business Network Material Traceability customers with an alternative method for pushing data, alongside the existing ECC add on and APIs.

This guide aims to assist SAP Business Network Material Traceability users in understanding the spreadsheet template for uploading events, using [existing APIs](https://api.sap.com/api/MaterialTraceabilityEventNotification_Provider/overview) as a reference. This guide is the first part of a two-part blog series. The first part covers uploading events for batches, while the second part delves into serialised products.

To follow the steps outlined in this guide, users must have an active subscription to the SAP Business Network Material Traceability application and access to a spreadsheet tool such as Microsoft Excel or OpenOffice Spreadsheet.

Users with the "ExpertUserDataCaptureTemplate" role assigned will have access to the "Upload Events" application. To access the application, users can either navigate directly from the FIORI launchpad or access it via the "Product Batches" or "Serialized Products" applications.

Using the Predefined Spreadsheet Template: The "Upload Events" application requires SAP Business Network Material Traceability events to be uploaded using a predefined spreadsheet template. This template can be downloaded from the "Upload Events" application itself.

![](/legacyfs/online/storage/blog_attachments/2023/04/DownloadTemplate.png)

### How to Fill Out the SAP Business Network Material Traceability Spreadsheet Template for Batch genealogy

The Upload Events template can be best explained with a sample genealogy. Here is an example of a product genealogy traced based on batch.

![](/legacyfs/online/storage/blog_attachments/2023/04/SampleBacthchocoGenealogy.png)Downloaded template will be filled with data needed to produce a genealogy graph like the given example.  JSON payload for such a product genealogy is as given.

```
{

    "produceEvents": [

        {

            "batchId": "SBNMT_BAT-CNBGEPA",

            "productId": "SBNMT_CNB_GEPA",

            "systemId": "SBNMT_FIN",

            "productName": "SBNMT_Choco Nuts Bar GEPA",

            "creationDate": "20210501",

            "expirationDate": "20250501",

            "location": "Germany",

            "status": "RELEASED",

            "quantities": [

                {

                    "qualifier": "PER_PACK",

                    "value": "200",

                    "unit": ""

                }

            ],

            "properties": [

                {

                    "name": "GEPA",

                    "value": true

                },

                {

                    "name": "RSPO_NEXT",

                    "value": true

                }

            ],

            "components": [

                {

                    "batchId": "SBNMT_BAT-CHGEPA-R",

                    "productId": "SBNMT_CH_GEPA",

                    "systemId": "SBNMT_FIN"

                },

                {

                    "batchId": "SBNMT_BAT-W001-R",

                    "productId": "SBNMT_WAFERS",

                    "systemId": "SBNMT_FIN"

                },

                {

                    "batchId": "SBNMT_BAT-CHN001-R",

                    "productId": "SBNMT_CHOPPED_NUTS",

                    "systemId": "SBNMT_FIN"

                }

            ]

        }

    ],

    "deliverEvents": [

        {

            "vendorBatchId": "SBNMT_BAT-CNBGEPA",

            "productId": "SBNMT_CNB_GEPA",

            "systemId": "SBNMT_FIN",

            "vendorDeliveryId": "VFIN-CNBGEPA-1",

            "vendorCountry": "DE",

            "vendorPostalCode": "74072",

            "purchaseOrderId": "PO-025",

            "purchaseOrderItem": "I025",

            "purchaseOrderDate": "20210510",

            "status": "RELEASED"

        },

        {

            "vendorBatchId": "SBNMT_BAT-CNBGEPA",

            "productId": "SBNMT_CNB_GEPA",

            "systemId": "SBNMT_FIN",

            "vendorDeliveryId": "VFIN-CNBGEPA-2",

            "vendorCountry": "DE",

            "vendorPostalCode": "69190",

            "purchaseOrderId": "PO-026",

            "purchaseOrderItem": "I026",

            "purchaseOrderDate": "20210512",

            "status": "RELEASED"

        },

        {

            "vendorBatchId": "SBNMT_BAT-CNBGEPA",

            "productId": "SBNMT_CNB_GEPA",

            "systemId": "SBNMT_FIN",

            "vendorDeliveryId": "VFIN-CNBGEPA-3",

            "vendorCountry": "DE",

            "vendorPostalCode": "60306",

            "purchaseOrderId": "PO-027",

            "purchaseOrderItem": "I027",

            "purchaseOrderDate": "20210513",

            "status": "RELEASED"

        }

    ],

    "receiveEvents": [

        {

            "batchId": "SBNMT_BAT-W001-R",

            "productId": "SBNMT_WAFERS",

            "productName": "SBNMT_Wafers",

            "systemId": "SBNMT_FIN",

            "creationDate": "20210401",

            "status": "RELEASED",

            "quantities": [

                {

                    "qualifier": "PER_PACK",

                    "value": "100",

                    "unit": ""

                }

            ],

            "deliveryItemKeys": [

                {

            ...