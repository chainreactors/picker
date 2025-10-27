---
title: Integration suite setup custom domain for integration endpoints in an extension landscape
url: https://blogs.sap.com/2023/02/13/integration-suite-setup-custom-domain-for-integration-endpoints-in-an-extension-landscape/
source: SAP Blogs
date: 2023-02-14
fetch_date: 2025-10-04T06:31:33.072841
---

# Integration suite setup custom domain for integration endpoints in an extension landscape

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Integration suite setup custom domain for integrat...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/163265&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integration suite setup custom domain for integration endpoints in an extension landscape](/t5/technology-blog-posts-by-members/integration-suite-setup-custom-domain-for-integration-endpoints-in-an/ba-p/13568623)

![Jordy_S](https://avatars.profile.sap.com/e/3/ide384e48a4779ff82275ae7810c222f0a120f8aaa00c316c6c1b3481595390765_small.jpeg "Jordy_S")

[Jordy\_S](https://community.sap.com/t5/user/viewprofilepage/user-id/102909)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=163265)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/163265)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568623)

‎2023 Feb 13
10:06 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/163265/tab/all-users "Click here to see who gave kudos to this post.")

11,095

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

## Introduction

In this blog post you will learn how to setup custom domains for SAP Integration Suite integration runtime based on Cloud Foundry when the subaccount is on the main landscape of the same region (e.g. eu20) and your Integration Suite service is created for the extension landscape (e.g. eu20-001).

The setup is a bit different compared to the documentation available in help.sap.com as of the writing of this blog and most of the blogs published are pointing to the Cloud Foundry CLI which will not work for this specific configuration.

To keep this blog to the point the focus is to provide detailed steps and information for this case. Information about obtaining a certificate or updating DNS records are only briefly touched.

## Prerequisites

To follow the steps explained please make sure you have or gathered:

* Administrator access to the subaccount in which Integration Suite is running. To be able to

  + Setup Custom Domain Manager

  + Setup authorization

* SAP Integration Suite is setup and running. Launchpad is accessible.

* DNS administrator authorization.

* Certificate administrator authorization.

Knowing the difference between extension and main landscape. Below an example but it applies to all regions supported:

* Main landscape = eu20

* Extension landscape = eu20-001

## Integration Suite extension landscape validation

Before going to the next paragraphs in this blog validate you have your subaccount in another landscape compared to the Integration Suite. This is an easy validation:

1. Login to the BTP cockpit and navigate to the subaccount containing the Integration Suite service overview tab and look for the API endpoint in the Cloud Foundry Environment section:![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-cockpit-subaccount-overview-tab-1.png)

2. Open the SAP Integration Suite application/launchpad from the BTP cockpit:![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-cockpit-subaccount-instances-and-subscriptions-1.png)

3. In the URL you will see the landscape used:![](/legacyfs/online/storage/blog_attachments/2023/02/Integration-suite-launchpad-region-in-URL.png)

4. If you see something like -000 behind the main region this means the SAP Integration Suite is using the extension landscape of the region. Be aware this is the case for API proxies, integration flow runtimes but doesn't have to be the case for API business hub enterprise (formerly known as API developer portal).

If your subaccount matches the region including possible -000 for integration suite the custom domain can be setup via the normal procedure. Otherwise please follow the rest of this blog.

## Configuration steps - Custom Domain manager setup

As mentioned the Cloud Foundry CLI with the custom domain plugin cannot be used for the extension landscape setup as described above. The Custom Domain Manager is a UI-based web application available within the service marketplace of the subaccount. To setup custom domains for integration suites at the extension landscape when the subaccount is at the main landscape follow the below steps and in my setup Custom Domain Manager is configured in one of the subaccounts containing an SAP Integration Suite:

1. Login to the BTP cockpit and navigate to the subaccount containing the Integration Suite service.

2. In the entitlement menu within the subaccount assign the custom domain service and only the standard (Application) plan:![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-cockpit-subaccount-entitlements.png)

3. After the assignment is completed in the *services->instances and subscriptions* menu create an instance for the standard plan. After the services is provision first assign the correct authorization to use it.

4. A role collection needs to be created containing the roles and assign it to the person doing the rest of the activities:

   * CustomDomainAdmin

   * CustomDomainViewer

5. If you open the application no error prompt should be shown. If this is the case this part is completed.![](/legacyfs/online/storage/blog_attachments/2023/02/BTP-cockpit-subaccount-instance-for-custom-domain-manager-1.png)

## Configuration steps - Custom Domain SaaS subscription setup

The Custom Domain Manager need to be open to perform the next steps.

1. Start with adding a reserved domain to the Custom Domain Manager application by navigating to the menu at the top called Domains and click the button Add Reserved Domain. This will open a pop-up window to enter the domain for which the certificate will be or is created via the Custom Domain Manager.

   * My advice is to enter the main domain including the subdomain. If you use a second custom domain for the same region and main domain you will run into the error:![](/legacyfs/online/storage/blog_attachments/2023/02/Custom-domain-manager-UI-custom-domain-already-occupied.png)

2. After the reserved domain is added in the other tab called custom domains register the custom domain via the button Create Custom Domain and option *for you Subaccount's SaaS subscription: ![](/legacyfs/online/storage/blog_attachments/2023/02/Custom-Domain-Manager-adding-custom-domain-for-SaaS.png)*

3. In this step it is very important to select the Integration Suite application in the correct landscape. You cannot use a custom domain linked to the main landscape for the extension landscape and vice versa:![](/legacyfs/online/storage/blog_attachments/2023/02/Custom-Domain-Manager-Saas-subcription-setup.png)...