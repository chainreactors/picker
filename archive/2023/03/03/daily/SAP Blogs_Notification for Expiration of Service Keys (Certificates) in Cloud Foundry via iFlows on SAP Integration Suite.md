---
title: Notification for Expiration of Service Keys (Certificates) in Cloud Foundry via iFlows on SAP Integration Suite
url: https://blogs.sap.com/2023/03/02/notification-for-expiration-of-service-keys-certificates-in-cloud-foundry-via-iflows-on-sap-integration-suite/
source: SAP Blogs
date: 2023-03-03
fetch_date: 2025-10-04T08:31:50.225584
---

# Notification for Expiration of Service Keys (Certificates) in Cloud Foundry via iFlows on SAP Integration Suite

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Notification for Expiration of Service Keys (Certi...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161725&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Notification for Expiration of Service Keys (Certificates) in Cloud Foundry via iFlows on SAP Integration Suite](/t5/technology-blog-posts-by-members/notification-for-expiration-of-service-keys-certificates-in-cloud-foundry/ba-p/13559692)

![vanessadayanc](https://avatars.profile.sap.com/b/0/idb0d25f1aae45e0db9f3c3ed64b43dcacc19839b08637c3a2e23bb6ac7bc974b7_small.jpeg "vanessadayanc")

[vanessadayanc](https://community.sap.com/t5/user/viewprofilepage/user-id/126506)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161725)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161725)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559692)

‎2023 Mar 02
10:53 PM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161725/tab/all-users "Click here to see who gave kudos to this post.")

6,943

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

Hello SAP Community,

in the context of a migration project from SAP CPI Neo to SAP IS Cloud Foundry (CF) Environment, I was searching for a solution to generate a notification for administrators about expiring Service Keys (Certificates) in SAP BTP CF via E-Mail. I did find some solutions for certificates in keystore, but no solution for the Service Keys - so I created one in form of an iFlow.

### Background

When proceeding a migration from SAP CPI in Neo Environment to SAP Integration Suite in Cloud Foundry, you will find several differences between the two systems. There are already a lot of Blogs and Guides with detailed information about the differences and best practices for [Migrating from the Neo Environment to the Multi-Cloud Foundation (Cloud Foundry and Kyma)](https://help.sap.com/docs/btp/migrating-from-neo-environment-to-multi-cloud-foundation-cloud-foundry-and-kyma/getting-started-with-your-migration?locale=en-US&q=), but I would like to focus on mainly one point:

For SettingUp Inbound HTTP Connections for Integration Flow Processing in SAP Cloud Foundry Environment it is necessary to create a Service Instance and Service Key for Inbound Authentication ([SAP Help](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/19af5e205fe14af6a4f8a9fd80d4dc92.html?locale=en-US)). Depending on your use case you can create three different types of Service Keys:

1. **ClientId/Secret**

2. **Certificate**

3. **External Certificate**

For further information please check out [help.sap](https://help.sap.com/docs/CLOUD_INTEGRATION/368c481cd6954bdfa5d0435479fd4eaf/0fc1446c4fa547d1b5f991f522c57484.html?locale=en-US)

If your use case requires **External Certificate**e.g. for Inbound Authentication from SAP ERP-Systems to SAP Integration Suite, you can add a sender client certificate (provided by sender administrator) to service key and maintain the validity date (validuntil).

![](/legacyfs/online/storage/blog_attachments/2023/02/ServiceKey.png)

In order to guarantee a constant communication, it is important to renew the certificates before the expire.

### Getting Started:

First of all I searched for a possibility to retrieve the Service Key information by calling CF-API endpoint. Depending on your landscape you can find the Endpoint of your Cloud Foundry API in one of your SubAccounts.

![](/legacyfs/online/storage/blog_attachments/2023/03/API-Endpoint.png)

To get the Service Key information it is necessary to use the cloud\_controller API, the documentation for V3 can be found [here](http://v3-apidocs.cloudfoundry.org/version/3.132.0/index.html) (V2 ist already deprecated).

#### Authentication:

The Cloud Foundry V3 API is secured using OAuth 2. Clients are expected to present a valid bearer token via HTTP header, that can be obtained from the Cloud Foundry UUA server or via CF CLI.

The only solution that worked in my testings were based on the following [post:](https://answers.sap.com/answers/13560602/view.html)

![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-01-13_00_58-How-to-authenticate-Cloud-Platform-API-_-SAP-Community.png)

I tried different versions to get a valid Authorization token for the CF-API but the solution below was the only one that worked for me using Postman.

SAP Integration Suite provides three Options vor OAuth2 Security Materials: OAuth2 Client Credentials, OAuth2 SAML Bearer Assertion, OAuth2 Authoriation Code. None of them will work with the grant\_type password. One way to get a token is to create the necessary Authorization data for a GET-Request via groovyscript in CPI:

1. Create two different Client Credentials as Security Material:

   1. **CF\_API\_Username** : Contains Username and Password of a SAP BTP User (Only use technical Users here!)

   2. **CF\_API\_ClientID:**User = cf and leave the password empty

2. Create a iFlow with a Start Timer and a Content Modifier

   1. Message Header: Content-Type = application/x-www-form-urlencoded

   2. Exchange Property: ApiUserCredentials = {{CF\_API\_Username}} for external configuration

3. Create Script Step:

```
import com.sap.gateway.ip.core.customdev.util.Message;

import java.util.HashMap;

import com.sap.it.api.ITApiFactory;

import com.sap.it.api.securestore.SecureStoreService;

import com.sap.it.api.securestore.UserCredential;

def Message processData(Message message) {

//get User from Configuration

def map = message.getProperties();

String user = map.get("ApiUserCredentials");

//service to get the credentials

def service = ITApiFactory.getApi(SecureStoreService.class, null);

//get user credential

def userCred = service.getUserCredential(user);

if (userCred == null){

throw new IllegalStateException("No User credential found for alias" + user);}

//HTTP Parameters value

String grant_type = "password";

String username = userCred.getUsername();

String password = new String(userCred.getPassword());

//Query

def query = "grant_type=" + grant_type + "&username=" + username + "&password=" + password;

message.setBody(query);

return message;

}
```

(Based on [post](https://answers.sap.com/answers/13115298/view.html))

4. User HTTP-Adapter to get a Token

![](/legacyfs/online/storage/blog_attachments/2023/03/2023-03-01-16_41_25-Get-Token.png) You will get back a response in the following format:

```
{

    "access_token": "<Token>",

    "token_type": "bearer",

    "id_token": "<id_toke>",

    "refresh_token": "<refresh_...