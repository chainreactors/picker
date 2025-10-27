---
title: Building a bot using Microsoft’s Power Virtual Agent on S/4 HANA on-premise… using SAP BTP
url: https://blogs.sap.com/2023/03/16/building-a-bot-using-microsofts-power-virtual-agent-on-s-4-hana-on-premise-using-sap-btp/
source: SAP Blogs
date: 2023-03-17
fetch_date: 2025-10-04T09:50:44.644621
---

# Building a bot using Microsoft’s Power Virtual Agent on S/4 HANA on-premise… using SAP BTP

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Building a bot using Microsoft’s Power Virtual Age...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159824&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Building a bot using Microsoft’s Power Virtual Agent on S/4 HANA on-premise… using SAP BTP](/t5/technology-blog-posts-by-members/building-a-bot-using-microsoft-s-power-virtual-agent-on-s-4-hana-on-premise/ba-p/13548431)

![sdeshmukh37](https://avatars.profile.sap.com/2/7/id27edb57de4a0bb6f31f8292adda815a84d0c110b68a0dcc97be1b829f2703106_small.jpeg "sdeshmukh37")

[sdeshmukh37](https://community.sap.com/t5/user/viewprofilepage/user-id/12534)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159824)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159824)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548431)

‎2023 Mar 16
9:36 PM

[14
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159824/tab/all-users "Click here to see who gave kudos to this post.")

4,684

* SAP Managed Tags
* [SAP Conversational AI](https://community.sap.com/t5/c-khhcw49343/SAP%2520Conversational%2520AI/pd-p/73555000100800001301)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Conversational AI

  SAP Business AI](/t5/c-khhcw49343/SAP%2BConversational%2BAI/pd-p/73555000100800001301)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

Few months back I started exploring SAP BTP and realized that it’s a such a huge topic in itself that its nearly impossible to learn every bit of it.

So I picked one topic [SAP Conversational AI](https://cai.tools.sap/) and started building a quick bot. My objective was to build a bot in conversation AI that pulls data from S4HANA on-premise system. So I started with Sales Order bot.

However few weeks back, I read on SAP service discovery center that SAP has [retired their Conversational AI product](https://discovery-center.cloud.sap/servicessearch/Conversational%20AI/). Which means now I need to find some other bot solution that help me achieve the same result i.e. Building Bot that pulls data/posts transaction to S/4 HANA on-premise.

Why I chose on-premise is because lot of customers are yet on ECC / S4HANA on-premise and not on cloud. Still they want to explore possibilities where BTP will help their business.

Building such bots will definitely ease out the job of SAP Business users from being always connected to system to perform any operation using SAP Fiori or SAP GUI. Even though SAP Fiori apps can be opened on Mobile, its not straight forward to simply open a app on mobile . Lets suppose I want to get the status of my order or invoice why not to give a simple solution of a bot that is embedded within Microsoft Teams. Users have to only use the mobile to chat with a Bot via Teams and get the details that they wish to in couple of seconds. and this to be achieved while on-premise ERP is in a secure zone.

So here it looks like:

![](/legacyfs/online/storage/blog_attachments/2023/03/img1.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/img2.png)

There could be multiple ways that Power Agent or for that matter Bot developed in any other technology, can pass the data to on-premise ECC. What I am using is through BTP Cloud Integration.

Okay .. now let us understand the Architecture that I used…

![](/legacyfs/online/storage/blog_attachments/2023/03/img3.png)

1. Develop custom CDS view in S/4 HANA to fetch the required data in the desired format.

2. Develop Odata service by publishing the final consumption CDS view. See the blog <https://blogs.sap.com/2016/04/06/expose-cds-views-as-odata-service/> to know how to build odata service on CDS view. If you don’t have S/4 HANA and have older ECC, you need to create Odata service using SEGW transaction that provides the required data to outside world.

3. To enable OnPremise S/4 HANA/ECC, setup a cloud connector. Please see <https://blogs.sap.com/2018/11/12/how-to-setup-cloud-connection/> to know the step by step procedure to setup the cloud connector.

4. Create a destination in your BTP account ( you can use BTP Trial account for this POC). This destination points to your on-premise ERP.

5. [Register to Cloud Integration service](https://developers.sap.com/tutorials/cp-starter-isuite-onboard-subscribe.html) and build the flow with SOAP Sender and OData receiver. This flow will accept the request from Bot in SOAP format and will forward the request to backend ERP as a OData call via secure channel. The OData response is mapped to Power Agent understandable format and forwarded to Power agent as SOAP Response

6. Build the bot in Microsoft Power Virtual Agent and use Power Automate to send the HTTP Soap request to BTP Cloud Integration and receive the response back.

7. You can deploy the bot in various channels like Microsoft Teams , Skype, Facebook, Twitter, etc.

8. For this POC, I have used Teams as this is a usual chatting platform used by most of the companies.

Now lets see the above steps in details. I will skip the CDS development, ODATA development steps and Cloud connector setup as I have provided the reference to the blogs that detail out these steps.

**Let us know functionally what the bot does:**

The Bot I have created helps to check the order/invoice status. We can even extend this further to Change the Sales Order or Create the new Order. This bot can be used by coth Sales team as well as the Business Partners.

Now let us deep dive in the solution:

**1. Develop custom CDS view in S/4 HANA to fetch the required data in the desired format.**

I have created wrapper CDS view on I\_SatesDocument that provides the required Order details. For this POC I am fetching:

* Order Status

* Shipping address

* Material Stock

* Delivery Date

My CDS view looks like

![](/legacyfs/online/storage/blog_attachments/2023/03/img4.png)

**2.** **Develop OData service by publishing the final consumption CDS view.**

![](/legacyfs/online/storage/blog_attachments/2023/03/img5.png)

**3. Enable On-premise S/4 HANA/ECC, setup a cloud connector.**

![](/legacyfs/online/storage/blog_attachments/2023/03/img6.png)

![](/legacyfs/online/storage/blog_attachments/2023/03/img7.png)

4. **Create a destination in your BTP account that points to your On-premise ERP via cloud connector**

![](/legacyfs/online/storage/blog_attachments/2023/03/img8.png)

**5. Register to Cloud Integration service and b...