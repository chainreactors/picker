---
title: SAP Private Link Service for AWS (Beta) is Available
url: https://blogs.sap.com/2022/11/22/sap-private-link-service-for-aws-beta-is-available/
source: SAP Blogs
date: 2022-11-23
fetch_date: 2025-10-03T23:29:19.527264
---

# SAP Private Link Service for AWS (Beta) is Available

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP Private Link Service for AWS (Beta) is Availab...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159436&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Private Link Service for AWS (Beta) is Available](/t5/technology-blog-posts-by-sap/sap-private-link-service-for-aws-beta-is-available/ba-p/13554928)

![philipp_becker](https://avatars.profile.sap.com/7/d/id7dc289f8d9c0d79bdb17d58045d29a875675592c077402922588bf718c9f40e7_small.jpeg "philipp_becker")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[philipp\_becker](https://community.sap.com/t5/user/viewprofilepage/user-id/448142)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159436)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159436)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554928)

‎2022 Nov 22
7:59 PM

[17
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159436/tab/all-users "Click here to see who gave kudos to this post.")

7,693

* SAP Managed Tags
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (2)

|
 **Update (2023-09-08):**  The SAP Private Link service on AWS is now Generally Available (GA)! Read all about it in [this blog post](https://blogs.sap.com/2023/09/07/sap-private-link-service-on-aws-is-now-generally-available-ga/). |

The SAP Private Link service establishes a private connection between selected SAP BTP services and selected services in your own IaaS provider accounts. By reusing the Private Link functionality of SAP's partner IaaS providers, the service lets you access your services through private network connections to avoid the need for public endpoints or data transfer via the public internet. In addition to the functionality that is already generally available for the SAP Private Link service on Azure, we're happy to announce that we now offer Beta support for SAP Private Link service on AWS. See also the [announcement from AWS](https://aws.amazon.com/blogs/awsforsap/how-to-connect-sap-btp-services-with-aws-services-using-sap-private-link-service/) on this.

### What does the Beta include?

With SAP Private Link service, Cloud Foundry applications running on SAP BTP with Amazon AWS as IaaS provider can communicate with services that support [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html) via a private connection. This ensures that traffic is not routed through the public internet, but stays within the AWS network infrastructure.

For the Beta, the SAP Private Link service supports connections to custom [AWS Endpoint Services](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html) as well as the following AWS Services:

* [Simple Storage Service (S3)](https://aws.amazon.com/s3/)

* [Simple Queue Service (SQS)](https://aws.amazon.com/sqs/)

* [Simple Notification Service (SNS)](https://aws.amazon.com/sns/)

* [Simple EMail Service (SES)](https://aws.amazon.com/ses/)

* [Relational Database Service (RDS) - Aurora Data API](https://aws.amazon.com/rds/)

The Beta will be initially available on the following [SAP BTP Cloud Foundry regions](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/f344a57233d34199b2123b9620d0bb41.html):

* cf-eu10 - Europe (Frankfurt)

* cf-us10 - US East (VA)

We plan to provide support for additional SAP BTP Cloud Foundry regions running on AWS over the course of the Beta.

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP_Private_Link_CF_AWS_Generic.jpg)

Connection from SAP BTP, Cloud Foundry environment to AWS using Private Link service

### What are possible use cases?

One possible use case is to use the SAP Private Link service to communicate with an SAP S/4HANA system or other SAP or non-SAP systems running on a VM in your own AWS account privately from within SAP BTP, Cloud Foundry environment.

This connection can be established by creating an AWS Endpoint Service that exposes an [AWS Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) which routes traffic to the SAP S/4HANA system. The service name of that AWS Endpoint Service must then be used to create an SAP Private Link service instance. As soon as the connection is established successfully, the SAP Private Link service provides a private hostname pointing to your AWS Endpoint Service.

You can also find the end-to-end S/4HANA extension scenario with step-by-step instructions, both for AWS and Azure, in [this repository](https://github.com/SAP-samples/btp-build-resilient-apps/tree/extension-privatelink/tutorials/05-PrivateLink).

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP_Private_Link_CF_AWS_NLB.jpg)

Connection from SAP BTP, Cloud Foundry environment to an AWS Load Balancer

The second use case is to use the service name of one of the supported services offered by AWS instead of a custom service name. The basic functionality is the same, but instead of a connection to a custom endpoint exposed via an AWS Endpoint Service, the connection will be established to a service natively provided by AWS, such as the Simple Queue Service.

![](/legacyfs/online/storage/blog_attachments/2022/11/SAP_Private_Link_CF_AWS_SQS.jpg)

Connection from SAP BTP, Cloud Foundry environment to AWS SQS using Private Link service

### How can I use it?

Check out our tutorials about how to

1. [Set Up SAP Private Link Service on Amazon Web Services (Beta)](https://developers.sap.com/tutorials/private-link-service-onboarding-aws.html)

2. [Connect SAP Private Link Service to AWS PrivateLink Service](https://developers.sap.com/tutorials/private-link-aws.html)

Besides that, we also provide a collection of [sample apps](https://github.com/SAP-samples/private-link-aws-services) that demonstrate how the AWS SDK has to be configured so that the traffic goes over Private Link.

### What to expect after Beta?

Currently, we support custom AWS Endpoint Services as well as a selection of services natively provided by AWS.

In the future, we plan to support the following:

* Google Cloud as IaaS provider and the corresponding [Google Cloud Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)

* Connections to other selected native AWS services, e.g. AWS Lamb...