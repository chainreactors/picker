---
title: How to suggest, create, and arrange the organizational structure using PPOM (Process and Organization Management).
url: https://blogs.sap.com/2023/03/15/how-to-suggest-create-and-arrange-the-organizational-structure-using-ppom-process-and-organization-management./
source: SAP Blogs
date: 2023-03-16
fetch_date: 2025-10-04T09:44:30.506478
---

# How to suggest, create, and arrange the organizational structure using PPOM (Process and Organization Management).

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* How to suggest, create, and arrange the organizati...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68553&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to suggest, create, and arrange the organizational structure using PPOM (Process and Organization Management).](/t5/enterprise-resource-planning-blog-posts-by-members/how-to-suggest-create-and-arrange-the-organizational-structure-using-ppom/ba-p/13570750)

![bour-rha](https://avatars.profile.sap.com/8/0/id80ba3671c2114139d3b710da18d83911e416899a1caed26ccaee976ceb104a52_small.jpeg "bour-rha")

[bour-rha](https://community.sap.com/t5/user/viewprofilepage/user-id/579242)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68553)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68553)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570750)

‎2023 Mar 15
7:13 PM

[1
Kudo](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68553/tab/all-users "Click here to see who gave kudos to this post.")

5,781

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (2)

**Overview**

The PPOM transaction is an SAP transaction that enables organizational object management. "Process and Organization Management".

This transaction allows users to create, modify, and display organizational objects such as organizational units, positions, employees, services, and teams.

It is often used by HR administrators to maintain and update the organizational structure of the company in the SAP system, By using the PPOM, users can assign positions to organizational units, assign employees to positions, create teams and services, and manage other aspects of the organizational structure.

![](/legacyfs/online/storage/blog_attachments/2023/03/Capture1.png)

Overall, PPOM is an essential tool for HR and organizational management in companies that use SAP.

Some advantages of using the PPOM for organizational management are:

1. **Integration with other SAP modules**: PPOM is integrated with other SAP modules, such as Personnel Administration (PA), Time Management (TM), and Payroll, which enables seamless data exchange between different modules.

2. **User-friendly interface**, which makes it easy for users to navigate and perform various organizational management tasks.

3. Allows administrators to **assign different roles to users**, restricting their access to certain organizational objects based on their job responsibilities.

4. **Maintains an audit trail** of all changes made to the organizational structure, enabling administrators to track who made the changes and when they were made.

5. **Allows users from different functional area**s, such as HR, finance, and operations, to collaborate on organizational management tasks, promoting cross-functional integration and teamwork.

6. By using PPOM to manage organizational objects, users can gain a **better understanding of the structure** of the company and how different departments and teams are organized.

**Configuration**

Before starting to code for a given client, it is important to analyze their needs and propose an appropriate solution.

It is necessary to check the HR module configuration and usage before proposing a solution, if there are external systems to retrieve data, or if the client prefers to use only flat files to set up the structure. In essence, a preliminary study is necessary to ensure that the proposed solution will meet the client's expectations and specific requirements.

To develop the PPOM structure effectively, the following options can be considered:

1. Use a specific program that can retrieve the necessary files in CSV or XLS format to create the PPOM structure in a single step. This can save time and effort in the development process.

2. Enable gradual tracking of changes in the structure by providing an option for updating the structure through a file. This can allow for easier maintenance and management of the structure over time, such as making deletions, updates, and insertions.

3. Expose web services to clients with external systems for live creation, modification, and deletion of the PPOM structure. This approach offers greater flexibility for the organization, as real-time updates can be made through external systems, without the need for manual intervention.

**The concept of dates is crucial for PPOM management.**

In general, it is recommended not to delete objects in a structure such as PPOM, but rather to limit them by date. This allows for a record of changes and previous versions of the structure, which can be useful for compliance, reporting, or reference for future decisions. Limiting objects by date can also help prevent accidental errors or data loss. However, each organization has its own policies and data management needs, so it is important to consider the specific requirements of the business when defining PPOM structure management practices.

![](/legacyfs/online/storage/blog_attachments/2023/03/Capture1-6.png)

Here are some important **BAPIs** to know for effective management of PPOM transactions:

**'RH\_OBJECT\_CREATE'** is used to create an organizational object. ( Create organizational units, positions, jobs, and other organizational objects in SAP…. )

To work effectively with the function module, it is important to understand the two main parameters: **current plan (plvar) and object types (otype)  .**

***Current plan (plvar)  :*** This plan includes all the organizational units, positions, jobs, and other related objects that are required to represent the structure of an organization in the system. The current plan is typically stored in a database table such as HRP1000 .

***Object types (otype) :*** To determine the object types to be created in SAP ABAP, you can analyze the organizational structure of the company and identify the different types of organizational units, such as departments, teams, positions, and job roles.

Another way to find information about the object types to be created in SAP ABAP is to access the **PP01** transaction and review the relevant fields. This can provide a comprehensive overview of the object types and their associated attributes, which can inform the creation process.![](/legacyfs/online/storage/blog_attachments/2023/03/Capture2.png)After creating the organizational objects, the next step is to link them.

To do this, we use the **'RH\_RELATION\_MAINTAIN'** function module. It enables the maintenance of relationships between organizational objects by creating, modifying, and deleting relationships a...