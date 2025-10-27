---
title: Cloud Integration – Send Mail via Microsoft Graph API with OAuth 2.0 Authorization Code
url: https://blogs.sap.com/2023/02/18/cloud-integration-send-mail-via-microsoft-graph-api-with-oauth-2.0-authorization-code/
source: SAP Blogs
date: 2023-02-19
fetch_date: 2025-10-04T07:29:53.876631
---

# Cloud Integration – Send Mail via Microsoft Graph API with OAuth 2.0 Authorization Code

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Cloud Integration - Send Mail via Microsoft Graph ...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157546&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Cloud Integration - Send Mail via Microsoft Graph API with OAuth 2.0 Authorization Code](/t5/technology-blog-posts-by-sap/cloud-integration-send-mail-via-microsoft-graph-api-with-oauth-2-0/ba-p/13549710)

![franz_forsthofer](https://avatars.profile.sap.com/4/f/id4f3278523cd0d6bf744f19d21b7e53670a18e95da005508b7065be13ac8c64c9_small.jpeg "franz_forsthofer")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[franz\_forsthofer](https://community.sap.com/t5/user/viewprofilepage/user-id/452730)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157546)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157546)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549710)

‎2023 Feb 18
10:29 AM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157546/tab/all-users "Click here to see who gave kudos to this post.")

20,391

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (2)

The blog "[Cloud Integration – Connect to Microsoft 365 Mail with OAuth2](https://blogs.sap.com/2020/08/20/cloud-intgration-connect-to-microsoft-365-mail-with-oauth2/)" contains chapters how you can connect from SAP Cloud Integration to Microsoft 365 via OAuth2 to **send** mails using the protocol SMTP. In this blog we describe an alternative to the SMTP protocol: we use the Microsoft Graph **REST** API to send mails using the HTTP receiver adapter of SAP Cloud Integration.

We create an integration flow which connects to the Microsoft Graph REST API described in <https://learn.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0&tabs=http>.

# Prerequisites

When connecting to Outlook 365 with OAuth2, you need to have an organizational directory/tenant in Microsoft Azure Active Directory and a user in this directory which has a subscription to Outlook 365. The following screen shot shows an example of such a user in the Azure Active Directory with name “testusermail” which has the license “Exchange Online (Plan1)”.

![](/legacyfs/online/storage/blog_attachments/2020/08/AzureMailUserLicenseView.png)
You can check whether the user has a subscription to Outlook 365 by logging-in with the user to  <https://outlook.office365.com/mail/>.
For the configuration tasks in the Azure Active Directory, you also need a user with the “Application administrator” and the “Application developer” role.

Furthermore, you need a SAP Cloud Integration or Integration Suite tenant on which you have a user with the “Integration Developer” role.

# Setup

We build an integration flow which you can call via an HTTP client and which connects to Microsoft Graph via the HTTP receiver adapter of SAP Cloud Integration. To set up this scenario, execute the following steps:

+ Step 1: Determine Redirect URI

+ Step 2: Create OAuth Client/App in Microsoft Azure Active Directory

+ Step 3: Create OAuth2 Authorization Code Credential in your SAP Cloud Integration Tenant

+ Step 4: Create Script Collection with a Groovy Script

+ Step 5: Create Integration Flow with Script Step and HTTP Receiver Adapter

+ Step 6: Execute the Integration Flow

# Step 1: Determine Redirect URI

When you log into the SAP Cloud Integration or Integration Suite WEB-UI, you see your host name in the browser address field:

```
https://<host name>/itspaces (for Cloud Integration)

https://<host name>/shell/home (for Integration Suite)
```

Use the <host name> to construct the following redirect URI:

|  |
| --- |
| https://<host name>/itspaces/odata/api/v1/OAuthTokenFromCode |

You need this redirect URI in the next step.

# Step 2: Create OAuth Client/App in Microsoft Azure Active Directory

1. Log into your Azure tenant by using <https://portal.azure.com/>
2. Select “App registrations” under “Azure services”.
   ![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-19-26.png)
3. Click on “New registration”, provide a name for your app, choose in the drop down “Select a platform” the value “**Web**“, and enter the **redirect URI** you determined at the beginning. Do not change the default setting for the “account types” (“Accounts in this organizational directory only”). After that, select “Register”.![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-22-7.png)

![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-30-5.png)Save the Application (client) ID anywhere on your local desktop. You will need this ID later to configure the OAuth2 Credential in CPI.

4. Choose “Certificates & secrets” in the menu on the left.

![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-49-36.png)5. Select “New client secret”, choose your preferred expiry period (“In 1 year”, “In 2 years” or “Never”). Optionally, you can also add a description. When you’re done, select “Add”.

![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-51-23.png)![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-53-35.png)

Remark: Before the secret expires you have to create a new secret and transfer the new secret to the SAP CPI OAuth2 Authorization Code credential (see below).

6. Use the “Copy to clipboard” button to remember the created secret (you will need this later to configure the OAuth2 credential in CPI).

![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_9-56-31.png)

7. Go back to the “Overview” view of the app and select the “Endpoints” tab.

![](/legacyfs/online/storage/blog_attachments/2020/08/image2020-7-29_10-10-30.png)

Copy the “OAuth 2.0 authorization endpoint (v2)” and the “OAuth 2.0 token endpoint (v2)” to your local desktop. You need these values later for the creation of the OAuth2 credential in Cloud Integration.

8. Choose “API permissions” in the menu on the left and check that the permission “Microsoft Graph User.Read” is configured. This permission should be there by default. If not then add it.![](/legacyfs/online/storage/blog_attachments/2020/08/AzureAppApiPermissions.png)

# Step 3: Create OAuth2 Authorization Code Credential in your SAP Cloud Integration Tenant

Log into your Cloud Integration tenant via the URL https://<host name>/itspaces (for Cloud Integration) or the URL <https://<host> name>/shell/home (for Integration Suite). Change to the “Operations View” (press the eye icon), and select the “Se...