---
title: Technical User Propagation – SAP BTP To S4 On Premise
url: https://blogs.sap.com/2022/12/21/technical-user-propagation-sap-btp-to-s4-on-premise/
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:12:56.548520
---

# Technical User Propagation – SAP BTP To S4 On Premise

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Technical User Propagation - SAP BTP To S4 On Prem...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159699&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Technical User Propagation - SAP BTP To S4 On Premise](/t5/technology-blog-posts-by-sap/technical-user-propagation-sap-btp-to-s4-on-premise/ba-p/13555630)

![munishsuri](https://avatars.profile.sap.com/0/6/id066ce1d46cc6f951f0bacf1ac3e30a70b558dfe75eac2091cc0be77eca1824cf_small.jpeg "munishsuri")

[munishsuri](https://community.sap.com/t5/user/viewprofilepage/user-id/118149)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159699)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159699)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13555630)

‎2022 Dec 21
9:38 PM

[18
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159699/tab/all-users "Click here to see who gave kudos to this post.")

13,421

* SAP Managed Tags
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Connectivity service](https://community.sap.com/t5/c-khhcw49343/SAP%2520Connectivity%2520service/pd-p/67837800100800004901)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Connectivity service

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BConnectivity%2Bservice/pd-p/67837800100800004901)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (4)

Use Case - Need to propagate technical user to the on premise S4 system using methodology of principal propagation. Authenticated applications running on BTP Cloud Foundry, can now propagate technical user utilizing **SAP-Connectivity-Technical-Authentication** header.

We recently had a requirement where we would need to propagate the Technical user but did not want to use Basic Auth as a security.

As of Cloud Connector version 2.15, consumers of the Connectivity service can propagate technical users from the cloud application towards the on-premise systems. To achieve this a JWT token is used representing the technical user, via the SAP-Connectivity-Technical-Authentication header.This is similar to principal propagation, but in this case, a technical user is propagated instead of a business user.

In the following blog, I would try to outline an approach for achieve the same, though it is something we have used to achieve the results and may not be production ready (Of Course), because the code should be more refined while achieving the same ![:slightly_smiling_face:](/html/@F5E1ACF1B11D8F2A0F728ABA9AA5B820/emoticons/1f642.png ":slightly_smiling_face:")

![](/legacyfs/online/storage/blog_attachments/2022/12/arch.png)

To verify and demonstrate the functionality, where an OData service is used on premise that I fetching the current user in the call and returning to the caller. From Cloud Foundry perspective there is an application that will be serving as an entry point for the User and the call is forwarded to another middleware, where the headers will be transformed for the request.

**Pre Req** - Principal propagation is already setup.

Let's start with the configuration on the on premise side.

1. Create an odata service - in this specific case to test the connection, a sample odata service is created, that is going to read the logged in user and return to the caller. Attaching a sample implementation - utilizing the current DDIC structures for the same and using **sy-uname.**![](/legacyfs/online/storage/blog_attachments/2022/12/onpremodata.png)

2. Creation of a User in **Su01**
   ![](/legacyfs/online/storage/blog_attachments/2022/12/su01user-1.png)

3. In the above step the most important part is the **alias -** this is the technical user for your         communication and you can find it from the BTP Service Key, in the above case this is the service key **client id of the connectivity service** of the sub account where you have connected your cloud connector. We are getting via binding the middleware application with connectivity service and using the environment variables to read the data.![](/legacyfs/online/storage/blog_attachments/2022/12/client-id.png)

4. Now you would need to map the user via transaction **certrule,**as the technical user is in managed in alias, we would mapping the user via alias, and the cloud connector will have Principal Propagation as a means of authentication.![](/legacyfs/online/storage/blog_attachments/2022/12/certrule_alias.png)

![](/legacyfs/online/storage/blog_attachments/2022/12/cc_cnname.png)

From the On premise perspective, we would be required to do only few additional configurations apart from the standard principal propagation setup.

Pre Req - Cloud Foundry Application that has XSUAA authentication and capable to call a destination.

In our POC, we have an app router, which is going to call the destination (middleware application).

XS-app.json of the app is configured in the following way,

```
{

  "welcomeFile": "/index.html",

  "authenticationMethod": "route",

  "logout": {

    "logoutEndpoint": "/do/logout"

  },

  "routes": [

    {

      "csrfProtection": false,

      "source": "^/sap/opu/odata/sap/Z_MUNISH_SSO_SRV/(.*)$",

      "target": "$1",

      "destination": "middleware_sso"

    },

    {

      "source": "^(.*)$",

      "target": "$1",

      "service": "html5-apps-repo-rt",

      "authenticationType": "xsuaa"

    }

  ]

}
```

it is pointing to **middleware\_sso**, which is nothing but a destination created on BTP sub account for the middle ware processing, though this can be achieved by **middleware chaining concept,**but I am putting the middleware logic out for this POC.

Config of **middleware\_sso** destination are shown below.

![](/legacyfs/online/storage/blog_attachments/2022/12/dest_config.png)

Till Now, we have configured the Principal Propagation and have an application available that is bounded to XSUAA and able to call the destination.

Coming to the Main part of now calling the Odata Service Destination, for that purpose we have a node js middle ware to append header and call the destination of the backend.

**Start.js**

```
const express = require("express");

const app = express();

const SapCfAxios = require("sap-cf-axios").default;

const passport = require("passport");

const { JWTStrategy } = require("@sap/xssec"...