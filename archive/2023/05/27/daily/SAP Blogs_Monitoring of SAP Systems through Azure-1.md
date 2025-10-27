---
title: Monitoring of SAP Systems through Azure-1
url: https://blogs.sap.com/2023/05/26/monitoring-of-sap-systems-through-azure-1/
source: SAP Blogs
date: 2023-05-27
fetch_date: 2025-10-04T11:39:44.403293
---

# Monitoring of SAP Systems through Azure-1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Monitoring of SAP Systems through Azure\_Part-1

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161377&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Monitoring of SAP Systems through Azure\_Part-1](/t5/technology-blog-posts-by-members/monitoring-of-sap-systems-through-azure-part-1/ba-p/13557980)

![brijesh_tripath](https://avatars.profile.sap.com/9/7/id97a1fc415fbf3c1709218d93aa0166f7023316029884a9368f0c071f971ac60c_small.jpeg "brijesh_tripath")

[brijesh\_tripath](https://community.sap.com/t5/user/viewprofilepage/user-id/139546)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161377)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161377)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557980)

‎2023 May 26
8:05 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161377/tab/all-users "Click here to see who gave kudos to this post.")

3,794

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [Cloud Operations](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Operations/pd-p/1aa2b5a9-42a9-4f0b-974f-aa4dec11e19f)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [Cloud Operations

  Topic](/t5/c-khhcw49343/Cloud%2BOperations/pd-p/1aa2b5a9-42a9-4f0b-974f-aa4dec11e19f)

View products (2)

In this article, we'll talk about Microsoft Azure's monitoring services and how we may use them.

Customers operating their SAP landscapes on Azure Virtual Machines and Azure Large Instances can use Azure Monitor for SAP Solutions, an Azure-native monitoring tool. With Azure Monitor for SAP Solutions, we are able to centrally collect and visualise telemetry data from Azure infrastructure and databases.

We are able to monitor a variety of SAP landscape elements, including the OS, high availability, SAP HANA, SAP NetWeaver, etc.

1. Azure SERVICES

Azure will employ the following services to provide the remedy:

Microsoft Azure Monitors- The capacity of Azure Monitor for SAP Solutions, which includes workbooks and log analytics, is used to extend the possibilities of monitoring. It reads the SAP data from the log analytics and makes it accessible to the workbooks so they may display it graphically.

Workspace for Log Analytics - Azure Monitor log data is stored in a specific environment called a Log Analytics workspace. Data sources and solutions are set up to store their data in a workspace, and each workspace has its own data repository and configuration.

Workbooks -Workbooks have the ability to query data from many Azure sources. We may modify this data in Workbooks to reveal information about the usability, performance, and general health of the underlying components.

Azure Key - A cloud service called Vault allows users to store and access secrets safely. Anything that we want to strictly restrict access to is considered a secret, including API keys, passwords, certificates, and cryptographic keys. Software, HSM-backed keys, secrets, and certificates can all be stored in vaults.

Managed identities - Services that manage credentials are no longer necessary thanks to managed identities. Applications can connect to services that enable Azure Active Directory (Azure AD) authentication using an identity provided by managed identities. Applications can receive Azure AD tokens by using the managed identity. AD authentication can be used with Managed Identities to access the key vaults and retrieve the SAP system secrets.

Azure Queue Storage - Azure Large numbers of messages can be stored using the queue storage service, which is accessible from anywhere by making authorised HTTP or HTTPS calls. Up to the maximum storage account capacity, a queue can hold millions of messages, each of which can have a maximum size of 64 KB. Queue storage is frequently utilized.

Azure Virtual Machine- One of the many categories of scalable, on-demand computing resources that Azure provides are Azure Virtual Machines (VM). The Azure Monitors will set up VMs. A Standard\_B2ms virtual machine is what you have here. The hosting of the monitoring payload is the duty of this VM.

OVERVIEW OF ARCHITECTURE

The high-level process for data collection from the SAP HANA database using Azure Monitor for SAP systems is depicted in the following diagram. If SAP HANA is set up on Azure VMs or Azure Large Instances, the architecture is the same in both cases.

![](/legacyfs/online/storage/blog_attachments/2023/05/Azure_arch-4.png)

Source:Microsoft.com

You can access the Azure Monitor for SAP Solutions service using the Azure portal.

You can access monitoring data in the Azure Monitor for SAP Solutions repository.

The managed resource group, which is automatically deployed as part of the deployment of the Azure Monitor for SAP solutions resource, The controlled resource group's resources aid in data collection. Important sources are:

a resource for Azure Functions that houses the monitoring code. This logic gathers data from the source systems and sends it to the framework for monitoring.

a resource in the Azure Key Vault that safely saves the SAP HANA database credentials and provider data.

The location for data storage is the Log Analytics workspace. When deploying your Azure Monitor for SAP Solutions resource, you have the option of using an existing workspace from the same subscription.

## 2. Create Azure Monitor for SAP solutions monitoring resource

Sign in to the [Azure portal](https://portal.azure.com/).

![](/legacyfs/online/storage/blog_attachments/2023/05/azure-1-2.png)

Source:Microsoft.com

1. In Azure **Search**, select **Azure Monitor for SAP solutions**.

![](/legacyfs/online/storage/blog_attachments/2023/05/azure-2-2.png)

Source:Microsoft.com

![](/legacyfs/online/storage/blog_attachments/2023/05/azure-3-2.png)

Source:Microsoft.com

**Conclusion-**

In this blog, I’ve tried to illustrate how we can monitor through Azure, which is fundamental and the first step towards doing more in this area. However, this is just the beginning of how MS Azure can be used.

Related blogs –

<https://learn.microsoft.com/en-us/azure/sap/monitor/about-azure-monitor-sap-solutions>

<https://blogs.sap.com/2020/10/20/sap-on-azure-the-starting-steps/>

Please share your feedback and your thoughts. Write back to me for questions and queries.

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fmonitoring-of-sap-systems-through-azure-part-1%2Fba-p%2F13557980%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [S/4...