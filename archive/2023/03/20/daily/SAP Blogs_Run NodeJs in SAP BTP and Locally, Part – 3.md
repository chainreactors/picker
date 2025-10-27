---
title: Run NodeJs in SAP BTP and Locally, Part – 3
url: https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-3/
source: SAP Blogs
date: 2023-03-20
fetch_date: 2025-10-04T10:05:15.165157
---

# Run NodeJs in SAP BTP and Locally, Part – 3

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Run NodeJs in SAP BTP and Locally, Part – 3

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160524&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Run NodeJs in SAP BTP and Locally, Part – 3](/t5/technology-blog-posts-by-members/run-nodejs-in-sap-btp-and-locally-part-3/ba-p/13552810)

![DebashishDas](https://avatars.profile.sap.com/d/7/idd75a2e80338e3be985cb2169d87aa8fb8ed01a1e2e6f4ff7c94f61a7c9d49849_small.jpeg "DebashishDas")

[DebashishDas](https://community.sap.com/t5/user/viewprofilepage/user-id/121928)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160524)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160524)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552810)

‎2023 Mar 19
10:25 AM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160524/tab/all-users "Click here to see who gave kudos to this post.")

4,036

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

*[Part – 2: Create Authentication instance.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-2/)*

**Part – 3: Run app locally.**

This part we will run the app from BAS using the XSUAA instance.

In srv->server.js file, going to change the port 5000 to 4000.

```
const port = process.env.PORT || 4000;
```

We have to create default destinations which will be called for our local application.

Create default-env.json file under app folder. Provide the below details –

```
"destinations": [

        {

            "name": "srv-api",

            "url": "http://localhost:4000/",

            "forwardAuthToken": true,

            "strictSSL": false

        }

    ]
```

Next, We have to provide the redirect uris for our local application, in mta.yaml .

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

            - https://*.hana.ondemand.com/**

            - https://*.trial.applicationstudio.cloud.sap/**
```

Build and deploy the mta.yaml

Now we have to bind our local app with xsuaa service.

Now build and deploy the mta.yaml, as it will update xsuaa service.

To do that in an easy way, open the command palette -> CF: bind a service locally run application

![](/legacyfs/online/storage/blog_attachments/2023/03/18-8.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/19-8.png)

Choose the required xsuaa service

![](/legacyfs/online/storage/blog_attachments/2023/03/20-5.png)

This will create the .env file, which holds the binding information of the approuter apps with xsuaa service

![](/legacyfs/online/storage/blog_attachments/2023/03/21-5.png)

Copy and paste it into default-env.json file. And format it to JSON.

![](/legacyfs/online/storage/blog_attachments/2023/03/22-10.png)

Now create add default-services.json file under srv folder. Make sure the file name should be same like default-services.json

Paste the credential part of the xsuaa service from app->default-env.json file

![](/legacyfs/online/storage/blog_attachments/2023/03/23-5.png)

Now start the service first. Navigate to the srv folder.

npm run start

![](/legacyfs/online/storage/blog_attachments/2023/03/24-6.png)

Open another terminal and navigate to app folder. start the approuter.

![](/legacyfs/online/storage/blog_attachments/2023/03/25-5.png)

Open in a New Tab

![](/legacyfs/online/storage/blog_attachments/2023/03/26-4.png)

Our App is running locally from BAS.

After making any changes server.js file, Restart the server.js.

![](/legacyfs/online/storage/blog_attachments/2023/03/27-2.png)

*[<< Part – 2: Create Authentication instance.](https://blogs.sap.com/2023/03/19/run-nodejs-in-sap-btp-and-locally-part-2/)*

**Reference links:**

<https://developers.sap.com/tutorials/btp-cf-buildpacks-node-create.html>

* [SAP BTP NodeJs](/t5/tag/SAP%20BTP%20NodeJs/tg-p/board-id/technology-blog-members)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Frun-nodejs-in-sap-btp-and-locally-part-3%2Fba-p%2F13552810%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP S/4HANA: Stop the 'Interapplication Spaghetti' 🍝 Start the Real-Time Transformation](/t5/technology-blog-posts-by-members/sap-s-4hana-stop-the-interapplication-spaghetti-start-the-real-time/ba-p/14229514)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  Saturday
* [Building a CAP service with cds‑mcp and Cline — HANDS‑ON SUPER BASIC GUIDE [ with screenshots ] 🍌](/t5/technology-blog-posts-by-members/building-a-cap-service-with-cds-mcp-and-cline-hands-on-super-basic-guide/ba-p/14223349)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [Evaluating SAP’s new MCP servers: UI5, CAP, and Fiori tools in practice](/t5/technology-blog-posts-by-members/evaluating-sap-s-new-mcp-servers-ui5-cap-and-fiori-tools-in-practice/ba-p/14205611)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  a month ago
* [SAP Business Technology Platform Blue-Green Deployment Approach in SAP BTP Cloud foundry](/t5/technology-blog-posts-by-members/sap-business-technology-platform-blue-green-deployment-approach-in-sap-btp/ba-p/14179173)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2025 Aug 22
* [Invoking LLM from Cloud Integration Responsibly – Made Easy with Generative AI Hub in SAP AI Core](/t5/technology-blog-posts-by-sap/invoking-llm-from-cloud-integration-responsibly-made-easy-with-generative/ba-p/14176222)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-bl...