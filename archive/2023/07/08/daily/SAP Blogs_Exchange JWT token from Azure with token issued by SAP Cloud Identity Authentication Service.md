---
title: Exchange JWT token from Azure with token issued by SAP Cloud Identity Authentication Service
url: https://blogs.sap.com/2023/07/07/exchange-jwt-token-from-azure-with-token-issued-by-sap-cloud-identity-authentication-service/
source: SAP Blogs
date: 2023-07-08
fetch_date: 2025-10-04T11:53:41.170930
---

# Exchange JWT token from Azure with token issued by SAP Cloud Identity Authentication Service

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Exchange JWT token from Azure with token issued by...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159037&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Exchange JWT token from Azure with token issued by SAP Cloud Identity Authentication Service](/t5/technology-blog-posts-by-sap/exchange-jwt-token-from-azure-with-token-issued-by-sap-cloud-identity/ba-p/13553444)

![harjeetjudge](https://avatars.profile.sap.com/5/a/id5a542fc0521696be11cdefe87b02c1bb6510a5cc86ceee9a8a357cd3c4191122_small.jpeg "harjeetjudge")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[harjeetjudge](https://community.sap.com/t5/user/viewprofilepage/user-id/107963)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159037)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159037)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553444)

‎2023 Jul 07
9:02 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159037/tab/all-users "Click here to see who gave kudos to this post.")

6,438

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Cloud Identity Services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Identity%2520Services/pd-p/67837800100800007337)

* [SAP Cloud Identity Services

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BIdentity%2BServices/pd-p/67837800100800007337)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

View products (2)

As a developer you may have the need to authenticate to applications hosted in SAP Business Technology Platform (SAP BTP) from 3rd party apps.  This can be accomplished using the JWT Bearer Token exchange in SAP Cloud Identity Services (IAS).  In this blog I will showcase how a JWT token from MS Azure can be exchanged with token issued by IAS.  The IAS token can be used to get an access token from SAP BTP to authenticate to SAP BTP applications.  The picture below highlights the high level workflow to achieve this goal.

![](/legacyfs/online/storage/blog_attachments/2023/07/1-34.png)

Step 1 of the process involves making a request to Microsoft Azure application using either Resource Owner Password Credentials or Authorization Code flow.  The end result of this process is that Azure AD will issue an ID token which we can use for token exchange.  Few things to note for this to work:

1. SAP Cloud Identity Authentication Service should be setup as an OIDC application in Microsoft Azure.  This can be accomplished using [this](https://blogs.sap.com/2022/10/06/connecting-sap-ias-as-a-proxy-to-azure-ad-using-openid-connect/) blog.

2. Update the manifest file for Azure app to make sure ***accesstokenAcceptedVersion*** is set to **2**.![](/legacyfs/online/storage/blog_attachments/2023/07/2-15.png)

3. Use the right token endpoint for Microsoft when making the token request from your client.  It should be *[https://login.microsoftonline.com/{{tenantID}}/oauth2/](https://login.microsoftonline.com/%7B%7BtenantID%7D%7D/oauth2/)**v2.0**/token.*Make sure to retrieve the v2 of the token.

4. ClientID used in the request should be for the SAP Cloud Identity Services application registered in MS Azure.

Here is screenshot of the request to MS Azure using Postman and retrieved token from Azure.

![](/legacyfs/online/storage/blog_attachments/2023/07/3-15.png)

Decoding the ID token shows that the aud field is set to the clientID of the IAS application in Azure.  Note that the token version is also set to 2.0.  Both of these are necessary for SAP Cloud Identity Authentication Service to accept this token for a token exchange.![](/legacyfs/online/storage/blog_attachments/2023/07/4-12.png)

In **Step 3**, the Azure token can be exchanged for a token issued by IAS.  To successfully do this exchange we need make sure that the issuer of the external corporate identity provider is configured as a corporate identity provider and set as a default identity provider or configured via Authentication Rules (Conditional Authentication) in the administration console for SAP Cloud Identity Services.  In addition Client ID and Client Secret are also required to send the request.

To retrieve the information required for token exchange, follow the steps below:

1. Access SAP Cloud Identity Authentication Service admin console using the URL: <https://<iashostname>.accounts.ondemand.com/admin>.

2. Authenticate as an administrator user.

3. Click **Applications & Resources >> Applications** and select your application.  In my case I am selecting the app created when trust is established between BTP subaccount and IAS.

4. Scroll down and click **Conditional Authentication.****![](/legacyfs/online/storage/blog_attachments/2023/07/8-10.png)**

5. Confirm that Azure is setup as the **Default Identity Provider** for your application.  Alternatively, it's possible to leave the Default Identity Provider to Identity Authentication and set conditional rules to forward the request to Azure.  For more information on setting up conditional rules, follow the [help guide](https://help.sap.com/docs/identity-authentication/identity-authentication/configure-conditional-authentication-for-application).![](/legacyfs/online/storage/blog_attachments/2023/07/9-6.png)

6. Click the back arrow and click **Client Authentication**.![](/legacyfs/online/storage/blog_attachments/2023/07/5-14.png)

7. Under **Secrets**, click **+Add** to add a new secret and click **Save**.![](/legacyfs/online/storage/blog_attachments/2023/07/6-10.png)

8. Make note of the **Client ID** and **Client Secret** as that's required for API authentication and click **OK**.![](/legacyfs/online/storage/blog_attachments/2023/07/7-11.png)

We can now send the request to IAS for the token exchange.  The request should be formulated using the following information:

* **Token URL**: <https://<iashostname>.accounts.ondemand.com/oauth2/token>

* Request Headers:

  + **Content-Type**: application/x-www-form-urlencoded

  + **Authentication**: Basic Authentication

* **Body:**

  + **assertion**: <id token from retrieved from Azure in the previous request>

  + **grant\_type:** urn:ietf:params:oauth:grant-type:jwt-bearer

  + **client\_id:** <client id from IAS>

  + **client\_secret**: <client secret from IAS>

See screenshot below of sample request and the response from IAS.

![](/legacyfs/online/storage/blog_attachments/2023/07/10-6.png)

Decoding the token, we can see that issuer is set to SAP Cloud Identity Authentication Service tenant.  We were able to successfully exchange the token from Azure with one issued by IAS.  The attributes you get back in the token will depend upon whether the user record exists in IAS or not.  In my case my user also exists in IAS so I see attributes like user\_uuid w...