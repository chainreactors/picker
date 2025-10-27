---
title: Integration of SAP Service and Asset Manager (SAM) with SAP Field Service Management (FSM) using the FSM Cloud Connector (proaxia)
url: https://blogs.sap.com/2023/03/01/integration-of-sap-service-and-asset-manager-sam-with-sap-field-service-management-fsm-using-the-fsm-cloud-connector-proaxia/
source: SAP Blogs
date: 2023-03-02
fetch_date: 2025-10-04T08:26:27.782140
---

# Integration of SAP Service and Asset Manager (SAM) with SAP Field Service Management (FSM) using the FSM Cloud Connector (proaxia)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Integration of SAP Service and Asset Manager (SSAM...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51707&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integration of SAP Service and Asset Manager (SSAM) with SAP Field Service Management (FSM) using the FSM Cloud Connector (proaxia)](/t5/enterprise-resource-planning-blog-posts-by-sap/integration-of-sap-service-and-asset-manager-ssam-with-sap-field-service/ba-p/13559111)

![syam_yalamati](https://avatars.profile.sap.com/c/c/idcc75c6a419801c58526985c23e4bb5ed3a063d1988910ac4b956c1b066bff7b9_small.jpeg "syam_yalamati")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[syam\_yalamati](https://community.sap.com/t5/user/viewprofilepage/user-id/210415)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51707)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51707)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559111)

‎2023 Mar 01
11:28 PM

[20
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51707/tab/all-users "Click here to see who gave kudos to this post.")

10,992

* SAP Managed Tags
* [Mobile Application Integration Framework](https://community.sap.com/t5/c-khhcw49343/Mobile%2520Application%2520Integration%2520Framework/pd-p/6baf0d27-c212-4154-85a9-71ed13c7b1ab)
* [SAP Mobile Asset Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Asset%2520Management/pd-p/73554900100700001067)
* [SAP Service and Asset Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Service%2520and%2520Asset%2520Manager/pd-p/73555000100800000639)
* [Mobile](https://community.sap.com/t5/c-khhcw49343/Mobile/pd-p/246015353107843540080736084568477)
* [SAP Field Service Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Field%2520Service%2520Management/pd-p/73554900100700002181)

* [Mobile Application Integration Framework

  Software Product Function](/t5/c-khhcw49343/Mobile%2BApplication%2BIntegration%2BFramework/pd-p/6baf0d27-c212-4154-85a9-71ed13c7b1ab)
* [SAP Mobile Asset Management

  Software Product](/t5/c-khhcw49343/SAP%2BMobile%2BAsset%2BManagement/pd-p/73554900100700001067)
* [SAP Service and Asset Manager

  Software Product](/t5/c-khhcw49343/SAP%2BService%2Band%2BAsset%2BManager/pd-p/73555000100800000639)
* [Mobile

  Topic](/t5/c-khhcw49343/Mobile/pd-p/246015353107843540080736084568477)
* [SAP Field Service Management

  Software Product](/t5/c-khhcw49343/SAP%2BField%2BService%2BManagement/pd-p/73554900100700002181)

View products (5)

SAP Service and Asset Manager (SSAM) Mobile Application integrates with SAP Field Service Management (FSM) as part of Field Service Technician persona using Proaxia connector. This scenario talks about ECC or S/4HANA Customer Service use case only, if you are looking for S/4HANA Service use case then please refer to my other blog: [Integration of SAP Service and Asset Manager(SSAM) with SAP FSM to support S/4HANA Service Processes](https://community.sap.com/t5/enterprise-resource-planning-blogs-by-sap/integration-of-sap-service-and-asset-manager-ssam-with-sap-fsm-to-support-s/ba-p/13632967).

SAP SAM is now integrated with SAP FSM planning board and show the current status of orders and tracks technician’s location to facilitate scheduling and dispatching. As part of this Integration, SAP SSAM also supports FSM Smartforms and allows the SAM mobile application to download, modify and upload FSM Smartforms assigned to an activity/operation.

![](/legacyfs/online/storage/blog_attachments/2023/03/SSAM-FSM-Integration-Flow.png)Process flow for SAP SAM Integration with SAP FSM

SAP SAM integrated directly with SAP FSM using the Service and Data APIs provided by SAP FSM. However, the underlying objects that need to be updated, (e.g. Service Orders (Service Calls in FSM), Operations (Activities in FSM), Employees (Persons in FSM) are created by the Proaxia connector. Therefore, the following pre-requisites must be implemented for the end-to-end scenarios to work.

## Prerequisites:

To execute the supported integration scenarios between SSAM and SAP FSM, the following prerequisites must be met and assuming that the Proaxia FSM connector will be configured and set up to replicate the data between the SAP backend and SAP FSM system.

* Proaxia FSM connector is configured and set-up to replicate data b/w SAP & FSM system

+ Enable 'External Id' flag under FSM connector Company definition section.

+ Implement BAdi methods to provide ID mapping between SAM & FSM.

## Implementation Details:

The following sections will explain the details on how to implement these prerequisites.

Make sure Proaxia FSM connector is configured and set-up in your environment to replicate data b/w SAP & FSM system. For more details about Proaxia connector, refer to the following documentation:

1. ECC CS/S4HANA CS integration <https://help.sap.com/viewer/fsm_integration/Cloud/en-US/ecc-cs-s4hana-cs-integration.html>
2. Integration overview [https://help.sap.com/docs/SAP\_FIELD\_SERVICE\_MANAGEMENT/fsm\_integration\_overview/integration-overview...](https://help.sap.com/docs/SAP_FIELD_SERVICE_MANAGEMENT/fsm_integration_overview/integration-overview.html?locale=en-US)
3. Cloud Connector documentation<https://proaxia-prod-doc.atlassian.net/wiki/spaces/PFCC/overview?homepageId=6029402>

### Enable 'External Id' flag under FSM connector Company definition settings

From SAP backend system, use menu option of FSM Connector, Customizing --> Objects --> Company --> Company Definition (Transaction Code: /PACG/ECM\_COMP).

![](/legacyfs/online/storage/blog_attachments/2023/02/FSM_Connector_Company_Def.png)

FSM Connector Company Definition

By enabling the External Id flag, you can switch on sending the External Id from the FSM connector to FSM.

![](/legacyfs/online/storage/blog_attachments/2023/02/Enable-External-Id-from-FSM-Connector-settings.png)

Enable External Id from FSM Connector settings

### Implement BAdi methods to provide ID mapping between SSAM & FSM:

Mobile Application Integration Framework (MAIF), which supports SAM backend integration features, provides different BAdi options to determine cross-referencing of key fields between FSM Connector and FSM Cloud system. The Badi /MERP/CA\_FSM\_CROSSREF\_BADI is delivered for both ERP & S/4HANA system to support this feature with following interface methods.

![](/legacyfs/online/storage/blog_attachments/2023/02/FSM_BADI_Interface.png)

BAdi Interface for FSM Id mapping

The following code samples are an example, you may need to make additional adjustments for your environment.

* Add local method GET\_COMPID to determine the FSM company Id. This method required for the GET\_EMPLOYEE\_IDS BADI method in Step2. This method returns the following data:

  **Import Parameter:**  iv\_account TYPE /pacg/ecm\_cloudaccount.                                            **Return Parameter:** rv\_compi...