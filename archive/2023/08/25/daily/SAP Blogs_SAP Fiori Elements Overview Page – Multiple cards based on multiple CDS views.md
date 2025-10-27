---
title: SAP Fiori Elements Overview Page – Multiple cards based on multiple CDS views
url: https://blogs.sap.com/2023/08/24/sap-fiori-elements-overview-page-multiple-cards-based-on-multiple-cds-views/
source: SAP Blogs
date: 2023-08-25
fetch_date: 2025-10-04T12:00:36.246266
---

# SAP Fiori Elements Overview Page – Multiple cards based on multiple CDS views

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Fiori Elements Overview Page - Multiple cards ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/165558&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Fiori Elements Overview Page - Multiple cards based on multiple CDS views](/t5/technology-blog-posts-by-members/sap-fiori-elements-overview-page-multiple-cards-based-on-multiple-cds-views/ba-p/13581205)

![SyedAllaBakshu](https://avatars.profile.sap.com/a/0/ida0381fbc351ee1cf7b7a3f6332d63c085caac3b94f4c271e04f2f46afe7e7c4b_small.jpeg "SyedAllaBakshu")

[SyedAllaBakshu](https://community.sap.com/t5/user/viewprofilepage/user-id/15779)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=165558)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/165558)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13581205)

‎2023 Aug 24
10:48 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/165558/tab/all-users "Click here to see who gave kudos to this post.")

4,521

* SAP Managed Tags
* [SAP Fiori](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori/pd-p/73554900100700000977)
* [SAP Fiori Elements](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Elements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori

  Software Product](/t5/c-khhcw49343/SAP%2BFiori/pd-p/73554900100700000977)
* [SAP Fiori Elements

  Software Product Function](/t5/c-khhcw49343/SAP%2BFiori%2BElements/pd-p/ed5c1ef6-932f-4c19-b2ba-1be375109ff5)

View products (3)

Hello All,

The purpose of this blog is to develop a single overview page based on multiple CDS view. At the end of this blog, we will be able to develop a Overview page with cards based on multiple CDS views.

There are 5 steps to be done :

1. Create CDS Views

2. Expose CDS View as OData

3. Activate the OData Service

4. Create App in WebIDE

5. Add cards to the Fiori App

**1. Create CDS View :** In this step, we are creating 2 CDS views :

a. ZSOCOUNT - CDS for displaying sales orders based on Sales order Type

```
@AbapCatalog.sqlViewName: 'ZCOUNT_SO'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'Sales orders by type'

define view ZCOUNTSO as select from vbak as Hdr

inner join vbap as Item on Hdr.vbeln = Item.vbeln {

     @UI.lineItem: [{ position: 10, label: 'Sales order Type', qualifier: 'Q3' }]

    key Hdr.auart as soType,

     @UI.lineItem: [{ position: 20, label: 'Sales order count', qualifier: 'Q3', type: #AS_DATAPOINT }]

    key count(*) as soCount

}

group by Hdr.auart
```

b. ZMATERIAL - CDS for displaying Materials based on PLANT

```
@AbapCatalog.sqlViewName: 'ZMATERIALS_PLANT'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'CDS for materials by plant'

define view ZMATERIALS as select from mara as A

    inner join   marc as C on A.matnr = C.matnr

{

//  key A.matnr  as Material,

    @UI.lineItem: [{ position: 10, label: 'Plant', qualifier: 'MARA' }]

  key C.werks  as Plant,

   @UI.lineItem: [{ position: 20, label: 'Materials created', qualifier: 'MARA', type: #AS_DATAPOINT }]

  key count(*) as MaterialsCreated

}

group by

  C.werks
```

**2.Expose CDS View as OData**

Add the annotation to both the CDS views :

```
@OData.publish: true
```

**3.Activate the OData Service**

Activate the oData in Backend using Tcode:  /N/IWFND/MAINT\_SERVICE

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture.jpg)

Activate OData service

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture2.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture3.jpg)

Similarly Activate the OData for second CDS ZMATERIALS.

**4. Create App in WebIDE**

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture4-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture5.jpg)

Select Overview Page

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture6.jpg)

Provide Project Name, Namespace, Title and Description

In the next step - Data Connection, connect your backend server and provide login credentials

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture7.jpg)

Select the OData service we created in previous steps

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture8.jpg)

Select the Annotation File

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture9.jpg)

Select Alias and click on Finish

New Project is created. You can test the app by running Webapp -> test -> testOVP.html.

**5. Add Cards to Fiori App**

Right click on Project -> New --> Card

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture10.jpg)

We will show the data in the form of a Bar chart, so we will select LIST:

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture11.jpg)

You can choose based on your requirement.

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture12.jpg)

Choose existing datasource

In template customisation, provide Entity set, Title, subtitle and card properties as you wish to display and click Finish :

![](/legacyfs/online/storage/blog_attachments/2023/08/Capture14.jpg)

Now in order to test the app, do these changes in the manifest.json file in the App :

```
	"sap.ovp": {

		"globalFilterModel": "ZCOUNTSO_CDS",

		"globalFilterEntityType": "ZCOUNTSOType",

		"containerLayout": "resizable",

		"enableLiveFilter": true,

		"considerAnalyticalParameters": false,

		"cards": {

			"card00": {

				"model": "ZCOUNTSO_CDS",

				"template": "sap.ovp.cards.list",

				"settings": {

					"title": "{{card00_title}}",

					"subTitle": "{{card00_subTitle}}",

					"entitySet": "ZCOUNTSO",

					"listType": "extended",

					"listFlavor": "bar",

					"sortBy": "soCount",

					"sortOrder": "descending",

					"addODataSelect": false,

					"annotationPath": "com.sap.vocabularies.UI.v1.LineItem#Q1"

				}

			}

		}

	}
```

Do not forget to add the UI annotations in the CDS. Final CDS code should be like this:

```
@AbapCatalog.sqlViewName: 'ZCOUNT_SO'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'Sales orders by type'

@OData.publish: true

define view ZCOUNTSO as select from vbak as Hdr

inner join vbap as Item on Hdr.vbeln = Item.vbeln {

     @UI.lineItem: [{ position: 10, label: 'Sales order Type', qualifier: 'Q1' }]

    key Hdr.auart as soType,

    @UI.dataPoint:

      {

      title: 'Number of failed idocs',

      criticalityCalculation: {

      improvementDirection: #TARGET,

      toleranceRangeLowValue: 5,

      toleranceRangeHighValue: 500,

      deviationRangeHighValue: 4000

      }

      }

    ...