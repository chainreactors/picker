---
title: Run NodeJs in SAP BTP and Locally, Part – 1
url: https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally/
source: SAP Blogs
date: 2023-03-20
fetch_date: 2025-10-04T10:05:19.617133
---

# Run NodeJs in SAP BTP and Locally, Part – 1

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Run NodeJs in SAP BTP and Locally, Part - 1

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160518&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Run NodeJs in SAP BTP and Locally, Part - 1](/t5/technology-blog-posts-by-members/run-nodejs-in-sap-btp-and-locally-part-1/ba-p/13552757)

![DebashishDas](https://avatars.profile.sap.com/d/7/idd75a2e80338e3be985cb2169d87aa8fb8ed01a1e2e6f4ff7c94f61a7c9d49849_small.jpeg "DebashishDas")

[DebashishDas](https://community.sap.com/t5/user/viewprofilepage/user-id/121928)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160518)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160518)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552757)

‎2023 Mar 19
9:12 AM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160518/tab/all-users "Click here to see who gave kudos to this post.")

8,159

* SAP Managed Tags
* [SAP Business Application Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Application%2520Studio/pd-p/67837800100800007077)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)

* [SAP Business Application Studio

  SAP Business Application Studio](/t5/c-khhcw49343/SAP%2BBusiness%2BApplication%2BStudio/pd-p/67837800100800007077)
* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)

View products (2)

This blog series is just a simple demo of how to create any Nodejs app and run it on both the local and SAP BTP platform.

**Part – 1: Create nodejs application.**

[*Part – 2: Create Authentication instance.*](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-2/)

[Part – 3: Run app locally.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-3/)

**Create Local NodeJs application**

First create folder basicnodejs.

Then inside create another folder srv, which will be for service providers.

Now from the terminal change the directory and go inside srv folder. we will need package.json file inside srv file.

Run command:

```
npm init --y
```

![](/legacyfs/online/storage/blog_attachments/2023/03/1-49.png)

Now add/modify under scripts.

```
"start": "node server.js"
```

Whenever we run npm run start, it will execute the file server.js

![](/legacyfs/online/storage/blog_attachments/2023/03/2-29.png)

We have to install express package- npm install express

![](/legacyfs/online/storage/blog_attachments/2023/03/3-31.png)

Create a server.js file inside srv folder, and add the below code

![](/legacyfs/online/storage/blog_attachments/2023/03/4-22.png)

Execute the command – npm run start

```
npm run start
```

Our node js application is running the static port 5000 that we have mentioned.

![](/legacyfs/online/storage/blog_attachments/2023/03/5-22.png)

Now let's create a simple mta.yaml file in the root directory and Provide the details to mta for  deployment details for Service  –

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
```

Now build and deploy the mta.yaml to BTP. It will create a basicnodejs-service application under the dev space.

Click on the URL of the application.

![](/legacyfs/online/storage/blog_attachments/2023/03/7-16.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/8-11.png)

We can access without any restriction from anywhere without having a BTP account.

So to make it restricted we will use approuter and authentication service in BTP.

Creating AppRouter:

For approuter, or to handle the routing, create app folder and package.json inside it

Install [@Sisn](/t5/user/viewprofilepage/user-id/1387241)/approuter inside app folder as a npm package.

```
npm install @sap/approuter
```

Now add the script to the package.json file -

```
"start": "node node_modules/@sap/approuter/approuter.js"
```

![](/legacyfs/online/storage/blog_attachments/2023/03/9-13.png)

Now we have to create the file xs-app.json, which is required by approuter. That will handle the routes.

![](/legacyfs/online/storage/blog_attachments/2023/03/10-15.png)

“srv-api” is a name that holds some information of a destination url.

Lets create the approuter module.

```
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
```

Now if we deployed the mta with these details only. It will crash.

Approuter will require some parameters which will be provided by the basicnodejs-service module.

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
```

basicnodejs-service provides configuration variables which will be required in basicnodejs-approuter

Now again build and deploy the mta.yaml

![](/legacyfs/online/storage/blog_attachments/2023/03/12-12.png)

We can check the User-Provided Variables. and find the variables that we have set in the approuter requires section.

![](/legacyfs/online/storage/blog_attachments/2023/03/13-14.png)

Now open the approuter url. We can access it without any credentials.

![](/legacyfs/online/storage/blog_attachments/2023/03/14-11.png)

In this part, created two modules. which can be accessed by anyone on the internet.

We will create authentication to restrict the service module. Only through approuter the service module will be accessible.

[*>>  Part – 2: Create Authentication instance.*](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-2/)

* [sap btp](/t5/tag/sap%20btp/tg-p/board-id/technology-blog-members)
* [SAP BTP NodeJs](/t5/tag/SAP%20BTP%20NodeJs/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwi...