---
title: SAP Datasphere & Partnerships – Confluent
url: https://blogs.sap.com/2023/06/10/sap-datasphere-partnerships-confluent/
source: SAP Blogs
date: 2023-06-11
fetch_date: 2025-10-04T11:45:13.175164
---

# SAP Datasphere & Partnerships – Confluent

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP Datasphere & Partnerships – Confluent

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161160&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Datasphere & Partnerships – Confluent](/t5/technology-blog-posts-by-members/sap-datasphere-partnerships-confluent/ba-p/13556677)

![pbaumann](https://avatars.profile.sap.com/c/8/idc8c457b999d268dfbaa0942f2ccff2e490f3114f22b089b9bc62ff13945b5830_small.jpeg "pbaumann")

[pbaumann](https://community.sap.com/t5/user/viewprofilepage/user-id/942)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161160)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161160)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556677)

‎2023 Jun 10
2:58 PM

0
Kudos

5,281

* SAP Managed Tags
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [Data and Analytics](https://community.sap.com/t5/c-khhcw49343/Data%2520and%2520Analytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)

* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [Data and Analytics

  Product Category](/t5/c-khhcw49343/Data%2Band%2BAnalytics/pd-p/87817424-f4e7-46f2-af14-88bf0f4ba034)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (3)

Together with [SAP Datasphere](https://news.sap.com/2023/03/sap-datasphere-power-of-business-data/), SAP launched new partnerships to complete the picture of analytical data management and the idea of a Business Data Fabric.

![](/legacyfs/online/storage/blog_attachments/2023/06/DB1-1-1.jpg)

***Fig1: SAP Datasphere & Partnerships – Source: SAP, 2023 (slightly adapted)***

For the other Partnerships look also here:

* [SAP Datasphere & Partnerships – Collibra](https://blogs.sap.com/2023/03/29/sap-datasphere-partnerships-collibra/)

* [SAP Datasphere & Partnerships – Databricks](https://blogs.sap.com/2023/03/25/sap-datasphere-partnerships-databricks/)

* [SAP Datasphere and Partnerships – DataRobot](https://blogs.sap.com/2023/05/12/sap-datasphere-and-partnerships-datarobot/) by fazam

* [SAP and Google Cloud Expand Partnership to Build the Future of Open Data and AI for Enterprises](https://news.sap.com/2023/05/sap-google-cloud-expanded-partnership-open-data-ai-enterprises/) (SAP News)

I already gave an general impression of the new partners in my blog “[SAP Datasphere – Q&A and Partnerships](https://blogs.sap.com/2023/03/12/sap-datasphere-qa-and-partnerships/)“, too. As I want to focus here on Confluent I repeat what I have written:
> **Confluent**
>
> Confluent, similar to Databricks, is a company build on another important open source software for data management – [Apache Kafka](https://kafka.apache.org/). If you have streaming data in your company, you will not pass having a look on Kafka. Confluent delivers Kafka from the cloud as a service with an optimized ecosystem.
>
> For data driven companies the speed of collecting and processing data in near-real-time is getting more and more important. If you [search the SAP Community](https://community.sap.com/search/?ct=blog&q=kafka&searchReferrer=contextual_navigation_development) you will find, that Kafka is a regular topic here, too.

If you ask yourself now what exactly the difference between Confluent and Kafka is, Confluent itself gives an answer [here](https://www.confluent.io/apache-kafka-vs-confluent/).

So, Kafka is an important building block for an Event-driven Architecture today. I have seen customers using Kafka a [Enterprise Service Bus](https://en.wikipedia.org/wiki/Enterprise_service_bus) or as backbone of their data pipelines in microservice-oriented architectures. Originally the technology was build and is still being used by LinkedIn for high throughput of streaming data.

**Event-driven Architecture**

[Gartner](https://www.gartner.com/en/information-technology/glossary/eda-event-driven-architecture) defines Event-driven Architecture as follows:
> **Event-driven architecture (EDA)** is a design paradigm in which a software component executes in response to receiving one or more event notifications. EDA is more loosely coupled than the client/server paradigm because the component that sends the notification doesn’t know the identity of the receiving components at the time of compiling.

In general the idea of Event-driven Architecture is not new in the SAP world. A very good overview about SAPs approach can be found in the blog [SAP’s Event-Driven Ecosystem Revisited](https://blogs.sap.com/2022/09/01/saps-event-driven-ecosystem-revisited/) by karsten.strothmann. He also activly went into discussion about [SAP Advanced Event Mesh vs Apache Kafka](https://answers.sap.com/questions/13850466/sap-advanced-event-mesh-vs-apache-kafka.html).

**What already works**

For sure you can find a lot of discussions about how to integrate Kafka in a SAP world like:

* [Advantco KAFKA adapter for SAP HANA Smart Data Integration (SDI)](https://blogs.sap.com/2021/02/18/advantco-kafka-adapter-for-sap-hana-smart-data-integration-sdi/)

* [Modern SAP ERP Data Integration using Apache Kafka](https://blogs.sap.com/2019/12/10/modern-sap-erp-data-integration-using-apache-kafka/)

* [Kafka to Hana Cloud](https://blogs.sap.com/2020/10/30/kafka-to-hana-cloud/)

* [S/4Hana to Kafka](https://blogs.sap.com/2020/10/06/s-4hana-to-kafka/)

* [Cloud Integration – What You Need to Know About the Kafka Adapter](https://blogs.sap.com/2021/03/16/cloud-integration-what-you-need-to-know-about-the-kafka-adapter/)

* [Build Log-based integration with SAP Data Intelligence](https://blogs.sap.com/2020/06/15/buid-log-based-integration-with-sap-data-intelligence/)

* [Ingesting Confluent/Kafka data into SAP Hana](https://blogs.sap.com/2023/06/11/ingesting-confluent-kafka-data-into-sap-hana)

In [2020 Kai Waehner](https://www.kai-waehner.de/blog/2020/08/25/kafka-sap-integration-alternatives-connectors-erp-r3-ecc-s4-hana-soap-rest-http-web-service-api-sdk-java/), Global Field CTO of Confluent, already showed different options how to connect Kafka with SAP systems. In general he saw and discussed the following opitions:

* Traditional middleware (ETL/ESB)

* Web services (SOAP/REST)

* 3rd party turnkey solutions

* Kafka-native connectivity with Kafka Connect

* Custom glue code using SAP SDKs

**The partnership**

So why this partnership?

[According to Erica Schultz](https://www.sap.com/assetdetail/2023/03/6a31166c-687e-0010-bca6-c68f7e60039b.html), President Field Operations at Confluent

"*Confluent makes it easy to connect and process real-time data streams...*"

"...o*ur customers have continuously told us that a tailored integration with SAP would significantly reduce their integration overhead, while maximizing the ROI for SAP investments.*"

"*Together with ...