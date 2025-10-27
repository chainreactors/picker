---
title: SAP UI5 Smart filter approach for passing date filter to a parameterized CDS view
url: https://blogs.sap.com/2022/10/17/sap-ui5-smart-filter-approach-for-passing-date-filter-to-a-parameterized-cds-view/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:07:07.880542
---

# SAP UI5 Smart filter approach for passing date filter to a parameterized CDS view

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP UI5 Smart filter approach for passing date fil...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159013&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP UI5 Smart filter approach for passing date filter to a parameterized CDS view](/t5/technology-blog-posts-by-members/sap-ui5-smart-filter-approach-for-passing-date-filter-to-a-parameterized/ba-p/13543748)

![jmalla](https://avatars.profile.sap.com/3/f/id3f7d7aaed8e1fa10457cc57133c17994820dced76f51e7743437c7f403e41954_small.jpeg "jmalla")

[jmalla](https://community.sap.com/t5/user/viewprofilepage/user-id/42347)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159013)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159013)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13543748)

‎2022 Oct 17
8:58 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159013/tab/all-users "Click here to see who gave kudos to this post.")

8,439

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (2)

Hi SAP Fiori and SAP UI5 development enthusiasts,

It's been a little while since I wrote my last blog and I came across an issue while developing a custom SAP UI5 application that was quite challenging and required a lot of painful research.  I finally managed to crack the code and come up with the solution.  A little background about the application - I was developing a stock inventory application for 3PL (Third Party logistics) partners to maintain their stock inventories in S/4 HANA and also be able to compare their stock to the SAP stock quantities in both material base unit and alternate units - e.g. KG, LB, TON, etc. for the same material.  Maybe the material base unit is KG, but the 3PL is maintaining this in TONs.

So there is an S/4 HANA CDS view called I\_MatlStkAtKeyDateInAltUoM which takes in a date parameter as in input and has Material, Plant, Storage Location, and Batch as keys with some other fields.

```
define view I_MatlStkAtKeyDateInAltUoM

  with parameters

    P_KeyDate : vdm_v_key_date

  as select from P_MatlStkAtKeyDateInAltUoM( P_KeyDate : $parameters.P_KeyDate )

...

{

      // Stock Identifier

      @ObjectModel.foreignKey.association: '_Product'

  key Material                                        as Product,

      @ObjectModel.foreignKey.association: '_Plant'

  key Plant,

      @ObjectModel.foreignKey.association: '_StorageLocation'

  key StorageLocation,

  key Batch,

      @ObjectModel.foreignKey.association: '_Supplier'

      // Units

      @Semantics.unitOfMeasure

  key MaterialBaseUnit,

      @Semantics.unitOfMeasure

  key AlternativeUnit,

      // Quantities in Base Unit of Measure

      @Semantics.quantity.unitOfMeasure: 'MaterialBaseUnit'

      @DefaultAggregation : #SUM

      MatlWrhsStkQtyInMatlBaseUnit,

      // Quantities in Alternative Unit of Measure

      @Semantics.quantity.unitOfMeasure: 'AlternativeUnit'

      @DefaultAggregation : #SUM

      cast( fltp_to_dec( MatlWrhsStkQtyInAltUoM as abap.dec(31,14) ) as nsdm_stock_qty_auom ) as MatlWrhsStkQtyInAltUoM,

....
```

If you view data for this CDS, Eclipse pops up an input box for entering the date since it is a mandatory parameter to the CDS view:

![](/legacyfs/online/storage/blog_attachments/2022/10/P_KEYDATE-Parameter.png)

P\_KEYDATE parameter

Quantities in material base unit and alternate unit are returned:

![](/legacyfs/online/storage/blog_attachments/2022/10/I_MATSTKATKEYDATEINALTUOM.png)

I\_MATSTKATKEYDATEINALTUOM results

So I developed a custom Fiori SAP UI5 application that looks like a Fiori elements List report object page - but has a way more flexibility - hence the custom SAP UI5 approach.

![](/legacyfs/online/storage/blog_attachments/2022/10/List-report-filter-and-table.png)

Custom Smart Filter and smart table like Fiori Elements List Report

The results look like this and allows the users to enter the ThreePLQuantity and Unit of measure:

![](/legacyfs/online/storage/blog_attachments/2022/10/Smart-table-results.png)

Smart table with results from query

The smart filter call to the backend OData service looks like this:

![](/legacyfs/online/storage/blog_attachments/2022/10/Call-to-backend-in-Chrome-Inspector-window.png)

Call to Backend S/4 HANA OData service

So here is the HTTP get call in url-encoded format:

```
GET MaterialStock(P_KeyDate=datetime%272022-09-27T12%3a00%3a00%27)/Set?sap-client=100&$skip=0&$top=100&$filter=Plant%20eq%20%27USA1%27%20and%20StorageLocation%20eq%20%271000%27&$select=Plant%2cStorageLocation%2cProduct%2cBatch%2cKeyDate%2cQuantityInBaseUoM%2cMaterialBaseUnit%2cQuantityInAltUoM%2cAlternativeUnit%2cThreePLQuantity%2cThreePLUnitOfMeasure%2cDifferenceQuantity%2cDifferenceUnitOfMeasure&$inlinecount=allpages HTTP/1.1
```

Here is the call in url-decoded format - much easier to read....

```
GETMaterialStock(P_KeyDate=datetime'2022-09-27T12:00:00')/Set?sap-client=100&$skip=0&$top=100&$filter=Plant eq 'USA1' and StorageLocation eq '1000'&$select=Plant,StorageLocation,Product,Batch,KeyDate,QuantityInBaseUoM,MaterialBaseUnit,QuantityInAltUoM,AlternativeUnit,ThreePLQuantity,ThreePLUnitOfMeasure,DifferenceQuantity,DifferenceUnitOfMeasure&$inlinecount=allpagesHTTP/1.1
```

So now here is where the subject matter for this blog comes in... and if you've read this far, maybe you have been searching for it.  It was really tricky to create the date filter and pass this to the backend from the date smart filter.

We need to get the date filter field value and call the OData service as ***GETMaterialStock(P\_KeyDate=datetime'2022-09-27T12:00:00')/Set***

A little strange that there is a /Set after the parameter in parenthesis....

I read all the blogs and SAP help articles on CDS with parameters that I could Google search along with smart filters for dates but the articles did not give enough insight into this topic.  I finally figured it out and wanted to share this knowledge with my fellow SAP Fiori and SAP UI5 developers.

So here is the smart filter and table - the SAP UI5 components are from the same SAP UI library as the Fiori elements - and this keeps the UI consistent with the SAP Fiori look and feel.  Consistency is a good thing....... from SAP UI5 coding to playing a tennis match.... be consistent ![:slightly_smiling_face:](/html/@F5E1ACF1B11D8F2A0F728ABA9AA5B820/emoticons/1f642.png ":slightly_smiling_face:")

Here is a snippet of the XML view - note that there is no date filter defined - but it is automatically shown on the filter bar:

```
<mvc:View

    xmlns:mvc="sap.ui.core.mvc"

    xmlns="sap.m"

    xmlns:smartFilterBar="sap.ui.comp...