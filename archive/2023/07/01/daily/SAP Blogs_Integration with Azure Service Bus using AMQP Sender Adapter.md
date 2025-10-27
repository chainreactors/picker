---
title: Integration with Azure Service Bus using AMQP Sender Adapter
url: https://blogs.sap.com/2023/06/30/integration-with-azure-service-bus-using-amqp-sender-adapter/
source: SAP Blogs
date: 2023-07-01
fetch_date: 2025-10-04T11:54:02.148866
---

# Integration with Azure Service Bus using AMQP Sender Adapter

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Integration with Azure Service Bus using AMQP Send...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161318&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Integration with Azure Service Bus using AMQP Sender Adapter](/t5/technology-blog-posts-by-members/integration-with-azure-service-bus-using-amqp-sender-adapter/ba-p/13557615)

![purusottam_agar](https://avatars.profile.sap.com/b/8/idb81a0f7cf2e4aa3f6d147f09fb239618a9c646e38ffdffb6030b0f6b175adb01_small.jpeg "purusottam_agar")

[purusottam\_agar](https://community.sap.com/t5/user/viewprofilepage/user-id/135926)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161318)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161318)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557615)

‎2023 Jun 30
9:57 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161318/tab/all-users "Click here to see who gave kudos to this post.")

3,997

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)

View products (2)

**Introduction**

AMQP sender adapter is used to poll messages from message broker like Azure service bus, RabbitMQ,Google PubSub,SAP Event Mesh etc.In this blog I will be using Azure Service Bus.

I connected Microsoft Azure Service Bus(ASB) to SAP Integration Suite using AMQP sender adapter and configured  the parameters like connection details and processing details.

![](/legacyfs/online/storage/blog_attachments/2023/06/Azure-Service-bus.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/AMQP_PROCESSING_WITHOUT_Host.png)

Initially it was a challenge to connect to Azure service bus topics because of not using the term "subscriptions" in Queue name in processing tab.

The Queue name value should be in the below format(for Topics).

Topic\_Name/subscriptions/Subscription\_Name.

So in the below screenshot I have used the term "subscriptions" in Queue name and messages were successfully received in integration flow from Azure Service bus.

![](/legacyfs/online/storage/blog_attachments/2023/06/AMQP_Processing2.png)

 So make sure to use "subscriptions" in Queue Name parameters for polling messages from Azure service bus topics.

Reference

[https://blogs.sap.com/2019/11/20/cloud-integration-connecting-to-external-messaging-systems-using-th...](https://blogs.sap.com/2019/11/20/cloud-integration-connecting-to-external-messaging-systems-using-the-amqp-adapter/)

* [SAPIntegrationSuiteCommunityChallenge2023](/t5/tag/SAPIntegrationSuiteCommunityChallenge2023/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fintegration-with-azure-service-bus-using-amqp-sender-adapter%2Fba-p%2F13557615%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [SAP BTP CI CD service for on premise S4 HANA systems RICEFW applications](/t5/technology-q-a/sap-btp-ci-cd-service-for-on-premise-s4-hana-systems-ricefw-applications/qaq-p/14234519)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  yesterday
* [SAP Build FAQ: Commercials, Getting Started and More](/t5/technology-blog-posts-by-sap/sap-build-faq-commercials-getting-started-and-more/ba-p/14233744)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  yesterday
* [SAP S4HANA Plant Maintenance for dummies](/t5/technology-blog-posts-by-members/sap-s4hana-plant-maintenance-for-dummies/ba-p/14234304)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Project-Based Services in SAP S/4HANA](/t5/technology-blog-posts-by-members/project-based-services-in-sap-s-4hana/ba-p/14234290)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday
* [Organizational Management in SAP S/4HANA HCM](/t5/technology-blog-posts-by-members/organizational-management-in-sap-s-4hana-hcm/ba-p/14234285)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  yesterday

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69efed1_small.jpeg "Sandra_Rossi")  Sandra\_Rossi](/t5/user/viewprofilepage/user-id/145194) | 4 |
| [![mickaelquesnot](https://avatars.profile.sap.com/5/9/id592e9cc97ec986f0d6ae5e9db725546658112960aaef6e03a2a7680bb1496070_small.jpeg "mickaelquesnot")  mickaelquesnot](/t5/user/viewprofilepage/user-id/150004) | 4 |
| [![smarchesini](https://avatars.profile.sap.com/0/c/id0cf1ddd928dd875ac324a5701f9e4d9a60995d0072e5b58f718f5dd57231fae9_small.jpeg "smarchesini")  ![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion") smarchesini](/t5/user/viewprofilepage/user-id/125739) | 3 |
| [![natanael1](https://avatars.profile.sap.com/5/7/id5755ebef974c12476c62d649735972c696010b8bb05e4ebc3ac052476ea15035_small.jpeg "natanael1")  natanael1](/t5/user/viewprofilepage/user-id/1557162) | 3 |
| [![dylan-drummond](https://avatars.profile.sap.com/0/0/id00cf6ce5e32b466c407ed6996e23a9b60703442ad43de8fe0e22782d75a73afb_small.jpeg "dylan-drummond")  dylan-drummond](/t5/user/viewprofilepage/user-id/197587) | 3 |
| [![Sharathmg](https://avatars.profile.sap.com/e/7/ide723da06d875310cb4cfc1b63341690484fa5a6c39220ef7d6ff0f1de992d174_small.jpeg "Sharathmg")  Shara...