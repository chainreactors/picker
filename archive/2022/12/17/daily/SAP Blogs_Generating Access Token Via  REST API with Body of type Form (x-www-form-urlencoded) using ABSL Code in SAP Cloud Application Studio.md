---
title: Generating Access Token Via  REST API with Body of type Form (x-www-form-urlencoded) using ABSL Code in SAP Cloud Application Studio
url: https://blogs.sap.com/2022/12/16/generating-access-token-via-rest-api-with-body-of-type-form-x-www-form-urlencoded-using-absl-code-in-sap-cloud-application-studio/
source: SAP Blogs
date: 2022-12-17
fetch_date: 2025-10-04T01:46:06.897870
---

# Generating Access Token Via  REST API with Body of type Form (x-www-form-urlencoded) using ABSL Code in SAP Cloud Application Studio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Generating Access Token Via REST API with Body of...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159997&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Generating Access Token Via REST API with Body of type Form (x-www-form-urlencoded) using ABSL Code in SAP Cloud Application Studio](/t5/technology-blog-posts-by-members/generating-access-token-via-rest-api-with-body-of-type-form-x-www-form/ba-p/13549601)

![msalmani](https://avatars.profile.sap.com/e/0/ide01fadfb8b08f371a1fe9683c864e9265dbeb09bc3ec9c8e0948ed51685c31cc_small.jpeg "msalmani")

[msalmani](https://community.sap.com/t5/user/viewprofilepage/user-id/43930)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159997)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159997)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549601)

‎2022 Dec 16
8:13 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159997/tab/all-users "Click here to see who gave kudos to this post.")

4,129

* SAP Managed Tags
* [SAP Cloud Applications Studio](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Applications%2520Studio/pd-p/67837800100800006741)
* [SAP Sales Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Sales%2520Cloud/pd-p/73554900100700002221)
* [SAP Service Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Service%2520Cloud/pd-p/73555000100700000801)
* [C4C Sales](https://community.sap.com/t5/c-khhcw49343/C4C%2520Sales/pd-p/825493229490678079515430289276035)
* [C4C Service](https://community.sap.com/t5/c-khhcw49343/C4C%2520Service/pd-p/569449780209093647095570245113309)

* [SAP Cloud Applications Studio

  SAP Cloud Applications Studio](/t5/c-khhcw49343/SAP%2BCloud%2BApplications%2BStudio/pd-p/67837800100800006741)
* [C4C Sales

  Software Product Function](/t5/c-khhcw49343/C4C%2BSales/pd-p/825493229490678079515430289276035)
* [C4C Service

  Software Product Function](/t5/c-khhcw49343/C4C%2BService/pd-p/569449780209093647095570245113309)
* [SAP Sales Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BSales%2BCloud/pd-p/73554900100700002221)
* [SAP Service Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BService%2BCloud/pd-p/73555000100700000801)

View products (5)

# 1. Introduction

In this blog, we will learn, how to generate Access Token Via REST API with Body of type Form using ABSL Code in SAP Cloud Application Studio. We will at first show how we can do the same using Postman and afterwards go to the details of sending this request using ABSL Code.

# 2. Sending Request Using Postman

## 2.1. Maintaining Body

In Postman we can send such Body using "x-www-form-urlencoded":

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-1.jpg)

Image 01: Body in type Form

After selecting this type, we can input key and values as following or we can use "Bulk Edit" to maintain them in bulk mode:

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-1-1.jpg)

Image 02: Key and Values - Body

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-2.jpg)

Image 03: Key and Values in Bulk Edit - Body

## 2.2. Maintaining Endpoint and Authorization

Rather than maintaining Body, we should maintain also Method, Endpoint and Authorization (in our example is Basic):

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-3.jpg)

Image 04: Request Endpoint and Authorization

## 2.3. Maintaining Header

Furthermore, we should add "Content-Type: application/x-www-form-urlencoded" as a header parameter:

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-4.jpg)

Image 05: Request Header

## 2.4. Generating Token

Once we send the request, access token will be generated:

![](/legacyfs/online/storage/blog_attachments/2022/11/Postman-5.jpg)

Image 06: Sending Request

# 3. Sending Request Using ABSL Code in SAP Cloud Application Studio

## 3.1. Add a new External Web Service

Now, we can implement the same request using SAP Cloud Application Studio. In this regard, we should at first add a new "External Web Service Integration" to the desired solution:

![](/legacyfs/online/storage/blog_attachments/2022/11/SDK-1.jpg)

Image 07: Adding External Web Service Integration

In the next screen, we select "REST" as web service type and press "Next":

![](/legacyfs/online/storage/blog_attachments/2022/11/SDK-2.jpg)

Image 08: Determine Web Service Type

Then we give Endpoint for generating access token and press "Next":

![](/legacyfs/online/storage/blog_attachments/2022/11/SDK-3.jpg)

Image 09: Configure REST API Endpoint

Afterwards, we select "Create Communication Scenario" and determine its name via "Communication Scenario Name" and and press "Next":

![](/legacyfs/online/storage/blog_attachments/2022/11/SDK-4.jpg)

Image 10: Create Communication Service

Finally, we review it and and press "Finish":

![](/legacyfs/online/storage/blog_attachments/2022/11/SDK-5.jpg)

Image 11: Review and finalizing the Web Service

## 3.2. Managing Communication Arrangement

Now, we can maintain communication arrangement by right click on the Communication Scenario in SDK and select "Manage Communication Arrangement":

![](/legacyfs/online/storage/blog_attachments/2022/11/SDK-6.jpg)

Image 12: Manage Communication Arrangement

Afterwards, we will be redirected to a C4C screen in which we can create a new communication arrangement:

![](/legacyfs/online/storage/blog_attachments/2022/11/C4C-1.jpg)

Image 13: Create a new Communication Arrangement 01

In the next step, we select the created communication scenario in SAP Cloud Application Studio:

![](/legacyfs/online/storage/blog_attachments/2022/11/C4C-2.jpg)

Image 14: Create a new Communication Arrangement 02

Then, we select the created web service in SAP Cloud Application Studio:

![](/legacyfs/online/storage/blog_attachments/2022/11/C4C-3-1.jpg)

Image 15: Create a new Communication Arrangement 03

In the next screen, we can maintain "Authentication Method" and "Credentials":

![](/legacyfs/online/storage/blog_attachments/2022/11/C4C-4.jpg)

Image 16: Create a new Communication Arrangement 04

Now, we are done and can finish and activate the communication arrangement:

![](/legacyfs/online/storage/blog_attachments/2022/11/C4C-5.jpg)

Image 17: Create a new Communication Arrangement 04

## 3.3. Developing an ABSL Function to Send the Request

Then, we can develop an ASBL function to send the request and generate Access Token. We should determine ServiceName and ServiceScenario based on what we created already in SAP Cloud Application Studio and then define HttpMethod. Because we want to send a body of type "Form", ContentType should be "application/x-www-form-urlencoded" and Key and Values of Body should be separated by ampersand "&".

![](/legacyfs/online/storage/blog_attachments/2022/12/C4C-6-1.jpg)

Image 18: Send a Request using ABSL Code

As we see above, we should use "WebServiceUtilities.ExecuteRESTServiceWithoutEncoding" to send such a requests with Body of type...