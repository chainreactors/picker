---
title: How to run SAP DWC Task Chain from SAP BTP Cloud Foundry
url: https://blogs.sap.com/2023/01/10/how-to-run-sap-dwc-task-chain-from-sap-btp-cloud-foundry/
source: SAP Blogs
date: 2023-01-11
fetch_date: 2025-10-04T03:31:37.453439
---

# How to run SAP DWC Task Chain from SAP BTP Cloud Foundry

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to run SAP DWC Task Chain from SAP BTP Cloud F...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162762&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to run SAP DWC Task Chain from SAP BTP Cloud Foundry](/t5/technology-blog-posts-by-members/how-to-run-sap-dwc-task-chain-from-sap-btp-cloud-foundry/ba-p/13565558)

![manasij_biswas](https://avatars.profile.sap.com/b/6/idb6be742fd11673956735e099525854610ab8f9363108d0f308eeba99370d000c_small.jpeg "manasij_biswas")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[manasij\_biswas](https://community.sap.com/t5/user/viewprofilepage/user-id/836196)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162762)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162762)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565558)

‎2023 Jan 10
11:11 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162762/tab/all-users "Click here to see who gave kudos to this post.")

5,728

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

Purpose:

The purpose of this blog is to explain how SAP DWC task chain can be scheduled or executed from SAP BTP cloud foundry environment using Node JS, so that SAP BTP can be used as a universal scheduling platform.

SAP DWC Task Chain:

SAP Task Chain is used to execute series of task like Table Replication, View Persistency and Data Flow runs. We can compare SAP DWC Task Chain with SAP BW Process Chain.

1. In this blog Sample Task Chain to persist view will be created.

2. That task chain will be executed from SAP BTP Cloud Foundry environment using Node JS.

3. For Authentication purpose Oauth 2.0 will be used

SAP Data Warehouse Cloud provides a public OData API to execute APIs inside DWC.

Here OAuth2.0 authorization with grant type Authorization Code is being used to authenticate request from Node JS.

Technical Details:

Let’s first create a simple Task chain which will persist data of a remote table.

![](/legacyfs/online/storage/blog_attachments/2023/01/2-12.jpg)

Let’s find out the backend executable link generated while executing Task Chain in DWC.

Open inspect from browser before executing Task chain. Open network tab as shown in below screenshot.

![](/legacyfs/online/storage/blog_attachments/2023/01/3-7.jpg)

Now hit Execute. As shown in below screenshot request url “\*/start” is being used in backend to execute task chain in SAP DWC.

![](/legacyfs/online/storage/blog_attachments/2023/01/4-10.jpg)

Now we will execute this “\*/start” URL from node js to execute task chain.

Technical set-up:

In SAP Data Warehouse Cloud, create an OAuth Client with the following specifications:

Purpose: Interactive Usage

Redirect URI: We will discuss about this URL later

![](/legacyfs/online/storage/blog_attachments/2023/01/5-4.jpg)

Note down OAuth Client ID and Secret code, we will use this information in Node JS to execute Task Chain.

Note down below authorization URL and Token URL from SAP DWC App Integration

![](/legacyfs/online/storage/blog_attachments/2023/01/6-3.jpg)

Now let’s create Node JS project to execute Task Chain

Passing Authorization URL, Token URL, ClientID, Client Secret & Call back URL from SAP DWC as mentioned earlier to get access token from SAP DWC.

![](/legacyfs/online/storage/blog_attachments/2023/01/7-3.jpg)

Lets try to post “\*/start” with above information in Postman to check if this process is working.

Go to Postman and enter Authorization URL, Token URL, ClientID, Client Secret & Call back URL.

![](/legacyfs/online/storage/blog_attachments/2023/01/8-3.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/9-4.jpg)

After entering above information click Get New Access Token

![](/legacyfs/online/storage/blog_attachments/2023/01/10-3.jpg)

After successful authentication clink Use Token. Then click on Send

![](/legacyfs/online/storage/blog_attachments/2023/01/11-4.jpg)

Status Code 202 – Job successfully executed, check SAP DWC integration monitor if the Task chain is running.

![](/legacyfs/online/storage/blog_attachments/2023/01/12-3.jpg)

Task Chain ran successfully in DWC.

![](/legacyfs/online/storage/blog_attachments/2023/01/13-3.jpg)

Let’s get back to Node JS code.

Passing access token for validation of request.

![](/legacyfs/online/storage/blog_attachments/2023/01/14-2.jpg)

Here is the main code to Post start URL with Access Token and Cookies generated from above code.

![](/legacyfs/online/storage/blog_attachments/2023/01/15-4.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/01/16-4.jpg)

Now let’s Push this code in SAP BTP Cloud Foundry.

![](/legacyfs/online/storage/blog_attachments/2023/01/17-2.jpg)

App successfully deployed in Cloud Foundry.

![](/legacyfs/online/storage/blog_attachments/2023/01/18-2.jpg)

Now go to SAP BTP Cloud Foundry and get the URL of the deployed APP.

![](/legacyfs/online/storage/blog_attachments/2023/01/19-3.jpg)

Now take the URL and add “/auth/callback”, this will be redirect URL. We have mentioned same URL in Node JS as shown in below screenshot.

![](/legacyfs/online/storage/blog_attachments/2023/01/20-2.jpg)

Put this URL in OAuth client Redirect URL section in SAP DWC.

![](/legacyfs/online/storage/blog_attachments/2023/01/21-2.jpg)

Now execute App URL from SAP BTP with “/auth” added at the end.

Lets check Integration Monitor in SAP DWC.  Task Chain started running.

Done ![:smiling_face_with_smiling_eyes:](/html/@94401D39447508D148B9179130A10607/emoticons/1f60a.png ":smiling_face_with_smiling_eyes:")

![](/legacyfs/online/storage/blog_attachments/2023/01/22-2.jpg)

We can schedule this node JS application periodically from SAP BTP Job Scheduling Service.

![](/legacyfs/online/storage/blog_attachments/2023/01/23-2.jpg)

Check below blog to know how to schedule application in SAP BTP.

[SAP BTP Cloud foundry Job Scheduling for CAP based project | SAP Blogs](https://blogs.sap.com/2021/03/15/sap-btp-cloud-foundry-job-scheduling-for-cap-based-project/)

To execute failed Task Chain replace “start” with “/retry” in the execution URL.

Appendix 3: All Project Files

In this appendix you can find all files required to run the described sample application.

manifest.yml

```
---

applications:

- name: TaskChainRun

  random-route: true

  buildpack: nodejs_buildpack

  memory: 512M

  command: node index
```

package.json

```
{

  "name": "node",

  "version": "1.0.0",

  "description": "",

  "main": "index.j...