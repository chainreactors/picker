---
title: Handle High Frequency Inbound Processing into SAP BW/4HANA System
url: https://blogs.sap.com/2023/03/07/handle-high-frequency-inbound-processing-into-sap-bw-4hana-system/
source: SAP Blogs
date: 2023-03-08
fetch_date: 2025-10-04T08:54:43.547705
---

# Handle High Frequency Inbound Processing into SAP BW/4HANA System

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Handle High Frequency Inbound Processing into SAP ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162401&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Handle High Frequency Inbound Processing into SAP BW/4HANA System](/t5/technology-blog-posts-by-sap/handle-high-frequency-inbound-processing-into-sap-bw-4hana-system/ba-p/13563739)

![Shuuka](https://avatars.profile.sap.com/3/3/id33e466443c9d2eb3d1100fa38cd4493213266fcc7ccadb21a5f359f71ea8b53f_small.jpeg "Shuuka")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Shuuka](https://community.sap.com/t5/user/viewprofilepage/user-id/41294)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162401)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162401)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563739)

‎2023 Mar 07
11:32 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162401/tab/all-users "Click here to see who gave kudos to this post.")

2,759

* SAP Managed Tags
* [SAP BW/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520BW%252F4HANA/pd-p/73554900100800000681)
* [BW Data Staging (WHM)](https://community.sap.com/t5/c-khhcw49343/BW%2520Data%2520Staging%2520%28WHM%29/pd-p/251465054721004088619393026581734)

* [SAP BW/4HANA

  SAP BW/4HANA](/t5/c-khhcw49343/SAP%2BBW%25252F4HANA/pd-p/73554900100800000681)
* [BW Data Staging (WHM)

  Software Product Function](/t5/c-khhcw49343/BW%2BData%2BStaging%2B%252528WHM%252529/pd-p/251465054721004088619393026581734)

View products (2)

## Background Information

With the migration to SAP BW/4HANA, source system of type “Web Service” is not available. And here comes a new capability “Write Interface” for DataStore Objects allowing to push data into inbound queue tables of Staging DataStore Objects and Standard DataStore Objects, replacing the push capability of PSA tables of DataSources of Web Service Source Systems. See SAP Note [2441826 - BW4SL & BWbridgeSL - Web Service Source Systems](https://launchpad.support.sap.com/#/notes/2441826).

There are two loading scenarios supported via the Write Interface:

1. For every call, a new internal request is opened ("One-step"), i.e., BW opens and closes an RSPM Request internally around the transferred records.

2. The external system administrates the RSPM Request explicitly and sends Data Packages into this Request ("Write into Request"), i.e., the external system opens the RSPM Request, n times sends data (with information on request and package) and closes it.

For systems that have new data coming in a low frequency, you can use the “One-step” procedure. Each time, when a set of new data records come, they are sent to the BW system and an RSPM request is generated.

For systems that have new data coming in a high frequency (with a low volume), you can use the “Write into Request” procedure, first open an RSPM request, and each time whenever new data comes, send data with the corresponding request and package, and close the request at the end.

“Write into Request” requires the external system to administrate the RSPM request and know how to package the data records. However, if you are in a situation where there is high-frequency and low-volume data, but the external system does not have the capability to handle RSPM requests and has to use “One-step” data sending, where each call creates a new RSPM Request. This will result in too many RSPM requests generated in a short period. Please note that generally, a large number of RSPM requests (several thousands of Requests in the same Datastore Objects) require the execution of the RSPM housekeeping to avoid further performance issues.

To avoid this performance limitation which is caused by many RSPM requests generated by “One-step” data sending you may consider having an alternative object where you can write data and use it for the temporary storage of data and load the needed data from this object via DataSource.

## ODP CDS DataSource based on ABAP CDS View

In this case, we would need to create an ABAP CDS view, and first, accept the high-frequency incoming data here (in the underlying table), then generate an ODP CDS DataSource based on this ABAP CDS view and load data from the DataSource with the custom frequency. In this way, you can avoid having too many RSPM requests generated in a short period for the target ADSO. Also, the process chain which loads data from the ABAP CDS view can be run with frequency according to the business requirements. For example, hourly.

The ABAP CDS view and the DataSource are acting like an extra inbound table (without request generated) for this ADSO. So, instead of directly writing data into the target ADSO, the system first writes data to the underlying table of the ABAP CDS view and the BW system loads data from the ODP which represents the ABAP CDS view.

![](/legacyfs/online/storage/blog_attachments/2023/03/P01.png)

Basically, the procedure would look like below:

1. **Create a database table.** All the fields (except the technical fields like REQTSN, DATAPAKID, RECORD, and RECORDMODE) are just copied from the inbound table of the target ADSO. Besides that, we add 2 fields, one as a key field and another for the delta mechanism. In the below example, “RECORD\_ID” is used as a key field, and “DELTA\_TIMESTAMP” is used for the delta mechanism.

2. **Create an ABAP CDS view.** Still not so much effort here. By using a CDS view, you can easily configure the delta mechanism as well as other custom settings you would like to have by various annotations. In the example, it is using the generic delta extraction annotation Analytics.dataExtraction.delta.byElement.name.

Then, all other modules are much easier. Since we are using exactly the same fields as in the target ADSO, the fields in the DataSource are auto-detected from the ABAP CDS view, and mappings in the transformation between DataSource and target ADSO are auto-generated with a direct assignment.

3. **Create ODP CDS DataSource.** Since the data extraction function is already configured in the ABAP CDS view, it is auto-released/exposed for ODP usage. So, you can easily create an ODP CDS DataSource based on the ABAP CDS view.

4. **Create transformation and DTP** between DataSource and target ADSO. As mentioned before, the fields in the ABAP CDS view are the same as fields in the target ADSO inbound table. The DataSource derived from it has the exact same fields as the target ADSO. As a result, the system will automatically map them in the transformation.

So far, this data flow is now available, and you can use it in your Process Chain.

In the example, we have a target ADSO named ADSO\_0004 and it has below key fields and non-key fields.

![](/legacyfs/online/storage/blog_attachments/2023/03/P02.png)

## 1. Enable Writing to Table and ABAP CDS View

### 1.1 Create a DDIC Structure with the Semantic Fields of the ADSO

These fields can be ...