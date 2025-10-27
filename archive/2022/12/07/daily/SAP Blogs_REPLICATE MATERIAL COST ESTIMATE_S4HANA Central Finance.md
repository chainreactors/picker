---
title: REPLICATE MATERIAL COST ESTIMATE_S4HANA Central Finance
url: https://blogs.sap.com/2022/12/06/replicate-material-cost-estimate_s4hana-central-finance/
source: SAP Blogs
date: 2022-12-07
fetch_date: 2025-10-04T00:40:08.357747
---

# REPLICATE MATERIAL COST ESTIMATE_S4HANA Central Finance

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* REPLICATE MATERIAL COST ESTIMATE\_S4HANA Central Fi...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68350&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [REPLICATE MATERIAL COST ESTIMATE\_S4HANA Central Finance](/t5/enterprise-resource-planning-blog-posts-by-members/replicate-material-cost-estimate-s4hana-central-finance/ba-p/13566921)

![jayanthmaydipalle](https://avatars.profile.sap.com/3/9/id39f2f01628b9e7878057186eeb6e72b348c4e916ea74b98293d0289bd9b83149_small.jpeg "jayanthmaydipalle")

[jayanthmaydipalle](https://community.sap.com/t5/user/viewprofilepage/user-id/223472)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68350)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68350)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566921)

‎2022 Dec 06
10:39 PM

[8
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68350/tab/all-users "Click here to see who gave kudos to this post.")

4,255

* SAP Managed Tags
* [SAP ERP](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP/pd-p/01200615320800000659)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Finance/pd-p/67837800100800006927)
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)

* [SAP ERP

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP/pd-p/01200615320800000659)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Finance

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BFinance/pd-p/67837800100800006927)
* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)

View products (4)

Product Costing is the tool used in SAP for planning costs and establishing material prices. It helps in estimating the Cost of goods sold for each product unit. Product Cost planning involves planning the costs for materials without reference to orders and set prices for materials and other cost accounting objects. It consists of creation of material cost estimates and transferring the results of material cost estimates to the material master.

Inventory Valuation is also a part of Product Costing and allows to valuate stocks of a material either together or separately, that is, according to different valuation criteria. Should this be expanded to include Inventory valuation.

Product Costing does not run in the Central Finance System. All the Product Costing relevant scenarios are maintained in the Source System and then replicated to cFIN System. Only exceptional objects could be maintained centrally in cFIN System and distributed to the Source, for example: Activity Rates planning. Data replicated from the source to the target system helps to enable comprehensive analysis of the financial data to attain Managerial Accounting requirements.

Material cost estimates function enables you to cost out your finished and semi finished materials and update the material master data with the calculated costs. Customers with distributed source systems require centralized cost estimate information to get a consolidated value chain across different company codes / plants. ![](/legacyfs/online/storage/blog_attachments/2022/12/101.jpg)

### **INITIAL LOAD OF MATERIAL COST ESTIMATES**

You can perform an initial load of material cost estimates to transfer material cost estimates from a source system to the Central Finance system, such as loading material cost estimates from periods prior to the start date of ongoing replication.

The initial load of material cost estimates is carried out using the SAP Landscape Transformation Replication Server (SLT).

The initial load has the same restriction and uses the same AIF interface as material cost estimate ongoing replication.

The material cost estimates to be transferred are validated against the transfer rules.

Note: Please specify the data scope of initial load via transaction LTRS in the SLT system before carrying out the initial load. If not, all the relevant material cost estimates in the source system will be transferred in the initial load process.

Define the initial load object in SLT using the predefined initial load object CFI\_KEKO\_L.

After the initial load of material cost estimates has been started in SLT, the data is transferred from the source system to the Central Finance system and validated against the transfer rules. The final processing result is shown in SAP Application Interface Framework (AIF), under namespace /FINCF, interface CE\_MAT.

![](/legacyfs/online/storage/blog_attachments/2022/12/103.jpg)

Goto **SE38**, start program IUUC\_REPL\_PREDEF\_OBJECTS.

Add above mentioned Initial load object (**CFI\_KEKO\_L**) and replication object (**CFI\_KEKO\_R**) by clicking on “Copy predefined object” in below mentioned screen.

![](/legacyfs/online/storage/blog_attachments/2022/12/104.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/105.jpg)

### **ONGOING REPLICATION OF MATERIAL COST ESTIMATES**

Product costing in CFIN refers to replicating the cost estimate from source systems to one centralized system in real time. Product costing with CFIN helps display cost estimates with group evaluation and the cost of the whole value chain can be analyzed in one centralized system.

Ongoing replication of Material cost estimates helps you to continuously replicate material cost estimates from source systems to the Central Finance system. For a mixed costing, the material cost estimates are replicated together with the relevant procurement alternatives.

![](/legacyfs/online/storage/blog_attachments/2022/12/102.jpg)

**Configuration in SAP S4 Central Finance system:**

![](/legacyfs/online/storage/blog_attachments/2022/12/106-2.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/107.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/108.jpg)

**DEFINE RULE FOR COST ESTIMATE REPLICATION**

You can define rules for replicating cost estimates from a source system to the Central Finance system. During ongoing replication all cost estimates from a source system will be validated against the rules you define here.

* Only correctly validated cost estimates are transferred from the source system to the Central Finance system.

* If no rules for cost estimates are defined here, then no cost estimates are transferred to the Central Finance system.

In the **header section**, you specify the following for replicating cost estimates:

* Logical System: Enter the logical system of the source system from which the cost estimates are transferred.

* Reference Object: Select the type of cost estimate that is transferred, for example 0 for Material Cost Estimate.

* Controlling Area: Enter the controlling area for the cost estimates that are ...