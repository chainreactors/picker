---
title: Identity and Authentication Management in SAP Business One
url: https://blogs.sap.com/2022/12/28/identity-and-authentication-management-in-sap-business-one/
source: SAP Blogs
date: 2022-12-29
fetch_date: 2025-10-04T02:39:48.735968
---

# Identity and Authentication Management in SAP Business One

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Identity and Authentication Management in SAP Busi...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/48475&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Identity and Authentication Management in SAP Business One](/t5/enterprise-resource-planning-blog-posts-by-sap/identity-and-authentication-management-in-sap-business-one/ba-p/13537802)

![Guy_Sujetzki](https://avatars.profile.sap.com/c/6/idc61d1018230f4ee869bebf3f7018862fa167551fff275fd456375012702c7b3c_small.jpeg "Guy_Sujetzki")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Guy\_Sujetzki](https://community.sap.com/t5/user/viewprofilepage/user-id/11258)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=48475)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/48475)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13537802)

‎2022 Dec 28
9:43 AM

[26
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/48475/tab/all-users "Click here to see who gave kudos to this post.")

26,470

* SAP Managed Tags
* [SAP Business One](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520One%252C%2520version%2520for%2520SAP%2520HANA/pd-p/67838200100800004775)

* [SAP Business One

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne/pd-p/01200615320800000816)
* [SAP Business One, version for SAP HANA

  SAP Business One](/t5/c-khhcw49343/SAP%2BBusiness%2BOne%25252C%2Bversion%2Bfor%2BSAP%2BHANA/pd-p/67838200100800004775)

View products (2)

With 10.0 FP 2208, SAP Business One introduces the Identity and Authentication Management (IAM) service, allowing users to authenticate with their Identity Provider’s (IDP) user when Signing-in to SAP Business One.

Connecting SAP Business One with an Identity provider can help you manage user access in a secured manner without compromising on user experience during sign-in to SAP Business One.

### **What are the main benefits from using IAM solution in SAP Business One?**

* Single sign-on (SSO) experience.

* Reduce Password fatigue – users do not need to remember an excessive amount of passwords.

* Enhance security during sign-in by utilizing IDP’s Multi Factor Authentication and reduce potential attack surface.

* A central user management solution, allowing Landscape administrators to setup IDP users (under one or more IDPs), bind them to SAP Business One company users and manage users from across all company databases in one place.

### **Identity Providers Management**

IAM can be activated by configuring IDPs and Users under newly added ‘*Identity Providers’*and ‘*Users’* tabs in SAP Business One System Landscape Directory (SLD) control center.
After upgrading to 10.0 FP 2208, The following Identity Providers appear by default under ‘*Identity Provider’* tab in SLD:

* SAP Business One Authentication Server – Built-in Authentication Service

* Active Directory Domain Services –  Built-in Authentication Service

It is also possible to add OIDC (Open ID Connect) IDP by clicking on *‘Add’*

* OIDC (Open ID Connect)*Note: with 10.0 FP 2208, it is possible to register '**AD FS**' or '**Azure Active Directory**' as external identity providers in OIDC.*

![](/legacyfs/online/storage/blog_attachments/2022/08/IDP-2.png)

Identity Providers tab in SLD

By default, to preserve backward compatibility, IDPs are set to ‘*inactive*‘ after upgrade. There is no change to the Sign-in experience for SAP Business One users unless an IDP is activated.

Before an IDP is activated, there are a few important prerequisites that need to be fulfilled:

* There must be at least one corresponding Landscape Admin user configured under ’*Users*’ tab in SLD.

* IDP users created and bound to SAP Business One company users across all companies.

* IDP property for add-ons was adopted.

### **User Management**

The newly added ‘*Users’* Tab in SLD, acts as a ‘one stop shop’ for:

* Adding / removing IDP users.

* Binding IDP users to SAP Business One users across company databases.

* Central user management solution: change PwD and activate / deactivate unified users (users created under SAP Business One Authentication Server IDP), assign users with Landscape Admin role.

*Note:* *The licenses assigned to SAP Business One company users remain unchanged after enabling the identity and authentication management.*

### **Sign-in to SAP Business One with an IDP**

Once an IDP is activated in SLD, SAP Business One users will experience a new Sign-in window. Depending on landscape's IDP configuration (IDP type, number of IDPs activated), users are redirected to their IDP within SAP Business One Sign-in window to authenticate.

 *Watch the quick demo below on how to setup Microsoft Azure as an identity provider in SAP Business One and Sign-in to SAP Business One Web client with an Azure account.*

### **How-to-guide**

As IAM has a noticeable footprint on user’s Sign-in journey in addition to behavioral changes in SAP Business One, it is highly recommended reviewing ‘[**I****dentity and authentication management in SAP Business One**](https://help.sap.com/docs/SAP_BUSINESS_ONE_IAM/548d6202b2b6491b824a488cfc447343/7f94c5836fad44e6a02322d39e229cc3.html)*‘* How-to-guide to learn more about the following topics:

* IAM Setup and Configuration

* Recovery / Reset of IAM

* Behavior changes

* Supported SAP Business One Components in 10 FP 2208

* Extension adaptations

### **Roll out plan**

The Identity and authentication management service is planned be rolled out in a phased manner.
With 10.0 FP 2208, IAM is supported by the following SAP Business One Products:

* SAP Business One

* SAP Business One, version for SAP HANA

Please note that with 10.0 FP release, The IAM service **is not supported by existing SAP Business One Cloud versions**. It is planned to be supported in SAP Business One Cloud in later versions.

Hope this Blog was useful to you as an introduction to SAP Business One’s Identification and Authentication Management service. I'm looking forward to hear about your experience from working with IAM in SAP Business One, be sure to leave your feedback in the comments section below.

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [b1pminsights](/t5/tag/b1pminsights/tg-p/board-id/erp-blog-sap)

69 Comments

* «
  Previous
* + 1
  + [2](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/identity-and-authentication-management-in-sap-business-one/ba-p/13537802/page/2#comments)
* [Next
  »](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/identity-and-authentication-management-in-sap-business-one/ba-p/13537802/page/2#comments)

You must be a registered user to add a comment. If you've alrea...