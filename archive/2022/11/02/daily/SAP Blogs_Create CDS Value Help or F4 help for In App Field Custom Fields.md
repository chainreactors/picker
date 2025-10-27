---
title: Create CDS Value Help or F4 help for In App Field Custom Fields
url: https://blogs.sap.com/2022/11/01/create-cds-value-help-or-f4-help-for-in-app-field-custom-fields/
source: SAP Blogs
date: 2022-11-02
fetch_date: 2025-10-03T21:31:50.160384
---

# Create CDS Value Help or F4 help for In App Field Custom Fields

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Create CDS Value Help or F4 help for In App Field ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161135&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Create CDS Value Help or F4 help for In App Field Custom Fields](/t5/technology-blog-posts-by-members/create-cds-value-help-or-f4-help-for-in-app-field-custom-fields/ba-p/13556603)

![SamannayaRoy](https://avatars.profile.sap.com/b/4/idb4bd2184a5a3d184405a5bc313e78efd61a3bc87ac585f4fa747cac6c5a2e1c0_small.jpeg "SamannayaRoy")

[SamannayaRoy](https://community.sap.com/t5/user/viewprofilepage/user-id/15378)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161135)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161135)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556603)

‎2022 Nov 01
6:25 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161135/tab/all-users "Click here to see who gave kudos to this post.")

46,858

* SAP Managed Tags
* [SAP BTP ABAP environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520ABAP%2520environment/pd-p/73555000100800001164)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP BTP ABAP environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%2BABAP%2Benvironment/pd-p/73555000100800001164)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

I was searching for different blogs for this F4 help but unfortunately couldn’t find a detailed blog on this. So, I felt to start writing the same for all technical developers.

For creation of CDS view we have 3 main interface view to be created.

**Step 1.**

First create a CDS view for Text table.

Use Object model annotations like @ObjectModel.representativeKey, @ObjectModel.dataCategory, @ObjectModel.usageType.dataClass, @ObjectModel.usageType.serviceQuality, @ObjectModel.usageType.sizeCategory, @ObjectModel.supportedCapabilities.

herewith I have also added the CDS view

![](/legacyfs/online/storage/blog_attachments/2022/10/Text-View-1.jpg)

Figure 1: TEXT CDS View- Basic View

Data Preview
![](/legacyfs/online/storage/blog_attachments/2022/10/Text-View_DP-1.jpg)

Figure 2: Data Preview on the Text View

**Adding the following code for reference.**

```
@AbapCatalog.sqlViewName: 'ZICOUNTRYTEXT'

@ClientHandling.algorithm: #SESSION_VARIABLE

@ObjectModel.representativeKey: 'Land1'

@ObjectModel.dataCategory: #TEXT

@ObjectModel.usageType.dataClass: #CUSTOMIZING

@ObjectModel.usageType.serviceQuality: #X

@ObjectModel.usageType.sizeCategory: #S

@ObjectModel.supportedCapabilities: [#SQL_DATA_SOURCE,#CDS_MODELING_DATA_SOURCE,#CDS_MODELING_ASSOCIATION_TARGET,#LANGUAGE_DEPENDENT_TEXT]

@Search.searchable: true

@VDM.viewType: #BASIC

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'Country Text'

define view ZI_countrytext

as select from t005t

{

@Semantics.language: true

    key spras as Spras,

    key land1 as Land1,

    @Semantics.text: true

      @Search.defaultSearchElement: true

    landx as Landx

}
```

**Step 2.**

Then associate the text view with Data table.

![](/legacyfs/online/storage/blog_attachments/2022/10/DataView-1.jpg)

Figure 3: Data Help View

Data preview for Help.

![](/legacyfs/online/storage/blog_attachments/2022/10/DataView_DP-1.jpg)

Figure 4: Data Preview

**Adding the following code for reference.**

```
@AbapCatalog.sqlViewName: 'ZICOUNTRY'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'Country Help'

@ClientHandling.algorithm: #SESSION_VARIABLE

@ObjectModel.representativeKey: 'Land1'

@ObjectModel.sapObjectNodeType.name: 'Land1'

@ObjectModel.usageType.dataClass: #CUSTOMIZING

@ObjectModel.usageType.serviceQuality: #A

@ObjectModel.usageType.sizeCategory: #S

@ObjectModel.supportedCapabilities: [#CDS_MODELING_ASSOCIATION_TARGET, #CDS_MODELING_DATA_SOURCE, #SQL_DATA_SOURCE]

@VDM.viewType: #BASIC

define view ZI_country

  as select from t005

  association [0..*] to ZI_countrytext as _countrytext on $projection.Land1 = _countrytext.Land1

{

      @ObjectModel.text.association: '_countrytext'

      @Search.defaultSearchElement: true

  key t005.land1 as Land1,

      _countrytext // Make association public

}
```

**Step 3.**

Then finally access the help data as VH simply by fetching data from Value Help.

Use these following annotations in header

**@ObjectModel.dataCategory: #VALUE\_HELP**
**@ObjectModel.usageType.dataClass: #CUSTOMIZING**
**@ObjectModel.usageType.serviceQuality: #A**
**@ObjectModel.usageType.sizeCategory: #S**
**@ObjectModel.supportedCapabilities**

And add **@ObjectModel.text.association** at the item level to refer data as Help view to given field. Add association value from previous view alias for reference.

![](/legacyfs/online/storage/blog_attachments/2022/10/VH-2.jpg)

Figure 5: Value Help CDS View

Data Preview

![](/legacyfs/online/storage/blog_attachments/2022/10/VH_DP-1.jpg)

Figure 6: Data Preview

**Code for above Value help is added below.**

```
@AbapCatalog.sqlViewName: 'ZIDESTCOUNTRYVH'

@AbapCatalog.compiler.compareFilter: true

@AbapCatalog.preserveKey: true

@AccessControl.authorizationCheck: #NOT_REQUIRED

@EndUserText.label: 'Destination country Value Help'

@ClientHandling.algorithm: #SESSION_VARIABLE

@ObjectModel.dataCategory: #VALUE_HELP

@ObjectModel.usageType.dataClass: #CUSTOMIZING

@ObjectModel.usageType.serviceQuality: #A

@ObjectModel.usageType.sizeCategory: #S

@ObjectModel.supportedCapabilities: [#CDS_MODELING_ASSOCIATION_TARGET, #CDS_MODELING_DATA_SOURCE, #SQL_DATA_SOURCE, #VALUE_HELP_PROVIDER, #SEARCHABLE_ENTITY]

@Search.searchable: true

@VDM.viewType: #BASIC

define view ZI_DestcountryVH

as select from ZI_country

{

 @ObjectModel.text.association: '_countrytext'

      @Search.defaultSearchElement: true

      key Land1,

      /* Associations */

      _countrytext

}
```

To use it as Value help for In APP custom Fields you need to release the view (**Path: Windows -> Show View -> Properties**).

And finally, we can have multiple usage of these Help View for Fiori applications like Query browser in analytics, or Fiori Tile in UI5, In App Extension in BTP.

In next blog I can see how to add it in Fiori App as a custom field and get the F4 (<https://blo...