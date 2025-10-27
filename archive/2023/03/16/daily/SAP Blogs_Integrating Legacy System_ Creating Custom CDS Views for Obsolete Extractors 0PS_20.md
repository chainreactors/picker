---
title: Integrating Legacy System: Creating Custom CDS Views for Obsolete Extractors 0PS_20
url: https://blogs.sap.com/2023/03/15/integrating-legacy-system-creating-custom-cds-views-for-obsolete-extractors-0ps_20/
source: SAP Blogs
date: 2023-03-16
fetch_date: 2025-10-04T09:44:17.364159
---

# Integrating Legacy System: Creating Custom CDS Views for Obsolete Extractors 0PS_20

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Integrating Legacy System: Creating Custom CDS Vie...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163586&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrating Legacy System: Creating Custom CDS Views for Obsolete Extractors 0PS\_20](/t5/technology-blog-posts-by-members/integrating-legacy-system-creating-custom-cds-views-for-obsolete-extractors/ba-p/13570914)

![abhilekhsharma57](https://avatars.profile.sap.com/4/e/id4e8889ff4629156938fba773be450640ddf4def16c07936fba144ecc5b6a3286_small.jpeg "abhilekhsharma57")

[abhilekhsharma57](https://community.sap.com/t5/user/viewprofilepage/user-id/124089)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163586)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163586)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570914)

‎2023 Mar 15
8:31 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163586/tab/all-users "Click here to see who gave kudos to this post.")

2,371

* SAP Managed Tags
* [BW (SAP Business Warehouse)](https://community.sap.com/t5/c-khhcw49343/BW%2520%28SAP%2520Business%2520Warehouse%29/pd-p/242586194391178517100436979900901)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [BW Content and Extractors](https://community.sap.com/t5/c-khhcw49343/BW%2520Content%2520and%2520Extractors/pd-p/144344546671011469492893748922901)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [BW (SAP Business Warehouse)

  Software Product Function](/t5/c-khhcw49343/BW%2B%252528SAP%2BBusiness%2BWarehouse%252529/pd-p/242586194391178517100436979900901)
* [BW Content and Extractors

  Software Product Function](/t5/c-khhcw49343/BW%2BContent%2Band%2BExtractors/pd-p/144344546671011469492893748922901)

View products (3)

### **Overview**

The problem of an obsolete extractor in an SAP system refers to the challenge of accessing data from a legacy system that is no longer supported or compatible with the latest version of the SAP system. This can impact decision-making, reporting, and analysis, and lead to data integrity issues. The solution is to check if SAP has provided the Standard CDS view for the obsolete extractor. If not, create a custom CDS view to map the data from the legacy system to the new SAP system using the CDS view, enabling the data to be extracted and used for reporting, analysis, and decision-making purposes.

### **SAP ECC vs SAP S4HANA**

SAP ERP Central Component (SAP ECC) is **an on-premises enterprise resource planning (ERP) system** used by many organizations worldwide. However, with the increasing demand for modern and agile system, SAP has launched it’s next generation ERP system, SAP S4/HANA.

S/4HANA was designed **to make ERP more modern, faster and easier to use through a simplified data model.**

A brownfield approach to conversion allows organizations to migrate from SAP ECC to S/4HANA by **converting their existing SAP environment without reimplementation or disruption to existing business processes.**

While migration some challenged are faced, one of them is obsolescence of extractors in SAP. If  SAP hasn't provided the standard CDS view for the extractor, it is recommended to build a Custom CDS view for that obsolete extractor in the S4/HANA system.

**Extractors** are important components of the SAP landscape that are required to extract data from the system and make it available for further processing. When an extractor becomes obsolete, it becomes challenging to obtain the required data, which may lead in the conversion process.

### **Solution**

The First step towards this is to check if SAP has provided the Standard CDS view for the obsolete extractor. If yes than we can use that Standard CDS view directly in place of obsolete extractor. If a compatible standard extractor is available, it is recommended to use that extractor instead of creating a custom solution. This approach can help to minimize the time and effort required for data integration and ensure that the extracted data is compatible with the new system.

We can also use another standard CDS view to create a custom CDS view can be an effective approach for addressing the problem of an obsolete extractor in an SAP system. By identifying a standard CDS view in the new system that is similar to the data being extracted from the legacy system, organizations can save time and effort by leveraging the existing structure and content of the standard view. Analyzing the standard view can help to identify the relevant fields and data elements needed for the custom CDS view, which can then be modified as necessary to map the data from the legacy system to the new SAP system. Testing the custom CDS view is crucial to ensure that it is accurately extracting and mapping the data, and once validated, it can be published for use in reporting and analysis. This approach can simplify the process of integrating legacy systems with the new SAP system, while ensuring that the extracted data is compatible and usable for decision-making purposes.

**\*\*** However, if a compatible standard extractor is not available, the next approach is to create a custom **CDS** view for the obsolete extractor. This involves mapping the data from the legacy system to the new SAP system using the CDS view, enabling the data to be extracted and used for reporting, analysis, and decision-making purposes

Core Data Service (CDS) Views are **virtual data models of SAP HANA which allows direct access to underlying tables of the HANA database and streamlined view of complex data structure. We can use these custom CDS views to extract data from S4/HANA system.**

***The steps to create a CDS View for an obsolete BW extractor are as follows:***

**Step 1:** Identify the obsolete extractor: The first step is to identify the extractor that has become obsolete. This information can be obtained from the SAP notes and release information.

**2496759** - Restrictions for BW extractors relevant for S/4HANA in the area of Enterprise Portfolio and Project Management

@Analytics.dataExtraction.enabled - Using this annotation CDS view can be used in BW for extraction

**Step 2:** Analyze the obsolete extractor: The next step is to analyze the obsolete extractor to understand its data structures, field names, and data types. This information will be useful in creating the CDS View.

**Step 3:** Create a CDS View: Once the analysis of the obsolete extractor is complete, the next step is to create a CDS View in SAP S4/HANA. The CDS View can be created using the SAP HANA Studio (Eclipse)

For reference <https://blogs.sap.com/2019/10/22/part2.-create-a-basic-cds-view/>

IMPORTANT: If you’re Using this CDS view for the BW (Business warehouse), Then it’s necessary to include annotation

@Analytics.dataExtraction.enabled (after this CDS view can be used in BW for extraction)

**Step 4:** Map the fields: The next s...