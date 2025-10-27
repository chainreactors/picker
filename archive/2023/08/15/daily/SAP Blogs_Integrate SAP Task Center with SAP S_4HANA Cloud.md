---
title: Integrate SAP Task Center with SAP S/4HANA Cloud
url: https://blogs.sap.com/2023/08/14/integrate-sap-task-center-with-sap-s-4hana-cloud/
source: SAP Blogs
date: 2023-08-15
fetch_date: 2025-10-04T12:01:31.128949
---

# Integrate SAP Task Center with SAP S/4HANA Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Integrate SAP Task Center with SAP S/4HANA Cloud

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54640&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integrate SAP Task Center with SAP S/4HANA Cloud](/t5/enterprise-resource-planning-blog-posts-by-sap/integrate-sap-task-center-with-sap-s-4hana-cloud/ba-p/13578163)

![dhruba_sap](https://avatars.profile.sap.com/4/6/id46dfc3684f20843b0a4d29845d61525dbb6a901c6586ae972d37f008e5a9f932_small.jpeg "dhruba_sap")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[dhruba\_sap](https://community.sap.com/t5/user/viewprofilepage/user-id/156533)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54640)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54640)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13578163)

‎2023 Aug 15
12:43 AM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54640/tab/all-users "Click here to see who gave kudos to this post.")

4,421

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (2)

The SAP Task Center service enables integration with SAP applications to provide a single entry point for end users to access all their assigned tasks. The tasks can be accessed by end users through the SAP Task Center Web application.

You can use SAP Task Center as a unified inbox for tasks across multiple applications with integrated user experience. Tasks from multiple SAP solutions are gathered in one list and ready to be processed in just one click, shortening the completion time for business-critical tasks. For example, business users can process all their tasks from the connected systems, without the need to switch and log in separately into different inboxes.

As shown in the diagram below, SAP Task Center is an infrastructure kernel service on SAP Business Technology Platform (SAP BTP), Cloud Foundry environment. It enables business users to manage their workflow tasks in one place by integrating tasks from multiple SAP applications (cloud and on premise).

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture1-24.png)

Lets elaborate the configuration steps to integrate Task Center with SAP S/4HANA Cloud in this blog.

The following steps need to be completed for the configuration

1. Setup BTP Subaccount for Task Center

2. Configure trust between BTP Subaccount and SAP Identity Authentication service (IAS)

3. Configure S/4HANA Cloud

4. Create/Update a destination in SAP BTP for your S/4HANA Cloud system

5. SAP Launchpad service configuration for Task Center

6. Update user UUID in S/4HANA

1. **Setup BTP Subaccount for Task Center**

There are 2 options to setup BTP subaccount for SAP Task Center.

1. Manual setup

2. Automatic setup using a booster

In the booster setup, the subaccount is created automatically without any manual error. It is the recommended one and will be followed in this blog. Please find the steps as listed below.

1.1 Login to your global BTP account create subaccount first.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture2-16.png)

1.2 Provide the Display Name, Description and choose region (actual data center) and Parent Global account. Create the subaccount.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture3-11.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture4-13.png)

1.3 Create Users in the BTP subaccount with Default identity provider to complete the setup.

**Sub Account >> Security >> Users >> Create Users**

1.4 Enable the cloud foundry for the sub account

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture5-11.png)

1.5 Create Space

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture6-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture7-10.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture8-10.png)

1.6 Deploy Task Center using Boosters setup

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture9-9.png)

1.7 Choose Standard Edition and other input fields

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture10-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture11-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture12-9.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture13-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture14-7.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture15-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture16-6.png)

1.8 Assign the required role for Launchpad administration, TaskCenter Administration and Destination Administration.

**Sub Account >> Security >> Users >> Select User >> Role Collections >> Assign Role Collection**

**2. Configure trust between BTP Subaccount and SAP Identity Authentication service (IAS)**

In order to use Task Center with S/4HANA Cloud, it is required to establish a trust between your BTP subaccount and SAP Cloud Identity Authentication Service used with your S/4HANA Cloud. Running the Booster setup for Task center will complete this step automatically.

This can be verified under **Security >> Trust Configuration**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture17-6.png)

**This IAS tenant will be used while login to the SAP Build Work Zone Site. The same IAS tenant should be used for SAP S/4HANA Cloud system.**

**3. Configure S/4HANA Cloud**

3.1 Note down the following attributes from BTP subaccount : **BTP sub Account >> Instances and Subscriptions >> Instances >> click on 3 dots >> View Parameters >> Service Keys >> View >> Form**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture18-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture19-9.png)

Note Down

**3.1.1   endpoints > inbox\_rest\_url**

**3.1.2   uaa > url**

**3.1.3   uaa > clientid**

**3.1.4   uaa > clientsecret**

3.2 Download the Trust from **BTP Sub Account >> Destinations >> Download Trust**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture20-6.png)

3.3 Maintain Communication Users

3.3.1 Login to SAP S/4HANA Cloud system and search for the App – Maintain Communication Users.

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture21-7.png)

3.3.2 Create a new communication user.  Specify a **User Name**, **Description,** and **Password.**

![](/legacyfs/online/storage/blog_attachments/2023/08/Picture22-6.pn...