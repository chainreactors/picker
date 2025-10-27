---
title: How to call SAP DMC WebServices through Node-RED
url: https://blogs.sap.com/2023/03/21/how-to-call-sap-dmc-webservices-through-node-red/
source: SAP Blogs
date: 2023-03-22
fetch_date: 2025-10-04T10:14:47.316673
---

# How to call SAP DMC WebServices through Node-RED

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Product Lifecycle Management](/t5/product-lifecycle-management/ct-p/plm)
* [PLM Blog Posts by Members](/t5/product-lifecycle-management-blog-posts-by-members/bg-p/plm-blog-members)
* How to call SAP DMC WebServices through Node-RED

Product Lifecycle Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/plm-blog-members/article-id/1431&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to call SAP DMC WebServices through Node-RED](/t5/product-lifecycle-management-blog-posts-by-members/how-to-call-sap-dmc-webservices-through-node-red/ba-p/13553352)

![marcobarat](https://avatars.profile.sap.com/4/b/id4bcd82bdadfaa388001881efbc05f486fa35de0b71c1220ca384ab8069526ef1_small.jpeg "marcobarat")

[marcobarat](https://community.sap.com/t5/user/viewprofilepage/user-id/129227)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=plm-blog-members&message.id=1431)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/plm-blog-members/article-id/1431)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553352)

‎2023 Mar 21
11:43 PM

[10
Kudos](/t5/kudos/messagepage/board-id/plm-blog-members/message-id/1431/tab/all-users "Click here to see who gave kudos to this post.")

2,793

* SAP Managed Tags
* [SAP Digital Manufacturing](https://community.sap.com/t5/c-khhcw49343/SAP%2520Digital%2520Manufacturing/pd-p/73555000100800001492)

* [SAP Digital Manufacturing

  SAP Digital Manufacturing](/t5/c-khhcw49343/SAP%2BDigital%2BManufacturing/pd-p/73555000100800001492)

View products (1)

Hello everybody! Today, I'd like to show you how to easily integrate Node-RED with SAP DMC to obtain the list of all active SFCs within a Workcenter. This integration opens up a world of possibilities for automating processes and optimizing workflows.

## Why Node-RED?

Node-RED is an open-source visual programming tool that allows users to create complex logic flows for IoT (Internet of Things) applications, APIs, and other backend systems. It was developed by IBM Emerging Technology in 2013 and has since become popular among developers due to its user-friendly interface and extensibility.

With Node-RED, users can create "flows" using a drag-and-drop interface. A flow is a series of nodes that are connected together to perform a specific task or set of tasks. These flows can be customized using a wide range of pre-built nodes or by creating custom nodes using JavaScript.

Node-RED is often used for IoT applications, where it can connect to various devices and sensors to collect and process data. However, it can also be used for other backend systems such as APIs, databases, and messaging systems. Its extensibility allows it to be integrated with a wide range of systems, making it a powerful tool for developers looking to create complex backend logics.

## **The scenario**

I know this scenario may seem straightforward, but by learning how to integrate SAP DMC REST API with Node-RED, you can unleash your creativity and extend your DMC's capabilities to achieve anything you can imagine. With Node-RED's visual programming interface, you can easily create custom workflows that fit your specific business needs.

So let's get started and see what we can achieve with this powerful combination of technologies!

## **Pre-requisites**

* a “Service-key” created inside SAP BTP – DMC subaccount

  + Auth-token url

  + Auth url

  + Client-id

  + Client-key

SAP DMC expose a lot of “standard” services that could be used through lots of different programming languages, like:

* Java

* Javascript

* ABAP

* others

and by reaching the official documentation (<https://api.sap.com/package/SAPDigitalManufacturingCloud/rest>) you can expand your horizon and learn all the services (old and new) are available for the purpose of extend your SAP DMC environment.

## **Let’s start!**

Create a new flow inside Node-RED and install a new library named “node-red-contrib-oauth2”:![](/legacyfs/online/storage/blog_attachments/2023/03/1-51.png)

this node will be used in order to obtain the bearer token and arrange the REST API Call.

Now, on our flow from scratch add a “inject” node and then attach the OAUTH node:

![](/legacyfs/online/storage/blog_attachments/2023/03/2-31.png)

and now configure the oauth2 code like follow:

![](/legacyfs/online/storage/blog_attachments/2023/03/3-32.png)

* *Grant Type*: Client Credentials

* *Access Token Url*: open SAP BTP DMC subaccount (cloudfoundry), go “Instances and Subscriptions”, go to “Instances” and open the key, here, check for the “url” and attach at the end of the url “/oauth/token”

* *Client ID*: search for client id

* *Client Secret*: search for Client Secret

If everything is fine, inside “msg.oauth2Response.access\_token” there will be our bearer token and we are ready to make our first call!

Now, add a “function code” in order to prepare the header of the HTTP call and paste this code inside:

```
msg.headers = {

Authorization: "Bearer " + msg.oauth2Response.access_token}

return msg;
```

![](/legacyfs/online/storage/blog_attachments/2023/03/4-24.png)

now let’s add the HTTP in node, this will be used to perform a “Get” request inside SAP DMC, in particular:

<https://api.sap.com/api/sapdme_sfc/tryout>

![](/legacyfs/online/storage/blog_attachments/2023/03/5-23.png)

(here, you can configure your environment and try the API exposed by SAP DMC! This is useful in order to obtain the URL to be used inside Node-RED).

Add the HTTP IN node:

![](/legacyfs/online/storage/blog_attachments/2023/03/6-18.png)

and configure it as:

![](/legacyfs/online/storage/blog_attachments/2023/03/7-17.png)

inside URL: get the url from the “try out”, for example, for us, we are in “Demo” env, so the url is like:
*<https://api.test.eu20.dmc.cloud.sap/sfc/v1/sfcsInWork?plant=ZZZ&resource=YYY>* please replace ZZZwith your Plant and YYY with your Resource name.

**Important note: the url depends on the server where your BTP is deployed, in this case, we are in EU20, and this is a Test environment.**

Now, add a “Debug” node in order to print the result:

![](/legacyfs/online/storage/blog_attachments/2023/03/8-12.png)

And now, let’s try by clicking on Inject node and check the result of the debug:

![](/legacyfs/online/storage/blog_attachments/2023/03/9-14.png)

As you can see, we obtained the list of SFCs (in this case is only one) that are available inside our given Workcenter!

Node-RED is an extremely powerful tool that allows for easy integration with SAP DMC. By accessing the REST APIs exposed by SAP DMC through the link provided above, users can plan and build their own custom logic flows using Node-RED. This makes it possible to create tailored solutions that are specific to the needs of individual businesses, using a user-friendly visual programming interface.

* [node-RED](/t5/tag/node-RED/tg-p/board-id/plm-blog-members)
* [sap dmc](/t5/tag/sap%20dmc/tg-p/board-id/plm-blog-members)
* [sfc](/t5/tag/sfc/tg-p/board-id/plm-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2F...