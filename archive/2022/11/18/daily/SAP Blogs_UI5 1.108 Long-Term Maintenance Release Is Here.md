---
title: UI5 1.108 Long-Term Maintenance Release Is Here
url: https://blogs.sap.com/2022/11/17/ui5-1.108-long-term-maintenance-release-is-here/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:26.102224
---

# UI5 1.108 Long-Term Maintenance Release Is Here

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* UI5 1.108 Long-Term Maintenance Release Is Here

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158687&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [UI5 1.108 Long-Term Maintenance Release Is Here](/t5/technology-blog-posts-by-sap/ui5-1-108-long-term-maintenance-release-is-here/ba-p/13552658)

![Margot](https://avatars.profile.sap.com/7/7/id77ff34b5dec4d975f022f3c281eeda1b006680a9fe6c67afeab4dcfd9bf849d4_small.jpeg "Margot")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Margot](https://community.sap.com/t5/user/viewprofilepage/user-id/8844)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158687)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158687)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552658)

‎2022 Nov 17
6:27 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158687/tab/all-users "Click here to see who gave kudos to this post.")

5,924

* SAP Managed Tags
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface](https://community.sap.com/t5/c-khhcw49343/User%2520Interface/pd-p/378427990965467211484671270864901)

* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [User Interface

  Topic](/t5/c-khhcw49343/User%2BInterface/pd-p/378427990965467211484671270864901)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (4)

![](/legacyfs/online/storage/blog_attachments/2020/10/UI5Officialheader.png)

To help you plan the upgrading, we want to let you know that version 1.108 of OpenUI5 and SAPUI5 is a Long-Term Maintenance (LTM) version. This version will get standard support until the end of 2027. UI5 1.108 is already available on our CDN for [SAPUI5](https://ui5.sap.com/)/[OpenUI5](https://sdk.openui5.org/).

### What you should expect

When upgrading to UI5 1.108, you’ll get a number of new features plus of all the features we’ve delivered since v1.96. Including, but not limited to:

**Enhanced core**

* New sap.ui.core.Element#closestTo method to replace the jQuery.fn.control extension function. (Note: You might need to add an outer loop when migrating your code to the new API!)

* Improved handling of aggregations in XML views

**Enhanced OData V4 model**

* Support for deferred delete scenarios

* New sap.ui.model.odata.v4.ODataModel#delete methods

* Support for inline creation rows

* New sap.ui.model.odata.v4.ODataModel#getKeepAliveContext method

**Enhanced OData V2 model**

* Support for deep create scenarios

* New sap.ui.model.ClientTreeBinding#getCount method

* New calendarWeekNumbering format option for sap.ui.core.format.DateFormat

* New sap.ui.model.oodata.v2.Context#delete method for deleting binding context irrespective of its status

**Improved user experience**

* New theme flavors of the Horizon visual theme of SAP Fiori

* Faster initial rendering of sap.m.List, sap.m.Table, sap.m.Tree controls

* Enablement of asynchronous loading of message details in sap.m.MessageBox

* New firstDayOfWeek property in sap.m.SinglePlanningCalendar

* New personalization panels with reuse content for various types of personalization

* New showClearIcon property in sap.m.ComboBox/MultiComboBox

* Configuration options for toolbar in sap.ui.richtexteditor.RichTextEditor (SAPUI5 only)

* Reworked design of the filter panel in the table personalization dialog of sap.ui.comp (SAPUI5 only)

* New file export capabilities in sap.ui.comp

* New uiStateChange event for sap.ui.comp.smartchart.SmartChart and sap.ui.comp.smarttable.SmartTable (SAPUI5 only)

**Enhanced flexibility** (SAPUI5 only)

* Filter unsaved changes and draft changes in key user adaptation

* Enablement of key user adaptation for TextArrangement annotation types in sap.ui.comp.smartfield.SmartField

* Enablement of add custom field scenarios in sap.ui.comp.smartfield.SmartFilterBar in key user adaptation

* Translation of UI changes done during key use adaptation (SAP BTP, CF environment)

**Improved accessibility**

* Keyboard interaction and accessibility improvements in sap.m.Carousel

* New or changed default role assignment in sap.m.List controls

* New API to change ARIA role assignment in sap.m.Link

* New titleLevel property in sap.m.MessagePage to set custom ARIA level

And there is more!
Check out our What’s New in the UI5 documentation for further information and get the full list of features coming with each release:

* What’s New in SAPUI5 [1.108](https://ui5.sap.com/1.108.0/#/topic/799291a4be7542c9a0a96ba425d0dec2) | [1.107](https://ui5.sap.com/#/topic/b88b40e124634bb4897f36846f23cd12) | [1.106](https://ui5.sap.com/#/topic/c70bb907d05a4f9fb6c36ecf73b3fb2e) | [1.105](https://ui5.sap.com/#/topic/5567dccb287b4dd9aa755a76cf25ae41) | [1.104](https://ui5.sap.com/#/topic/f01ebd44da544fa8824464447b896a5c) | [1.103](https://ui5.sap.com/#/topic/7534ae89605d45ae989fea85b70f24d8) | [1.102](https://ui5.sap.com/#/topic/b530db37f4db4164b5e68f20bff93a9a) | [1.101](https://ui5.sap.com/#/topic/5a184109b1ec44e7ab7e43d40ef56847) | [1.100](https://ui5.sap.com/#/topic/5deb78f36022473487be44cb3a71140a) | [1.99](https://ui5.sap.com/#/topic/5e35c2512e014e3b9831afd1cd041ed4) | [1.98](https://ui5.sap.com/#/topic/7aacb4e107c44c90b5b0dd97fcb1f333) | [1.97](https://ui5.sap.com/#/topic/f21858fa6a07451c9cb86e0c023a7092)

* What’s New in OpenUI5 [1.108](https://sdk.openui5.org/1.108.0/#/topic/799291a4be7542c9a0a96ba425d0dec2) | [1.107](https://sdk.openui5.org/#/topic/b88b40e124634bb4897f36846f23cd12) | [1.106](https://sdk.openui5.org/#/topic/c70bb907d05a4f9fb6c36ecf73b3fb2e) | [1.105](https://sdk.openui5.org/#/topic/5567dccb287b4dd9aa755a76cf25ae41) | [1.104](https://sdk.openui5.org/#/topic/f01ebd44da544fa8824464447b896a5c) | [1.103](https://sdk.openui5.org/#/topic/7534ae89605d45ae989fea85b70f24d8) | [1.102](https://sdk.openui5.org/#/topic/b530db37f4db4164b5e68f20bff93a9a) | [1.101](https://sdk.openui5.org/#/topic/5a184109b1ec44e7ab7e43d40ef56847) | [1.100](https://sdk.openui5.org/#/topic/5deb78f36022473487be44cb3a71140a) | [1.99](https://sdk.openui5.org/#/topic/5e35c2512e014e3b9831afd1cd041ed4) | [1.98](https://sdk.openui5.org/#/topic/7aacb4e107c44c90b5b0dd97fcb1f333) | [1.97](https://sdk.openui5.org/#/topic/f21858fa6a07451c9cb86e0c023a7092)

Additionally, your can benefit from hundreds of bug fixes and improvements that have been shipped since then. Therefore, we recommend moving to UI5 1.108 once it becomes available for you.

Want to keep up with UI5 announcement...