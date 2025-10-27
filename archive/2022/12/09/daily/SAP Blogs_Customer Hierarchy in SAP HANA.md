---
title: Customer Hierarchy in SAP HANA
url: https://blogs.sap.com/2022/12/08/customer-hierarchy-in-sap-hana/
source: SAP Blogs
date: 2022-12-09
fetch_date: 2025-10-04T00:59:59.694312
---

# Customer Hierarchy in SAP HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Customer Hierarchy in SAP HANA

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68561&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Customer Hierarchy in SAP HANA](/t5/enterprise-resource-planning-blog-posts-by-members/customer-hierarchy-in-sap-hana/ba-p/13570980)

![ashisK](https://avatars.profile.sap.com/9/c/id9c2af9a71d85ed3d678f672d165b5eda2d6ec2e2c74783cd2992ba63bd85ca6f_small.jpeg "ashisK")

[ashisK](https://community.sap.com/t5/user/viewprofilepage/user-id/45763)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68561)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68561)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13570980)

‎2022 Dec 08
7:00 PM

[14
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68561/tab/all-users "Click here to see who gave kudos to this post.")

59,163

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sales](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)
* [SD (Sales and Distribution)](https://community.sap.com/t5/c-khhcw49343/SD%2520%28Sales%2520and%2520Distribution%29/pd-p/209057551571413566377230676804921)

* [SD (Sales and Distribution)

  Software Product Function](/t5/c-khhcw49343/SD%2B%252528Sales%2Band%2BDistribution%252529/pd-p/209057551571413566377230676804921)
* [SAP S/4HANA Cloud Public Edition Sales

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSales/pd-p/3ea305d0-7b1c-4ac1-ba66-d1181cec07e0)

View products (2)

# **1.** **Introduction**

## **1.1** Objectives

The purpose of this document is to provide extensive understanding of Customer Hierarchy Solution in S4 and its usage in various business processes.

## **1.2** High Level Understanding

Customer hierarchies are used when a customer has a complex chain or organizational structure in which all or some of the parts of this structure will benefit from an agreement made for the customer’s company as a whole.

For example, a large customer may have dependent offices, each responsible for their own purchasing, and as individuals, they would not benefit from a global pricing scheme. However, as part of a customer’s hierarchy, they would still benefit from being associated with the larger parent company.

## **1.3** Why and when to use Customer Hierarchy

* Before setting out and maintaining a customer hierarchy, we would need to determine the requirement for the hierarchy. If the requirement is a report, such as reporting bookings or billings for global customers within a hierarchy, this can be done using a standard reporting hierarchy within the sales information system.

* If the requirement is merely to offer prices according to a specific group, one could think about using a customer group on the customer master record, rather than a customer hierarchy.

* If, on the other hand, business wants to have a customer hierarchy to offer special price agreements or rebates across a customer’s organization on a global level, which may not be covered by a standard grouping, this can be covered by using the customer hierarchy.

* The customer hierarchy integrates and relies on the partner determination in conjunction with the customer hierarchy settings to promote the linking between the customers. The partner determination causes the customer hierarchy to be represented in the sales document.

* The customer hierarchy is a hierarchical organizational structure that consists of higher and lower-level nodes. Each node is assigned within the structure to form a graphical diagram of the customer’s organization.

# **2.** **Maintain Customer Hierarchy**

## **2.1** Prerequisite Steps:

* **Create Customer Master Records:**

Make sure that customers (Sold to Party) are created in the system using **BP** TCode.

* **Create Customer Hierarchy Node**

Hierarchy Nodes can be created as customer masters using **BP** TCode, and like any other customer master, the hierarchy node is defined also on sales area level. The following fields are mandatory in customer hierarchy node master data:

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-1.png)

## **2.2** Building the Customer Hierarchy Structure (TCode: VDH1N)

**VDH1N** transaction code is used in S4 to create customer hierarchy structure.

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-2.png)

Maintenance of customer hierarchy in S4 comprises below processes:

1. Create new hierarchy structure.

2. Add new node/customer to an existing hierarchy structure

3. Change validity period of existing hierarchy assignment

4. Reassign node/customer from an existing hierarchy structure

5. Remove node/customer from an existing hierarchy structure

Steps/Governance to be followed for each business processes are mentioned below:

### **2.2.1** **Process variant 1 – Create new Hierarchy structure**

As per the business need, customer hierarchy structure can be created either Single Level or Multilevel. Prices (net price/discount) and CMIR can be maintained at any level hierarchy node, accordingly, the lower-level end customers will inherit all the prices and CMIR from the higher-level node.

***Business Governance***

1. A request for a new Hierarchy assignment is issued containing the business reasoning.

2. Business validation and approval or rejection is given from relevant managers.

***Operational Governance***

1. Once the hierarchy nodes are created in MDG, hierarchy structure can be built in S4 using “Create Assignment” functionality in VDH1N transaction code.

2. As required by business scenario, Higher level node number and lower-level node/customer number along with Sales Org., Distribution Channel and Division needs to be provided to create a new hierarchy assignment.

3. Validity period needs to be maintained for the newly created assignment. Once the validity period expires, system automatically deactivate the hierarchy assignment.

4. By using this Create Assignment functionality, multilevel hierarchy structure can be created for a specific lower-level end customer.

Click on the “Create Assignment” button (highlighted in red) to create a new hierarchy assignment.

![](/legacyfs/online/storage/blog_attachments/2022/12/Fig-3.png)

### **2.2.2** **Process variant 2 – Add new node/customer to an existing hierarchy structure**

After the customer hierarchy structure is built in S4, there might be a business need to add a new node/customer to that existing hierarchy structure. In such cases, Assign functionality should be used to add a new node/customer to the existing hierarchy structure.

***Business Governance***

1. A request for a new Hierarchy assignment of a new node/customer to an existing hierarchy structure is issued containing the business reasoning.

2. Business validation and approval or rejection is given from relevant managers.

***Operational Governance*...