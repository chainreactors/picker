---
title: Access Request Service Configuration in SAP IAG for Target SAP S4Hana Private Cloud
url: https://blogs.sap.com/2023/08/26/access-request-service-configuration-in-sap-iag-for-target-sap-s4hana-private-cloud/
source: SAP Blogs
date: 2023-08-27
fetch_date: 2025-10-04T11:59:16.243928
---

# Access Request Service Configuration in SAP IAG for Target SAP S4Hana Private Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Access Request Service Configuration in SAP IAG fo...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163901&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Access Request Service Configuration in SAP IAG for Target SAP S4Hana Private Cloud](/t5/technology-blog-posts-by-members/access-request-service-configuration-in-sap-iag-for-target-sap-s4hana/ba-p/13572459)

![amalakar46](https://avatars.profile.sap.com/d/9/idd9260b919d36dddb3ac9a86444fc911e6acfcbceb05dfd8a73e1a8be7900355a_small.jpeg "amalakar46")

[amalakar46](https://community.sap.com/t5/user/viewprofilepage/user-id/122984)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163901)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163901)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13572459)

‎2023 Aug 26
12:12 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163901/tab/all-users "Click here to see who gave kudos to this post.")

11,460

* SAP Managed Tags
* [SAP Cloud Identity Access Governance](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Access%2520Governance/pd-p/73555000100800000334)

* [SAP Cloud Identity Access Governance

  SAP Cloud Identity Access Governance](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BAccess%2BGovernance/pd-p/73555000100800000334)

View products (1)

SAP Cloud Identity Access Governance (often referred to as SAP IAG) is a cloud service from SAP Business Technology Platform (BTP). It offers similar functionality as SAP Access Control (SAP GRC).

SAP Cloud Identity Access Governance offers Software as a Service (SaaS), which enables companies to comprise several distinct identity management and access governance capabilities .

SAP Cloud IAG offers five core services:

* Access Analysis

* Role Design

* Access Request

* Access Certification

* Privileged Access Management

In this Blog I will explain how Access Request Service is configured in SAP Identity access and governance and SAP user access request can be raised for SAP S4Hana Private Cloud.

Make Sure SAP IAS (Identity Authentication Service) and IPS (Identity Provision Service) initial setup has been completed.

Below are the steps for configuring the Access Request Service: -

1. S4Hana Private Cloud System integration with SAP IAG.

2. Responsibilities are defined with proper Authorizaiton

3. IPS Proxy System is enabled between SAP IAG and SAP IAS.

4. Workflow Setup

5. Business Rules Activation and deploy.

6. Upload Notification template.

7. Access Request Priority are maintained.

8. Access Request Reason codes are maintained.

**Architecture Overview**

![](/legacyfs/online/storage/blog_attachments/2023/08/Achitecture-1.png)

1.**S4Hana Private Cloud System integration with SAP IAG.**

For integration, please perform below steps: -

1. Cloud Connector Setup. Like S4Hana On Premise – S4Hana Private cloud will connect SAP Cloud Identity Access Governance through the Cloud Connector.

2. Create Destination for the S4Hana Private Cloud System in the SAP Cloud Identity Access Governance Subaccount

3. Create an Application Instance for SAP S4Hana Private Cloud System in SAP Cloud Identity Access Governance Fiori Launchpad.

After above configuration Run Repository Sync to sync all relevant data from the SAP S4Hana private cloud target system to SAP Cloud Identity Access Governance, which can be applied in access request service.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture2-29.png)

in SAP IAG , for S4hana Private Cloud system – Application Type will be “S4Hana on – Premise”.

2. **Responsibilities are defined with proper Authorizaiton.**

Predefined role collections are deployed with the SAP Cloud Identity Access Governance service. These role collections ensure that users can access and use specific apps that are relevant for their job function and their dedicated tasks.

Role collections are not directly assigned to users in the SAP BTP cockpit. Instead, users in Identity Authentication (IAS) are assigned to groups. These groups are mapped with SAP BTP role collections.

The required steps are the following:

1. Create user groups in Identity Authentication and assign users to them.

2. Map role collections in the SAP BTP Cockpit to the created user groups.

3. Synchronize user groups information between the Identity Authentication and SAP Cloud Identity Access Governance subaccount.

The following groups are required in SAP IAS. The SAP Cloud Identity Access Governance services look for these specific groups. Make sure you create them with the names listed below with the same case. The name is case sensitive.

When you create these groups, you must follow this naming convention: IAG\_<TYPE>\_<NAME>

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture3-25.png)

Role collection in BTP is mapped with these groups for proper authorization in Identity authentication Tenant. Before that Set Identity Authentication as a trusted identity provider.

To ensure user groups information is synchronized between the Identity Authentication service tenant and the tenant for SAP Cloud Identity Access Governance on SAP Business Technology Platform (SAP BTP), you must maintain the required system in Identity Authentication and the destination in the tenant for SAP Cloud Identity Access Governance in SAP BTP and then run the SCI User Group Sync job in the Job Scheduler app.

3. **IPS Proxy is enabled between SAP IAG and SAP IAS.**

To Create an access request for a new user id in target application, user should be present in SAP IAG user source. We have made SAP IAS as user source, for this we must create a proxy system and map that proxy system in SAP IAG.

1. Map Proxy system in SAP IAG: -

Navigate to Administration - Applications

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture5-24.png)

2. Map User Source as IAS system                                                  Navigate to Administration – Configuration – Application Parameter and maintain user source as IAS system created in above step.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture6-22.png)

4.**Workflow Setup: -**

There is no configuration required for the workflow. For all workflow-related actions, you need to make use of pre-delivered workflow templates. You require these templates to create access requests.

The SAP Identity Access Governance solution pre-delivers both the workflow and notification templates. If this has not been the case, create a support ticket using the GRC-IAG component and request those templates.

You can find the uploaded workflow templates in the Maintain Workflow Template app. Use one of these template.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture7-22.png)

5.**Business Rules Activation and deploy.**

SAP Business Rules service is used to define the stages, paths, and other workflow rules used by Access Request service to move the request items through the stages of an a...