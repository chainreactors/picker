---
title: Defect Corrections for Work Packages Card and Detail Analytical List Page
url: https://blogs.sap.com/2023/07/31/defect-corrections-for-work-packages-card-and-detail-analytical-list-page/
source: SAP Blogs
date: 2023-08-01
fetch_date: 2025-10-06T16:59:58.888243
---

# Defect Corrections for Work Packages Card and Detail Analytical List Page

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Defect Corrections for Work Packages Card and Deta...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/165223&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Defect Corrections for Work Packages Card and Detail Analytical List Page](/t5/technology-blog-posts-by-sap/defect-corrections-for-work-packages-card-and-detail-analytical-list-page/ba-p/13571805)

![krithika_shankaranarayan](https://avatars.profile.sap.com/d/e/idde6f8d254071f5f27cc4c69f8fe3e2471c971347d1a5583227885d0ca90d1631_small.jpeg "krithika_shankaranarayan")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[krithika\_shankaranarayan](https://community.sap.com/t5/user/viewprofilepage/user-id/230474)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=165223)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/165223)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571805)

‎2023 Jul 31
9:41 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/165223/tab/all-users "Click here to see who gave kudos to this post.")

957

* SAP Managed Tags
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)

View products (2)

## **Introduction**

This blog is part of the blogs series for the new Solution readiness dashboard delivered as part of Focused Build SP12 delivery. In this blog, we will get an overview of the Defect Corrections for Work Packages Card and the corresponding details for analyzing the card via Analytical List Page.

## **Pre-requisite**

Please go through the following blogs:

[Initial Set up and Pre-requisites](https://blogs.sap.com/2023/07/25/solution-readiness-dashboard-initial-set-up-and-pre-requisites/)

[What is Solution Readiness Dashboard and Brief Overview on Cards](https://blogs.sap.com/2023/07/25/understanding-the-new-solution-readiness-dashboard/)

## **Defect Corrections for Work Packages Card**

In this card, we can see the Defect corrections for work packages that have been assigned to the selected project. The following categories of defect corrections are displayed in this card i.e, Completed, To be done, Withdrawn, Overdue. Hover on the bar to get the corresponding number of defect corrections in each category.

**Completed –** Defect Corrections which have the status as Confirmed or Handed Over to Release.

**To be done –** Defect Corrections which have one of the following statuses Created, Being Corrected, Information Required, To be Retested w/o Transport, Transport to Retesting, In delivery and Due Date is in the Future

**Withdrawn –** Defect Corrections which have the status withdrawn.

**Overdue** – Defect Corrections which have the related Work package Due Date (SFT Due Date) in past.

![](/legacyfs/online/storage/blog_attachments/2023/07/Defect-Corrections-for-Work-Packages.png)

Defect Corrections for Work Packages

**Navigation to Defect Correction Details:** Header of the card has navigation enabled to the Defect Correction Detail page.

## **Defect Correction Details Analytical List Page**

This provides a better insight for analyzing the defect corrections in detail. It provides a visual representation of the chart and table.

Please refer to the [Smart Chart](https://experience.sap.com/fiori-design-web/smart-chart/) and [Smart Table](https://experience.sap.com/fiori-design-web/smart-table/) documentation to understand in detail how these controls behave.

For the general features, refer to the following section in Requirement blog. [Link to be provided after publishing].

The filters are carried forward from the overview pages and if required, users can also apply their own filters on the below fields available in the Adapt Filter section.

![](/legacyfs/online/storage/blog_attachments/2023/07/Select-Filters_DC.png)

Select Filters

For example, user can choose Priority field here for filtering and then view the High priority Defect Corrections for which the user has to click on **Go** button to further reflect these changes for analysing on the chart or table view.

![](/legacyfs/online/storage/blog_attachments/2023/07/Defect-Correction-Details.png)

Defect Correction Details

Users can navigate further to **My Defect Corrections** application, by clicking on Defect Correction Id field in the Table view to get more insights into the details of the defect corrections.

By choosing multiple defect corrections, users can also navigation to Mass change application with the corresponding defect corrections chosen for further performing an action on the list of defect corrections. For example, as a user I would like the defect corrections which are Low to be prioritized to High then I would perform the action in Mass Change application and then by triggering an refresh in the overview page and again analyzing the Defect Correction Details I see that my changes are reflected are immediately for the user.

### **Chart Configurations**

|
 **Default Dimensions** |
 Priority |

|
 **Default Measures** |
 Number of Defect Corrections |

|
 **Default Chart Type** |
 Stacked Bar Chart |

|
 **Default Sort** |
 Defect Correction ID (Descending Order) |

### **Table Configurations**

|
 **Default Columns** |
 Defect Correction ID, Title, Status, Priority, Category, Work Package Id, Wave, Effort in PDA, Current Processor, Architect, Developer, Tester, Due Date, |

|
 **Sort** |
 Defect Correction ID (Descending Order) |

|
 **Group** |
 None |

###

## **Key Takeaways**

* Detail pages have a filter bar, a chart, and a table view.

* The content of chart and table is based on selections made in filter bar.

* The default chart and table configurations can also be adjusted by user as per their need.

* More filtering options can be added by using the “Adapt Filter” feature.

* Users can create and save views using the variant management feature of the dashboard.

Please feel free to provide feedback either directly here in the comment section or, in case of questions, you can submit them [here](https://answers.sap.com/tags/bd524d9b-1ee4-452d-a5b4-c25520976179). You are also encouraged to follow SAP Solution Manager tag [here](https://answers.sap.com/tags/01200615320800000636) and Focused Build for SAP Solution Manager tag [here](https://answers.sap.com/tags/bd524d9b-1ee4-452d-a5b4-c25520976179).

## **Important Links and Resources**

* [Usage Rights](https://support.sap.com/en/alm/usage-rights.html)

* [SP12 de...