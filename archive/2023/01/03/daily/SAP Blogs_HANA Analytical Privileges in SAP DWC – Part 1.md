---
title: HANA Analytical Privileges in SAP DWC – Part 1
url: https://blogs.sap.com/2023/01/02/hana-analytical-privileges-in-sap-dwc-part-1/
source: SAP Blogs
date: 2023-01-03
fetch_date: 2025-10-04T02:54:52.746779
---

# HANA Analytical Privileges in SAP DWC – Part 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* HANA Analytical Privileges in SAP DWC - Part 1

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161593&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [HANA Analytical Privileges in SAP DWC - Part 1](/t5/technology-blog-posts-by-sap/hana-analytical-privileges-in-sap-dwc-part-1/ba-p/13561255)

![olaf_fischer](https://avatars.profile.sap.com/a/e/idaed1a3dac7bbce276fff8e781a1b48900bc5de97effa9e2f5761008979986ec9_small.jpeg "olaf_fischer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[olaf\_fischer](https://community.sap.com/t5/user/viewprofilepage/user-id/214938)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161593)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161593)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561255)

‎2023 Jan 02
1:59 PM

[12
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161593/tab/all-users "Click here to see who gave kudos to this post.")

3,137

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

## Introduction

SAP DWC comes with build-in data access controls (DAC). They are used to enforce a row-level security and are fully integrated within SAP DWC. One example of integration is that a view persistence run is DAC-aware and ensures that the filtering properly works on the persisted result.

SAP HANA natively supports row-level security as well by offering analytical privileges. Compared to SAP DWC, they offer a different set of capabilities. Depending on your scenario, you might have specific interest in using some of these capabilities or re-use analytical privilege definitions you have created before.

This blog post sketches a configuration that allows you to use the native SAP HANA row-level security in the context of SAP DWC. Please note that these definitions are not surfaced to SAP DWC and hence are not integrated in the standard authorization concept.

The second part of the blog can be found here: [HANA Analytical Privileges in SAP DWC - Part 2](https://blogs.sap.com/2023/01/05/hana-analytical-privileges-in-sap-dwc-part-2/)

## Initial Scenario

As a starting point we assume the following configuration in SAP DWC: One space holds the data and exposes it via sharing to second space for external consumption.

With the view names we will use through the blog post, it reads like this:

We have one space named *Consumption* with a view exposing data for reporting, e.g. SAP SAC and we have a separate space *Inbound* hosting the data itself. Cross space sharing permits the *view\_CONSUMPTION* the access to *view\_DATA*.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-1.jpg)

## The Problem Statement

Without any row-level security in place, the filters of the data request are propagated directly via the consumption view to the data view. The direction of arrows follows the request direction.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-2.jpg)

What we need is a way to merge the filters from the SAC Story request with the filters, reflecting the authorizations of the current application user. The picture below illustrates this goal: the SAC filters and the authorization filter is merged into a new effective filter. This merged filter is sent to the data view. As a result, the use sees only the portion of data that fits to both filter definitions.

![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-3.jpg)

Please note that merging with the authorization filter should be done close or even better directly at the level of the consumption view – and not far below in the data layer. This avoids stacking of authorization definitions and in addition, allows all views below the consumption to benefit from the complete set of filters.

**Note:** I used the term “Story Filter”. This should refer to the effective set of filters that are found in the data requests to SAP DWC. Sometimes filters defined in the SAP SAC UI are not included in the requests to SAP DWC.

## Solution Concept

The solution described in the blog post uses the HANA Analytical Privileges to perform the merge. We extend our sample configuration with a HANA view (incl. Analytical Privileges) and re-route the requests to pass through this new entity.

**How to create a HANA view with Analytical Privileges**

Creating an open SQL user in the *Inbound* space creates a new schema on HANA with the name e.g., *Inbound#Filter*. Within this new schema the SQL user has sufficient permissions to create a view – and here is main trick – with analytical privileges!
![](/legacyfs/online/storage/blog_attachments/2023/01/Picture-4.jpg)

You can think of this HANA view to consist of two parts:

* An authorization filter definition describing the subset of data the application user can access

* A merging capability that combines the authorization filter with any filter used to select data. In our scenario this would merge the SAC Story filters with the authorization filter.

The picture illustrates the new request flow: The consumption view requests the data from the view *View\_DATA\_AP* (with analytical privileges). After merging of filters, the request is forwarded to the view *View\_DATA* (without analytical privileges).

## Solution – Step-by-Step

After we understood the overall concept, we can start with the real implementation. As you might expect there are several little details we have to consider. If you feel lost in the details – please go back to the overview, go back on track and then again continue with the step-by-step.

We start in creating all relevant entities without the analytical privileges. After testing the data flow and configuration we enable the analytical privileges.

### Prepare Space *Inbound* and Test Data

The sample will use the following company data you can download here:
[https://github.com/SAP-samples/data-warehouse-cloud-content/blob/main/Sample\_Bikes\_Sales\_content/CSV...](https://github.com/SAP-samples/data-warehouse-cloud-content/blob/main/Sample_Bikes_Sales_content/CSV/Products.csv)

**Space Configuration**

1. Create a space *Inbound*

2. Create an open SQL user with name „filter“ and assign read/write privileges and the grant option

3. Create an Analysis User. We will need it later for testing and to determine the list of technical users we need to grant access.

**View with Test Data**

1. Upload the test data into a table named DATA

2. Create a view *View\_DATA* with a 1:1 mapping of all columns.

3. Expose the view *View\_DATA* for consumption. Via this option you allow all open SQL user of the space *Inbound* to access the data.

Note: The view with the test data is not shared with the consumption space. We don’t want to expose unprotected data.

### Get List of Techn...