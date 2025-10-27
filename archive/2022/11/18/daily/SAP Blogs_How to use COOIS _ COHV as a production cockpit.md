---
title: How to use COOIS / COHV as a production cockpit
url: https://blogs.sap.com/2022/11/17/how-to-use-coois-cohv-as-a-production-cockpit/
source: SAP Blogs
date: 2022-11-18
fetch_date: 2025-10-03T23:06:28.496821
---

# How to use COOIS / COHV as a production cockpit

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to use COOIS / COHV as a production cockpit

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68380&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to use COOIS / COHV as a production cockpit](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-use-coois-cohv-as-a-production-cockpit/ba-p/13567442)

![23985754](https://avatars.profile.sap.com/6/d/id6dbb46aa097be58a0abc7145bb86cf79845f5c4b381a1eeef7f1e0f638103ba1_small.jpeg "23985754")

[23985754](https://community.sap.com/t5/user/viewprofilepage/user-id/811428)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68380)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68380)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567442)

‎2022 Nov 17
6:13 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68380/tab/all-users "Click here to see who gave kudos to this post.")

14,660

* SAP Managed Tags
* [MAN Production Planning (PP)](https://community.sap.com/t5/c-khhcw49343/MAN%2520Production%2520Planning%2520%28PP%29/pd-p/877902606110120463147070804386975)
* [User Experience](https://community.sap.com/t5/c-khhcw49343/User%2520Experience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)

* [MAN Production Planning (PP)

  Software Product Function](/t5/c-khhcw49343/MAN%2BProduction%2BPlanning%2B%252528PP%252529/pd-p/877902606110120463147070804386975)
* [User Experience

  Topic](/t5/c-khhcw49343/User%2BExperience/pd-p/4616d815-f39e-45c8-b13b-5a2d6679778f)

View products (2)

**Introduction**

This post describes how to use the full potential of the Production Information System (transactions COOIS COHV COOISPI COHVPI).

These transactions are too often used at only 10% of their capacity. This blog shows how to transform them into a shop floor production executing system for example.

These transactions have no limits as you can display all Production and Planning information and you can manage all access to the transaction through the navigation profile.

Remember that COHV and COOIS use the same program. Only COHV permits to add mass processing.

The COHV transaction is generally known for reporting, whereas it allows access to practically ALL transactions. With the cockpit, it is possible to select / display the information needed on a single screen (a BADI allows 10 additional fields to be added if necessary). It can be used in production directly on a workstation for many actions (depending on the variants) :

▪ WM Staging

▪ Confirmation

▪ Quality data entry

▪ Declarations

▪ Consumption

▪ Release/closure of production orders

▪ Scrapping

▪ Mass changes

▪ KPIs, daily controls, etc.

The implementation of this solution is simple as it requires adjustments and little or no configuration. It is often done first by a consultant and then handed over to key users for adjustments.

It could sometimes avoid MES integration, avoid or simplify bespoke transactions or reports with BADI.

**Process**

Call the transaction COHV or COOIS*![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-13_212057.png)*

Define a selection variant which will become the access to the cockpit.

In the initial screen, select the different screens to be displayed. You must choose the value "List of Objects" in the "List" drop-down menu : this is the gateway to the cockpit !

*![](/legacyfs/online/storage/blog_attachments/2022/11/Object-Overview.png)*

This function brings up another tab : "Obj.Selection"

|
 Before selection |
 After selection |

|
 ![](/legacyfs/online/storage/blog_attachments/2022/11/Before-1.png) |
 ![](/legacyfs/online/storage/blog_attachments/2022/11/after-selection.png) |

Choose the sub-screens to display with a layout (for instance here the missing parts)

On the "Obj.Selection" tab select :

* object "items" with the value "0000000001" for instance

* object "components" with the value "/MISSPARTS" for the "Layout" field and the value "2" for the "item" field.

Nota Bene : The value of the field "ITEM" corresponds to the sub-screen (ALV Grid) number of the selected object which will be displayed on the result screen

*![](/legacyfs/online/storage/blog_attachments/2022/11/Miss-parts.png)*

On the "Selection" tab, enter values : for instance, the field "Production Plan", "Order Type" and System Status" (REL)

*![](/legacyfs/online/storage/blog_attachments/2022/11/selection-screen.png)*

Select the icon "Save as Variant…"

![](/legacyfs/online/storage/blog_attachments/2022/11/Variante.png)

Enter values for the fields "Variant Name" and "Description" then click on the save icon. This variant could be used as a cockpit selected by user or added to a transaction + variant

On the initial screen, click on the execute icon. The Cockpit is displayed.

* Define the “Navigation Profile”

*![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-13_212304.png)*

* Select the "Navigation Profile" icon and choose "Change Navigation Profile"

* To add a "transaction" icon, check the "application toolbar" box and click on the "new entry" icon then call a transaction

![](/legacyfs/online/storage/blog_attachments/2022/11/MIGO.png)

Fill in the values, in the example the Transaction MIGO and a value for the text that will be displayed on the icon. Finally, click on continue (or press enter)

The same method is used to insert a function call (add an icon Reread of Refresh in this example)

After inserting the transactions (routing, BOM, production version, Gantt) and functions (reread and refresh) save the navigation profile by clicking on the save icon. CO11N access is also used a lot. There are no limits and it is possible to add a navigation profile to each part. (production declaration, print Handling Unit, Quality information, etc.)

Here is the preview of a cockpit on COHV after adding a custom navigation profile

*![](/legacyfs/online/storage/blog_attachments/2022/11/2022-11-13_212434.png)*

**Conclusion**

COHV is very powerful with the cockpit (enabled by the function : object overview and navigation profile). I have implemented this solution several times and the feedbacks from clients and users are excellent : this solution is stable and scalable. Users no longer use transactions or the SAP menu: everything can be in this production cockpit, even most of the functionality of an MES. It is the best PP transaction !
It is even possible to start the cockpit directly by creating a transaction with a variant to avoid going through the selection screen. This is possible to use it with FIORI as well.

This post refers to the COOIS/COHV transaction. The same approach can be used for PP-PI with COOISPI/COHVPI.

After reading this blog post, you should now be able to create a production cockpit and propose this solution to your clients.

As an SAP User eXperience consultant, this post will be followed by other "killer app" transactions that should be more widely known given the excellent customer feedback

Thanks a lot for y...