---
title: Run NodeJs in SAP BTP and Locally, Part – 2
url: https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-2/
source: SAP Blogs
date: 2023-03-20
fetch_date: 2025-10-04T10:05:12.974405
---

# Run NodeJs in SAP BTP and Locally, Part – 2

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Run NodeJs in SAP BTP and Locally, Part - 2

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160523&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Run NodeJs in SAP BTP and Locally, Part - 2](/t5/technology-blog-posts-by-members/run-nodejs-in-sap-btp-and-locally-part-2/ba-p/13552771)

![DebashishDas](https://avatars.profile.sap.com/d/7/idd75a2e80338e3be985cb2169d87aa8fb8ed01a1e2e6f4ff7c94f61a7c9d49849_small.jpeg "DebashishDas")

[DebashishDas](https://community.sap.com/t5/user/viewprofilepage/user-id/121928)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160523)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160523)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552771)

‎2023 Mar 19
10:26 AM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160523/tab/all-users "Click here to see who gave kudos to this post.")

3,602

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)

View products (2)

This blog series is just a simple demo of how to create any Nodejs app and run it on both local and SAP BTP platform.

*[Part – 1: Create nodejs application.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally/)*

**Part – 2: Create Authentication instance.**

*[Part – 3: Run app locally.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-3/)*

**Create Authentication**

To do that we will need BTP authorization and Trust management service (XSUAA)

Which we will create using MTA.yaml file.

```
resources:

 - name: basicnodejs-xsuaa

   type: org.cloudfoundry.managed-service

   parameters:

     service: xsuaa

     service-plan: application

     config:

        xsappname: basicnodejs-${org}-${space}

        tenant-mode: dedicated
```

build and deploy the mta.yaml file.

![](/legacyfs/online/storage/blog_attachments/2023/03/15-10.png)

But who will going to use these services?

We have to specify that two modules are going to access this service. Bind those modules with xsuaa instance service.

```
ID: basicnodejs

_schema-version: '3.1'

version: 0.0.1

parameters:

  enable-parallel-deployments: true

modules:

  - name: basicnodejs-service

    type: nodejs

    path: srv

    build-parameters:

      ignore:

        - 'default-*.json'

        - .env

        - '*node_modules*'

        - package-lock.json

    provides:

      - name: srv-api

        properties:

          srv-url: ${default-url}

    requires:

      - name: basicnodejs-xsuaa

  - name: basicnodejs-approuter

    type: approuter.nodejs

    path: app

    build-parameters:

      ignore:

        - 'default-*.json'

        - .env

        - '*node_modules*'

        - package-lock.json

    parameters:

      memory: 256M

      disk-quota: 512M

      keep-existing-routes: true

    requires:

      - name: srv-api

        group: destinations

        properties:

          name: srv-api # must be used in xs-app.json as well

          url: ~{srv-url}

      	  forwardAuthToken: true

      - name: basicnodejs-xsuaa

resources:

 - name: basicnodejs-xsuaa

   type: org.cloudfoundry.managed-service

   parameters:

     service: xsuaa

     service-plan: application

     config:

        xsappname: basicnodejs-${org}-${space}

        tenant-mode: dedicated
```

Please notice we have added one more property inside approuter module.

forwardAuthToken: true

It will not use the authentication mechanism in BTP until we mention the parameter route in xs-app.json.

```
{

    "authenticationMethod": "route",

    "routes": [{

        "source": "^/(.*)$",

        "target": "$1",

        "destination": "srv-api"

    }]

}
```

This will redirect us to the BTP login page if you are not logged in.

Even if we provide the BTP credentials we can not access our desired application.

One more parameter in the XSUAA service tells where to redirect after the authentication.

```
resources:

 - name: basicnodejs-xsuaa

   type: org.cloudfoundry.managed-service

   parameters:

     service: xsuaa

     service-plan: application

     config:

        xsappname: basicnodejs-${org}-${space}

        tenant-mode: dedicated

        oauth2-configuration:

          redirect-uris:

          - "https://*.hana.ondemand.com/**"
```

Deploy and execute the approuter. It will ask you to login and then landed you on the Service.

Wait….. Even though we have done the authentication mechanism, we are able to access the direct basicnodejs-service url in BTP.

Because we have not provided any condition in the service, whether the user is authenticated by the XSUAA. In CAPM it is handled by the framework.

But our case we have to do it manually.

Let's add some npm packages and modify server.js file.

```
npm install @sap/xsenv @sap/xssec passport
```

In srv -> server.js file -

```
const express = require("express");

const passport = require("passport");

const xsenv = require("@sap/xsenv");

const JWTStrategy = require("@sap/xssec").JWTStrategy;

const services = xsenv.getServices({ uaa:"basicnodejs-xsuaa" });  // XSUAA service

const app = express();

passport.use(new JWTStrategy(services.uaa));

app.use(passport.initialize());

app.use(passport.authenticate("JWT", { session: false }));

app.get("/", function (req, res, next) {

  res.send("Welcome User: " + req.user.name.givenName);

});

const port = process.env.PORT || 5000;

app.listen(port, function () {

  console.log("Basic NodeJs listening on port " + port);

});
```

Build and deploy mta.yaml

Now try to execute the basicnodejs-service url from BTP.

![](/legacyfs/online/storage/blog_attachments/2023/03/16-7.png)

Execute Approuter -

![](/legacyfs/online/storage/blog_attachments/2023/03/17-11.png)

In this part, created the xsuaa instance and run the app from approuter only.

Next, we will run the same app from BAS itself.

*[>> Part – 3: Run app locally.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-3/)*

*[<< Part – 1: Create nodejs application.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally/)*

* [NodeJS](/t5/tag/NodeJS/tg-p/board-id/technology-blog-members)
* [sap btp](/t5/tag/sap%20btp/tg-p/board-id/technology-blog-members)

3 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnol...