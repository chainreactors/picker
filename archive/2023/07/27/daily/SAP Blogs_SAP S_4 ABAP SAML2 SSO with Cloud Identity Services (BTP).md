---
title: SAP S/4 ABAP SAML2 SSO with Cloud Identity Services (BTP)
url: https://blogs.sap.com/2023/07/26/sap-s-4-abap-saml2-sso-with-cloud-identity-services-btp/
source: SAP Blogs
date: 2023-07-27
fetch_date: 2025-10-04T11:54:37.346096
---

# SAP S/4 ABAP SAML2 SSO with Cloud Identity Services (BTP)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* SAP S/4 ABAP SAML2 SSO with Cloud Identity Service...

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68270&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP S/4 ABAP SAML2 SSO with Cloud Identity Services (BTP)](/t5/enterprise-resource-planning-blog-posts-by-members/sap-s-4-abap-saml2-sso-with-cloud-identity-services-btp/ba-p/13565742)

![BlackmanCC](https://avatars.profile.sap.com/b/c/idbc8baff8f841aa00a5c52c948cdb816a7a18a28d7772c78739e12d3b06f27694_small.jpeg "BlackmanCC")

[BlackmanCC](https://community.sap.com/t5/user/viewprofilepage/user-id/16006)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68270)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68270)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565742)

‎2023 Jul 27
12:15 AM

[10
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68270/tab/all-users "Click here to see who gave kudos to this post.")

9,671

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

In this blog I explain how to setup Single Sign On for a (On Premise) S/4 HANA system with SAP Cloud Identity Services on BTP using SAML2. You can use this SSO for your Fiori Apps and other http services, e.g. WebGUI, not for SAP GUI.

We use Azure AD as a Corporate Identity provider in Cloud Identity Services. There are already some good blogs about this, e.g. [Connecting SAP IAS as a proxy to Azure AD using OpenID Connect.](https://blogs.sap.com/2022/10/06/connecting-sap-ias-as-a-proxy-to-azure-ad-using-openid-connect/)

In our case we only do Single Sign On. The users in our system are already there and will not be created through Identity Propagation.

1. Get the SAML Metadata of your Cloud Identity Services Tenant![](/legacyfs/online/storage/blog_attachments/2023/07/GetSAMLMetadata-1.png)![](/legacyfs/online/storage/blog_attachments/2023/07/GetSAMLMetadata2.png)

2. Get the "Signing Certificate"In the same view you have to display the "Signing Certifcate". Please copy the "Certificate Information" String and put it in a text file, e.g. my\_tenant\_signing\_cert.cer![](/legacyfs/online/storage/blog_attachments/2023/07/GetSigningCertificate.png)It would really be nice if SAP could deliver a "Get public key" button to get the needed information.

3. Export the public key of the "Signing Certificate", open the text file (double-click in Windows) and export the public key of the certificate (choose the first option "DER coded..."), filename e.g. public\_key\_my\_tenant\_signing\_cert.cer.![](/legacyfs/online/storage/blog_attachments/2023/07/ExportPublicKey.png)

4. Enable the ABAP Platform as an SAML Service Provider

   Call Transaction "SAML2" in your S/4 system

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML-1.png)

   As a provider name choose what you want or system and client name e.g. SYS\_100

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML2.png)
   You should choose Selection Mode Automatic if you only have one Identity Provider connected, because you do not want to choose an Identity Provider every time.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML3.png)

   Now you can download your Metadata of your SAML2 configuration in the S/4 client.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML4-1.png)

5. Create an "Application" for your S/4 HANA System

   ![](/legacyfs/online/storage/blog_attachments/2023/07/CreateApplication-1.png)

   Now you have to upload the metadata.xml of your S/4 configuration to your SAML2 configuration in BTP Cloud Identity Service.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML5-1.png)

   Please set all switches to ON.
   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML6-1.png)
   In the section "Subject Name Identifier" please choose Email because we user Email for authentication.
   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML7-1.png)
   In the section "Conditional Authentification" pleas choose your Coporate Identity provider
   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML8-1.png)

6. Please continue in your SAML2 configuration in S/4 and add your Identity Provider. You do this by uploading the XML-file you saved from your "Tenant Settings" in Cloud Identity Service.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML9-1.png)

   For Metadata Verification please upload your public key.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML10-2.png)
   Please enter an Alias for your provider which is shown when you should choose an Identity Provider. In our case this is not necessary because we only have one Identity Provider and switched on automatic selection before.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML11-1.png)
   For better security choose SHA-256 instead of SHA-1

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML12-1.png)

   Please enter the "Supported NameID Formats" with the "Add" button. Choose "Uncpecified" and as "User ID Mapping Mode" Email. Please disable "Allow Identity Provider to create NameID" because in our case the users have you be already created in the system and we do not want that users without roles get created.

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML13-1.png)

   Please enable your "Trusted Provider".

   ![](/legacyfs/online/storage/blog_attachments/2023/07/EnableSAML14.png)

For troubleshooting please follow the guided answers under [SAML 2.0 configuration or SAML 2.0 authentication does not work as expected. How can I troubleshoot ...](https://ga.support.sap.com/dtp/viewer/#/tree/121/actions/779)

* [Cloud](/t5/tag/Cloud/tg-p/board-id/erp-blog-members)
* [sap single sign-on](/t5/tag/sap%20single%20sign-on/tg-p/board-id/erp-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-members%2Fsap-s-4-abap-saml2-sso-with-cloud-identity-services-btp%2Fba-p%2F13565742%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Max line items in service contract in public cloud 2508](/t5/enterprise-resource-planning-q-a/max-line-items-in-service-contract-in-public-cloud-2508/qaq-p/14233931)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  yesterday
* [GRC, Trade and Tax with SAP S/4HANA Cloud Public Edition ...