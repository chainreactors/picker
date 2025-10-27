---
title: SSO Configuration on Asset Management steps involved.
url: https://blogs.sap.com/2023/05/17/sso-configuration-on-asset-management-steps-involved./
source: SAP Blogs
date: 2023-05-18
fetch_date: 2025-10-04T11:39:36.750503
---

# SSO Configuration on Asset Management steps involved.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SSO Configuration on Asset Management steps involv...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/158925&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SSO Configuration on Asset Management steps involved.](/t5/technology-blog-posts-by-sap/sso-configuration-on-asset-management-steps-involved/ba-p/13553211)

![ALLAMPRABHU](https://avatars.profile.sap.com/9/2/id92a1cf86eb5abe121b7d9b220d6dd47376bb0b2475937b5b4f3aa9faca9f6cd7_small.jpeg "ALLAMPRABHU")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ALLAMPRABHU](https://community.sap.com/t5/user/viewprofilepage/user-id/126333)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=158925)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/158925)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553211)

‎2023 May 17
11:11 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/158925/tab/all-users "Click here to see who gave kudos to this post.")

4,135

* SAP Managed Tags
* [SAP Mobile Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Mobile%2520Services/pd-p/668874921104038800958643358380369)

* [SAP Mobile Services

  Software Product Function](/t5/c-khhcw49343/SAP%2BMobile%2BServices/pd-p/668874921104038800958643358380369)

View products (1)

SSO based on Principal Propagation for SAP Asset Manager

Agenda:
Single Sign-on Authentication Types:

Single Sign-on based on Principal Propagation for SAP Asset Manager (BTP)

Principal Propagation -process Flow

![](/legacyfs/online/storage/blog_attachments/2023/05/Principal-propagation.png)

Principal Propagation: Architecture Overview

![](/legacyfs/online/storage/blog_attachments/2023/05/Architecture-Digram.png)

 technical landscape

![](/legacyfs/online/storage/blog_attachments/2023/05/technical-landscape.png)

Principle Propagation Compatibility

In the context of the SAP Mobile Add-On, the authorization expectation is for the SAP Cloud Connector to pass the cloud user identity through principal propagation in a subject pattern that is matched to a matched alias in the back end system.

SAP uses Rule based certificate mapping

![](/legacyfs/online/storage/blog_attachments/2023/05/SAP_GUI_CONFIG.png)

Backend user names
![](/legacyfs/online/storage/blog_attachments/2023/05/user_names.png)

Set the Principal propagation.

![](/legacyfs/online/storage/blog_attachments/2023/05/Cloud-connector_PP.png)

Step1.

SAP Cloud platform authentication setup using IAS with Azure AD

Connection to Corporate Active Directory need to establish.

Prerequisite: Cloud connector is installed and connected to SCP subaccount

![](/legacyfs/online/storage/blog_attachments/2023/05/Cloud-connector.png)

Cloud Connector configuration

Step 2.

Check the BTP

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP.png)

BTP Cockpit

click on Local Service Provider and edit & click on Get Metadata and upload in the IAS.

Step 3.

Go to IAS tenant.

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS.png)

IAS Home screen

Application & Add new Application.

![](/legacyfs/online/storage/blog_attachments/2023/05/Add-Application.png)

Add Application

Give the name to the Application.

Application Display Name:

Application Home URL: keep empty.

Application Type:

Step 4.

Go to SAP BTP Cockpit

On Trust, create a Trust Management

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP_Configuration.png)

Add identity Authentication Tenant (we have two tenant one is used for development & quality and other is used for production.

Select the trail and confirmation popup will appear.

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP_CONFIG.png)

download the metadata.

Step 5.

Go to IAS --> Application --> Bundled Applications --> where you have created the Asset manager DEV.

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS1.png)

Define from Metadata (upload the metadata which you have downloaded.

check the SAML 2.0 Configuration and signing Certificates.

check SHA-256 and Sign assertions is oN and sign single logout message is on and require signed single logout messages.

Save

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS2.png)

Step 6.

Steps for IAS -Azure AD

SAML 2.0 Configuration -->go to Tenant settings and under the Assertion consumer service end point you see the metadata where you can download the metadata.

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS3.png)

Step 7:

Upload the metadata into Azure AD

To configure the integration of SAP cloud platform Identity Authentication into Azure AD, you need to add SAP Cloud Platform Identity Authentication from the gallery to your list of managed SaaS apps.

Sign into the Azure portal using either a work or school account to Microsoft account.

in the left navigation pane, select the Azure Active Directory service.

navigate to Enterprise Applications and then select App applications.

to Add new application, select New Application

in the Add from the gallery section, type SAP Cloud Platform Identity Authentication in the search box. select SAP cloud Platform Identity Authentication from results panel and then add the app.

wait a few second s while the ap is added to your tenant.

download the metadata.

![](/legacyfs/online/storage/blog_attachments/2023/05/AD.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/AD1.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/AD3.png)

Login to IAS and upload the metadata in IAS.

Go to Identity Authentication Service --> Corporate Identity Providers --> create --> Add identity Provider & define the Metadata.

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS4.png)

select the Microsoft ADFS/Azure AD as the Identity Provider Type

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS5.png)

Enable the Single Sign on button & go to conditional Authentication and select the Default identity provider.

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS6.png)

Enable Single Sign-on

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS7.png)

Set conditional Authentication.

![](/legacyfs/online/storage/blog_attachments/2023/05/IAS8.png)

Save

Go to BTP

Security à Trust à Add - Identity Authentication Tenant / Trusted Identity Provider

& Add-Trusted identity Provider & upload the IAS metadata which you have downloaded

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP1.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP3.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP5.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP6.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP9.png)

Click on the Add-Trusted identity Provider & upload the IAS metadata which you have downloaded.

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP99.png)

![](/legacyfs/online/storage/blog_attachments/2023/05/BTP10.png)

## Id...