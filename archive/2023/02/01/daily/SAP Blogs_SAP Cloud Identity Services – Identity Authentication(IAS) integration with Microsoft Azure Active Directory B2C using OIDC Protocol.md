---
title: SAP Cloud Identity Services – Identity Authentication(IAS) integration with Microsoft Azure Active Directory B2C using OIDC Protocol
url: https://blogs.sap.com/2023/01/31/sap-cloud-identity-services-identity-authenticationias-integration-with-microsoft-azure-active-directory-b2c-using-oidc-protocol/
source: SAP Blogs
date: 2023-02-01
fetch_date: 2025-10-04T05:20:05.593128
---

# SAP Cloud Identity Services – Identity Authentication(IAS) integration with Microsoft Azure Active Directory B2C using OIDC Protocol

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Cloud Identity Services - Identity Authenticat...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158789&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Cloud Identity Services - Identity Authentication(IAS) integration with Microsoft Azure Active Directory B2C using OIDC Protocol](/t5/technology-blog-posts-by-sap/sap-cloud-identity-services-identity-authentication-ias-integration-with/ba-p/13552871)

![arpitoberoi](https://avatars.profile.sap.com/3/6/id36194236d0417289de7062a33ae4f007057b312d95c052b162a3d9c8443f4962_small.jpeg "arpitoberoi")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[arpitoberoi](https://community.sap.com/t5/user/viewprofilepage/user-id/115)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158789)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158789)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552871)

‎2023 Jan 31
5:03 PM

[20
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158789/tab/all-users "Click here to see who gave kudos to this post.")

18,888

* SAP Managed Tags
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)

View products (1)

## Scenario Overview

As modern enterprise landscape is evolving and becoming more and more cloud oriented, we have seen direct impact of this evolution on the way SAP customers run and deploy their mission critical applications. SAP customers are adopting SAP Business Technology platform to achieve their journey into cloud world.

Without compromising security one of the key ask of applications hosted on SAP BTP is simplified and great user experience.

In this scenario, I will take you through the steps to deploy an application on SAP BTP and give access to **EXTERNAL** users for this application using [Microsoft Azure Active Directory B2C](https://learn.microsoft.com/en-us/azure/active-directory-b2c/overview)

and [SAP Cloud Identity Services - Identity Authentication.](https://discovery-center.cloud.sap/serviceCatalog/identity-authentication?region=all)

### Few things to keep in mind

* External Users: Users who are not employees of your organisation. For example Vendors

* This scenarios covers authentication part and not authorisation part

* The steps covered in this scenario for [Microsoft Azure Active Directory B2C](https://azure.microsoft.com/en-gb/trial/get-started-active-directory-b2c/) are on a Trial Test Tenant

* This scenario covers authentication using Open ID Connect (OIDC) protocol

* You will also need admin access to your SAP IAS tenant

* You will also need admin/developer access in SAP BTP subaccount

### References and links to helpful blogs and material

* [How OIDC flow works and various components of the flow](https://help.sap.com/docs/IDENTITY_AUTHENTICATION/6d6d63354d1242d185ab4830fc04feb1/a789c9c8c0f5439da8c30b5d9e43bece.html)

* [Authentication and Principal Propagation between Microsoft Azure Active Directory and SAP BTP](https://blogs.sap.com/2022/11/02/principal-propagation-in-a-multi-cloud-solution-between-microsoft-azure-and-sap-business-technology-platform-btp-part-vi-calling-the-microsoft-graph-on-behalf-of-the-sap-authenticated-user/)

**Special Thanks and Mention**

I would like to specially thank mraepple and martijn.deboer for their help and guidance during this setup.

### High Level Diagram

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-24_17-59-27.png)

High Level Diagram

### Authorisation Flow Diagram

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-24_18-01-03.png)

Authorisation Flow Diagram

### Steps:

*Note: These are the steps which I took to understand the concept and also for my PoC. There are some shortcuts here. For your live implementation all relevant stake holders from SAP skillset and Microsoft skillset need to be involved.*

## Config in SAP BTP Subaccount

#### Pre-requisite

* Make sure your SAP IAS tenant is setup under 'SAP BTP Global Account->Security->Trust Configuration' as shown below:

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-24_20-25-47.png)

#### Configuration in BTP Subaccount

* Go to your subaccount and choose 'Security->Trust Configuration'. Click on 'Establish Trust'. If pre-requisite are met, you will see a popup 'Establish Trust to Custom Identity Provider' and in this popup when you will click on drop down, you will see you IAS tenant as shown below

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-24_20-31-21.png)

* Please make sure in next screen, you select 'Available for User Logon' check box

#### Quick Hello World Application

* There are hundreds if not thousands blogs available on developing [SAPUI5 applications](https://developers.sap.com/tutorials/appstudio-fioriapps-create.html), CAP applications therefore I won't be explaining how to create an application in this blog

* For my PoC, I used SAP Business Application studio to create a SAPUI5 free style application and deployed it to my SAP BTP subaccount

* This application is 'Managed Router' application. But in **case of custom router you will have to create service binding of your application but you will have to bind your application to 'SAP Cloud Identity Service' instead of XSUAA**

* Here is my simple 'Hello World' application deployed as HTML5 application in SAP BTP Subaccount

![](/legacyfs/online/storage/blog_attachments/2023/01/2023-01-24_20-44-38.png)

#### Configuration in Microsoft Azure Active Directory B2C

Now the fun begins.........

*Disclaimer: I am not Microsoft Expert. Following knowledge is what I gathered during implementation of PoC. If you don't have access to Microsoft Azure Active Directory B2C tenant, you can spin up your trial tenant at this link [Azure Active Directory B2C—Free Trial | Microsoft Azure](https://azure.microsoft.com/en-gb/trial/get-started-active-directory-b2c/) ( Please bear in mind that you will need a credit card and also you need to keep an eye on any charges etc)*

As this whole authentication works on principle of JWT tokens, the JWT token issued by Azure AD B2C should be in a format that SAP IAS is able to decode it and pass it on to your application.

### Challenge:

**JWT token created from standard Azure AD B2C User Flow gets rejected by SAP IAS!!!**

As of now when you create an application(user flow) in Azure AD B2C, you have choice to pick

* Sign Up and Sign In Flow

* Profile Editing

* Password Reset

* Sign Up

* Sign In

* Sign in using resource owner password credentials

For our need we chose 'Sign Up and Sign In Flow'. As with this flow an external user can create a user in AD B2C by registering and after registering they can authenticate themselves against AD B2C. *However the JWT token which gets issued ...